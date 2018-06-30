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

ACCOUNT_KEYID = os.environ.get('CONNIO_ACCOUNT_KEYID')
ACCOUNT_KEYSECRET = os.environ.get('CONNIO_ACCOUNT_KEYSECRET')

MIGRATION_PATH = "/Users/emre/DevHome/Projects/Connio/v3.1/octopus/connio-solo/migration/"

# from_host = "https://api.connio.cloud"
# from_host = "https://api.connio.com"
from_host = "https://api3.inv.connio.net"
    
# to_host = "http://localhost:8081"
to_host = "https://api.connio.cloud"

frmSys = Client(username="user", 
                    password="password",
                    sysadmin=True,
                    host=from_host)

toSys = Client(username="user", 
                    password="password",
                    sysadmin=True,
                    host=to_host)

TempAdminList = []

#str(message.payload.decode("utf-8"))

def migrate_system():
    """
    Some example usage of different connio resources.
    """

    if not os.path.exists(MIGRATION_PATH):
        os.makedirs(MIGRATION_PATH)

    # List all master accounts
    print('Discovering master accounts on the source....')

    masters = dict()
    
    sortedAccountList = sorted(frmSys.accounts.list(), key = operator.itemgetter('date_created'))

    no = 1
    for sysaccount in sortedAccountList:
        if sysaccount.owner_account_id == None:
            master = frmSys.accounts.get(sysaccount.id).fetch()
            print('No {}. Master account: {}, {}, {}'.format(no, master.id, master.name, master.date_created))
            masters[master.id] = master.name            
            no += 1

    # subs = dict()
    # no = 1
    # for sysaccount in sortedAccountList:
    #     if sysaccount.owner_account_id != None:
    #         sub = frmSys.accounts.get(sysaccount.id).fetch()
    #         print('No {}. Sub account: {}, {}, {}, Owner: {}'.format(no, sub.id, sub.name, sub.date_created, masters.get(sub.owner_account_id) or subs.get(sub.owner_account_id)))
    #         subs[sub.id] = sub.name            
    #         no += 1


    # List all system users
    sortedUserList = sorted(frmSys.users.list(), key = operator.itemgetter('date_created'))
    no = 1
    for sysusr in sortedUserList:
        if sysusr.status == 'confirmed' and sysusr.role == 'admin' and masters.get(sysusr.account_id) is not None:
            #print('No {}. Migrating account: {}'.format(no, masters.get(sysusr.account_id) or subs.get(sysusr.account_id)))
            migrate_master(sysusr.account_id, masters[sysusr.account_id], None, sysusr.email, sysusr.name, sysusr.apikey.id, sysusr.apikey.secret, from_host, to_host)
            masters.pop(sysusr.account_id, None)
            no += 1

    # Remove all temporary admin users
    no = 1
    for temp_admin in TempAdminList:
        print('no {}, deleting {} of {}'.format(no, temp_admin['email'], temp_admin['account_id']))
        # Clean temporary admin created on the target account
        for sysusr in toSys.users.stream():
            if sysusr.account_id == temp_admin['account_id'] and sysusr.email != temp_admin['email'] and sysusr.role == 'admin':
                killCli = Client(username=sysusr.apikey.id, password=sysusr.apikey.secret, host=to_host)
                for user in killCli.account.users.stream():
                    if user.email == temp_admin['email']:
                        user.delete()
                        break
        no += 1
    
    # Remove migration directory
    os.removedirs(MIGRATION_PATH)

def migrate_master(account_id, account_name, owner_account, admin_user_email, admin_user_name, from_admin_key_id, from_admin_key_secret, from_host, to_host):        
    # clean account if exists
    try:
        master = toSys.accounts.get(account_name).fetch()
        master.delete(True)
    except:
        #ignore
        print("Nothing to delete")

    fromCli = Client(username=from_admin_key_id, 
                    password=from_admin_key_secret,
                    host=from_host)

    # Build account map
    tblFromOldAccountIdToNewAccountId = dict()

    token = toSys.accounts.create(name=account_name, owner=owner_account, tags=['migration'], userInfo=UserInfo(email=admin_user_email, role='admin', name=admin_user_name))
    admin = toSys.api.helpers.activate(token['token'])

    time.sleep(3)

    # Update admin api key and set password
    toCli = clone_user(MIGRATION_PATH, admin, from_admin_key_id, from_admin_key_secret, to_host)

    time.sleep(3)

    tblFromOldAccountIdToNewAccountId[account_id] = admin.account_id

    clone_account(tblFromOldAccountIdToNewAccountId, toCli, admin.account_id, fromCli, account_id, account_name, admin_user_email)

