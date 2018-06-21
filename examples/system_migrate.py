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

ACCOUNT_KEYID = os.environ.get('CONNIO_ACCOUNT_KEYID')
ACCOUNT_KEYSECRET = os.environ.get('CONNIO_ACCOUNT_KEYSECRET')

def migrate_system(migration_path):
    """
    Some example usage of different connio resources.
    """

    # from_host = "https://api.connio.cloud"
    from_host = "https://api.connio.com"
    # from_host = "https://api3.inv.connio.net"
    
    to_host = "http://localhost:8081"
    
    frmSys = Client(username="user", 
                    password="password",
                    sysadmin=True,
                    host=from_host)

    # List all master accounts
    print('Discovering master accounts on the source....')

    masters = dict()
    no = 1
    for sysaccount in frmSys.accounts.stream():
        if sysaccount.owner_account_id == None:
            master = frmSys.accounts.get(sysaccount.id).fetch()
            print('No {}. Master account: {}, {}, {}'.format(no, master.id, master.name, master.date_created))
            masters[master.id] = master.name            
            no += 1

    #List all system users
    no = 1
    for sysusr in frmSys.users.stream():
        if sysusr.status == 'confirmed' and sysusr.role == 'admin' and masters.get(sysusr.account_id) is not None:
            print('Migrating account: {}'.format(masters[sysusr.account_id]))            
            migrate_account(migration_path, sysusr.account_id, masters[sysusr.account_id], sysusr.email, sysusr.name, sysusr.apikey.id, sysusr.apikey.secret, from_host, to_host)
            masters.pop(sysusr.account_id, None)
        no += 1

