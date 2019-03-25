from connio.rest import Client
from connio.rest.api.v3.account.propertyy import PropertyInstance
from connio.rest.api.v3.account.method import MethodInstance

from readwrite_methods import *
from L200 import *

def wire(client, name='LogikaL200', friendly="Logika L200 Controller", base="ModbusGateway"):
    # Create Logika L200 profile
    compressor = client.account.deviceprofiles.create(name=name, 
                                                  friendly_name=friendly,
                                                  base_profile=base,
                                                  description='Logika L200 controller',
                                                  tags=['logika', 'L200'],
                                                  device_class='controller',
                                                  product_name='L200',
                                                  vendor_name='Logika'
                                                )

    #------ Add base profile properties
    
    client.account.properties(compressor.id).create(name='tagValue', data_type='string', access_type='protected', publish_type='never')

    client.account.properties(compressor.id).create(name='cfgSerialNumber', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='cfgLogikaModel', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='cfgLogikaFwVersion', data_type='string', access_type='protected', publish_type='never')    
    client.account.properties(compressor.id).create(name='cfgLevel1Pwd', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='cfgLevel2Pwd', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='cfgLevel3Pwd', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='activeAlarms', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='activeAlarmsNonAck', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='controllerState', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='compressorState', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='blockingAlarm', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='relayOutputs', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='digitalInputs', data_type='string', access_type='protected', publish_type='never')