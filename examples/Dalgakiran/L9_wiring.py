from connio.rest import Client
from connio.rest.api.v3.account.propertyy import PropertyInstance
from connio.rest.api.v3.account.method import MethodInstance

from readwrite_methods import *
from L9 import *

def wire(client):
    # Create Logika L9 profile
    compressor = client.account.deviceprofiles.create(name='LogikaL9', 
                                                  friendly_name='Logika L9 Controller',
                                                  base_profile='BaseLogikaProfile',
                                                  description='Logika L9 controller',
                                                  tags=['logika', 'L9'],
                                                  device_class='controller',
                                                  product_name='L9',
                                                  vendor_name='Logika'
                                                )
    #------ Add profile properties

    client.account.properties(compressor.id).create(name='P0x', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='H0x', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='t0x', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='PAx', data_type='object', access_type='protected', publish_type='never')

    #------ Add profile methods

    accessLevel2 = 'private'

    client.account.methods(compressor.id).create(name='fetchAlarmList', method_impl= MethodInstance.MethodImplementation(fetchAlarmList_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchReadRequest', method_impl= MethodInstance.MethodImplementation(fetchReadRequest_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchWriteRequest', method_impl= MethodInstance.MethodImplementation(fetchWriteRequest_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchModbusSettings', method_impl= MethodInstance.MethodImplementation(fetchModbusSettings_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchControllerStates', method_impl= MethodInstance.MethodImplementation(fetchControllerStates_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchCompressorStates', method_impl= MethodInstance.MethodImplementation(fetchCompressorStates_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchCompressorStateTypes', method_impl= MethodInstance.MethodImplementation(fetchCompressorStateTypes_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='hasInverter', method_impl= MethodInstance.MethodImplementation(hasInverter_body()), access_type=accessLevel2)
    
    # Controller specific SET methods (private)

    accessLevel3 = 'private'
    
    client.account.methods(compressor.id).create(name='setP0x', method_impl= MethodInstance.MethodImplementation(setP0x_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setH0x', method_impl= MethodInstance.MethodImplementation(setH0x_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='sett0x', method_impl= MethodInstance.MethodImplementation(sett0x_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setPAx', method_impl= MethodInstance.MethodImplementation(setPAx_body()), access_type=accessLevel3)

    # Controller specific tag R/W operations

    accessLevel4 = 'public'

    client.account.methods(compressor.id).create(name='sendCommand', method_impl= MethodInstance.MethodImplementation(sendCommand_body()), access_type=accessLevel4)
    #
    client.account.methods(compressor.id).create(name='readP0x', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('P0')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readH0x', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('H0')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readt0x', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('t0')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readPAx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('PA')), access_type=accessLevel4)
    #
    client.account.methods(compressor.id).create(name='writeP0x', method_impl= MethodInstance.MethodImplementation(writeP0x_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeH0x', method_impl= MethodInstance.MethodImplementation(writeH0x_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writet0x', method_impl= MethodInstance.MethodImplementation(writet0x_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writePAx', method_impl= MethodInstance.MethodImplementation(writePAx_body()), access_type=accessLevel4)