def migrate_account(migration_path, account_id, account_name, admin_user_email, admin_user_name, from_admin_key_id, from_admin_key_secret, from_host, to_host):    
    """
    Migrate an account from one system to another.
    """
    if not os.path.exists(migration_path):
        os.makedirs(migration_path)

    # Build account map
    tblFromOldAccountIdToNewAccountId = dict()    

    toSys = Client(username="user", 
                    password="password",
                    sysadmin=True,
                    host=to_host)

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

    token = toSys.accounts.create(name=account_name, userInfo=UserInfo(email=admin_user_email, role='admin', name=admin_user_name))
    admin = toSys.api.helpers.activate(token['token'])

    tblFromOldAccountIdToNewAccountId[account_id] = admin.account_id

    time.sleep(3)

    # Update admin api key and set password
    toCli = cloneUser(migration_path, admin, from_admin_key_id, from_admin_key_secret, to_host)

    time.sleep(2)

    # cleanup(toCli)
    for app in toCli.account.apps.stream():
        app.delete()

    # Build default profile map
    tblFromOldProfIdToNewProfId = dict()

    sortedDPList = sorted(fromCli.account.deviceprofiles.list(), key = operator.itemgetter('date_created'))

    # Migrate all Device Profiles
    no = 1
    for dpf in sortedDPList:
        if dpf.name == 'ConnectedDevice' or dpf.name == 'Device' or dpf.name == 'Gateway':
            print('Device profile {}. Device Profile: {}, {}, {}'.format(no, dpf.id, dpf.name, dpf.date_created))
            tblFromOldProfIdToNewProfId[dpf.id] = dpf.name   
        else:
            print('Device profile {}. Device Profile: {}, {}, {}'.format(no, dpf.id, dpf.name, dpf.date_created))

            base_profile = tblFromOldProfIdToNewProfId.get(dpf.base_profile_id)
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
            tblFromOldProfIdToNewProfId[dpf.id] = dpf.name
            
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
                    print('Prop #{}. Property of {}: {}, {}, {}, {}, {}'.format(pno, newdp.name, newprp.id, newprp.name, newprp.inherited, newprp.access_type, newprp.date_created))
                    pno += 1

        no += 1

    # Migrate all App Profiles
    sortedAPList = sorted(fromCli.account.appprofiles.list(), key = operator.itemgetter('date_created'))
    
    no = 1
    for apf in sortedAPList:
        if apf.name == 'Sample':
            tblFromOldProfIdToNewProfId[apf.id] = apf.name
            print('App profile {}. App Profile: {}, {}, {}'.format(no, apf.id, apf.name, apf.date_created))    
        else:
            print('App profile {}. App Profile: {}, {}, {}'.format(no, apf.id, apf.name, apf.date_created))    
            newapf = toCli.account.appprofiles.create(name=apf.name, 
                                                 friendly_name=apf.friendly_name,
                                                 base_profile=tblFromOldProfIdToNewProfId.get(apf.base_profile_id),
                                                 description=apf.description,
                                                 tags=apf.tags,
                                                 version=apf.version,
                                                 product_name=apf.product_name,
                                                 vendor_name=apf.vendor_name,
                                                 image_url=apf.image_url
                                                )
            tblFromOldProfIdToNewProfId[apf.id] = apf.name
            
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
                    print('Prop #{}. Property of {}: {}, {}, {}, {}, {}'.format(pno, newprp.name, newprp.id, newprp.name, newprp.inherited, newprp.access_type, newprp.date_created))
                    pno += 1

        no += 1

    # Migrate all Apps
    tblApps = dict()
    no = 1
    for app in fromCli.account.apps.stream():
        newapp = toCli.account.apps.create(name=app.name,
                                     profile=tblFromOldProfIdToNewProfId.get(app.profile_id),  
                                     friendly_name=app.friendly_name,
                                     description=app.description,
                                     tags=app.tags,
                                     status=app.status
                                    )
        no += 1
        tblApps[app.id] = newapp.id

    # Migrate all Devices
    no = 1
    for dev in fromCli.account.devices.stream():
        # Copy device id into migration folder
        text_file = open(migration_path + "device", "w")
        text_file.write(dev.id)
        text_file.close()

        text_file = open(migration_path + "apikey", "w")
        text_file.write(dev.apikey.id)
        text_file.write('\n')
        text_file.write(dev.apikey.secret)
        text_file.close()

        #convert app ids
        apps = []
        for i in dev.apps:
            apps.append(tblApps[i])
            
        newDev = toCli.account.devices.create(name=dev.name,
                                     profile=tblFromOldProfIdToNewProfId.get(dev.profile_id),
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
        print('Device #{}. {}, {}, {}'.format(no, newDev.id, newDev.name, newDev.date_created))
        no += 1

        os.remove(migration_path + "device")
        os.remove(migration_path + "apikey")

    # Migrate all Sub accounts
    no = 1
    for acc in fromCli.accounts.stream():
        if acc.status != AccountInstance.Status.CREATED and acc.status != AccountInstance.Status.CLOSED:
            newSub = toCli.accounts.create(name=acc.name, 
                                        friendly_name=acc.friendly_name)
            print('New subaccount name: ('+ str(no) + ') ' + newSub.name + ', id: ' + newSub.id)
            tblFromOldAccountIdToNewAccountId[acc.id] = newSub.id
            no = no + 1

    # Migrate all API Clients
    no = 1
    for apicli in fromCli.account.apiclients.stream():
        # Copy API client id into migration folder
        text_file = open(migration_path + "apiclient", "w")
        text_file.write(apicli.id)
        text_file.close()

        text_file = open(migration_path + "apikey", "w")
        text_file.write(apicli.apikey.id)
        text_file.write('\n')
        text_file.write(apicli.apikey.secret)
        text_file.close()

        # Convert app ids
        if apicli.apikey.context['type'] == 'app':
            apps = []
            for i in apicli.apikey.context['ids']:
                apps.append(tblApps[i])
            apicli.apikey.context['ids'] = apps
        # Convert account ids
        elif apicli.apikey.context['type'] == 'account':
            accountIDs = []
            for i in apicli.apikey.context['ids']:
                accountIDs.append(tblFromOldAccountIdToNewAccountId[i])
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

        os.remove(migration_path + "apiclient")
        os.remove(migration_path + "apikey")

    # Migrate all Users
    no = 1
    for fromusr in fromCli.account.users.stream():
        if fromusr.email != admin.email:
            # Copy API client id into migration folder
            text_file = open(migration_path + "user", "w")
            text_file.write(fromusr.id)
            text_file.close()

            text_file = open(migration_path + "apikey", "w")
            text_file.write(fromusr.apikey.id)
            text_file.write('\n')
            text_file.write(fromusr.apikey.secret)
            text_file.close()

            token = toCli.account.users.create(email=fromusr.email, role=fromusr.role, name=fromusr.name)
            usr = toSys.api.helpers.activate(token['token'])

            print('No {}. User: {}, {}, {}, {}, {}'.format(no, usr.id, usr.name, usr.role, usr.email, usr.date_created))
            no += 1

            os.remove(migration_path + "user")
            os.remove(migration_path + "apikey")

    
    # # Migrate all User keys (for admin)
    # no = 1
    # for fromusr in fromCli.account.users.stream():
    #     text_file = open(migration_path + "apikey", "w")
    #     text_file.write(fromusr.apikey.id)
    #     text_file.write('\n')
    #     text_file.write(fromusr.apikey.secret)
    #     text_file.close()

    #     usr = toCli.account.users(fromusr.email).fetch()
    #     apikey = usr.apikey.regen()
         
    #     print('No {}. User: {}, {}, {}, {}, keyid: {}, secret: {}'.format(no, usr.id, usr.name, usr.email, usr.date_created, apikey.id, apikey.secret))
    #     no += 1

    #     os.remove(migration_path + "apikey")

    # Remove migration directory
    os.removedirs(migration_path)


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

def cloneUser(migration_path, user, src_user_key_id, src_user_key_secret, to_host):
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


def main(argv):
    migration_path = "/Users/emre/DevHome/Projects/Connio/v3.1/octopus/connio-solo/migration/"
    try:
        opts, _ = getopt.getopt(argv,"m:",["migration_path="])
    except getopt.GetoptError:
        migration_path="/Users/emre/DevHome/Projects/Connio/v3.1/octopus/connio-solo/migration/"  

    for opt, arg in opts:
        if opt == '-h':
            print('migrate.py -m <migration_path>')
            sys.exit()
        elif opt in ("-m", "--migration_path"):
            migration_path = arg

    if os.path.isfile(migration_path + "user"):
        os.remove(migration_path + "user")

    if os.path.isfile(migration_path + "device"):
        os.remove(migration_path + "device")

    if os.path.isfile(migration_path + "apikey"):
        os.remove(migration_path + "apikey")

    migrate_system(migration_path)

if __name__ == '__main__':
    main(sys.argv[1:])