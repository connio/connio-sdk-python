from connio.rest import Client
from connio.rest.api.v3.account.propertyy import PropertyInstance
from connio.rest.api.v3.account.method import MethodInstance

from readwrite_methods import *
from L200 import *

def wire(client, name='LogikaL200', friendly="Logika L200 Controller", base="BaseLogikaProfile"):
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
    client.account.properties(compressor.id).create(name='activeAlarms', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='activeAlarms_Slave1', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='activeAlarms_Slave2', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='activeAlarms_Slave3', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='activeAlarms_Slave4', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='activeAlarmsNonAck', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='controllerState', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='compressorState', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='blockingAlarm', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='relayOutputs', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='digitalInputs', data_type='string', access_type='protected', publish_type='never')
    
    client.account.properties(compressor.id).create(name="AmbientTemperature", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="InternalVoltageVcc", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="InternalVoltageVL", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="ResidualCompressorCapacity", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="ExcessCompressorCapacity", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="CurrentStopPressure", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="CurrentStartPressure", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="CurrentTotalPower", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="AverageAirDelivery", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="CurrentTotalAirDelivery", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="CompressorsConfigured", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="CompressorsSlave", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="CompressorsSetToMaintenance", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="CompressorsAvailable", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="CompressorsSelected", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="CompressorsOn", data_type='object', access_type='protected', publish_type='never')

    client.account.properties(compressor.id).create(name="WPx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="WTx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="Vx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="Sx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="Rx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="T01", data_type='object', access_type='protected', publish_type='never')
      
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
    client.account.methods(compressor.id).create(name='setAmbientTemperature', method_impl= MethodInstance.MethodImplementation(setAmbientTemperature_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setInternalVoltageVcc', method_impl= MethodInstance.MethodImplementation(setInternalVoltageVcc_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setInternalVoltageVL', method_impl= MethodInstance.MethodImplementation(setInternalVoltageVL_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setResidualCompressorCapacity', method_impl= MethodInstance.MethodImplementation(setResidualCompressorCapacity_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setExcessCompressorCapacity', method_impl= MethodInstance.MethodImplementation(setExcessCompressorCapacity_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setCurrentStopPressure', method_impl= MethodInstance.MethodImplementation(setCurrentStopPressure_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setCurrentStartPressure', method_impl= MethodInstance.MethodImplementation(setCurrentStartPressure_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setCurrentTotalPower', method_impl= MethodInstance.MethodImplementation(setCurrentTotalPower_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setAverageAirDelivery', method_impl= MethodInstance.MethodImplementation(setAverageAirDelivery_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setCurrentTotalAirDelivery', method_impl= MethodInstance.MethodImplementation(setCurrentTotalAirDelivery_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setCompressorsConfigured', method_impl= MethodInstance.MethodImplementation(setCompressorsConfigured_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setCompressorsSlave', method_impl= MethodInstance.MethodImplementation(setCompressorsSlave_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setCompressorsSetToMaintenance', method_impl= MethodInstance.MethodImplementation(setCompressorsSetToMaintenance_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setCompressorsAvailable', method_impl= MethodInstance.MethodImplementation(setCompressorsAvailable_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setCompressorsSelected', method_impl= MethodInstance.MethodImplementation(setCompressorsSelected_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setCompressorsOn', method_impl= MethodInstance.MethodImplementation(setCompressorsOn_body()), access_type=accessLevel3)


    client.account.methods(compressor.id).create(name='setR02', method_impl= MethodInstance.MethodImplementation(setR02_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setV01', method_impl= MethodInstance.MethodImplementation(setV01_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setWPx', method_impl= MethodInstance.MethodImplementation(setWPx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setWTx', method_impl= MethodInstance.MethodImplementation(setWTx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setV04', method_impl= MethodInstance.MethodImplementation(setV04_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setV02_V03', method_impl= MethodInstance.MethodImplementation(setV02_V03_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setV07', method_impl= MethodInstance.MethodImplementation(setV07_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS11', method_impl= MethodInstance.MethodImplementation(setS11_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setT01', method_impl= MethodInstance.MethodImplementation(setT01_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS14', method_impl= MethodInstance.MethodImplementation(setS14_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setR01', method_impl= MethodInstance.MethodImplementation(setR01_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS00_S01_S02', method_impl= MethodInstance.MethodImplementation(setS00_S01_S02_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS09_S10', method_impl= MethodInstance.MethodImplementation(setS09_S10_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS06', method_impl= MethodInstance.MethodImplementation(setS06_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS05', method_impl= MethodInstance.MethodImplementation(setS05_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS07_S08', method_impl= MethodInstance.MethodImplementation(setS07_S08_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS12_S13', method_impl= MethodInstance.MethodImplementation(setS12_S13_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS17', method_impl= MethodInstance.MethodImplementation(setS17_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS16', method_impl= MethodInstance.MethodImplementation(setS16_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS03_S04', method_impl= MethodInstance.MethodImplementation(setS03_S04_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS18_S19', method_impl= MethodInstance.MethodImplementation(setS18_S19_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS21', method_impl= MethodInstance.MethodImplementation(setS21_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS20', method_impl= MethodInstance.MethodImplementation(setS20_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setS22', method_impl= MethodInstance.MethodImplementation(setS22_body()), access_type=accessLevel3)

    accessLevel4 = 'public'

    # Controller specific tag R/W operations - Read-only tags first
    client.account.methods(compressor.id).create(name='readAmbientTemperature', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('AmbientTemperature')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readInternalVoltageVcc', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('InternalVoltageVcc')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readInternalVoltageVL', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('InternalVoltageVL')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readResidualCompressorCapacity', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('ResidualCompressorCapacity')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readExcessCompressorCapacity', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('ExcessCompressorCapacity')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readCurrentStopPressure', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('CurrentStopPressure')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readCurrentStartPressure', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('CurrentStartPressure')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readCurrentTotalPower', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('CurrentTotalPower')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readAverageAirDelivery', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('AverageAirDelivery')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readCurrentTotalAirDelivery', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('CurrentTotalAirDelivery')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readCompressorsConfigured', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('CompressorsConfigured')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readCompressorsSlave', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('CompressorsSlave')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readCompressorsSetToMaintenance', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('CompressorsSetToMaintenance')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readCompressorsAvailable', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('CompressorsAvailable')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readCompressorsSelected', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('CompressorsSelected')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readCompressorsOn', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('CompressorsOn')), access_type=accessLevel4)


    client.account.methods(compressor.id).create(name='readWPx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WP')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readWTx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WT')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readR02', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('R02')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readV01', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('V01')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readV04', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('V04')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readV02_V03', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('V02')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readV07', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('V07')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS11', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S11')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readT01', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('T01')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS14', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('RS14')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readR01', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('R01')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS00_S01_S02', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S00')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS09_S10', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S09')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS06', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S06')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS05', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S05')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS07', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S07')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS12_S13', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S12')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS17', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S17')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS16', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S16')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS03_S04', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S03')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS18_S19', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S18')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS21', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S21')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS20', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S20')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readS22', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('S22')), access_type=accessLevel4)

    client.account.methods(compressor.id).create(name='writeWTx', method_impl= MethodInstance.MethodImplementation(writeWTx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeWPx', method_impl= MethodInstance.MethodImplementation(writeWPx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeR02', method_impl= MethodInstance.MethodImplementation(writeR02_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeV01', method_impl= MethodInstance.MethodImplementation(writeV01_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeV04', method_impl= MethodInstance.MethodImplementation(writeV04_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeV02_V03', method_impl= MethodInstance.MethodImplementation(writeV02_V03_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeV07', method_impl= MethodInstance.MethodImplementation(writeV07_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS11', method_impl= MethodInstance.MethodImplementation(writeS11_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeT01', method_impl= MethodInstance.MethodImplementation(writeT01_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS14', method_impl= MethodInstance.MethodImplementation(writeS14_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeR01', method_impl= MethodInstance.MethodImplementation(writeR01_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS00_S01_S02', method_impl= MethodInstance.MethodImplementation(writeS00_S01_S02_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS09_S10', method_impl= MethodInstance.MethodImplementation(writeS09_S10_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS06', method_impl= MethodInstance.MethodImplementation(writeS06_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS05', method_impl= MethodInstance.MethodImplementation(writeS05_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS07_S08', method_impl= MethodInstance.MethodImplementation(writeS07_S08_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS12_S13', method_impl= MethodInstance.MethodImplementation(writeS12_S13_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS17', method_impl= MethodInstance.MethodImplementation(writeS17_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS16', method_impl= MethodInstance.MethodImplementation(writeS16_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS03_S04', method_impl= MethodInstance.MethodImplementation(writeS03_S04_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS18_S19', method_impl= MethodInstance.MethodImplementation(writeS18_S19_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS21', method_impl= MethodInstance.MethodImplementation(writeS21_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS20', method_impl= MethodInstance.MethodImplementation(writeS20_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeS22', method_impl= MethodInstance.MethodImplementation(writeS22_body()), access_type=accessLevel4)