def clone_account(accountMap, toCli, to_account_id, fromCli, from_account_id, from_account_name, from_admin_email = None, owner_account = None):
    print('Migrating account id: {}, name: {}, owner: {}'.format(from_account_id, from_account_name, owner_account or 'None'))

    # Build profile map
    tblFromOldProfIdToNewProfId = dict()
    # Build app map
    tblApps = dict()

    # Remove default app (ie Sample)
    for app in toCli.account.apps.stream():
        app.delete()

    clone_deviceprofiles(fromCli, from_account_id, toCli, tblFromOldProfIdToNewProfId)

    clone_appprofiles(fromCli, from_account_id, toCli, tblFromOldProfIdToNewProfId)

    clone_apps(fromCli, from_account_id, toCli, tblFromOldProfIdToNewProfId, tblApps)

    clone_devices(fromCli, from_account_id, toCli, tblFromOldProfIdToNewProfId, tblApps)

    clone_apiclients(fromCli, from_account_id, toCli, tblFromOldProfIdToNewProfId, tblApps, accountMap)

    clone_users(fromCli, from_account_id, toCli, from_admin_email)

    # Migrate all Sub accounts
    sortedAccountList = sorted(frmSys.accounts.list(), key = operator.itemgetter('date_created'))
    no = 1
    for acc in sortedAccountList:
        if acc.owner_account_id == from_account_id and acc.status != AccountInstance.Status.CREATED and acc.status != AccountInstance.Status.CLOSED:
            # Create a temp admin to clone the account
            temp_admin_email = "admin_{}@connio-migrator.com".format(acc.name)

            token = toSys.accounts.create(name=acc.name, owner=to_account_id, tags=['migration'], userInfo=UserInfo(email=temp_admin_email, role='admin', name="connio-migrator"))
            admin = toSys.api.helpers.activate(token['token'])
            time.sleep(3)
            tempToCli = Client(username=admin.apikey.id, password=admin.apikey.secret, host=to_host)
            accountMap[acc.id] = admin.account_id

            TempAdminList.append( {'account_id': admin.account_id, 'email': temp_admin_email } )

            # Find admin user of the source account and create on the target
            sortedUserList = sorted(frmSys.users.list(), key = operator.itemgetter('date_created'))            
            for sysusr in sortedUserList:
                if sysusr.status == 'confirmed' and sysusr.role == 'admin' and sysusr.account_id == acc.id:
                    fromCli = Client(username=sysusr.apikey.id, password=sysusr.apikey.secret, host=from_host)
                    clone_account(accountMap, tempToCli, admin.account_id, fromCli, acc.id, acc.name, None, acc.owner_account_id)
                    no += 1                   
    
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

def clone_user(migration_path, user, src_user_key_id, src_user_key_secret, to_host):
    """
    Updates admin password and modify api key credentials to make it exact same to source system
    admin credentials.

    :param migration_path: 
    :param user: target system account's user
    :param src_user_key_id: source system account's user key id
    :param src_user_key_secret: source system account's user key secret
    :param to_host:

    :returns: connio.rest.api.v3.account.user.UserList
    :rtype: connio.rest.api.v3.account.user.UserList
    """
    # setup a client with current admin credentials 
    toCli = Client(username=user.apikey.id, password=user.apikey.secret, host=to_host)

    # Set admin password to default 
    user.update(password="password")

    # Update api key
    text_file = open(migration_path + "apikey", "w")
    text_file.write(src_user_key_id)
    text_file.write('\n')
    text_file.write(src_user_key_secret)
    text_file.close()

    usr = toCli.account.users(user.email).fetch()
    apikey = usr.apikey.regen()
        
    print('User: {}, {}, {}, {}, keyid: {}, secret: {}'.format(usr.id, usr.name, usr.email, usr.date_created, apikey.id, apikey.secret))

    os.remove(migration_path + "apikey")

    # return a client with modified credentials
    return Client(username=apikey.id, 
                password=apikey.secret,
                host=to_host)

