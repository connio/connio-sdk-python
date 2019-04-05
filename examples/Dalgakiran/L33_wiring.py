from connio.rest import Client
from connio.rest.api.v3.account.propertyy import PropertyInstance
from connio.rest.api.v3.account.method import MethodInstance

from readwrite_methods import *
from L33 import *

def wire(client, name='LogikaL33', friendly="Logika L33 Controller", base="BaseLogikaProfile"):
    # Create Logika L33 profile
    compressor = client.account.deviceprofiles.create(name=name, 
                                                  friendly_name=friendly,
                                                  base_profile=base,
                                                  description='Logika L33 controller',
                                                  tags=['logika', 'L33'],
                                                  device_class='controller',
                                                  product_name='L33',
                                                  vendor_name='Logika'
                                                )

    #------ Add profile properties

    client.account.properties(compressor.id).create(name="workingFlags", data_type='object', access_type='protected', publish_type='never')
    unit = PropertyInstance.MeasurementUnit('Celsius', '°C')
    measurement = PropertyInstance.Measurement('temperature', unit)
    client.account.properties(compressor.id).create(name='secondTemperature', data_type='number', access_type='protected', publish_type='never', 
          description='Secondary Temperature (°C * 10)', measurement=measurement, boundaries={'min': -10, 'max': 125})    
    unit = PropertyInstance.MeasurementUnit('Bar', 'bar')
    measurement = PropertyInstance.Measurement('pressure', unit)
    client.account.properties(compressor.id).create(name='secondPressure', data_type='number', access_type='protected', publish_type='never', 
          description='Secondary Pressure (Bar * 10)', measurement=measurement, boundaries={'min': 0, 'max': 16})    
    unit = PropertyInstance.MeasurementUnit('Volt', 'V')
    measurement = PropertyInstance.Measurement('electricity', unit)
    client.account.properties(compressor.id).create(name='drive24VSupply', data_type='number', access_type='protected', publish_type='never', 
          description='Drive 24V Supply (V * 10)', measurement=measurement, boundaries={'min': 0, 'max': 300})
    client.account.properties(compressor.id).create(name='driveAnalogInput', data_type='number', access_type='protected', publish_type='never', 
          description='Drive analog Input (V * 10)', measurement=measurement, boundaries={'min': 0, 'max': 300})  
    client.account.properties(compressor.id).create(name='configSwitches', data_type='object', access_type='protected', publish_type='never')

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

    condition = PropertyInstance.Condition(when=PropertyInstance.Condition.ConditionType.CHANGED)
    retention = PropertyInstance.Retention(context=PropertyInstance.Context(type='default'), capacity='0', condition=condition)
    client.account.properties(compressor.id).create(name="driveStatus", data_type='string', access_type='protected', publish_type='never', retention=retention)
    client.account.properties(compressor.id).create(name="driveMeasures", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="driveFaultString", data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="driveCommands", data_type='string', access_type='protected', publish_type='never')

    client.account.properties(compressor.id).create(name="WPx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="SPx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="WPs", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="WPS2Px", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="WPS2Ps", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="WTx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="Wtx_", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="STAx", data_type='object', access_type='protected', publish_type='never')
    #client.account.properties(compressor.id).create(name="ST3", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="STT1", data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="STD1", data_type='number', access_type='protected', publish_type='never')    
    client.account.properties(compressor.id).create(name="R0x", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="DSx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="DAx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="DFx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="V0x", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="D1", data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="D3", data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="D6", data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="D7", data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="Sx", data_type='object', access_type='protected', publish_type='never')

  
    #------ Add profile methods

    accessLevel2 = 'private'

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
    client.account.methods(compressor.id).create(name='setWorkingFlags', method_impl= MethodInstance.MethodImplementation(setWorkingFlags_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSecondTemperature', method_impl= MethodInstance.MethodImplementation(setSecondTemperature_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSecondPressure', method_impl= MethodInstance.MethodImplementation(setSecondPressure_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDrive24VSupply', method_impl= MethodInstance.MethodImplementation(setDrive24VSupply_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDriveAnalogInput', method_impl= MethodInstance.MethodImplementation(setDriveAnalogInput_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setConfigSwitches', method_impl= MethodInstance.MethodImplementation(setConfigSwitches_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDriveStatus', method_impl= MethodInstance.MethodImplementation(setDriveStatus_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDriveMeasures', method_impl= MethodInstance.MethodImplementation(setDriveMeasures_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDriveFaultString', method_impl= MethodInstance.MethodImplementation(setDriveFaultString_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDriveCommands', method_impl= MethodInstance.MethodImplementation(setDriveCommands_body()), access_type=accessLevel3)
    
    client.account.methods(compressor.id).create(name='setWPx', method_impl= MethodInstance.MethodImplementation(setWPx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSPx', method_impl= MethodInstance.MethodImplementation(setSPx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSP5', method_impl= MethodInstance.MethodImplementation(setSP5_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSP6', method_impl= MethodInstance.MethodImplementation(setSP6_body()), access_type=accessLevel3)
    #client.account.methods(compressor.id).create(name='setWPs', method_impl= MethodInstance.MethodImplementation(setWPs_body()), access_type=accessLevel3)
    #client.account.methods(compressor.id).create(name='setWPS2Px', method_impl= MethodInstance.MethodImplementation(setWPS2Px_body()), access_type=accessLevel3)
    #client.account.methods(compressor.id).create(name='setWPS2Ps', method_impl= MethodInstance.MethodImplementation(setWPS2Ps_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setWTx', method_impl= MethodInstance.MethodImplementation(setWTx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setWtx_', method_impl= MethodInstance.MethodImplementation(setWtx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSTAx', method_impl= MethodInstance.MethodImplementation(setSTAx_body()), access_type=accessLevel3)
    #client.account.methods(compressor.id).create(name='setST3', method_impl= MethodInstance.MethodImplementation(setST3_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSTT1', method_impl= MethodInstance.MethodImplementation(setSTT1_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSTD1', method_impl= MethodInstance.MethodImplementation(setSTD1_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setR0x', method_impl= MethodInstance.MethodImplementation(setR0x_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDSx', method_impl= MethodInstance.MethodImplementation(setDSx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDAx', method_impl= MethodInstance.MethodImplementation(setDAx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDFx', method_impl= MethodInstance.MethodImplementation(setDFx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setV0x', method_impl= MethodInstance.MethodImplementation(setV0x_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setD6', method_impl= MethodInstance.MethodImplementation(setD6_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setD7', method_impl= MethodInstance.MethodImplementation(setD7_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setD1', method_impl= MethodInstance.MethodImplementation(setD1_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setD3', method_impl= MethodInstance.MethodImplementation(setD3_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS12_S13_S14', method_impl= MethodInstance.MethodImplementation(setS12_S13_S14_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS02', method_impl= MethodInstance.MethodImplementation(setS02_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS07', method_impl= MethodInstance.MethodImplementation(setS07_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS08_S09', method_impl= MethodInstance.MethodImplementation(setS08_S09_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS11', method_impl= MethodInstance.MethodImplementation(setS11_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS16', method_impl= MethodInstance.MethodImplementation(setS16_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS15', method_impl= MethodInstance.MethodImplementation(setS15_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS21_S22', method_impl= MethodInstance.MethodImplementation(setS21_S22_body()), access_type=accessLevel3)

    #client.account.methods(compressor.id).create(name='setDF7', method_impl= MethodInstance.MethodImplementation(setDF7_body()), access_type=accessLevel3)


    client.account.methods(compressor.id).create(name='makeCompressorCommand', method_impl= MethodInstance.MethodImplementation(makeCompressorCommand_body()), access_type='protected')

    accessLevel4 = 'public'
    
    # Controller specific public methods
    client.account.methods(compressor.id).create(name='hasInverter', method_impl= MethodInstance.MethodImplementation(hasInverter_body()), access_type=accessLevel4)
    
    # Controller specific tag R/W operations - Read-only tags first
    client.account.methods(compressor.id).create(name='readWorkingFlags', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('workingFlags')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSecondTemperature', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('secondTemperature')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSecondPressure', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('secondPressure')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDrive24VSupply', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('drive24VSupply')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDriveAnalogInput', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('driveAnalogInput')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readConfigSwitches', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('configSwitches')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDriveStatus', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('driveStatus')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDriveMeasures', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('driveMeasures')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDriveFaultString', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('driveFaultString')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDriveCommands', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('driveCommands')), access_type=accessLevel4)
        
    client.account.methods(compressor.id).create(name='readWPx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WP')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSPx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('SP')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSP5', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('SP5')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSP6', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('SP6')), access_type=accessLevel4)
    #client.account.methods(compressor.id).create(name='readWPs', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WPs')), access_type=accessLevel4)
    #client.account.methods(compressor.id).create(name='readWPS2Px', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WPS2P')), access_type=accessLevel4)
    #client.account.methods(compressor.id).create(name='readWPS2Ps', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WPS2Ps')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readWTx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WT')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readWtx_', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('Wt')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSTAx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('STA')), access_type=accessLevel4)
    #client.account.methods(compressor.id).create(name='readST3', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('ST3')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSTT1', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('STT1')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSTD1', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('STD1')), access_type=accessLevel4)    
    client.account.methods(compressor.id).create(name='readR0x', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('R0')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDSx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DS')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDAx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DA')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDFx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DF')), access_type=accessLevel4)
    #client.account.methods(compressor.id).create(name='readDF7', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DF7')), access_type=accessLevel4)
    
    # Write Only Tags
    client.account.methods(compressor.id).create(name='writeRelativeSpeed', method_impl= MethodInstance.MethodImplementation(writeRelativeSpeed_body()), access_type=accessLevel4)
    # 
    client.account.methods(compressor.id).create(name='writeLevel1Password', method_impl= MethodInstance.MethodImplementation(writeLevel1Password_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeLevel2Password', method_impl= MethodInstance.MethodImplementation(writeLevel2Password_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeLevel3Password', method_impl= MethodInstance.MethodImplementation(writeLevel3Password_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeConfigSwitches', method_impl= MethodInstance.MethodImplementation(writeConfigSwitches_body()), access_type=accessLevel4)    
    client.account.methods(compressor.id).create(name='writeWPx', method_impl= MethodInstance.MethodImplementation(writeWPx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeSPx', method_impl= MethodInstance.MethodImplementation(writeSPx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeSP5', method_impl= MethodInstance.MethodImplementation(writeSP5_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeSP6', method_impl= MethodInstance.MethodImplementation(writeSP6_body()), access_type=accessLevel4)
    #client.account.methods(compressor.id).create(name='writeWPs', method_impl= MethodInstance.MethodImplementation(writeWPs_body()), access_type=accessLevel4)
    #client.account.methods(compressor.id).create(name='writeWPS2Px', method_impl= MethodInstance.MethodImplementation(writeWPS2Px_body()), access_type=accessLevel4)
    #client.account.methods(compressor.id).create(name='writeWPS2Ps', method_impl= MethodInstance.MethodImplementation(writeWPS2Ps_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeWTx', method_impl= MethodInstance.MethodImplementation(writeWTx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeWtx_', method_impl= MethodInstance.MethodImplementation(writeWtx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeSTAx', method_impl= MethodInstance.MethodImplementation(writeSTAx_body()), access_type=accessLevel4)
    #client.account.methods(compressor.id).create(name='writeST3', method_impl= MethodInstance.MethodImplementation(writeST3_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeSTT1', method_impl= MethodInstance.MethodImplementation(writeSTT1_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeSTD1', method_impl= MethodInstance.MethodImplementation(writeSTD1_body()), access_type=accessLevel4)    
    client.account.methods(compressor.id).create(name='writeR0x', method_impl= MethodInstance.MethodImplementation(writeR0x_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeDSx', method_impl= MethodInstance.MethodImplementation(writeDSx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeDAx', method_impl= MethodInstance.MethodImplementation(writeDAx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeDFx', method_impl= MethodInstance.MethodImplementation(writeDFx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeV0x', method_impl= MethodInstance.MethodImplementation(writeV0x_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeD6', method_impl= MethodInstance.MethodImplementation(writeD6_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeD7', method_impl= MethodInstance.MethodImplementation(writeD7_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeD1', method_impl= MethodInstance.MethodImplementation(writeD1_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeD3', method_impl= MethodInstance.MethodImplementation(writeD3_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS12_S13_S14', method_impl= MethodInstance.MethodImplementation(writeS12_S13_S14_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS02', method_impl= MethodInstance.MethodImplementation(writeS02_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS07', method_impl= MethodInstance.MethodImplementation(writeS07_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS08_S09', method_impl= MethodInstance.MethodImplementation(writeS08_S09_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS11', method_impl= MethodInstance.MethodImplementation(writeS11_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS16', method_impl= MethodInstance.MethodImplementation(writeS16_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS15', method_impl= MethodInstance.MethodImplementation(writeS15_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS21_S22', method_impl= MethodInstance.MethodImplementation(writeS21_S22_body()), access_type=accessLevel4)
    #client.account.methods(compressor.id).create(name='writeDF7', method_impl= MethodInstance.MethodImplementation(writeDF7_body()), access_type=accessLevel4)