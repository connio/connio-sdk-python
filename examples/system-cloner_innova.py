import os
import time
import getopt
import operator

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from connio.rest import Client
from connio.rest.api.v3.account import UserInfo
from connio.rest.api.v3.account import AccountInstance
from connio.base.exceptions import ConnioException
from connio.base.exceptions import ConnioRestException

from six import u

def _red(words):
    return u("\033[31m\033[49m%s\033[0m") % words
def _teal(words):
    return u("\033[36m\033[49m%s\033[0m") % words
def _white(words):
    return u("\033[37m\033[49m%s\033[0m") % words
def _blue(words):
    return u("\033[34m\033[49m%s\033[0m") % words

from_host = "https://api3.inv.connio.net"
#to_host = "https://api.connio.cloud"
to_host = "https://api.skywaveiot.com" 

frmSys = Client(username="user", 
                    password="password",
                    sysadmin=True,
                    host=from_host)

toSys = Client(username="user", 
                    password="password",
                    sysadmin=True,
                    host=to_host)

text_file = None

# Master accounts
tblAccounts = dict()

def clone_system():
    """
    Clones the given system on the target.
    """
    global text_file
    text_file = open("lookup_table.txt", "w")

    # List all master accounts
    print(_blue('Discovering master accounts on the source....'))

    # Build account map
    tblFromOldAccountIdToNewAccountId = dict()

    # All users
    tblUsers = dict()

    # deleteList = sorted(toSys.accounts.list(status='open'), key = operator.itemgetter('date_created'))
    # for sysaccount in deleteList:
    #     sysaccount.delete(True)

    # List all system users
    sortedUserList = sorted(frmSys.users.list(status='confirmed'), key = operator.itemgetter('date_created'))    
    for sysusr in sortedUserList:
        if sysusr.status == 'confirmed' and sysusr.role == 'admin' and tblUsers.get(sysusr.account_id) is None:
            tblUsers[sysusr.account_id] = sysusr


    sortedAccountList = sorted(frmSys.accounts.list(status='open'), key = operator.itemgetter('date_created'))

    no = 1
    for sysaccount in sortedAccountList:
        if sysaccount.status != 'closed':
            sysacc = frmSys.accounts.get(sysaccount.id).fetch()
            print(_teal('{}. System account: {} [{}], owner: {}, {}'.format(no, sysacc.name, sysacc.id, sysacc.owner_account_id, sysacc.date_created)))
            tblAccounts[sysacc.id] = sysacc.name            
            no += 1

            sysusr = tblUsers.get(sysacc.id)
            if sysusr is not None:
                print(_blue('Admin user for account: {} is {}'.format(sysacc.id, sysusr.email)))
                try:
                    clone_master(tblFromOldAccountIdToNewAccountId, sysusr.account_id, sysaccount.name, sysaccount.plan, tblFromOldAccountIdToNewAccountId.get(sysaccount.owner_account_id), sysusr.id, sysusr.email, sysusr.name, sysusr.apikey.id, sysusr.apikey.secret, from_host, to_host)
                except ConnioRestException as ce:
                    print(ce)
                    continue
            else:
                print(_red('Admin user cannot be located for account: {}'.format(sysacc.id)))

    text_file.close()
                