def clone_users(fromCli, from_account, toCli, from_admin_email=None):
    # Migrate all Users
    no = 1
    for fromusr in fromCli.account.users.stream():
        if fromusr.email != from_admin_email:
            # Copy API client id into migration folder
            text_file = open(MIGRATION_PATH + "user", "w")
            text_file.write(fromusr.id)
            text_file.close()

            text_file = open(MIGRATION_PATH + "apikey", "w")
            text_file.write(fromusr.apikey.id)
            text_file.write('\n')
            text_file.write(fromusr.apikey.secret)
            text_file.close()

            token = toCli.account.users.create(email=fromusr.email, role=fromusr.role, name=fromusr.name)
            usr = toSys.api.helpers.activate(token['token'])

            time.sleep(3)

            usr.update(password='password')

            print('No {}. User: {}, {}, {}, {}, {}'.format(no, usr.id, usr.name, usr.role, usr.email, usr.date_created))
            no += 1

            os.remove(MIGRATION_PATH + "user")
            os.remove(MIGRATION_PATH + "apikey")


def clone_apiclients(fromCli, from_account, toCli, profileMap, appMap, accountMap):
    # Migrate all API Clients
    no = 1
    for apicli in fromCli.account.apiclients.stream():
        # Copy API client id into migration folder
        text_file = open(MIGRATION_PATH + "apiclient", "w")
        text_file.write(apicli.id)
        text_file.close()

        text_file = open(MIGRATION_PATH + "apikey", "w")
        text_file.write(apicli.apikey.id)
        text_file.write('\n')
        text_file.write(apicli.apikey.secret)
        text_file.close()

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

        #Filter out deprecated scopes
        deprecated_scopes=["index:create", "index:delete", "index:modify", "index:read", "view:create", "view:delete", "view:modify", "view:read"]        
        filtered_scopes = [s for s in apicli.apikey.scope if s not in deprecated_scopes]

        filtered_scopes=["app:execute" if x=="app:execute-method" else x for x in filtered_scopes]
        filtered_scopes=["device:execute" if x=="device:execute-method" else x for x in filtered_scopes]

        toCli.account.apiclients.create(name=apicli.name,
                                        friendly_name=apicli.friendly_name,
                                        description=apicli.description,
                                        tags=apicli.tags,
                                        context=apicli.apikey.context,
                                        scope=filtered_scopes,
                                        )

        os.remove(MIGRATION_PATH + "apiclient")
        os.remove(MIGRATION_PATH + "apikey")

def clone_devices(fromCli, from_account, toCli, profileMap, appMap):
    # Migrate all Devices
    no = 1
    for dev in fromCli.account.devices.stream():
        # Copy device id into migration folder
        text_file = open(MIGRATION_PATH + "device", "w")
        text_file.write(dev.id)
        text_file.close()

        text_file = open(MIGRATION_PATH + "apikey", "w")
        text_file.write(dev.apikey.id)
        text_file.write('\n')
        text_file.write(dev.apikey.secret)
        text_file.close()

        #convert app ids
        apps = []
        for i in dev.apps:
            apps.append(appMap[i])
            
        try:
            newDev = toCli.account.devices.create(name=dev.name,
                                        profile=profileMap.get(dev.profile_id),
                                        apps=apps,
                                        friendly_name=dev.friendly_name,
                                        description=dev.description,
                                        tags=dev.tags,
                                        location=dev.location,
                                        custom_ids=dev.custom_ids,
                                        status=dev.status,
                                        period=dev.period,
                                        annotate_with_location=dev.annotate_with_location,
                                        annotate_with_meta=dev.annotate_with_meta
                                        )
            if no % 150 == 0:
                print('Device #{}. {}, {}, {}'.format(no, newDev.id, newDev.name, newDev.date_created))
            no += 1
        except ConnioException as err:
            print('***** ERROR: {}'.format(err))


        os.remove(MIGRATION_PATH + "device")
        os.remove(MIGRATION_PATH + "apikey")


def clone_apps(fromCli, from_account, toCli, profileMap, appMap):
    # Migrate all Apps   
    no = 1
    for app in fromCli.account.apps.stream():
        newapp = toCli.account.apps.create(name=app.name,
                                     profile=profileMap.get(app.profile_id),  
                                     friendly_name=app.friendly_name,
                                     description=app.description,
                                     tags=app.tags,
                                     status=app.status
                                    )
        no += 1
        appMap[app.id] = newapp.id

