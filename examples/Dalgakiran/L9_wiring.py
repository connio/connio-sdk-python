# -*- coding: utf-8 -*-
from connio.rest import Client
from connio.rest.api.v3.account.propertyy import PropertyInstance
from connio.rest.api.v3.account.method import MethodInstance

from readwrite_methods import *
from L9 import *

def wire(client, name="LogikaL9", friendly="Logika L9 Controller", base="BaseLogikaProfile"):
    # Create Logika L9 profile
    compressor = client.account.deviceprofiles.create(name=name, 
                                                  friendly_name=friendly,
                                                  base_profile=base,
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
    client.account.properties(compressor.id).create(name='r__', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='S_h', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='Fad', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='S__', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='Inx', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='rL5', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='con', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='nc', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='OFl', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='dry', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='E_h', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='SPd', data_type='number', access_type='protected', publish_type='never')
    # client.account.properties(compressor.id).create(name='PAx', data_type='object', access_type='protected', publish_type='never')

    #------ Add profile methods

    accessLevel2 = 'private'

    client.account.methods(compressor.id).create(name='fetchAlarmList', method_impl= MethodInstance.MethodImplementation(fetchAlarmList_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchReadRequest', method_impl= MethodInstance.MethodImplementation(fetchReadRequest_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchWriteRequest', method_impl= MethodInstance.MethodImplementation(fetchWriteRequest_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchModbusSettings', method_impl= MethodInstance.MethodImplementation(fetchModbusSettings_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchControllerStates', method_impl= MethodInstance.MethodImplementation(fetchControllerStates_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchCompressorStates', method_impl= MethodInstance.MethodImplementation(fetchCompressorStates_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchCompressorStateTypes', method_impl= MethodInstance.MethodImplementation(fetchCompressorStateTypes_body()), access_type=accessLevel2)
    
    # Controller specific SET methods (private)

    accessLevel3 = 'private'
    
    client.account.methods(compressor.id).create(name='setRelayOutputs', method_impl= MethodInstance.MethodImplementation(setRelayOutputs_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDigitalInputs', method_impl= MethodInstance.MethodImplementation(setDigitalInputs_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setP0x', method_impl= MethodInstance.MethodImplementation(setP0x_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setH0x', method_impl= MethodInstance.MethodImplementation(setH0x_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='sett0x', method_impl= MethodInstance.MethodImplementation(sett0x_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setr__', method_impl= MethodInstance.MethodImplementation(setr___body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS_h', method_impl= MethodInstance.MethodImplementation(setS_h_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setFad', method_impl= MethodInstance.MethodImplementation(setFad_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setInx', method_impl= MethodInstance.MethodImplementation(setInx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setrL5', method_impl= MethodInstance.MethodImplementation(setrL5_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setcon', method_impl= MethodInstance.MethodImplementation(setcon_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setnc', method_impl= MethodInstance.MethodImplementation(setnc_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setOFl', method_impl= MethodInstance.MethodImplementation(setOFl_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setdry', method_impl= MethodInstance.MethodImplementation(setdry_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setE_h', method_impl= MethodInstance.MethodImplementation(setE_h_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSPd', method_impl= MethodInstance.MethodImplementation(setSPd_body()), access_type=accessLevel3)
    # client.account.methods(compressor.id).create(name='setPAx', method_impl= MethodInstance.MethodImplementation(setPAx_body()), access_type=accessLevel3)

    client.account.methods(compressor.id).create(name='makeCompressorCommand', method_impl= MethodInstance.MethodImplementation(makeCompressorCommand_body()), access_type='protected')

    # Controller specific tag R/W operations

    accessLevel4 = 'public'

    client.account.methods(compressor.id).create(name='hasInverter', method_impl= MethodInstance.MethodImplementation(hasInverter_body()), access_type=accessLevel4)
    #
    client.account.methods(compressor.id).create(name='readP0x', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('P0')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readH0x', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('H0')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readt0x', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('t0')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readr__', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('r__')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS_h', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S_h')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readFad', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('Fad')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS__', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S__')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readInx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('In')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readrL5', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('rL5')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readcon', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('con')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readnc', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('nc')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readOFl', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('OFl')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readdry', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('dry')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readE_h', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('E_h')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSPd', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('SPd')), access_type=accessLevel4)
    # client.account.methods(compressor.id).create(name='readPAx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('PA')), access_type=accessLevel4)
    #
    client.account.methods(compressor.id).create(name='writeLevel1Password', method_impl= MethodInstance.MethodImplementation(writeLevel1Password_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeLevel2Password', method_impl= MethodInstance.MethodImplementation(writeLevel2Password_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeP0x', method_impl= MethodInstance.MethodImplementation(writeP0x_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeH0x', method_impl= MethodInstance.MethodImplementation(writeH0x_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writet0x', method_impl= MethodInstance.MethodImplementation(writet0x_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writer__', method_impl= MethodInstance.MethodImplementation(writer___body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS_h', method_impl= MethodInstance.MethodImplementation(writeS_h_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeFad', method_impl= MethodInstance.MethodImplementation(writeFad_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS__', method_impl= MethodInstance.MethodImplementation(writeS___body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeInx', method_impl= MethodInstance.MethodImplementation(writeInx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writerL5', method_impl= MethodInstance.MethodImplementation(writerL5_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writecon', method_impl= MethodInstance.MethodImplementation(writecon_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writenc', method_impl= MethodInstance.MethodImplementation(writenc_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeOFl', method_impl= MethodInstance.MethodImplementation(writeOFl_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writedry', method_impl= MethodInstance.MethodImplementation(writedry_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeE_h', method_impl= MethodInstance.MethodImplementation(writeE_h_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeSPd', method_impl= MethodInstance.MethodImplementation(writeSPd_body()), access_type=accessLevel4)

    # client.account.methods(compressor.id).create(name='writePAx', method_impl= MethodInstance.MethodImplementation(writePAx_body()), access_type=accessLevel4)