def clone_master(tblFromOldAccountIdToNewAccountId,
                 account_id, 
                 account_name, 
                 account_plan, 
                 owner_account, 
                 admin_user_id,
                 admin_user_email, 
                 admin_user_name, 
                 from_admin_key_id, 
                 from_admin_key_secret, 
                 from_host, 
                 to_host):        

    # clean account on the destination system if exists
    try:
        master = toSys.accounts.get(account_name).fetch()
        master.delete(True)
    except:
        #ignore
        print("Nothing to delete")

    # skip account if it is already on the destination system
    try:
        toSys.accounts.get(account_name).fetch()
        print(_blue('|-Skipping account: {}'.format(account_name)))
        return       
    except:
        #ignore
        pass

    token = toSys.accounts.create(name=account_name, owner=owner_account, tags=['INNOVA', 'MIGRATED'], userInfo=UserInfo(email=admin_user_email, role='admin', name=admin_user_name), plan=account_plan)
    admin = toSys.api.helpers.activate(token['token'])

    # Wait until activation is propagated
    while(1):
        try:
            # setup a client with current admin credentials 
            admin.update(password='password')                        
            break
        except:
            time.sleep(.5)
            continue

    text_file.write('{};{};user;{};{},{},{}\n'.format(account_name, owner_account, admin_user_id, admin.id, admin.apikey.id, admin.apikey.secret))
    
    admin.update(password='password')
    print(_blue("|-{} account is created successfully.".format(account_name)))

    toCli = None
    while(1):
        try:
            toCli = Client(username=admin.apikey.id, 
                        password=admin.apikey.secret,
                        host=to_host)
            break
        except:
            time.sleep(1.5)
            continue

    tblFromOldAccountIdToNewAccountId[account_id] = admin.account_id

    fromCli = None
    while(1):
        try:
            fromCli = Client(username=from_admin_key_id, 
                        password=from_admin_key_secret,
                        host=from_host)
            break
        except:
            time.sleep(1.5)
            continue

    clone_account(tblFromOldAccountIdToNewAccountId, toCli, admin.account_id, fromCli, account_id, account_name, admin_user_email)

def clone_account(accountMap, toCli, to_account_id, fromCli, from_account_id, from_account_name, from_admin_email = None, owner_account = None):
    print(_blue('|-Cloning account {} [{}], owner: {}'.format(from_account_name, from_account_id, owner_account or 'None')))

    # Build profile map
    tblFromOldProfIdToNewProfId = dict()
    # Build app map
    tblApps = dict()

    # Remove default app (i.e. Sample)
    for app in toCli.account.apps.stream():
        app.delete()

    migInfo = { 'from_account_id': from_account_id, 
                'from_account_name': from_account_name, 
                'owner_account_id': owner_account }

    newccount = toCli.account.fetch()
    text_file.write('{};{};{};account;{};{}\n'.format(from_account_id, from_account_name, owner_account, newccount.id, newccount.name))

    clone_deviceprofiles(migInfo, fromCli, toCli, tblFromOldProfIdToNewProfId)

    clone_appprofiles(migInfo, fromCli, toCli, tblFromOldProfIdToNewProfId)

    clone_apps(migInfo, fromCli, toCli, tblFromOldProfIdToNewProfId, tblApps)

    clone_devices(migInfo, fromCli, toCli, tblFromOldProfIdToNewProfId, tblApps)

    clone_apiclients(migInfo, fromCli, toCli, tblFromOldProfIdToNewProfId, tblApps, accountMap)

    clone_users(migInfo, fromCli, toCli, from_admin_email)

    # # Migrate all Sub accounts
    # sortedAccountList = sorted(frmSys.accounts.list(), key = operator.itemgetter('date_created'))
    # no = 1
    # for acc in sortedAccountList:
    #     if acc.owner_account_id == from_account_id and acc.status != AccountInstance.Status.CREATED and acc.status != AccountInstance.Status.CLOSED:
    #         # Create a temp admin to clone the account
    #         temp_admin_email = "admin_{}@connio-migrator.com".format(acc.name)

    #         token = toSys.accounts.create(name=acc.name, owner=to_account_id, tags=['migration'], userInfo=UserInfo(email=temp_admin_email, role='admin', name="connio-migrator"))
    #         admin = toSys.api.helpers.activate(token['token'])

    #         time.sleep(5)

    #         tempToCli = Client(username=admin.apikey.id, password=admin.apikey.secret, host=to_host)
    #         accountMap[acc.id] = admin.account_id

    #         TempAdminList.append( {'account_id': admin.account_id, 'email': temp_admin_email } )

    #         # Find admin user of the source account and create on the target
    #         sortedUserList = sorted(frmSys.users.list(), key = operator.itemgetter('date_created'))            
    #         for sysusr in sortedUserList:
    #             if sysusr.status == 'confirmed' and sysusr.role == 'admin' and sysusr.account_id == acc.id:
    #                 fromCli = Client(username=sysusr.apikey.id, password=sysusr.apikey.secret, host=from_host)
    #                 clone_account(accountMap, tempToCli, admin.account_id, fromCli, acc.id, acc.name, None, acc.owner_account_id)
    #                 no += 1   
    # 

