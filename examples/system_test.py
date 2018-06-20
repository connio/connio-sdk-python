import os
import time
import operator

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from connio.rest import Client
from connio.rest.api.v3.account import UserInfo

ACCOUNT_KEYID = os.environ.get('CONNIO_ACCOUNT_KEYID')
ACCOUNT_KEYSECRET = os.environ.get('CONNIO_ACCOUNT_KEYSECRET')

def example():
    """
    Some example usage of different connio resources.
    """

    # client = Client(username="_key_384829132696204034", 
    #                 password="840b43d162b040e4a9c14e7899f0151c",
    #                 host="http://localhost:8081")

    #from_host = "https://api3.inv.connio.net"
    from_host = "https://api.connio.cloud"
    to_host = "http://localhost:8081"

    frmSys = Client(username="user", 
                    password="password",
                    sysadmin=True,
                    host=from_host)

    toSys = Client(username="user", 
                    password="password",
                    sysadmin=True,
                    host=to_host)

    # token = sys.accounts.create(name='deneme18', userInfo=UserInfo(email='emre18@inbiza.com', role='admin', name='emre'))

    # user = sys.api.helpers.activate(token['token'])
    # print('token: {}'.format(token['token']))

    # print('Master account: {}, {}, {}'.format(new_master.id, new_master.name, new_master.date_created))

    # List all master accounts
    masters = dict()
    no = 1
    for sysaccount in frmSys.accounts.stream():
        if sysaccount.owner_account_id == None:
            master = frmSys.accounts.get(sysaccount.id).fetch()
            print('No {}. Master account: {}, {}, {}'.format(no, master.id, master.name, master.date_created))
            # if master.name[:6] == 'deneme' and master.status == 'open':
            #     master.delete()
            #     master.delete(True)
            masters[master.id] = master.name
        no=+1

    #List all system users
    no = 1
    for sysusr in frmSys.users.stream():
        # print('No {}. User: {}, {}, {}, {}, {}, {}'.format(no, sysusr.role, sysusr.status, sysusr.id, sysusr.name, sysusr.email, sysusr.date_created))
        if sysusr.status == 'confirmed' and sysusr.role == 'admin' and masters.get(sysusr.account_id) is not None:
            print('MM {}'.format(masters[sysusr.account_id]))            
            # print('\tNo {}. User: {}, {}, {}'.format(no, sysusr.id, sysusr.apikey.id, sysusr.apikey.secret))
            # if masters[sysusr.account_id] == 'innova4':
            #     get(sysusr.apikey.id, sysusr.apikey.secret, from_host)
            get(sysusr.apikey.id, sysusr.apikey.secret, from_host)
            masters.pop(sysusr.account_id, None)
        no += 1

    # List all system accounts
    # no = 1
    # for sysaccount in sys.accounts.stream():
    #     if sysaccount.owner_account_id == None:
    #         master_account = sys.accounts.get(sysaccount.id)
    #         master = master_account.fetch()
    #         print('No {}. Master account: {}, {}, {}'.format(no, master.id, master.name, master.date_created))


            # client = Client(username="user", 
            #         password="password",
            #         host="https://api3.inv.connio.net")


            # subno = 1
            # for sub in client.accounts.stream():
            #     if sub.owner_account_id == master.id:
            #         print('\tNo {}. Sub account: {}, {}, {}'.format(subno, sub.id, sub.name, sub.date_created))
            #         subno += 1

            # usrno = 1
            # for usr in master_account.users.stream():
            #     print('No {}. User: {}, {}, {}, {}'.format(usrno, usr.id, usr.name, usr.email, usr.date_created))
            #     usrno += 1

            # clino = 1
            # for cli in master_account.apiclients.stream():
            #     print('No {}. Api Client: {}, {}, {}'.format(clino, cli.id, cli.name, cli.date_created))
            #     clino += 1

            # dpfno = 1
            # for dpf in master_account.deviceprofiles.stream():
            #     print('No {}. Device Profile: {}, {}, {}'.format(dpfno, dpfi.id, dpf.name, dpf.date_created))
            #     dpfno += 1
            
            # no += 1

    # Get master account details
    # account = client.accounts.get('_acc_384829101551762077')

    # master = account.fetch()    
    # print('Master account: ' + master.name)

    # List API Clients
    # no = 1
    # for apiclient in account.apiclients.stream():
    #     print('No {}. ApiClient: {}, {}, {}'.format(no, apiclient.id, apiclient.name, apiclient.date_created))
    #     no += 1

    

    # Create sub accounts
    # for i in range(1, 11):
    #     newSub = client.accounts.create(name='SubAcc.' + str(i))
    #     print('New subaccount name: ' + newSub.name + ', id: ' + newSub.id)

    # List users
    # no = 1
    # for usr in client.account.users.stream():
    #     print('No {}. User: {}, {}, {}, {}'.format(no, usr.id, usr.name, usr.email, usr.date_created))
    #     no += 1

    # Create an app
    # client.account.apps.create(name='SampleApp',
    #                            profile='Sample',
    #                            friendly_name='My first app',
    #                            description='The first sample app',
    #                            tags=['test']
    #                           )

    # Create a provisioning key
    # client.account.apiclients.create(name='ProvisioningClient',
    #                                 friendly_name='Provisioning Key',
    #                                 description='An API Client for device provisioning',
    #                                 tags=['provisioning'],
    #                                 context={'type': "account", 'ids': [master.id]},
    #                                 scope=['device:read'],
    #                                 )
                                         
    # Create new device profile
    # compressor = client.account.deviceprofiles.create(name='Compressor', 
    #                                               friendly_name='Compressor Machine',
    #                                               base_profile='ConnectedDevice',
    #                                               description='Industrial compressor',
    #                                               tags=['test'],
    #                                               device_class='compressor',
    #                                               product_name='Logika101',
    #                                               vendor_name='Dalgakiran'
    #                                             )

    # Add property to the device profile
    # client.account.properties(compressor.id).create(name='temperature',
    #                                         friendly_name='Temperature',
    #                                         description='Temperature Sensor',
    #                                         tags=['temp'],
    #                                         data_type='number', 
    #                                         access_type='protected', 
    #                                         publish_type='always',
    #                                         # retention=prp.retention
    #                                     )

    # client.account.properties(compressor.id).create(name='humidity',
    #                                         friendly_name='Humidity',
    #                                         description='Humidity Sensor',
    #                                         tags=['humidity'],
    #                                         data_type='number', 
    #                                         access_type='protected', 
    #                                         publish_type='always',
    #                                         # retention=prp.retention
    #                                     )

    # client.account.properties(compressor.id).create(name='pressure',
    #                                         friendly_name='Pressure',
    #                                         description='Pressure Sensor',
    #                                         tags=['pressure'],
    #                                         data_type='number', 
    #                                         access_type='protected', 
    #                                         publish_type='always',
    #                                         # retention=prp.retention
    #                                     )

    # Create devices generated from this device profile
    # for i in range(1, 11):
    #     device = client.account.devices.create(name='Device.{}'.format(i), 
    #                                            profile='compressor',
    #                                            )
    #     print('New device: {}, {}'.format(device.id, device.name))

