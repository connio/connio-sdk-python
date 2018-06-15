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

    client = Client(username="_key_374133108962950176", 
                    password="722ac50c51b048e1b159092c4a321b1b")

    # Get master account details
    master = client.accounts.get().fetch()    
    print('Master account: ' + master.name)
                                     
    # Create new device profile
    compressor = client.account.deviceprofiles.create(name='i4100', 
                                                  friendly_name='Compressor Machine',
                                                  base_profile='Gateway',
                                                  description='Industrial compressor',
                                                  tags=['test'],
                                                  device_class='compressor',
                                                  product_name='i4100',
                                                  vendor_name='Dalgakıran'
                                                )

    # Add property to the device profile
    client.account.properties(compressor.id).create(name='ActiveAlarms1', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='ActiveAlarms2', data_type='number', access_type='protected', publish_type='always')

    for i in range(1, 11):
        client.account.properties(compressor.id).create(name='AlarmRecords' + str(i), data_type='number', access_type='protected', publish_type='always')

    for i in range(1, 5):
        client.account.properties(compressor.id).create(name='AO' + str(i), data_type='string', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='AP3', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='AP4', data_type='string', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='bL', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='BlockingStates', data_type='number', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='C02', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='C07_1', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='C07_2', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='C08', data_type='string', access_type='protected', publish_type='always')
    
    client.account.properties(compressor.id).create(name='C10', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='C19_1', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='C19_2', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='C20_1', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='C20_2', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='C22', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='C23', data_type='string', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='C__', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='C_H', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='CAF', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='CDF', data_type='number', access_type='protected', publish_type='always')

    for i in range(1, 11):
        client.account.properties(compressor.id).create(name='Cntrl_Identifier' + str(i), data_type='number', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='con', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='ControlCommand', data_type='number', access_type='public', publish_type='always')
    client.account.properties(compressor.id).create(name='CSF', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='DigitalInputs', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='DisplayedState', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='DisplayState1', data_type='number', access_type='protected', publish_type='always')

    for i in range(0, 7):
        client.account.properties(compressor.id).create(name='DR' + str(i), data_type='number', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='drY', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='FAd', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='FR1', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='FR2', data_type='number', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='GatewayError', data_type='object', access_type='protected', publish_type='always')

    for i in range(0, 8):
        client.account.properties(compressor.id).create(name='H0' + str(i), data_type='number', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='ln2', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='ln3', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='ln4', data_type='number', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='Indexes', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='initialState', data_type='number', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='Level1Password1', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='Level1Password2', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='Level2Password1', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='Level2Password2', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='Level3Password1', data_type='string', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='Level3Password2', data_type='string', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='LoadHours1', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='LoadHours2', data_type='number', access_type='protected', publish_type='always')
    
    for i in range(1, 13):
        client.account.properties(compressor.id).create(name='MaintenanceHours' + str(i), data_type='number', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='Modbus_Release', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='ModelNumber', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='nc', data_type='number', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='NonAcknowledgedActiveAlarms1', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='NonAcknowledgedActiveAlarms2', data_type='number', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='OFL', data_type='number', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='PA1', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='PA2', data_type='number', access_type='protected', publish_type='always')

    for i in range(0, 8):
        client.account.properties(compressor.id).create(name='P0' + str(i), data_type='number', access_type='protected', publish_type='always')

    for i in range(1, 8):
        client.account.properties(compressor.id).create(name='PI' + str(i), data_type='number', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='PM1', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='PT1', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='PT2', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='PT3', data_type='number', access_type='protected', publish_type='always')
    
    client.account.properties(compressor.id).create(name='r__', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='RelayOuts', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='Release_No', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='rL5', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='S__', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='S_h', data_type='number', access_type='protected', publish_type='always')

    client.account.properties(compressor.id).create(name='ScrewTemp1', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='SupplyVoltage', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='TotalHours1', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='TotalHours2', data_type='number', access_type='protected', publish_type='always')
    client.account.properties(compressor.id).create(name='WorkingPress1', data_type='number', access_type='protected', publish_type='always')

    for i in range(1, 9):
        client.account.properties(compressor.id).create(name='t0' + str(i), data_type='number', access_type='protected', publish_type='always')

    for i in range(1, 7):
        client.account.properties(compressor.id).create(name='WP' + str(i), data_type='number', access_type='protected', publish_type='always')

    for i in range(1, 8):
        client.account.properties(compressor.id).create(name='WT' + str(i), data_type='number', access_type='protected', publish_type='always')

    # Create new app profile
    client.account.appprofiles.create(name='CompressorManagement',                                                   
                                                  friendly_name='Compressor Management App',
                                                  description='Dalgakıran compressor management application',
                                                  tags=['compressor'],
                                                  version='1.0',
                                                  product_name='i4100',
                                                  vendor_name='Dalgakıran',
                                                  system=[{'deviceProfileId': compressor.id, 'cardinality': 0}]
                                                )
    
    # Create an app
    compressorApp = client.account.apps.create(name='CompressorManager',
                               profile='CompressorManagement',
                               friendly_name='Compressor Manager',
                               description='Unit of Compressor Management App',
                               tags=['compressor']
                              )

    # Create devices generated from this device profile
    # for i in range(1, 11):
    #     device = client.account.devices.create(name='Device.{}'.format(i), 
    #                                            profile='compressor',
    #                                            )
    #     print('New device: {}, {}'.format(device.id, device.name))

    device = client.account.devices.create(name='i4100_demo', 
                                           profile='i4100',
                                           custom_ids={'mac': '06:ac:58:7f:6d:35'},
                                           apps=[compressorApp.id]
                                          )

    # Create a provisioning key
    client.account.apiclients.create(name='ProvisioningClient2',
                                    friendly_name='Provisioning Key',
                                    description='An API Client for device provisioning',
                                    tags=['provisioning'],
                                    context={'type': 'app', 'ids': [compressorApp.id]},
                                    scope=['device:read'],
                                    )
    
if __name__ == '__main__':
    example()