def clone_properties(migInfo, fromCli, toCli, fromDP, toDP):
    propertyMap = dict()

    owner_account_name = '<none>'
    if migInfo['owner_account_id'] is not None:
        owner_account_name = tblAccounts.get(migInfo['owner_account_id']) or '<none>'
    
    try:
        pno = 1
        for prp in fromCli.account.properties(fromDP.id).stream():
            if prp.inherited == False:      
                propertyMap[prp.id] = prp.name     

                publishType = prp.publish_type
                if prp.access_type == 'public':
                    publishType = 'always'
                    
                newprp=toCli.account.properties(toDP.id).create(name=prp.name.replace('.', '_'),
                                                            friendly_name=prp.friendly_name,
                                                            description=prp.description,
                                                            tags=prp.tags,
                                                            data_type=prp.data_type, 
                                                            access_type=prp.access_type, 
                                                            publish_type=publishType,
                                                            measurement=prp.measurement,
                                                            retention=prp.retention,
                                                            boundaries=prp.boundaries
                                                        )
                print(_teal('|---Clonning property #{}. Property of {}: {}, {}, {}, {}'.format(pno, toDP.name, newprp.name, newprp.inherited, newprp.access_type, newprp.date_created)))

                text_file.write('{};{};property;{};{}\n'.format(migInfo['from_account_name'], owner_account_name, prp.id, newprp.id))

                pno += 1
    except ConnioRestException as ce:
        print(ce)
    except ConnioException as e:
        print(e)

    return propertyMap

def clone_methods(migInfo, fromCli, toCli, fromDP, toDP):
    methodMap = dict()
    newMethodMap = dict()

    owner_account_name = '<none>'
    if migInfo['owner_account_id'] is not None:
        owner_account_name = tblAccounts.get(migInfo['owner_account_id']) or '<none>'
    
    try:
        no = 1
        for mtd in fromCli.account.methods(fromDP.id).stream():
            print(_red('|---SKIPPING method #{}. Alert of {}: {}, {}'.format(no, fromDP.name, mtd.name, mtd.date_created)))
            continue

            if mtd.inherited == False:
                methodMap[mtd.id] = mtd.name                
                newmtd=toCli.account.methods(toDP.id).create(name=mtd.name,
                                                        friendly_name=mtd.friendly_name,
                                                        description=mtd.description,
                                                        tags=mtd.tags,
                                                        access_type=mtd.access_type,
                                                        method_impl=mtd.method_impl,
                                                        )
                newMethodMap[newmtd.name] = newmtd.id
                print(_teal('|---Cloning method #{}. Method of {}: {}, {}, {}, {}'.format(no, toDP.name, newmtd.name, newmtd.inherited, newmtd.access_type, newmtd.date_created)))

                text_file.write('{};{};method;{};{}\n'.format(migInfo['from_account_name'], owner_account_name, mtd.id, newmtd.id))

                no += 1
    except ConnioRestException as ce:
        print(ce)
    except ConnioException as e:
        print(e)

    return (methodMap, newMethodMap)

