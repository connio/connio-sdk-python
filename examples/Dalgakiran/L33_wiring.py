from connio.rest import Client
from connio.rest.api.v3.account.propertyy import PropertyInstance
from connio.rest.api.v3.account.method import MethodInstance

from readwrite_methods import *
from L33 import *

def wire(client):
    # Create Logika L33 profile
    compressor = client.account.deviceprofiles.create(name='LogikaL33', 
                                                  friendly_name='Logika L33 Controller',
                                                  base_profile='BaseLogikaProfile',
                                                  description='Logika L3 controller',
                                                  tags=['logika', 'L3'],
                                                  device_class='controller',
                                                  product_name='L33',
                                                  vendor_name='Logika'
                                                )

    #------ Add profile properties

    client.account.properties(compressor.id).create(name="DisplayedState", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="SecondTemperature", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="SecondPressure", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="Drive24VSupply", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="DriveAnalogInput", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="RelativeSpeed", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="ConfigurationSwitches", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="Language", data_type='object', access_type='protected', publish_type='never')

    client.account.properties(compressor.id).create(name="ClockTimers", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="PressureSelectionBits", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="DaylightSavingTimeAdjustment", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="Indexes", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="MaintenanceOperationRecords", data_type='object', access_type='protected', publish_type='never')

    client.account.properties(compressor.id).create(name="DriveStatus", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="DriveMeasures", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="DriveFaultString", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="DriveCommands", data_type='object', access_type='protected', publish_type='never')

    client.account.properties(compressor.id).create(name="WPx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="SPx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="WPs", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="WPS2Px", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="WPS2Ps", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="WTx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="Wtx_", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="STAx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="ST3", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="STT1", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="STD1", data_type='object', access_type='protected', publish_type='never')    
    client.account.properties(compressor.id).create(name="R0x", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="DSx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="DAx", data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name="DFx", data_type='object', access_type='protected', publish_type='never')
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

    accessLevel3 = 'private'

    # Controller specific SET methods (private)
    client.account.methods(compressor.id).create(name='setDisplayedState', method_impl= MethodInstance.MethodImplementation(setDisplayedState_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSecondTemperature', method_impl= MethodInstance.MethodImplementation(setSecondTemperature_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSecondPressure', method_impl= MethodInstance.MethodImplementation(setSecondPressure_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDrive24VSupply', method_impl= MethodInstance.MethodImplementation(setDrive24VSupply_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDriveAnalogInput', method_impl= MethodInstance.MethodImplementation(setDriveAnalogInput_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setRelativeSpeed', method_impl= MethodInstance.MethodImplementation(setRelativeSpeed_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setConfigurationSwitches', method_impl= MethodInstance.MethodImplementation(setConfigurationSwitches_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setLanguage', method_impl= MethodInstance.MethodImplementation(setLanguage_body()), access_type=accessLevel3)
    
    client.account.methods(compressor.id).create(name='setClockTimers', method_impl= MethodInstance.MethodImplementation(setClockTimers_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setPressureSelectionBits', method_impl= MethodInstance.MethodImplementation(setPressureSelectionBits_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDaylightSavingTimeAdjustment', method_impl= MethodInstance.MethodImplementation(setDaylightSavingTimeAdjustment_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setIndexes', method_impl= MethodInstance.MethodImplementation(setIndexes_body()), access_type=accessLevel3)
    
    client.account.methods(compressor.id).create(name='setMaintenanceOperationRecords', method_impl= MethodInstance.MethodImplementation(setMaintenanceOperationRecords_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDriveStatus', method_impl= MethodInstance.MethodImplementation(setDriveStatus_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDriveMeasures', method_impl= MethodInstance.MethodImplementation(setDriveMeasures_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDriveFaultString', method_impl= MethodInstance.MethodImplementation(setDriveFaultString_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDriveCommands', method_impl= MethodInstance.MethodImplementation(setDriveCommands_body()), access_type=accessLevel3)
    
    client.account.methods(compressor.id).create(name='setWPx', method_impl= MethodInstance.MethodImplementation(setWPx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSPx', method_impl= MethodInstance.MethodImplementation(setSPx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSP5', method_impl= MethodInstance.MethodImplementation(setSP5_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSP6', method_impl= MethodInstance.MethodImplementation(setSP6_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setWPs', method_impl= MethodInstance.MethodImplementation(setWPs_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setWPS2Px', method_impl= MethodInstance.MethodImplementation(setWPS2Px_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setWPS2Ps', method_impl= MethodInstance.MethodImplementation(setWPS2Ps_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setWTx', method_impl= MethodInstance.MethodImplementation(setWTx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setWtx_', method_impl= MethodInstance.MethodImplementation(setWtx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSTAx', method_impl= MethodInstance.MethodImplementation(setSTAx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setST3', method_impl= MethodInstance.MethodImplementation(setST3_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSTT1', method_impl= MethodInstance.MethodImplementation(setSTT1_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setSTD1', method_impl= MethodInstance.MethodImplementation(setSTD1_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setR0x', method_impl= MethodInstance.MethodImplementation(setR0x_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setR03', method_impl= MethodInstance.MethodImplementation(setR03_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDSx', method_impl= MethodInstance.MethodImplementation(setDSx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDAx', method_impl= MethodInstance.MethodImplementation(setDAx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDFx', method_impl= MethodInstance.MethodImplementation(setDFx_body()), access_type=accessLevel3)
    client.account.methods(compressor.id).create(name='setDF7', method_impl= MethodInstance.MethodImplementation(setDF7_body()), access_type=accessLevel3)
   
    accessLevel4 = 'public'
     # Controller specific public methods
    client.account.methods(compressor.id).create(name='sendCommand', method_impl= MethodInstance.MethodImplementation(sendCommand_body()), access_type=accessLevel4)
    
    # Controller specific tag R/W operations - Read-only tags first
    client.account.methods(compressor.id).create(name='readDisplayedState', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DisplayedState')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSecondTemperature', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('SecondTemperature')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSecondPressure', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('SecondPressure')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDrive24VSupply', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('Drive24VSupply')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDriveAnalogInput', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DriveAnalogInput')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readClockTimers', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('ClockTimers')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDriveStatus', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DriveStatus')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDriveMeasures', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DriveMeasures')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDriveFaultString', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DriveFaultString')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDriveCommands', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DriveCommands')), access_type=accessLevel4)
    
    client.account.methods(compressor.id).create(name='readLanguage', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('Language')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readConfigurationSwitches', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('ConfigurationSwitches')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readPressureSelectionBits', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('PressureSelectionBits')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDaylightSaving', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DaylightSaving')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readIndexes', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('Indexes')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readMaintenanceOperationRecords', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('MaintenanceOperationRecords')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readWPx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WP')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSPx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('SP')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSP5', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('SP5')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSP6', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('SP6')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readWPs', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WPs')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readWPS2Px', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WPS2P')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readWPS2Ps', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WPS2Ps')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readWTx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('WT')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readWtx_', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('Wt_')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSTAx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('STA')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readST3', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('ST3')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSTT1', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('STT1')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readSTD1', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('STD1')), access_type=accessLevel4)    
    client.account.methods(compressor.id).create(name='readR0x', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('R0')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readR03', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('R03')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDSx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DS')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDAx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DA')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDFx', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DF')), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='readDF7', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('DF7')), access_type=accessLevel4)
    # Write Only Tags
    client.account.methods(compressor.id).create(name='writeRelativeSpeed', method_impl= MethodInstance.MethodImplementation(writeRelativeSpeed_body()), access_type=accessLevel4)
    # 
    client.account.methods(compressor.id).create(name='writeConfigurationSwitches', method_impl= MethodInstance.MethodImplementation(writeConfigurationSwitches_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeLanguage', method_impl= MethodInstance.MethodImplementation(writeLanguage_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeClockTimers', method_impl= MethodInstance.MethodImplementation(writeClockTimers_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writePressureSelectionBits', method_impl= MethodInstance.MethodImplementation(writePressureSelectionBits_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeIndexes', method_impl= MethodInstance.MethodImplementation(writeIndexes_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeMaintenanceOperationRecords', method_impl= MethodInstance.MethodImplementation(writeMaintenanceOperationRecords_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeWPx', method_impl= MethodInstance.MethodImplementation(writeWPx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeSPx', method_impl= MethodInstance.MethodImplementation(writeSPx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeSP5', method_impl= MethodInstance.MethodImplementation(writeSP5_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeSP6', method_impl= MethodInstance.MethodImplementation(writeSP6_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeWPs', method_impl= MethodInstance.MethodImplementation(writeWPs_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeWPS2Px', method_impl= MethodInstance.MethodImplementation(writeWPS2Px_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeWPS2Ps', method_impl= MethodInstance.MethodImplementation(writeWPS2Ps_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeWTx', method_impl= MethodInstance.MethodImplementation(writeWTx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeWtx_', method_impl= MethodInstance.MethodImplementation(writeWtx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeSTAx', method_impl= MethodInstance.MethodImplementation(writeSTAx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeST3', method_impl= MethodInstance.MethodImplementation(writeST3_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeSTT1', method_impl= MethodInstance.MethodImplementation(writeSTT1_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeSTD1', method_impl= MethodInstance.MethodImplementation(writeSTD1_body()), access_type=accessLevel4)    
    client.account.methods(compressor.id).create(name='writeR0x', method_impl= MethodInstance.MethodImplementation(writeR0x_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeR03', method_impl= MethodInstance.MethodImplementation(writeR03_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeDSx', method_impl= MethodInstance.MethodImplementation(writeDSx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeDAx', method_impl= MethodInstance.MethodImplementation(writeDAx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeDFx', method_impl= MethodInstance.MethodImplementation(writeDFx_body()), access_type=accessLevel4)
    client.account.methods(compressor.id).create(name='writeDF7', method_impl= MethodInstance.MethodImplementation(writeDF7_body()), access_type=accessLevel4)