def clone_appprofiles(fromCli, from_account, toCli, profileMap):
    # Migrate all App Profiles
    sortedAPList = sorted(fromCli.account.appprofiles.list(), key = operator.itemgetter('date_created'))
    
    no = 1
    for apf in sortedAPList:
        #print('App profile {}. App Profile: {}, {}, {}'.format(no, apf.id, apf.name, apf.date_created))
        profileMap[apf.id] = apf.name
        no += 1
    
    no = 1
    for apf in sortedAPList:        
        if apf.name != 'Sample':
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
            
            pno = 1
            for prp in fromCli.account.properties(apf.id).stream():
                if prp.inherited == False:                   
                    newprp=toCli.account.properties(newapf.id).create(name=prp.name,
                                                                friendly_name=prp.friendly_name,
                                                                description=prp.description,
                                                                tags=prp.tags,
                                                                data_type=prp.data_type, 
                                                                access_type=prp.access_type, 
                                                                publish_type=prp.publish_type,
                                                                measurement=prp.measurement,
                                                                # retention=prp.retention
                                                            )
                    #print('Prop #{}. Property of {}: {}, {}, {}, {}, {}'.format(pno, newprp.name, newprp.id, newprp.name, newprp.inherited, newprp.access_type, newprp.date_created))
                    pno += 1
            no += 1


def clone_deviceprofiles(fromCli, from_account, toCli, profileMap):
    
    sortedDPList = sorted(fromCli.accounts.get(from_account).deviceprofiles.list(), key = operator.itemgetter('date_created'))

    no = 1
    for dpf in sortedDPList:
        #print('Device profile {}. Device Profile: {}, {}, {}'.format(no, dpf.id, dpf.name, dpf.date_created))
        profileMap[dpf.id] = dpf.name
        no += 1

    # Migrate all Device Profiles
    no = 1
    for dpf in sortedDPList:
        if dpf.name != 'ConnectedDevice' and dpf.name != 'Device' and dpf.name != 'Gateway':
            base_profile = profileMap.get(dpf.base_profile_id)
            # # EXCEPTION:
            if dpf.name == 'WeatherStation':
                base_profile = 'ConnectedDevice'

            newdp = toCli.account.deviceprofiles.create(name=dpf.name, 
                                                    friendly_name=dpf.friendly_name,
                                                    base_profile=base_profile,
                                                    description=dpf.description,
                                                    tags=dpf.tags,
                                                    device_class=dpf.device_class,
                                                    product_name=dpf.product_name,
                                                    vendor_name=dpf.vendor_name,
                                                    image_url=dpf.image_url
                                                )
            profileMap[dpf.id] = dpf.name
            
            pno = 1
            for prp in fromCli.account.properties(dpf.id).stream():
                if prp.inherited == False:                   
                    newprp=toCli.account.properties(newdp.id).create(name=prp.name.replace('.', '_'),
                                                                friendly_name=prp.friendly_name,
                                                                description=prp.description,
                                                                tags=prp.tags,
                                                                data_type=prp.data_type, 
                                                                access_type=prp.access_type, 
                                                                publish_type=prp.publish_type,
                                                                measurement=prp.measurement,
                                                                # retention=prp.retention
                                                            )
                    #print('Prop #{}. Property of {}: {}, {}, {}, {}, {}'.format(pno, newdp.name, newprp.id, newprp.name, newprp.inherited, newprp.access_type, newprp.date_created))
                    pno += 1
            no += 1

def main(argv):
    # MIGRATION_PATH = "/Users/emre/DevHome/Projects/Connio/v3.1/octopus/connio-solo/migration/"
    # try:
    #     opts, _ = getopt.getopt(argv,"m:",["migration_path="])
    # except getopt.GetoptError:
    #     MIGRATION_PATH="/Users/emre/DevHome/Projects/Connio/v3.1/octopus/connio-solo/migration/"

    # for opt, arg in opts:
    #     if opt == '-h':
    #         print('migrate.py -m <migration_path>')
    #         sys.exit()
    #     elif opt in ("-m", "--migration_path"):
    #         MIGRATION_PATH = arg

    if os.path.isfile(MIGRATION_PATH + "user"):
        os.remove(MIGRATION_PATH + "user")

    if os.path.isfile(MIGRATION_PATH + "device"):
        os.remove(MIGRATION_PATH + "device")

    if os.path.isfile(MIGRATION_PATH + "apikey"):
        os.remove(MIGRATION_PATH + "apikey")

    migrate_system()

if __name__ == '__main__':
    main(sys.argv[1:])