def clone_alerts(migInfo, fromCli, toCli, fromDP, toDP, propertyMap, methodMap, newMethodMap):
    from connio.rest.api.v3.account.alert import AlertInstance

    owner_account_name = '<none>'
    if migInfo['owner_account_id'] is not None:
        owner_account_name = tblAccounts.get(migInfo['owner_account_id']) or '<none>'
    
    try:
        no = 1
        for alr in fromCli.account.alerts(fromDP.id).stream():
            print(_red('|---SKIPPING alert #{}. Alert of {}: {}, {}'.format(no, fromDP.name, alr.name, alr.date_created)))
            continue

            replacedNotifications = []                    
            for n in alr.notifications:
                if n.action == 'method':
                    methodId = newMethodMap.get(methodMap.get(n.method))
                    notif = AlertInstance.Notification(
                        action=n.action,
                        name=n.name,
                        level=n.level,
                        message=n.message,
                        to=n.to,
                        subject=n.subject,
                        parameter=n.parameter,
                        method=methodId
                    )
                    replacedNotifications.append(notif)

            triggerPropId = propertyMap.get(alr.trigger)
            newalr=toCli.account.alerts(toDP.id).create(name=alr.name,
                                                        friendly_name=alr.friendly_name,
                                                        description=alr.description,
                                                        tags=alr.tags,
                                                        trigger=triggerPropId,
                                                        status=alr.status,
                                                        metric=alr.metric,
                                                        conditions=alr.conditions,
                                                        notifications=replacedNotifications
                                                    )
            print(_teal('|---Cloning alert #{}. Alert of {}: {}, {}'.format(no, toDP.name, newalr.name, newalr.date_created)))

            text_file.write('{};{};alert;{};{}\n'.format(migInfo['from_account_name'], owner_account_name, alr.id, newalr.id))

            no += 1
    except ConnioRestException as ce:
        print(ce)
    except ConnioException as e:
        print(e)
    
def clone_deviceprofiles(migInfo, fromCli, toCli, profileMap):
    sortedDPList = sorted(fromCli.accounts.get(migInfo['from_account_id']).deviceprofiles.list(), key = operator.itemgetter('date_created'))

    for dpf in sortedDPList:        
        profileMap[dpf.id] = dpf.name

    owner_account_name = '<none>'
    if migInfo['owner_account_id'] is not None:
        owner_account_name = tblAccounts.get(migInfo['owner_account_id']) or '<none>'
    
    # Cloning all Device Profiles
    no = 1
    for dpf in sortedDPList:
        if dpf.name != 'ConnectedDevice' and dpf.name != 'Device' and dpf.name != 'Gateway':
            print(_teal('|--Cloning device profile #{}. Device Profile: {}, {}, {}'.format(no, dpf.id, dpf.name, dpf.date_created)))
            base_profile = profileMap.get(dpf.base_profile_id)
           
            tags = None
            if dpf.tags:                
                tags = dpf.tags[:32]

            newdp = toCli.account.deviceprofiles.create(name=dpf.name, 
                                                    friendly_name=dpf.friendly_name,
                                                    base_profile=base_profile,
                                                    description=dpf.description,
                                                    tags=tags,
                                                    device_class=dpf.device_class,
                                                    product_name=dpf.product_name,
                                                    vendor_name=dpf.vendor_name,
                                                    image_url=dpf.image_url
                                                )
            profileMap[dpf.id] = dpf.name

            text_file.write('{};{};deviceprofile;{};{}\n'.format(migInfo['from_account_name'], owner_account_name, dpf.id, newdp.id))
            
            propertyMap = clone_properties(migInfo, fromCli, toCli, dpf, newdp)
            
            (methodMap, newMethodMap) = clone_methods(migInfo, fromCli, toCli, dpf, newdp)

            clone_alerts(migInfo, fromCli, toCli, dpf, newdp, propertyMap, methodMap, newMethodMap)

            no += 1

