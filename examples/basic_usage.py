import os
import time

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from connio.rest import Client

ACCOUNT_KEYID = os.environ.get('CONNIO_ACCOUNT_KEYID')
ACCOUNT_KEYSECRET = os.environ.get('CONNIO_ACCOUNT_KEYSECRET')

def example():
    """
    Some example usage of different connio resources.
    """

    client = Client(username="_key_381845811449612485", 
                    password="3dc37bf89ad94f199adc11463099337d")

    # Get master account details
    master = client.accounts.get().fetch()    
    print('Master account: ' + master.name)

    # Create sub accounts
    for i in range(1, 11):
        newSub = client.accounts.create(name='SubAcc.' + str(i))
        print('New subaccount name: ' + newSub.name + ', id: ' + newSub.id)

    # List users
    no = 1
    for usr in client.account.users.stream():
        print('No {}. User: {}, {}, {}, {}'.format(no, usr.id, usr.name, usr.email, usr.date_created))
        no += 1

    # Create an app
    client.account.apps.create(name='SampleApp',
                               profile='Sample',
                               friendly_name='My first app',
                               description='The first sample app',
                               tags=['test']
                              )

    client.account.apiclients.create(name='ProvisioningClient',
                                    friendly_name='Provisioning Key',
                                    description='An API Client for device provisioning',
                                    tags=['provisioning'],
                                    context={'type': "account", 'ids': [master.id]},
                                    scope=['device:read'],
                                    )
                                         
    # original = client.account.deviceprofiles.get('compressor3').fetch()
    compressor = client.account.deviceprofiles.create(name='Compressor', 
                                                  friendly_name='Compressor Machine',
                                                  base_profile='ConnectedDevice',
                                                  description='Industrial compressor',
                                                  tags=['test'],
                                                  device_class='compressor',
                                                  product_name='Logika101',
                                                  vendor_name='Dalgakiran'
                                                )

    client.account.properties(compressor.id).create(name='temperature',
                                            friendly_name='Temperature',
                                            description='Temperature Sensor',
                                            tags=['temp'],
                                            data_type='number', 
                                            access_type='protected', 
                                            publish_type='always',
                                            # retention=prp.retention
                                        )

    client.account.properties(compressor.id).create(name='humidity',
                                            friendly_name='Humidity',
                                            description='Humidity Sensor',
                                            tags=['humidity'],
                                            data_type='number', 
                                            access_type='protected', 
                                            publish_type='always',
                                            # retention=prp.retention
                                        )

    client.account.properties(compressor.id).create(name='pressure',
                                            friendly_name='Pressure',
                                            description='Pressure Sensor',
                                            tags=['pressure'],
                                            data_type='number', 
                                            access_type='protected', 
                                            publish_type='always',
                                            # retention=prp.retention
                                        )

    for i in range(1, 11):
        device = client.account.devices.create(name='Device.{}'.format(i), 
                                               profile='compressor',
                                               )
        print('New device: {}, {}'.format(device.id, device.name))
    
if __name__ == '__main__':
    example()
