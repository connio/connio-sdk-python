# -*- coding: utf-8 -*-
from connio.rest import Client
from connio.rest.api.v3.account.propertyy import PropertyInstance
from connio.rest.api.v3.account.method import MethodInstance

from readwrite_methods import *
from L26 import *

def wire(client, name="LogikaL26", friendly="Logika L26 Controller", base="BaseLogikaProfile"):
    # Create Logika L26 profile
    compressor = client.account.deviceprofiles.create(name=name, 
                                                  friendly_name=friendly,
                                                  base_profile=base,
                                                  description='Logika L26 controller',
                                                  tags=['logika', 'L26'],
                                                  device_class='controller',
                                                  product_name='L26',
                                                  vendor_name='Logika'
                                                )

    #------ Add profile properties

    unit = PropertyInstance.MeasurementUnit('Bar', 'bar')
    measurement = PropertyInstance.Measurement('pressure', unit)
    client.account.properties(compressor.id).create(name='auxPressure', data_type='number', access_type='protected', publish_type='never', measurement=measurement, boundaries={'min': 0, 'max': 16})
    
    unit = PropertyInstance.MeasurementUnit('Volt', 'V')
    measurement = PropertyInstance.Measurement('electricity', unit)
    client.account.properties(compressor.id).create(name='ptcInput', data_type='number', access_type='protected', publish_type='never', measurement=measurement, boundaries={'min': 0, 'max': 300})
    
    unit = PropertyInstance.MeasurementUnit('Frequence', 'Hz')
    measurement = PropertyInstance.Measurement('custom', unit)
    client.account.properties(compressor.id).create(name='analogueOutFreq', data_type='number', access_type='protected', publish_type='never', 
      measurement=measurement, boundaries={'min': 0, 'max': 400})
  
    client.account.properties(compressor.id).create(name='configSwitches', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='configSelections', data_type='object', access_type='protected', publish_type='never')

    condition = PropertyInstance.Condition(when=PropertyInstance.Condition.ConditionType.CHANGED)
    retention = PropertyInstance.Retention(context=PropertyInstance.Context(type='default'), capacity='0', condition=condition)
    client.account.properties(compressor.id).create(name="driveStatus", data_type='string', access_type='protected', publish_type='never', retention=retention)
    #
    client.account.properties(compressor.id).create(name="driveMeasures", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="driveFaultString", data_type='string', access_type='protected', publish_type='never')

    # Inverter properties
    unit = PropertyInstance.MeasurementUnit('RPM', 'rpm')
    measurement = PropertyInstance.Measurement('custom', unit)
    client.account.properties(compressor.id).create(name='motorSpeed', data_type='number', access_type='protected', publish_type='never', measurement=measurement)
    unit = PropertyInstance.MeasurementUnit('Frequence', 'Hz')
    measurement = PropertyInstance.Measurement('custom', unit)
    client.account.properties(compressor.id).create(name='motorFrequency', data_type='number', access_type='protected', publish_type='never', measurement=measurement)
    unit = PropertyInstance.MeasurementUnit('Current', 'A')
    measurement = PropertyInstance.Measurement('electricity', unit)
    client.account.properties(compressor.id).create(name='motorCurrent', data_type='number', access_type='protected', publish_type='never', measurement=measurement)

    client.account.properties(compressor.id).create(name='WPx', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='WTx', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='Wtx_', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='C07_x', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='C02', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='C08', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='C10', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='C07_5', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='C25', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='APx', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='C19_x', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='PIx', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='FRx', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='PTx', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='PM1', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='AOx', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='C20_x', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='C22', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='DRx', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='DAx', data_type='object', access_type='protected', publish_type='never')

    #------ Add profile methods

    accessLevel2 = 'private'

    # Overriden methods
    client.account.methods(compressor.id).create(name='fetchAlarmList', method_impl= MethodInstance.MethodImplementation(fetchAlarmList_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchReadRequest', method_impl= MethodInstance.MethodImplementation(fetchReadRequest_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchWriteRequest', method_impl= MethodInstance.MethodImplementation(fetchWriteRequest_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchModbusSettings', method_impl= MethodInstance.MethodImplementation(fetchModbusSettings_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchControllerStates', method_impl= MethodInstance.MethodImplementation(fetchControllerStates_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchCompressorStates', method_impl= MethodInstance.MethodImplementation(fetchCompressorStates_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='fetchCompressorStateTypes', method_impl= MethodInstance.MethodImplementation(fetchCompressorStateTypes_body()), access_type=accessLevel2)
    
    accessLevel3 = 'private'

    # Controller specific SET methods (private)
    client.account.methods(compressor.id).create(name='setRelayOutputs', method_impl= MethodInstance.MethodImplementation(setRelayOutputs_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDigitalInputs', method_impl= MethodInstance.MethodImplementation(setDigitalInputs_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setAuxPressure', method_impl= MethodInstance.MethodImplementation(setAuxPressure_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setPTCInput', method_impl= MethodInstance.MethodImplementation(setPTCInput_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setAnalogueOutFreq', method_impl= MethodInstance.MethodImplementation(setAnalogueOutFreq_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setConfigSwitches', method_impl= MethodInstance.MethodImplementation(setConfigSwitches_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setConfigSelections', method_impl= MethodInstance.MethodImplementation(setConfigSelections_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDriveStatus', method_impl= MethodInstance.MethodImplementation(setDriveStatus_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDriveMeasures', method_impl= MethodInstance.MethodImplementation(setDriveMeasures_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDriveFaultString', method_impl= MethodInstance.MethodImplementation(setDriveFaultString_body()), access_type=accessLevel3)

    client.account.methods(compressor.id).create(name='setWPx', method_impl= MethodInstance.MethodImplementation(setWPx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setWTx', method_impl= MethodInstance.MethodImplementation(setWTx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setWtx_', method_impl= MethodInstance.MethodImplementation(setWtx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setC07_x', method_impl= MethodInstance.MethodImplementation(setC07x_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setC08', method_impl= MethodInstance.MethodImplementation(setC08_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setC02', method_impl= MethodInstance.MethodImplementation(setC02_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setC10', method_impl= MethodInstance.MethodImplementation(setC10_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setC07_5', method_impl= MethodInstance.MethodImplementation(setC07_5_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setC25', method_impl= MethodInstance.MethodImplementation(setC25_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setAPx', method_impl= MethodInstance.MethodImplementation(setAPx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setC19_x', method_impl= MethodInstance.MethodImplementation(setC19x_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setPIx', method_impl= MethodInstance.MethodImplementation(setPIx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setFRx', method_impl= MethodInstance.MethodImplementation(setFRx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setPTx', method_impl= MethodInstance.MethodImplementation(setPTx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setPM1', method_impl= MethodInstance.MethodImplementation(setPM1_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setAOx', method_impl= MethodInstance.MethodImplementation(setAOx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setC20_x', method_impl= MethodInstance.MethodImplementation(setC20x_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setC22', method_impl= MethodInstance.MethodImplementation(setC22_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDRx', method_impl= MethodInstance.MethodImplementation(setDRx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDAx', method_impl= MethodInstance.MethodImplementation(setDAx_body()), access_type=accessLevel3)

    client.account.methods(compressor.id).create(name='makeCompressorCommand', method_impl= MethodInstance.MethodImplementation(makeCompressorCommand_body()), access_type='protected')

    accessLevel4 = 'public'
       
    # Controller specific public methods
    client.account.methods(compressor.id).create(name='hasInverter', method_impl= MethodInstance.MethodImplementation(hasInverter_body()), access_type=accessLevel4)
    
    # Controller specific tag R/W operations - Read-only tags first
    client.account.methods(compressor.id).create(name='readAuxPressure', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('auxPressure')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readPTCInput', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('ptcInput')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readAnalogueOutFreq', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('analogueOut')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readConfigSwitches', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('configSwitches')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readConfigSelections', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('configSelections')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDriveStatus', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('driveStatus')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDriveMeasures', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('driveMeasures')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDriveFaultString', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('driveFaultString')), access_type=accessLevel4)

    #
    client.account.methods(compressor.id).create(name='readWPx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WP')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readWTx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WT')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readWtx_', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('Wt')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readC07_x', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('C07')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readC02', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('C02')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readC08', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('C08')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readC10', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('C10')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readC07_5', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('C07_5')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readC25', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('C25')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readAPx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('AP')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readC19_x', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('C19')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readPIx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('PI')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readFRx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('FR')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readPTx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('PT')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readPM1', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('PM1')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readAOx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('AO')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readC20_x', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('C20')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readC22', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('C22')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDRx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DR')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDAx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DA')), access_type=accessLevel4)

    #
    client.account.methods(compressor.id).create(name='writeWPx', method_impl= MethodInstance.MethodImplementation(writeWPx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeWTx', method_impl= MethodInstance.MethodImplementation(writeWTx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeWtx_', method_impl= MethodInstance.MethodImplementation(writeWtx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeC07_x', method_impl= MethodInstance.MethodImplementation(writeC07x_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeC02', method_impl= MethodInstance.MethodImplementation(writeC02_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeC08', method_impl= MethodInstance.MethodImplementation(writeC08_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeC10', method_impl= MethodInstance.MethodImplementation(writeC10_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeC07_5', method_impl= MethodInstance.MethodImplementation(writeC07_5_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeC25', method_impl= MethodInstance.MethodImplementation(writeC25_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeAPx', method_impl= MethodInstance.MethodImplementation(writeAPx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeAP4', method_impl= MethodInstance.MethodImplementation(writeAP4_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeC19_1', method_impl= MethodInstance.MethodImplementation(writeC19_1_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeC19_2', method_impl= MethodInstance.MethodImplementation(writeC19_2_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writePIx', method_impl= MethodInstance.MethodImplementation(writePIx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeFRx', method_impl= MethodInstance.MethodImplementation(writeFRx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writePTx', method_impl= MethodInstance.MethodImplementation(writePTx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writePM1', method_impl= MethodInstance.MethodImplementation(writePM1_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeAOx', method_impl= MethodInstance.MethodImplementation(writeAOx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeC20_x', method_impl= MethodInstance.MethodImplementation(writeC20x_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeC2x', method_impl= MethodInstance.MethodImplementation(writeC22_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeDRx', method_impl= MethodInstance.MethodImplementation(writeDRx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeDAx', method_impl= MethodInstance.MethodImplementation(writeDAx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeLevel1Password', method_impl= MethodInstance.MethodImplementation(writeLevel1Password_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeLevel2Password', method_impl= MethodInstance.MethodImplementation(writeLevel2Password_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeLevel3Password', method_impl= MethodInstance.MethodImplementation(writeLevel3Password_body()), access_type=accessLevel4)