def clone_apiclients(migInfo, fromCli, toCli, profileMap, appMap, accountMap):    
    def includes(item):
        obsoleted = ['index:delete', 'index:create', 'index:read', 'index:modify', 'view:delete', 'view:create', 'view:read', 'view:modify']
        if item in obsoleted:
            return False
        else:
            return True
    def replace(item):
        if item == 'app:execute-method':
            return 'app:execute'
        elif item == 'device:execute-method':
            return 'device:execute'
        else:
            return item

    owner_account_name = '<none>'
    if migInfo['owner_account_id'] is not None:
        owner_account_name = tblAccounts.get(migInfo['owner_account_id']) or '<none>'

    no = 1
    for apicli in fromCli.account.apiclients.stream():
        try:
            # Convert app ids
            if apicli.apikey.context['type'] == 'app':
                apps = []
                for i in apicli.apikey.context['ids']:
                    apps.append(appMap[i])
                apicli.apikey.context['ids'] = apps
            # Convert account ids
            elif apicli.apikey.context['type'] == 'account':
                accountIDs = []
                for i in apicli.apikey.context['ids']:
                    accountIDs.append(accountMap[i])
                apicli.apikey.context['ids'] = accountIDs
            
            while(1):
                try:                    
                    filteredScopes = list(filter(lambda x: includes(x), apicli.apikey.scope))
                    filteredScopes = list(map(lambda x: replace(x), filteredScopes))
                    
                    newApiCli = toCli.account.apiclients.create(name=apicli.name,
                                                    friendly_name=apicli.friendly_name,
                                                    description=apicli.description,
                                                    tags=apicli.tags,
                                                    context=apicli.apikey.context,
                                                    scope=filteredScopes,
                                                    )

                    text_file.write('{};{};apiclient;{},{},{};{},{},{}\n'.format(
                        migInfo['from_account_name'], owner_account_name,
                        apicli.id, apicli.apikey.id, apicli.apikey.secret, 
                        newApiCli.id, newApiCli.apikey.id, newApiCli.apikey.secret))
                        
                    print(_teal('|--Api Client #{}. {}, {}, {}'.format(no, newApiCli.id, newApiCli.name, newApiCli.date_created)))
                    no += 1
                    break
                except ConnioRestException as ce:
                    # Probably too many request error occurred - cool it down
                    print(ce)
                    if ce.code == 'IllegalContextIdList':
                        break
                    else:
                        time.sleep(15)
                        continue
        except Exception as e:
            print(e)
            continue

def clone_devices(migInfo, fromCli, toCli, profileMap, appMap):
    print(_teal('.....Starting to cloning devices......'))

    owner_account_name = '<none>'
    if migInfo['owner_account_id'] is not None:
        owner_account_name = tblAccounts.get(migInfo['owner_account_id']) or '<none>'

    no = 1
    for dev in fromCli.account.devices.stream():        
        #convert app ids
        apps = []
        for i in dev.apps:
            apps.append(appMap[i])

        tags = None
        if dev.tags:                
            tags = dev.tags[:32]
            
        while(1):
            try:
                newDev = toCli.account.devices.create(name=dev.name,
                                            profile=profileMap.get(dev.profile_id),
                                            apps=apps,
                                            friendly_name=dev.friendly_name,
                                            description=dev.description,
                                            tags=tags,
                                            location=dev.location,
                                            custom_ids=dev.custom_ids,
                                            status=dev.status,
                                            period=dev.period,
                                            annotate_with_location=dev.annotate_with_location,
                                            annotate_with_meta=dev.annotate_with_meta
                                            )

                text_file.write('{};{};device;{};{}\n'.format(migInfo['from_account_name'], owner_account_name, dev.id, newDev.id))

                if no % 150 == 0:
                    print(_teal('|--Device #{}. {}, {}, {}'.format(no, newDev.id, newDev.name, newDev.date_created)))
                    time.sleep(10)
                no += 1
                break
            except ConnioRestException as ce:
                # Probably too many request error occurred - cool it down
                print(ce)
                print("...waiting...")
                time.sleep(10)
                continue

def clone_apps(migInfo, fromCli, toCli, profileMap, appMap):

    owner_account_name = '<none>'
    if migInfo['owner_account_id'] is not None:
        owner_account_name = tblAccounts.get(migInfo['owner_account_id']) or '<none>'

    no = 1
    for app in fromCli.account.apps.stream():
        newapp = toCli.account.apps.create(name=app.name,
                                     profile=profileMap.get(app.profile_id),  
                                     friendly_name=app.friendly_name,
                                     description=app.description,
                                     tags=app.tags,
                                     status=app.status
                                    )
        print(_teal('|--App #{}. {}, {}, {}'.format(no, newapp.id, newapp.name, newapp.date_created)))

        text_file.write('{};{};app;{};{}\n'.format(migInfo['from_account_name'], owner_account_name, app.id, newapp.id))

        no += 1
        appMap[app.id] = newapp.id

        dno = 1
        for connector in app.data_connectors.list():
            print(_teal('|---App {}: {}. data connector id: {}, type: {}, server: {}, db name: {}, disabled: {}'.format(
                app.name,
                dno,
                connector.id, 
                connector.type, 
                connector.config['server'],
                connector.config['database_name'],
                connector.disabled)
            ))
            newapp.data_connectors.create(
                id=connector.id,
                type=connector.type,
                disabled=connector.disabled,
                config=connector.config
            )
            dno += 1