def get(admin_key_id, admin_key_secret, host=None):
    client = Client(username=admin_key_id, 
                    password=admin_key_secret,
                    host=host)

    no = 1
    for usr in client.account.users.stream():
        print('{}.User: {}, {}, {}, {}'.format(no, usr.id, usr.name, usr.email, usr.date_created))
        no += 1

    sortedDPList = sorted(client.account.deviceprofiles.list(), key = operator.itemgetter('date_created'))
    # Migrate all user created device profiles
    no = 1
    for dpf in sortedDPList:
        print('{}.Device Profile: {}, {}, {}'.format(no, dpf.id, dpf.name, dpf.date_created))
        no += 1

    sortedAPList = sorted(client.account.appprofiles.list(), key = operator.itemgetter('date_created'))
    # Migrate all user created app profiles
    no = 1
    for apf in sortedAPList:
        print('{}.App Profile: {}, {}, {}'.format(no, apf.id, apf.name, apf.date_created))
        no += 1 

    no = 1
    for apicli in client.account.apiclients.stream():
        print('{}.Api Client: {}, {}, {}'.format(no, apicli.id, apicli.name, apicli.date_created))
        no += 1

    no = 1
    for device in client.account.devices.stream():
        print('{}.Device: {}, {}, {}'.format(no, device.id, device.name, device.date_created))
        no += 1
    
    no = 1
    for app in client.account.apps.stream():
        print('{}.App: {}, {}, {}'.format(no, app.id, app.name, app.date_created))
        no += 1
    
    
if __name__ == '__main__':
    example()
