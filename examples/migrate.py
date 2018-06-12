import os
import getopt
import time
import operator

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from connio.rest import Client
from connio.rest.api.v3.account import AccountInstance


ACCOUNT_KEYID = os.environ.get('CONNIO_ACCOUNT_KEYID')
ACCOUNT_KEYSECRET = os.environ.get('CONNIO_ACCOUNT_KEYSECRET')

def migrate(migration_path):
    """
    Migrate an account from one system to another.
    """
    if not os.path.exists(migration_path):
        os.makedirs(migration_path)

    #INNOVA
    # fromCli = Client(username="xxx", 
    #                 password="xxx",
    #                 host="https://api3.inv.connio.net")

    fromCli = Client(username="_key_381845811449612485", 
                    password="3dc37bf89ad94f199adc11463099337d")

    toCli = Client(username="_key_378022407411318644", 
                    password="0e3915d079fa4da38cb478f84c707333",
                    host="http://localhost:8081")

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
    for dpf in toCli.account.deviceprofiles.stream():
        if dpf.name != 'ConnectedDevice' and dpf.name != 'Device' and dpf.name != 'Gateway':
            dpf.delete()
    for apf in toCli.account.appprofiles.stream():
        if apf.name != 'Sample':
            apf.delete()
    for acc in toCli.accounts.stream():
        if acc.status == AccountInstance.Status.OPEN:
            acc.delete()
    # for acc in toCli.accounts.stream():
    #     if acc.status == AccountInstance.Status.CLOSED:
    #         acc.delete(True)

    # Build account map
    tblFromOldAccountIdToNewAccountId = dict()

    master = fromCli.accounts.get().fetch()
    new_master = toCli.accounts.get().fetch()
    print("Migrating account `{}`".format(master.name))

    tblFromOldAccountIdToNewAccountId[master.id] = new_master.id

    # Migrate all users
    no = 1
    for usr in fromCli.account.users.stream():
        print('No {}. User: {}, {}, {}, {}'.format(no, usr.id, usr.name, usr.email, usr.date_created))
        no += 1

    # Build default profile map
    tblFromOldProfIdToNewProfId = dict()

    sortedDPList = sorted(fromCli.account.deviceprofiles.list(), key = operator.itemgetter('date_created'))

    # Migrate all user created device profiles
    no = 1
    for dpf in sortedDPList:
        if dpf.name == 'ConnectedDevice' or dpf.name == 'Device' or dpf.name == 'Gateway':
            print('Device profile {}. Device Profile: {}, {}, {}'.format(no, dpf.id, dpf.name, dpf.date_created))
            tblFromOldProfIdToNewProfId[dpf.id] = dpf.name   
        else:
            print('Device profile {}. Device Profile: {}, {}, {}'.format(no, dpf.id, dpf.name, dpf.date_created))    
            newdp = toCli.account.deviceprofiles.create(name=dpf.name, 
                                                 friendly_name=dpf.friendly_name,
                                                 base_profile=tblFromOldProfIdToNewProfId.get(dpf.base_profile_id),
                                                 description=dpf.description,
                                                 tags=dpf.tags,
                                                 device_class=dpf.device_class,
                                                 product_name=dpf.product_name,
                                                 vendor_name=dpf.vendor_name
                                                )
            tblFromOldProfIdToNewProfId[dpf.id] = dpf.name
            
            pno = 1
            for prp in fromCli.account.properties(dpf.id).stream():
                if prp.inherited == False:                   
                    newprp=toCli.account.properties(newdp.id).create(name=prp.name,
                                                              friendly_name=prp.friendly_name,
                                                              description=prp.description,
                                                              tags=prp.tags,
                                                              data_type=prp.data_type, 
                                                              access_type=prp.access_type, 
                                                              publish_type=prp.publish_type,
                                                                # retention=prp.retention
                                                            )
                    print('Prop #{}. Property of {}: {}, {}, {}, {}, {}'.format(pno, newdp.name, newprp.id, newprp.name, newprp.inherited, newprp.access_type, newprp.date_created))
                    pno += 1

        no += 1

    # Migrate all user created app profiles
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
                                                 vendor_name=apf.vendor_name
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
                                                                # retention=prp.retention
                                                            )
                    print('Prop #{}. Property of {}: {}, {}, {}, {}, {}'.format(pno, newprp.name, newprp.id, newprp.name, newprp.inherited, newprp.access_type, newprp.date_created))
                    pno += 1

        no += 1

    # Migrate all user created apps
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

    # Migrate all user created devices
    no = 1
    for dev in fromCli.account.devices.stream(limit=10):
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
            
        toCli.account.devices.create(name=dev.name,
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

        os.remove(migration_path + "device")
        os.remove(migration_path + "apikey")

    # Migrate all user created sub accounts
    no = 1
    for acc in fromCli.accounts.stream():
        newSub = toCli.accounts.create(name=acc.name, 
                                       friendly_name=acc.friendly_name)
        print('New subaccount name: ('+ str(no) + ') ' + newSub.name + ', id: ' + newSub.id)
        tblFromOldAccountIdToNewAccountId[acc.id] = newSub.id
        no = no + 1

    # Migrate all user created API clients
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

        toCli.account.apiclients.create(name=apicli.name,
                                        friendly_name=apicli.friendly_name,
                                        description=apicli.description,
                                        tags=apicli.tags,
                                        context=apicli.apikey.context,
                                        scope=apicli.apikey.scope,
                                        )

        os.remove(migration_path + "apiclient")
        os.remove(migration_path + "apikey")

    os.removedirs(migration_path)

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

    migrate(migration_path)

if __name__ == '__main__':
    main(sys.argv[1:])