def clone_appprofiles(migInfo, fromCli, toCli, profileMap):
    sortedAPList = sorted(fromCli.account.appprofiles.list(), key = operator.itemgetter('date_created'))
    
    for apf in sortedAPList:
        profileMap[apf.id] = apf.name

    owner_account_name = '<none>'
    if migInfo['owner_account_id'] is not None:
        owner_account_name = tblAccounts.get(migInfo['owner_account_id']) or '<none>'

    # 
    no = 1
    for apf in sortedAPList:        
        if apf.name != 'Sample':
            print(_teal('|--Cloning app profile #{}. App Profile: {}, {}, {}'.format(no, apf.id, apf.name, apf.date_created)))
            newapf = toCli.account.appprofiles.create(name=apf.name, 
                                                    friendly_name=apf.friendly_name,
                                                    base_profile=profileMap.get(apf.base_profile_id),
                                                    description=apf.description,
                                                    tags=apf.tags,
                                                    version=apf.version,
                                                    product_name=apf.product_name,
                                                    vendor_name=apf.vendor_name,
                                                    image_url=apf.image_url
                                                )
            profileMap[apf.id] = apf.name

            text_file.write('{};{};appprofile;{};{}\n'.format(migInfo['from_account_name'], owner_account_name, apf.id, newapf.id))
              
            propertyMap = clone_properties(migInfo, fromCli, toCli, apf, newapf)
            
            (methodMap, newMethodMap) = clone_methods(migInfo, fromCli, toCli, apf, newapf)

            clone_alerts(migInfo, fromCli, toCli, apf, newapf, propertyMap, methodMap, newMethodMap)

            no += 1

def clone_users(migInfo, fromCli, toCli, from_admin_email=None):

    owner_account_name = '<none>'
    if migInfo['owner_account_id'] is not None:
        owner_account_name = tblAccounts.get(migInfo['owner_account_id']) or '<none>'

    # Migrate all Users
    no = 1
    for fromusr in fromCli.account.users.stream():
        if fromusr.email != from_admin_email:            
            token = toCli.account.users.create(email=fromusr.email, role=fromusr.role, name=fromusr.name)
            usr = toSys.api.helpers.activate(token['token'])
            while(1):
                try:
                    usr.update(password='password')
                    break
                except:
                    time.sleep(0.5)
                    continue

            print('No {}. User: {}, {}, {}, {}, {}'.format(no, usr.id, usr.name, usr.role, usr.email, usr.date_created))

            text_file.write('{};{};user;{};{},{},{}\n'.format(migInfo['from_account_name'], owner_account_name, fromusr.id, usr.id, usr.apikey.id, usr.apikey.secret))

        no += 1
        
def main(argv):
    try:
        clone_system()
    except ConnioRestException as ce:
        print(ce)
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])


def cleanup(toCli):
    # Cleanup existing profiles     
    for user in toCli.account.users.stream():
        if user.role != user.Role.ADMIN:
            user.delete() 
    for apicli in toCli.account.apiclients.stream():
        apicli.delete()
    for device in toCli.account.devices.stream():
        device.delete()
    for app in toCli.account.apps.stream():
        app.delete()
    sortedList = sorted(toCli.account.deviceprofiles.list(), key = operator.itemgetter('date_created'), reverse=True)
    for dpf in sortedList:
        if dpf.name != 'ConnectedDevice' and dpf.name != 'Device' and dpf.name != 'Gateway':
            dpf.delete()
    sortedList = sorted(toCli.account.appprofiles.list(), key = operator.itemgetter('date_created'), reverse=True)
    for apf in sortedList:
        if apf.name != 'Sample':
            apf.delete()
    for acc in toCli.accounts.stream():
        if acc.status == AccountInstance.Status.OPEN:
            acc.delete()
    # for acc in toCli.accounts.stream():
    #     if acc.status == AccountInstance.Status.CLOSED:
    #         acc.delete(True)