# ~fetchAlarmList()
# ~fetchReadRequestList()
# ~fetchWriteRequestList()
# ~fetchModbusSettings()
# ~fetchControllerStates()
# ~fetchCompressorStates()
# ~fetchCompressorStateTypes()
# ~hasInverter()

#
#
#
def fetchAlarmList_body():
    return """/**
    Gets the controller specific alarm list
*/
return { list: [ 
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,1), code: 'A01', label: "Emergency Stop" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,2), code: 'A02', label: "Motor Overheat" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,3), code: 'A03', label: "Fan Overheat" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,4), code: 'A04', label: "Door Open" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,5), code: 'A05', label: "AC Phase Missing" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,6), code: 'A06', label: "Phase Sequence Wrong" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,7), code: 'A07', label: "Input Common Missing" },
 //
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,0), code: 'A08', label: "High Work Press" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,1), code: 'A09', label: "Screw Temperature Fault" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,2), code: 'A10', label: "High Screw Temperature" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,3), code: 'A11', label: "Low Screw Temperature" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,4), code: 'A12', label: "Black Out" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,5), code: 'A13', label: "RS232-1 Fault" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,6), code: 'A14', label: "Low Voltage" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,7), code: 'A15', label: "Fieldbus Error" },
 //
 { byteNo: 3, type: 'alarm', bit: Math.pow(2,4), code: 'A20', label: "Separator Filter" },
 { byteNo: 3, type: 'alarm', bit: Math.pow(2,5), code: 'A21', label: "PTC Motor" },
 { byteNo: 3, type: 'alarm', bit: Math.pow(2,6), code: 'A22', label: "Work Press Fault" },
 //
 { byteNo: 4, type: 'alarm', bit: Math.pow(2,0), code: 'A24', label: "Security" },
 { byteNo: 4, type: 'alarm', bit: Math.pow(2,2), code: 'A26', label: "Maint C H Blk" },
 { byteNo: 4, type: 'warning', bit: Math.pow(2,6), code: 'A30', label: "EEPROM Fault" },
 { byteNo: 4, type: 'warning', bit: Math.pow(2,7), code: 'A31', label: "Air Filter" },
 //
 { byteNo: 5, type: 'warning', bit: Math.pow(2,0), code: 'A32', label: "Screw Temp Warning" },
 { byteNo: 5, type: 'warning', bit: Math.pow(2,1), code: 'A33', label: "Low Voltage Warning" },
 { byteNo: 5, type: 'warning', bit: Math.pow(2,2), code: 'A34', label: "High Voltage" },
 { byteNo: 5, type: 'warning', bit: Math.pow(2,3), code: 'A35', label: "RS232-2 Fault" },
 { byteNo: 5, type: 'warning', bit: Math.pow(2,4), code: 'A36', label: "Too Many Starts" },
 { byteNo: 5, type: 'warning', bit: Math.pow(2,5), code: 'A37', label: "Multi Unit Fault" },
 //
 { byteNo: 6, type: 'warning', bit: Math.pow(2,0), code: 'A40', label: "Restart Changed to Manual" },
 { byteNo: 6, type: 'warning', bit: Math.pow(2,1), code: 'A41', label: "Restart Changed to Auto" },
 { byteNo: 6, type: 'alarm', bit: Math.pow(2,5), code: 'A45', label: "Bearing High Temperature" },
 { byteNo: 6, type: 'alarm', bit: Math.pow(2,6), code: 'A46', label: "Low Aux Pressure" },
 { byteNo: 6, type: 'alarm', bit: Math.pow(2,7), code: 'A47', label: "High Temperature" },
 //
 { byteNo: 7, type: 'warning', bit: Math.pow(2,2), code: 'A50', label: "Change Air Filter" },
 { byteNo: 7, type: 'warning', bit: Math.pow(2,3), code: 'A51', label: "Change Oil Filter" },
 { byteNo: 7, type: 'warning', bit: Math.pow(2,4), code: 'A52', label: "Change Sep Filter" },
 { byteNo: 7, type: 'warning', bit: Math.pow(2,5), code: 'A53', label: "Change Oil" },
 { byteNo: 7, type: 'warning', bit: Math.pow(2,6), code: 'A54', label: "Check Compressor" },
 { byteNo: 7, type: 'warning', bit: Math.pow(2,7), code: 'A55', label: "Check Bearings" },
 //
 { byteNo: 9, type: 'warning', bit: Math.pow(2,1), code: 'A65', label: "Time Keeper Fault" },
 { byteNo: 9, type: 'warning', bit: Math.pow(2,2), code: 'A66', label: "High Safety Temperature" },
 { byteNo: 9, type: 'warning', bit: Math.pow(2,3), code: 'A67', label: "High Safety Temperature Soft" },
 { byteNo: 9, type: 'warning', bit: Math.pow(2,4), code: 'A68', label: "Exp Temperatue Fault" },
 { byteNo: 9, type: 'warning', bit: Math.pow(2,5), code: 'A69', label: "Delta Temperature" }, 
 { byteNo: 9, type: 'warning', bit: Math.pow(2,6), code: 'A70', label: "Dryer Temperature" }, 
 { byteNo: 9, type: 'alarm', bit: Math.pow(2,7), code: 'A71', label: "Delta Press Filter" }, 
 //
 { byteNo: 10, type: 'warning', bit: Math.pow(2,0), code: 'A72', label: "Delta Press Filter Warning" },
 { byteNo: 10, type: 'warning', bit: Math.pow(2,1), code: 'A73', label: "Exp Press Fault" },
 { byteNo: 10, type: 'warning', bit: Math.pow(2,2), code: 'A74', label: "DST Adjuster" },
 { byteNo: 10, type: 'warning', bit: Math.pow(2,7), code: 'A79', label: "Exp Temperature Warning" },
 //
 { byteNo: 11, type: 'alarm', bit: Math.pow(2,0), code: 'A80', label: "Drive Fault" },
 { byteNo: 11, type: 'warning', bit: Math.pow(2,1), code: 'A81', label: "Drive Warning" },
 { byteNo: 11, type: 'alarm', bit: Math.pow(2,3), code: 'A83', label: "Drive No Comm" },
],
blackOutCode: 'A12' };
"""

#
#
#
def fetchReadRequest_body():
    return """/**

*/
const requests = {
  cfgSerialNumber:                  { request: "r,meth:setSerialNumber,-,20,-,1,0x00" },
  cfgLogikaModel:                   { request: "r,meth:setLogikaModel,-,2,-,1,0x0A" },
  cfgLogikaFwVersion:               { request: "r,meth:setLogikaFwVersion,-,2,-,1,0x0B" },
  cfgLevel1Pwd:                     { request: "r,meth:setLevel1Pwd,-,6,-,1,0x100" },
  cfgMaintCycles:                   { request: "r,meth:setMaintCycles,-,12,-,1,0x52C" },
  totalHours:                       { request: "r,meth:setTotalHours,-,4,-,1,0x600" },
  totalLoadHours:                   { request: "r,meth:setTotalLoadHours,-,4,-,1,0x602" },
  maintCounters:                    { request: "r,meth:setMaintCounters,-,24,-,1,0x604" },
  loadPercInLast100h:               { request: "r,meth:setLoadPercInLast100h,-,2,-,1,0x610" },
  nbrOfStartsInLastHour:            { request: "r,meth:setNbrOfStartsInLastHour,-,2,-,1,0x611" },
  controllerTime:                   { request: "r,meth:setControllerTime,-,8,-,1,0x800" },
  // ---- Controller specific ----
  IOBoardFwVersion:                 { request: "r,meth:setIOBoardFwVersion,-,2,-,1,0x0D" },
  workingFlags:                     { request: "r,meth:setWorkingFlags,-,2,-,1,0x403" },
  secondTemperature:                { request: "r,meth:setSecondTemperature,-,2,-,1,0x408" },
  secondPressure:                   { request: "r,meth:setSecondPressure,-,2,-,1,0x409" },
  configSwitches:                   { request: "r,meth:setConfigSwitches,-,4,-,1,0x500" },
  drive24VSupply:                   { request: "r,meth:setDrive24VSupply,-,2,-,1,0x40B" },
  driveAnalogInput:                 { request: "r,meth:setDriveAnalogInput,-,2,-,1,0x40C" },
  driveStatus:                      { request: "r,meth:setDriveStatus,-,2,-,1,0xA00" },
  driveMeasures:                    { request: "r,meth:setDriveMeasures,-,20,-,1,0xA01" },
  driveFaultString:                 { request: "r,meth:setDriveFaultString,-,26,-,1,0xA0B" },
  driveCommands:                    { request: "r,meth:setDriveCommands,-,2,-,1,0xA18" },

  //
  AmbientTemperature:               { request: "r,meth:setAmbientTemperature,-,2,-,1,0x405" ),
  InternalVoltageVcc:               { request: "r,meth:setInternalVoltageVcc,-,2,-,1,0x406" ),
  InternalVoltageVL:                { request: "r,meth:setInternalVoltageVL,-,2,-,1,0x407" ),
  ResidualCompressorCapacity:       { request: "r,meth:setResidualCompressorCapacity,-,2,-,1,0x408" ),
  ExcessCompressorCapacity:         { request: "r,meth:setExcessCompressorCapacity,-,2,-,1,0x409" ),
  CurrentStopPressure:              { request: "r,meth:setCurrentStopPressure,-,2,-,1,0x40A" ),
  CurrentStartPressure:             { request: "r,meth:setCurrentStartPressure,-,2,-,1,0x40B" ),
  CurrentTotalPower:                { request: "r,meth:setCurrentTotalPower,-,4,-,1,0x40C" ),
  AverageAirDelivery:               { request: "r,meth:setAverageAirDelivery,-,4,-,1,0x40E" ),
  CurrentTotalAirDelivery:          { request: "r,meth:setCurrentTotalAirDelivery,-,4,-,1,0x410" ),
  CompressorsConfigured:            { request: "r,meth:setCompressorsConfigured,-,2,-,1,0x412" ),
  CompressorsSlave:                 { request: "r,meth:setCompressorsSlave,-,2,-,1,0x413" ),
  CompressorsSetToMaintenance:      { request: "r,meth:setCompressorsSetToMaintenance,-,2,-,1,0x414" ),
  CompressorsAvailable:             { request: "r,meth:setCompressorsAvailable,-,2,-,1,0x415" ),
  CompressorsSelected:              { request: "r,meth:setCompressorsSelected,-,2,-,1,0x416" ),
  CompressorsOn:                    { request: "r,meth:setCompressorsOn,-,2,-,1,0x417" ),
  TotalEnergyConsumption:           { request: "r,meth:setTotalEnergyConsumption,-,4,-,1,0x600" ),
  AirProduced:                      { request: "r,meth:setAirProduced,-,4,-,1,0x602" ),
  //Slave Read Tags
  SlaveFwVersion_Comp0:             { request: "r,meth:setSlaveFwVersion_Comp0,-,2,-,1,0x1000" ),
  SlaveFwVersion_Comp1:             { request: "r,meth:setSlaveFwVersion_Comp1,-,2,-,1,0x1100" ),
  SlaveFwVersion_Comp2:             { request: "r,meth:setSlaveFwVersion_Comp2,-,2,-,1,0x1200" ),
  SlaveFwVersion_Comp3:             { request: "r,meth:setSlaveFwVersion_Comp3,-,2,-,1,0x1300" ),
  SlaveControllerState_Comp0:       { request: "r,meth:setSlaveControllerState_Comp0,-,2,-,1,0x1001" ),
  SlaveControllerState_Comp1:       { request: "r,meth:setSlaveControllerState_Comp1,-,2,-,1,0x1101" ),
  SlaveControllerState_Comp2:       { request: "r,meth:setSlaveControllerState_Comp2,-,2,-,1,0x1201" ),
  SlaveControllerState_Comp3:       { request: "r,meth:setSlaveControllerState_Comp3,-,2,-,1,0x1301" ),
  SlaveRelativeSpeed_Comp0:         { request: "r,meth:setSlaveRelativeSpeed_Comp0,-,2,-,1,0x1002" ),
  SlaveRelativeSpeed_Comp1:         { request: "r,meth:setSlaveRelativeSpeed_Comp1,-,2,-,1,0x1102" ),
  SlaveRelativeSpeed_Comp2:         { request: "r,meth:setSlaveRelativeSpeed_Comp2,-,2,-,1,0x1202" ),
  SlaveRelativeSpeed_Comp3:         { request: "r,meth:setSlaveRelativeSpeed_Comp3,-,2,-,1,0x1302" ),
  SlaveControllerType_Comp0:        { request: "r,meth:setSlaveControllerType_Comp0,-,2,-,1,0x1004" ),
  SlaveControllerType_Comp1:        { request: "r,meth:setSlaveControllerType_Comp1,-,2,-,1,0x1104" ),
  SlaveControllerType_Comp2:        { request: "r,meth:setSlaveControllerType_Comp2,-,2,-,1,0x1204" ),
  SlaveControllerType_Comp3:        { request: "r,meth:setSlaveControllerType_Comp3,-,2,-,1,0x1304" ),
  SlaveSelenoidDelay_Comp0:         { request: "r,meth:setSlaveSelenoidDelay_Comp0,-,2,-,1,0x1005" ),
  SlaveSelenoidDelay_Comp1:         { request: "r,meth:setSlaveSelenoidDelay_Comp1,-,2,-,1,0x1105" ),
  SlaveSelenoidDelay_Comp2:         { request: "r,meth:setSlaveSelenoidDelay_Comp2,-,2,-,1,0x1205" ),
  SlaveSelenoidDelay_Comp3:         { request: "r,meth:setSlaveSelenoidDelay_Comp3,-,2,-,1,0x1305" ),
  SlaveAirFlow_Comp0:               { request: "r,meth:setSlaveAirFlow_Comp0,-,2,-,1,0x1006" ),
  SlaveAirFlow_Comp1:               { request: "r,meth:setSlaveAirFlow_Comp1,-,2,-,1,0x1106" ),
  SlaveAirFlow_Comp2:               { request: "r,meth:setSlaveAirFlow_Comp2,-,2,-,1,0x1206" ),
  SlaveAirFlow_Comp3:               { request: "r,meth:setSlaveAirFlow_Comp3,-,2,-,1,0x1306" ),

  SlaveNominalPower_Comp0:          { request: "r,meth:setSlaveNominalPower_Comp0,-,2,-,1,0x1008" ),
  SlaveNominalPower_Comp1:          { request: "r,meth:setSlaveNominalPower_Comp1,-,2,-,1,0x1108" ),
  SlaveNominalPower_Comp2:          { request: "r,meth:setSlaveNominalPower_Comp2,-,2,-,1,0x1208" ),
  SlaveNominalPower_Comp3:          { request: "r,meth:setSlaveNominalPower_Comp3,-,2,-,1,0x1308" ),
  SlaveUnloadPower_Comp0:           { request: "r,meth:setSlaveUnloadPower_Comp0,-,2,-,1,0x1009" ),
  SlaveUnloadPower_Comp1:           { request: "r,meth:setSlaveUnloadPower_Comp1,-,2,-,1,0x1109" ),
  SlaveUnloadPower_Comp2:           { request: "r,meth:setSlaveUnloadPower_Comp2,-,2,-,1,0x1209" ),
  SlaveUnloadPower_Comp3:           { request: "r,meth:setSlaveUnloadPower_Comp3,-,2,-,1,0x1309" ),
  SlavePriorityInS0_Comp0:          { request: "r,meth:setSlavePriorityInS0_Comp0,-,2,-,1,0x100A" ),
  SlavePriorityInS0_Comp1:          { request: "r,meth:setSlavePriorityInS0_Comp1,-,2,-,1,0x110A" ),
  SlavePriorityInS0_Comp2:          { request: "r,meth:setSlavePriorityInS0_Comp2,-,2,-,1,0x120A" ),
  SlavePriorityInS0_Comp3:          { request: "r,meth:setSlavePriorityInS0_Comp3,-,2,-,1,0x130A" ),
  SlavePriorityInS1_Comp0:          { request: "r,meth:setSlavePriorityInS1_Comp0,-,2,-,1,0x100B" ),
  SlavePriorityInS1_Comp1:          { request: "r,meth:setSlavePriorityInS1_Comp1,-,2,-,1,0x110B" ),
  SlavePriorityInS1_Comp2:          { request: "r,meth:setSlavePriorityInS1_Comp2,-,2,-,1,0x120B" ),
  SlavePriorityInS1_Comp3:          { request: "r,meth:setSlavePriorityInS1_Comp3,-,2,-,1,0x130B" ),
  SlavePriorityInS2_Comp0:          { request: "r,meth:setSlavePriorityInS2_Comp0,-,2,-,1,0x100C" ),
  SlavePriorityInS2_Comp1:          { request: "r,meth:setSlavePriorityInS2_Comp1,-,2,-,1,0x110C" ),
  SlavePriorityInS2_Comp2:          { request: "r,meth:setSlavePriorityInS2_Comp2,-,2,-,1,0x120C" ),
  SlavePriorityInS2_Comp3:          { request: "r,meth:setSlavePriorityInS2_Comp3,-,2,-,1,0x130C" ),
  SlavePriorityInS3_Comp0:          { request: "r,meth:setSlavePriorityInS3_Comp0,-,2,-,1,0x100D" ),
  SlavePriorityInS3_Comp1:          { request: "r,meth:setSlavePriorityInS3_Comp1,-,2,-,1,0x110D" ),
  SlavePriorityInS3_Comp2:          { request: "r,meth:setSlavePriorityInS3_Comp2,-,2,-,1,0x120D" ),
  SlavePriorityInS3_Comp3:          { request: "r,meth:setSlavePriorityInS3_Comp3,-,2,-,1,0x130D" ),
  SlaveUnloadTime_Comp0:            { request: "r,meth:setSlaveUnloadTime_Comp0,-,2,-,1,0x100E" ),
  SlaveUnloadTime_Comp1:            { request: "r,meth:setSlaveUnloadTime_Comp1,-,2,-,1,0x110E" ),
  SlaveUnloadTime_Comp2:            { request: "r,meth:setSlaveUnloadTime_Comp2,-,2,-,1,0x120E" ),
  SlaveUnloadTime_Comp3:            { request: "r,meth:setSlaveUnloadTime_Comp3,-,2,-,1,0x130E" ),
  SlaveSafetyTime_Comp0:            { request: "r,meth:setSlaveSafetyTime_Comp0,-,2,-,1,0x100F" ),
  SlaveSafetyTime_Comp1:            { request: "r,meth:setSlaveSafetyTime_Comp1,-,2,-,1,0x110F" ),
  SlaveSafetyTime_Comp2:            { request: "r,meth:setSlaveSafetyTime_Comp2,-,2,-,1,0x120F" ),
  SlaveSafetyTime_Comp3:            { request: "r,meth:setSlaveSafetyTime_Comp3,-,2,-,1,0x130F" ),
  SlaveStartsHour_Comp0:            { request: "r,meth:setSlaveStartsHour_Comp0,-,2,-,1,0x1010" ),
  SlaveStartsHour_Comp1:            { request: "r,meth:setSlaveStartsHour_Comp1,-,2,-,1,0x1110" ),
  SlaveStartsHour_Comp2:            { request: "r,meth:setSlaveStartsHour_Comp2,-,2,-,1,0x1210" ),
  SlaveStartsHour_Comp3:            { request: "r,meth:setSlaveStartsHour_Comp3,-,2,-,1,0x1310" ),
  SlaveAnalogInput_Comp0:           { request: "r,meth:setSlaveAnalogInput_Comp0,-,2,-,1,0x1011" ),
  SlaveAnalogInput_Comp1:           { request: "r,meth:setSlaveAnalogInput_Comp1,-,2,-,1,0x1111" ),
  SlaveAnalogInput_Comp2:           { request: "r,meth:setSlaveAnalogInput_Comp2,-,2,-,1,0x1211" ),
  SlaveAnalogInput_Comp3:           { request: "r,meth:setSlaveAnalogInput_Comp3,-,2,-,1,0x1311" ),
  SlaveExcludedForMaint_Comp0:      { request: "r,meth:setSlaveExcludedForMaint_Comp0,-,2,-,1,0x1012" ),
  SlaveExcludedForMaint_Comp1:      { request: "r,meth:setSlaveExcludedForMaint_Comp1,-,2,-,1,0x1112" ),
  SlaveExcludedForMaint_Comp2:      { request: "r,meth:setSlaveExcludedForMaint_Comp2,-,2,-,1,0x1212" ),
  SlaveExcludedForMaint_Comp3:      { request: "r,meth:setSlaveExcludedForMaint_Comp3,-,2,-,1,0x1312" ),
  SlaveEnableMaintenance_Comp0:     { request: "r,meth:setSlaveEnableMaintenance_Comp0,-,2,-,1,0x1013" ),
  SlaveEnableMaintenance_Comp1:     { request: "r,meth:setSlaveEnableMaintenance_Comp1,-,2,-,1,0x1113" ),
  SlaveEnableMaintenance_Comp2:     { request: "r,meth:setSlaveEnableMaintenance_Comp2,-,2,-,1,0x1213" ),
  SlaveEnableMaintenance_Comp3:     { request: "r,meth:setSlaveEnableMaintenance_Comp3,-,2,-,1,0x1313" ),
  SlaveChangeAirFilter_Comp0:       { request: "r,meth:setSlaveChangeAirFilter_Comp0,-,2,-,1,0x1014" ),
  SlaveChangeAirFilter_Comp1:       { request: "r,meth:setSlaveChangeAirFilter_Comp1,-,2,-,1,0x1114" ),
  SlaveChangeAirFilter_Comp2:       { request: "r,meth:setSlaveChangeAirFilter_Comp2,-,2,-,1,0x1214" ),
  SlaveChangeAirFilter_Comp3:       { request: "r,meth:setSlaveChangeAirFilter_Comp3,-,2,-,1,0x1314" ),
  SlaveChangeOilFilter_Comp0:       { request: "r,meth:setSlaveChangeOilFilter_Comp0,-,2,-,1,0x1015" ),
  SlaveChangeOilFilter_Comp1:       { request: "r,meth:setSlaveChangeOilFilter_Comp1,-,2,-,1,0x1115" ),
  SlaveChangeOilFilter_Comp2:       { request: "r,meth:setSlaveChangeOilFilter_Comp2,-,2,-,1,0x1215" ),
  SlaveChangeOilFilter_Comp3:       { request: "r,meth:setSlaveChangeOilFilter_Comp3,-,2,-,1,0x1315" ),
  SlaveChangeSeperatorFilter_Comp0: { request: "r,meth:setSlaveChangeSeperatorFilter_Comp0,-,2,-,1,0x1016" ),
  SlaveChangeSeperatorFilter_Comp1: { request: "r,meth:setSlaveChangeSeperatorFilter_Comp1,-,2,-,1,0x1116" ),
  SlaveChangeSeperatorFilter_Comp2: { request: "r,meth:setSlaveChangeSeperatorFilter_Comp2,-,2,-,1,0x1216" ),
  SlaveChangeSeperatorFilter_Comp3: { request: "r,meth:setSlaveChangeSeperatorFilter_Comp3,-,2,-,1,0x1316" ),
  SlaveChangeOil_Comp0:             { request: "r,meth:setSlaveChangeOil_Comp0,-,2,-,1,0x1017" ),
  SlaveChangeOil_Comp1:             { request: "r,meth:setSlaveChangeOil_Comp1,-,2,-,1,0x1117" ),
  SlaveChangeOil_Comp2:             { request: "r,meth:setSlaveChangeOil_Comp2,-,2,-,1,0x1217" ),
  SlaveChangeOil_Comp3:             { request: "r,meth:setSlaveChangeOil_Comp3,-,2,-,1,0x1317" ),
  SlaveCheckCompressor_Comp0:       { request: "r,meth:setSlaveCheckCompressor_Comp0,-,2,-,1,0x1018" ),
  SlaveCheckCompressor_Comp1:       { request: "r,meth:setSlaveCheckCompressor_Comp1,-,2,-,1,0x1118" ),
  SlaveCheckCompressor_Comp2:       { request: "r,meth:setSlaveCheckCompressor_Comp2,-,2,-,1,0x1218" ),
  SlaveCheckCompressor_Comp3:       { request: "r,meth:setSlaveCheckCompressor_Comp3,-,2,-,1,0x1318" ),
  SlaveBearingLubrication_Comp0:    { request: "r,meth:setSlaveBearingLubrication_Comp0,-,2,-,1,0x1019" ),
  SlaveBearingLubrication_Comp1:    { request: "r,meth:setSlaveBearingLubrication_Comp1,-,2,-,1,0x1119" ),
  SlaveBearingLubrication_Comp2:    { request: "r,meth:setSlaveBearingLubrication_Comp2,-,2,-,1,0x1219" ),
  SlaveBearingLubrication_Comp3:    { request: "r,meth:setSlaveBearingLubrication_Comp3,-,2,-,1,0x1319" ),
  SlaveNumberOfTotalCompressorHours_Comp0:    { request: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp0,-,4,-,1,0x101A" ),
  SlaveNumberOfTotalCompressorHours_Comp1:    { request: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp1,-,4,-,1,0x111A" ),
  SlaveNumberOfTotalCompressorHours_Comp2:    { request: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp2,-,4,-,1,0x121A" ),
  SlaveNumberOfTotalCompressorHours_Comp3:    { request: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp3,-,4,-,1,0x131A" ),
  SlaveNumberOfLoadCompressorHours_Comp0:     { request: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp0,-,4,-,1,0x101C" ),
  SlaveNumberOfLoadCompressorHours_Comp1:     { request: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp1,-,4,-,1,0x111C" ),
  SlaveNumberOfLoadCompressorHours_Comp2:     { request: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp2,-,4,-,1,0x121C" ),
  SlaveNumberOfLoadCompressorHours_Comp3:     { request: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp3,-,4,-,1,0x131C" ),
  SlaveMaintCounters_Comp0:                   { request: "r,meth:setSlaveMaintCounters_Comp0,-,24,-,1,0x101E" ),
  SlaveMaintCounters_Comp1:                   { request: "r,meth:setSlaveMaintCounters_Comp1,-,24,-,1,0x111E" ),
  SlaveMaintCounters_Comp2:                   { request: "r,meth:setSlaveMaintCounters_Comp2,-,24,-,1,0x121E" ),
  SlaveMaintCounters_Comp3:                   { request: "r,meth:setSlaveMaintCounters_Comp3,-,24,-,1,0x131E" ),
  
  //
  R02:                               { request: "r,meth:setR02,-,2,-,1,0x500" },
  V01:                               { request: "r,meth:setV01,-,2,-,1,0x501" },
  WPx:                               { request: "r,meth:setWPx,-,12,-,1,0x502" },
  WTx:                               { request: "r,meth:setWTx,-,8,-,1,0x508" },
  V04:                               { request: "r,meth:setV04,-,2,-,1,0x50C" },
  V02:                               { request: "r,meth:setV02_V03,-,4,-,1,0x50D" },
  V07:                               { request: "r,meth:setV07, -,2,-,0x50F" },
  S11:                               { request: "r,meth:setS11, -,2,-,0x510" },
  T01:                               { request: "r,meth:setT01, -,2,-,0x511" },
  S14:                               { request: "r,meth:setS14, -,2,-,0x512" },
  R01:                               { request: "r,meth:setR01, -,2,-,0x513" },
  S00:                               { request: "r,meth:setS00_S01_S02, -,6,-,0x514" },
  S09:                               { request: "r,meth:setS09_S10, -,4,-,0x517" },
  S06:                               { request: "r,meth:setS06, -,2,-,0x519" },
  S05:                               { request: "r,meth:setS05, -,2,-,0x51A" },
  S07:                               { request: "r,meth:setS07_S08, -,4,-,0x51B" },
  S12:                               { request: "r,meth:setS12_S13, -,4,-,0x51D" },
  S17:                               { request: "r,meth:setS17, -,2,-,0x51F" },
  S16:                               { request: "r,meth:setS16, -,2,-,0x520" },
  S03:                               { request: "r,meth:setS03_S04, -,4,-,0x521" },
  S18:                               { request: "r,meth:setS18_S19, -,4,-,0x523" },
  S21:                               { request: "r,meth:setS21, -,2,-,0x525" },
  S20:                               { request: "r,meth:setS20, -,2,-,0x526" },
  S22:                               { request: "r,meth:setS22, -,2,-,0x527" },
};
return requests[value].request;
"""

#
#
#
def fetchWriteRequest_body():
    return """/**

*/
const requests = {
    cfgLevel1Pwd:                               { rprop:"cfgLevel1Pwd", rcmd: "r,meth:setLevel1Pwd,-,6,-,1,0x100", min: 1, max: 1, offset: "0x100"},
    TotalEnergyConsumption:                     { rprop:"TotalEnergyConsumption", rcmd: "r,meth:setTotalEnergyConsumption,-,4,-,1,0x600", min: 1, max: 1 offset: "0X600", multiplier: [10] },
    AirProduced:                                { rprop:"AirProduced", rcmd: "r,meth:setAirProduced,-,4,-,1,0x602", min: 1, max: 1 offset: "0x602"},
    //Slave Write Tags
    SlaveControllerType_Comp0:                  { rprob: "SlaveControllerType_Comp0", rcmd: "r,meth:setSlaveControllerType_Comp0,-,2,-,0x1004", min: 1, max: 1, offset:"0x1004" },
    SlaveControllerType_Comp1:                  { rprob: "SlaveControllerType_Comp1", rcmd: "r,meth:setSlaveControllerType_Comp1,-,2,-,0x1104", min: 1, max: 1, offset:"0x1104" },
    SlaveControllerType_Comp2:                  { rprob: "SlaveControllerType_Comp2", rcmd: "r,meth:setSlaveControllerType_Comp2,-,2,-,0x1204", min: 1, max: 1, offset:"0x1204" },
    SlaveControllerType_Comp3:                  { rprob: "SlaveControllerType_Comp3", rcmd: "r,meth:setSlaveControllerType_Comp3,-,2,-,0x1304", min: 1, max: 1, offset:"0x1304" },
    SlaveSelenoidDelay_Comp0:                   { rprob: "SlaveSelenoidDelay_Comp0", rcmd: "r,meth:setSlaveSelenoidDelay_Comp0,-,2,-,0x1005", min: 1, max: 1, offset:"0x1005" },
    SlaveSelenoidDelay_Comp1:                   { rprob: "SlaveSelenoidDelay_Comp1", rcmd: "r,meth:setSlaveSelenoidDelay_Comp1,-,2,-,0x1105", min: 1, max: 1, offset:"0x1105" },
    SlaveSelenoidDelay_Comp2:                   { rprob: "SlaveSelenoidDelay_Comp2", rcmd: "r,meth:setSlaveSelenoidDelay_Comp2,-,2,-,0x1205", min: 1, max: 1, offset:"0x1205" },
    SlaveSelenoidDelay_Comp3:                   { rprob: "SlaveSelenoidDelay_Comp3", rcmd: "r,meth:setSlaveSelenoidDelay_Comp3,-,2,-,0x1305", min: 1, max: 1, offset:"0x1305" },
    SlaveAirFlow_Comp0:                         { rprob: "SlaveAirFlow_Comp0", rcmd: "r,meth:setSlaveAirFlow_Comp0,-,2,-,0x1006", min: 1, max: 1, offset:"0x1006", multiplier: [10] },
    SlaveAirFlow_Comp1:                         { rprob: "SlaveAirFlow_Comp1", rcmd: "r,meth:setSlaveAirFlow_Comp1,-,2,-,0x1106", min: 1, max: 1, offset:"0x1106", multiplier: [10] },
    SlaveAirFlow_Comp2:                         { rprob: "SlaveAirFlow_Comp2", rcmd: "r,meth:setSlaveAirFlow_Comp2,-,2,-,0x1206", min: 1, max: 1, offset:"0x1206", multiplier: [10] },
    SlaveAirFlow_Comp3:                         { rprob: "SlaveAirFlow_Comp3", rcmd: "r,meth:setSlaveAirFlow_Comp3,-,2,-,0x1306", min: 1, max: 1, offset:"0x1306", multiplier: [10] },
    SlaveNominalPower_Comp0:                    { rprob: "SlaveNominalPower_Comp0", rcmd: "r,meth:setSlaveNominalPower_Comp0,-,2,-,0x1008", min: 1, max: 1, offset:"0x1008" },
    SlaveNominalPower_Comp1:                    { rprob: "SlaveNominalPower_Comp1", rcmd: "r,meth:setSlaveNominalPower_Comp1,-,2,-,0x1108", min: 1, max: 1, offset:"0x1108" },
    SlaveNominalPower_Comp2:                    { rprob: "SlaveNominalPower_Comp2", rcmd: "r,meth:setSlaveNominalPower_Comp2,-,2,-,0x1208", min: 1, max: 1, offset:"0x1208" },
    SlaveNominalPower_Comp3:                    { rprob: "SlaveNominalPower_Comp3", rcmd: "r,meth:setSlaveNominalPower_Comp3,-,2,-,0x1308", min: 1, max: 1, offset:"0x1308" },
    SlaveUnloadPower_Comp0:                     { rprob: "SlaveUnloadPower_Comp0", rcmd: "r,meth:setSlaveUnloadPower_Comp0,-,2,-,0x1009", min: 1, max: 1, offset:"0x1009" },
    SlaveUnloadPower_Comp1:                     { rprob: "SlaveUnloadPower_Comp1", rcmd: "r,meth:setSlaveUnloadPower_Comp1,-,2,-,0x1109", min: 1, max: 1, offset:"0x1109" },
    SlaveUnloadPower_Comp2:                     { rprob: "SlaveUnloadPower_Comp2", rcmd: "r,meth:setSlaveUnloadPower_Comp2,-,2,-,0x1209", min: 1, max: 1, offset:"0x1209" },
    SlaveUnloadPower_Comp3:                     { rprob: "SlaveUnloadPower_Comp3", rcmd: "r,meth:setSlaveUnloadPower_Comp3,-,2,-,0x1309", min: 1, max: 1, offset:"0x1309" },
    SlavePriorityInS0_Comp0:                    { rprob: "SlavePriorityInS0_Comp0", rcmd: "r,meth:setSlavePriorityInS0_Comp0,-,2,-,0x100A", min: 1, max: 1, offset:"0x100A" },
    SlavePriorityInS0_Comp1:                    { rprob: "SlavePriorityInS0_Comp1", rcmd: "r,meth:setSlavePriorityInS0_Comp1,-,2,-,0x110A", min: 1, max: 1, offset:"0x110A" },
    SlavePriorityInS0_Comp2:                    { rprob: "SlavePriorityInS0_Comp2", rcmd: "r,meth:setSlavePriorityInS0_Comp2,-,2,-,0x120A", min: 1, max: 1, offset:"0x120A" },
    SlavePriorityInS0_Comp3:                    { rprob: "SlavePriorityInS0_Comp3", rcmd: "r,meth:setSlavePriorityInS0_Comp3,-,2,-,0x130A", min: 1, max: 1, offset:"0x130A" },
    SlavePriorityInS1_Comp0:                    { rprob: "SlavePriorityInS1_Comp0", rcmd: "r,meth:setSlavePriorityInS1_Comp0,-,2,-,0x100B", min: 1, max: 1, offset:"0x100B" },
    SlavePriorityInS1_Comp1:                    { rprob: "SlavePriorityInS1_Comp1", rcmd: "r,meth:setSlavePriorityInS1_Comp1,-,2,-,0x110B", min: 1, max: 1, offset:"0x110B" },
    SlavePriorityInS1_Comp2:                    { rprob: "SlavePriorityInS1_Comp2", rcmd: "r,meth:setSlavePriorityInS1_Comp2,-,2,-,0x120B", min: 1, max: 1, offset:"0x120B" },
    SlavePriorityInS1_Comp3:                    { rprob: "SlavePriorityInS1_Comp3", rcmd: "r,meth:setSlavePriorityInS1_Comp3,-,2,-,0x130B", min: 1, max: 1, offset:"0x130B" },
    SlavePriorityInS2_Comp0:                    { rprob: "SlavePriorityInS2_Comp0", rcmd: "r,meth:setSlavePriorityInS2_Comp0,-,2,-,0x100C", min: 1, max: 1, offset:"0x100C" },
    SlavePriorityInS2_Comp1:                    { rprob: "SlavePriorityInS2_Comp1", rcmd: "r,meth:setSlavePriorityInS2_Comp1,-,2,-,0x110C", min: 1, max: 1, offset:"0x110C" },
    SlavePriorityInS2_Comp2:                    { rprob: "SlavePriorityInS2_Comp2", rcmd: "r,meth:setSlavePriorityInS2_Comp2,-,2,-,0x120C", min: 1, max: 1, offset:"0x120C" },
    SlavePriorityInS2_Comp3:                    { rprob: "SlavePriorityInS2_Comp3", rcmd: "r,meth:setSlavePriorityInS2_Comp3,-,2,-,0x130C", min: 1, max: 1, offset:"0x130C" },
    SlavePriorityInS3_Comp0:                    { rprob: "SlavePriorityInS3_Comp0", rcmd: "r,meth:setSlavePriorityInS3_Comp0,-,2,-,0x100D", min: 1, max: 1, offset:"0x100D" },
    SlavePriorityInS3_Comp1:                    { rprob: "SlavePriorityInS3_Comp1", rcmd: "r,meth:setSlavePriorityInS3_Comp1,-,2,-,0x110D", min: 1, max: 1, offset:"0x110D" },
    SlavePriorityInS3_Comp2:                    { rprob: "SlavePriorityInS3_Comp2", rcmd: "r,meth:setSlavePriorityInS3_Comp2,-,2,-,0x120D", min: 1, max: 1, offset:"0x120D" },
    SlavePriorityInS3_Comp3:                    { rprob: "SlavePriorityInS3_Comp3", rcmd: "r,meth:setSlavePriorityInS3_Comp3,-,2,-,0x130D", min: 1, max: 1, offset:"0x130D" },
    SlaveUnloadTime_Comp0:                      { rprob: "SlaveUnloadTime_Comp0", rcmd: "r,meth:setSlaveUnloadTime_Comp0,-,2,-,0x100E", min: 1, max: 1, offset:"0x100E" },
    SlaveUnloadTime_Comp1:                      { rprob: "SlaveUnloadTime_Comp1", rcmd: "r,meth:setSlaveUnloadTime_Comp1,-,2,-,0x110E", min: 1, max: 1, offset:"0x110E" },
    SlaveUnloadTime_Comp2:                      { rprob: "SlaveUnloadTime_Comp2", rcmd: "r,meth:setSlaveUnloadTime_Comp2,-,2,-,0x120E", min: 1, max: 1, offset:"0x120E" },
    SlaveUnloadTime_Comp3:                      { rprob: "SlaveUnloadTime_Comp3", rcmd: "r,meth:setSlaveUnloadTime_Comp3,-,2,-,0x130E", min: 1, max: 1, offset:"0x130E" },
    SlaveSafetyTime_Comp0:                      { rprob: "SlaveSafetyTime_Comp0", rcmd: "r,meth:setSlaveSafetyTime_Comp0,-,2,-,0x100F", min: 1, max: 1, offset:"0x100F" },
    SlaveSafetyTime_Comp1:                      { rprob: "SlaveSafetyTime_Comp1", rcmd: "r,meth:setSlaveSafetyTime_Comp1,-,2,-,0x110F", min: 1, max: 1, offset:"0x110F" },
    SlaveSafetyTime_Comp2:                      { rprob: "SlaveSafetyTime_Comp2", rcmd: "r,meth:setSlaveSafetyTime_Comp2,-,2,-,0x120F", min: 1, max: 1, offset:"0x120F" },
    SlaveSafetyTime_Comp3:                      { rprob: "SlaveSafetyTime_Comp3", rcmd: "r,meth:setSlaveSafetyTime_Comp3,-,2,-,0x130F", min: 1, max: 1, offset:"0x130F" },
    SlaveStartsHour_Comp0:                      { rprob: "SlaveStartsHour_Comp0", rcmd: "r,meth:setSlaveStartsHour_Comp0,-,2,-,0x1010", min: 1, max: 1, offset:"0x1010" },
    SlaveStartsHour_Comp1:                      { rprob: "SlaveStartsHour_Comp1", rcmd: "r,meth:setSlaveStartsHour_Comp1,-,2,-,0x1110", min: 1, max: 1, offset:"0x1110" },
    SlaveStartsHour_Comp2:                      { rprob: "SlaveStartsHour_Comp2", rcmd: "r,meth:setSlaveStartsHour_Comp2,-,2,-,0x1210", min: 1, max: 1, offset:"0x1210" },
    SlaveStartsHour_Comp3:                      { rprob: "SlaveStartsHour_Comp3", rcmd: "r,meth:setSlaveStartsHour_Comp3,-,2,-,0x1310", min: 1, max: 1, offset:"0x1310" },
    SlaveAnalogInput_Comp0:                     { rprob: "SlaveAnalogInput_Comp0", rcmd: "r,meth:setSlaveAnalogInput_Comp0,-,2,-,0x1011", min: 1, max: 1, offset:"0x1011" },
    SlaveAnalogInput_Comp1:                     { rprob: "SlaveAnalogInput_Comp1", rcmd: "r,meth:setSlaveAnalogInput_Comp1,-,2,-,0x1111", min: 1, max: 1, offset:"0x1111" },
    SlaveAnalogInput_Comp2:                     { rprob: "SlaveAnalogInput_Comp2", rcmd: "r,meth:setSlaveAnalogInput_Comp2,-,2,-,0x1211", min: 1, max: 1, offset:"0x1211" },
    SlaveAnalogInput_Comp3:                     { rprob: "SlaveAnalogInput_Comp3", rcmd: "r,meth:setSlaveAnalogInput_Comp3,-,2,-,0x1311", min: 1, max: 1, offset:"0x1311" },
    SlaveExcludedForMaint_Comp0:                { rprob: "SlaveExcludedForMaint_Comp0", rcmd: "r,meth:setSlaveExcludedForMaint_Comp0,-,2,-,0x1012", min: 1, max: 1, offset:"0x1012" },
    SlaveExcludedForMaint_Comp1:                { rprob: "SlaveExcludedForMaint_Comp1", rcmd: "r,meth:setSlaveExcludedForMaint_Comp1,-,2,-,0x1112", min: 1, max: 1, offset:"0x1112" },
    SlaveExcludedForMaint_Comp2:                { rprob: "SlaveExcludedForMaint_Comp2", rcmd: "r,meth:setSlaveExcludedForMaint_Comp2,-,2,-,0x1212", min: 1, max: 1, offset:"0x1212" },
    SlaveExcludedForMaint_Comp3:                { rprob: "SlaveExcludedForMaint_Comp3", rcmd: "r,meth:setSlaveExcludedForMaint_Comp3,-,2,-,0x1312", min: 1, max: 1, offset:"0x1312" },
    SlaveEnableMaintenance_Comp0:               { rprob: "SlaveEnableMaintenance_Comp0", rcmd: "r,meth:setSlaveEnableMaintenance_Comp0,-,2,-,0x1013", min: 1, max: 1, offset:"0x1013" },
    SlaveEnableMaintenance_Comp1:               { rprob: "SlaveEnableMaintenance_Comp1", rcmd: "r,meth:setSlaveEnableMaintenance_Comp1,-,2,-,0x1113", min: 1, max: 1, offset:"0x1113" },
    SlaveEnableMaintenance_Comp2:               { rprob: "SlaveEnableMaintenance_Comp2", rcmd: "r,meth:setSlaveEnableMaintenance_Comp2,-,2,-,0x1213", min: 1, max: 1, offset:"0x1213" },
    SlaveEnableMaintenance_Comp3:               { rprob: "SlaveEnableMaintenance_Comp3", rcmd: "r,meth:setSlaveEnableMaintenance_Comp3,-,2,-,0x1313", min: 1, max: 1, offset:"0x1313" },
    SlaveChangeAirFilter_Comp0:                 { rprob: "SlaveChangeAirFilter_Comp0", rcmd: "r,meth:setSlaveChangeAirFilter_Comp0,-,2,-,0x1014", min: 1, max: 1, offset:"0x1014" },
    SlaveChangeAirFilter_Comp1:                 { rprob: "SlaveChangeAirFilter_Comp1", rcmd: "r,meth:setSlaveChangeAirFilter_Comp1,-,2,-,0x1114", min: 1, max: 1, offset:"0x1114" },
    SlaveChangeAirFilter_Comp2:                 { rprob: "SlaveChangeAirFilter_Comp2", rcmd: "r,meth:setSlaveChangeAirFilter_Comp2,-,2,-,0x1214", min: 1, max: 1, offset:"0x1214" },
    SlaveChangeAirFilter_Comp3:                 { rprob: "SlaveChangeAirFilter_Comp3", rcmd: "r,meth:setSlaveChangeAirFilter_Comp3,-,2,-,0x1314", min: 1, max: 1, offset:"0x1314" },
    SlaveChangeOilFilter_Comp0:                 { rprob: "SlaveChangeOilFilter_Comp0", rcmd: "r,meth:setSlaveChangeOilFilter_Comp0,-,2,-,0x1015", min: 1, max: 1, offset:"0x1015" },
    SlaveChangeOilFilter_Comp1:                 { rprob: "SlaveChangeOilFilter_Comp1", rcmd: "r,meth:setSlaveChangeOilFilter_Comp1,-,2,-,0x1115", min: 1, max: 1, offset:"0x1115" },
    SlaveChangeOilFilter_Comp2:                 { rprob: "SlaveChangeOilFilter_Comp2", rcmd: "r,meth:setSlaveChangeOilFilter_Comp2,-,2,-,0x1215", min: 1, max: 1, offset:"0x1215" },
    SlaveChangeOilFilter_Comp3:                 { rprob: "SlaveChangeOilFilter_Comp3", rcmd: "r,meth:setSlaveChangeOilFilter_Comp3,-,2,-,0x1315", min: 1, max: 1, offset:"0x1315" },
    SlaveChangeSeperatorFilter_Comp0:           { rprob: "SlaveChangeSeperatorFilter_Comp0", rcmd: "r,meth:setSlaveChangeSeperatorFilter_Comp0,-,2,-,0x1016", min: 1, max: 1, offset:"0x1016" },
    SlaveChangeSeperatorFilter_Comp1:           { rprob: "SlaveChangeSeperatorFilter_Comp1", rcmd: "r,meth:setSlaveChangeSeperatorFilter_Comp1,-,2,-,0x1116", min: 1, max: 1, offset:"0x1116" },
    SlaveChangeSeperatorFilter_Comp2:           { rprob: "SlaveChangeSeperatorFilter_Comp2", rcmd: "r,meth:setSlaveChangeSeperatorFilter_Comp2,-,2,-,0x1216", min: 1, max: 1, offset:"0x1216" },
    SlaveChangeSeperatorFilter_Comp3:           { rprob: "SlaveChangeSeperatorFilter_Comp3", rcmd: "r,meth:setSlaveChangeSeperatorFilter_Comp3,-,2,-,0x1316", min: 1, max: 1, offset:"0x1316" },
    SlaveChangeOil_Comp0:                       { rprob: "SlaveChangeOil_Comp0", rcmd: "r,meth:setSlaveChangeOil_Comp0,-,2,-,0x1017", min: 1, max: 1, offset:"0x1017" },
    SlaveChangeOil_Comp1:                       { rprob: "SlaveChangeOil_Comp1", rcmd: "r,meth:setSlaveChangeOil_Comp1,-,2,-,0x1117", min: 1, max: 1, offset:"0x1117" },
    SlaveChangeOil_Comp2:                       { rprob: "SlaveChangeOil_Comp2", rcmd: "r,meth:setSlaveChangeOil_Comp2,-,2,-,0x1217", min: 1, max: 1, offset:"0x1217" },
    SlaveChangeOil_Comp3:                       { rprob: "SlaveChangeOil_Comp3", rcmd: "r,meth:setSlaveChangeOil_Comp3,-,2,-,0x1317", min: 1, max: 1, offset:"0x1317" },
    SlaveCheckCompressor_Comp0:                 { rprob: "SlaveCheckCompressor_Comp0", rcmd: "r,meth:setSlaveCheckCompressor_Comp0,-,2,-,0x1018", min: 1, max: 1, offset:"0x1018" },
    SlaveCheckCompressor_Comp1:                 { rprob: "SlaveCheckCompressor_Comp1", rcmd: "r,meth:setSlaveCheckCompressor_Comp1,-,2,-,0x1118", min: 1, max: 1, offset:"0x1118" },
    SlaveCheckCompressor_Comp2:                 { rprob: "SlaveCheckCompressor_Comp2", rcmd: "r,meth:setSlaveCheckCompressor_Comp2,-,2,-,0x1218", min: 1, max: 1, offset:"0x1218" },
    SlaveCheckCompressor_Comp3:                 { rprob: "SlaveCheckCompressor_Comp3", rcmd: "r,meth:setSlaveCheckCompressor_Comp3,-,2,-,0x1318", min: 1, max: 1, offset:"0x1318" },
    SlaveBearingLubrication_Comp0:              { rprob: "SlaveBearingLubrication_Comp0", rcmd: "r,meth:setSlaveBearingLubrication_Comp0,-,2,-,0x1019", min: 1, max: 1, offset:"0x1019" },
    SlaveBearingLubrication_Comp1:              { rprob: "SlaveBearingLubrication_Comp1", rcmd: "r,meth:setSlaveBearingLubrication_Comp1,-,2,-,0x1119", min: 1, max: 1, offset:"0x1119" },
    SlaveBearingLubrication_Comp2:              { rprob: "SlaveBearingLubrication_Comp2", rcmd: "r,meth:setSlaveBearingLubrication_Comp2,-,2,-,0x1219", min: 1, max: 1, offset:"0x1219" },
    SlaveBearingLubrication_Comp3:              { rprob: "SlaveBearingLubrication_Comp3", rcmd: "r,meth:setSlaveBearingLubrication_Comp3,-,2,-,0x1319", min: 1, max: 1, offset:"0x1319" },
    SlaveNumberOfTotalCompressorHours_Comp0:    { rprob: "SlaveNumberOfTotalCompressorHours_Comp0", rcmd: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp0,-,4,-,0x101A", min: 1, max: 1, offset:"0x101A" },
    SlaveNumberOfTotalCompressorHours_Comp1:    { rprob: "SlaveNumberOfTotalCompressorHours_Comp1", rcmd: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp1,-,4,-,0x111A", min: 1, max: 1, offset:"0x111A" },
    SlaveNumberOfTotalCompressorHours_Comp2:    { rprob: "SlaveNumberOfTotalCompressorHours_Comp2", rcmd: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp2,-,4,-,0x121A", min: 1, max: 1, offset:"0x121A" },
    SlaveNumberOfTotalCompressorHours_Comp3:    { rprob: "SlaveNumberOfTotalCompressorHours_Comp3", rcmd: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp3,-,4,-,0x131A", min: 1, max: 1, offset:"0x131A" },
    SlaveNumberOfLoadCompressorHours_Comp0:     { rprob: "SlaveNumberOfLoadCompressorHours_Comp0", rcmd: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp0,-,4,-,0x101C", min: 1, max: 1, offset:"0x101C" },
    SlaveNumberOfLoadCompressorHours_Comp1:     { rprob: "SlaveNumberOfLoadCompressorHours_Comp1", rcmd: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp1,-,4,-,0x111C", min: 1, max: 1, offset:"0x111C" },
    SlaveNumberOfLoadCompressorHours_Comp2:     { rprob: "SlaveNumberOfLoadCompressorHours_Comp2", rcmd: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp2,-,4,-,0x121C", min: 1, max: 1, offset:"0x121C" },
    SlaveNumberOfLoadCompressorHours_Comp3:     { rprob: "SlaveNumberOfLoadCompressorHours_Comp3", rcmd: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp3,-,4,-,0x131C", min: 1, max: 1, offset:"0x131C" },

    
    R02:      { rprob: "R02", rcmd: "r,meth:setR02,-,2,-,1,0x500", min: 2, max: 2, offset:"0x500"},
    V01:      { rprob: "V01", rcmd: "r,meth:setV01,-,2,-,1,0x501", min: 1, max: 1, offset:"0x501"},
    WP:       { rprob: "WPx", rcmd: "r,meth:setWPx,-,12,-,1,0x502", min: 1, max: 6, offset:"0x502", multiplier: [,10,10,10,10,10] },
    WT:       { rprob: "WTx", rcmd: "r,meth:setWTx,-,8,-,1,0x508", min: 1, max: 4, offset:"0x508", multiplier: [10,10,10,10] },
    V04:      { rprob: "V04", rcmd: "r,meth:setV04,-,2,-,1,0x50C", min: 4, max: 4, offset:"0x50C"},
    V02:      { rprob: "V02", rcmd: "r,meth:setV02_V03,-,4,-,1,0x50D", min: 2, max: 3, offset:"0x50D"},
    V07:      { rprob: "V07", rcmd: "r,meth:setV07, -,2,-,0x50F", min: 7, max: 7, offset:"0x50F"},
    S11:      { rprob: "S11", rcmd: "r,meth:setS11, -,2,-,0x510", min: 11, max:11, offset:"0x510"},
    T01:      { rprob: "T01", rcmd: "r,meth:setT01, -,2,-,0x511", min: 1, max: 1, offset:"0x511"},
    S14:      { rprob: "S14", rcmd: "r,meth:setS14, -,2,-,0x512", min: 14, max: 14, offset:"0x512"},
    R01:      { rprob: "R01", rcmd: "r,meth:setR01, -,2,-,0x513", min: 1, max: 1, offset:"0x513"},
    S00:      { rprob: "S00", rcmd: "r,meth:setS00_S01_S02, -,6,-,0x514", min: 0, max: 2, offset:"0x514", multiplier: [,,0.1] },
    S09:      { rprob: "S09", rcmd: "r,meth:setS09_S10, -,4,-,0x517", min: 9, max: 9, offset:"0x517"},
    S06:      { rprob: "S06", rcmd: "r,meth:setS06, -,2,-,0x519", min: 6, max: 6, offset:"0x519"},
    S05:      { rprob: "S05", rcmd: "r,meth:setS05, -,2,-,0x51A", min: 5, max: 5, offset:"0x51A"},
    S07:      { rprob: "S07", rcmd: "r,meth:setS07_S08, -,4,-,0x51B", min: 7, max: 8, offset:"0x51B"},
    S12:      { rprob: "S12", rcmd: "r,meth:setS12_S13, -,4,-,0x51D", min: 12, max: 13, offset:"0x51D"},
    S17:      { rprob: "S12", rcmd: "r,meth:setS17, -,2,-,0x51F", min: 17, max: 17, offset:"0x51F"},
    S16:      { rprob: "S16", rcmd: "r,meth:setS16, -,2,-,0x520", min: 16, max: 16, offset:"0x520"},
    S03:      { rprob: "S03", rcmd: "r,meth:setS03_S04, -,4,-,0x521", min: 3, max: 4, offset:"0x521"},
    S18:      { rprob: "S18", rcmd: "r,meth:setS18_S19, -,4,-,0x523", min: 18, max: 19, offset:"0x523"},
    S21:      { rprob: "S21", rcmd: "r,meth:setS21, -,2,-,0x525", min: 21, max: 21, offset:"0x525"},
    S20:      { rprob: "S20", rcmd: "r,meth:setS20, -,2,-,0x526", min: 20, max: 20, offset:"0x526"},
    S22:      { rprob: "S22", rcmd: "r,meth:setS22, -,2,-,0x527", min: 22, max: 22, offset:"0x527"},

};
return requests[value];
"""

#
#
#
def fetchModbusSettings_body():
    return """/**
*/

if (value) {
  return "/dev/ttyS1:9600:8:N:1|"+
    "g0:0,g1:3600,g2:60,g3:3,g4:5|"+
    "r,meth:setAlarms,5,12,1,1,0x200|"+
    "r,meth:setNonAckAlarms,5,12,1,1,0x208|"+
    "r,meth:setControllerState,5,2,1,1,0x400|"+
    "r,meth:setCompressorState,5,2,1,1,0x401|"+
    "r,meth:setBlockingAlarm,5,2,1,1,0x401|"+
    "r,meth:setScrewTemperature,3,2,0,1,0x406|"+
    "r,meth:setWorkingPressure,3,2,0,1,0x404|"+
    "r,meth:setSecondTemperature,3,2,0,1,0x408|"+
    "r,meth:setSecondPressure,3,2,0,1,0x409|"+
    "r,meth:setConfigSwitches,60,4,1,1,0x500|"+    
    "r,meth:setControllerSupplyVoltage,60,2,1,1,0x40A|"+
    "r,meth:setTotalHours,3600,4,1,1,0x600|"+
    "r,meth:setTotalLoadHours,3600,4,1,1,0x602|"+
    "r,meth:setMaintCounters,3600,24,1,1,0x604|"+
    "r,meth:setDriveStatus,60,2,0,1,0xA00|"+
    "r,meth:setDriveMeasures,5,20,0,1,0xA01";
}
else {
  return "/dev/ttyS1:9600:8:N:1|"+
    "g0:0,g1:3600,g2:60,g3:3,g4:5|"+
    "r,meth:setAlarms,5,12,1,1,0x200|"+
    "r,meth:setNonAckAlarms,5,12,1,1,0x208|"+
    "r,meth:setControllerState,5,2,1,1,0x400|"+
    "r,meth:setCompressorState,5,2,1,1,0x401|"+
    "r,meth:setBlockingAlarm,5,2,1,1,0x401|"+
    "r,meth:setScrewTemperature,3,2,0,1,0x406|"+
    "r,meth:setWorkingPressure,3,2,0,1,0x404|"+
    "r,meth:setSecondTemperature,3,2,0,1,0x408|"+
    "r,meth:setSecondPressure,3,2,0,1,0x409|"+
    "r,meth:setConfigSwitches,60,4,1,1,0x500|"+
    "r,meth:setControllerSupplyVoltage,60,2,1,1,0x40A|"+
    "r,meth:setTotalHours,3600,4,1,1,0x600|"+
    "r,meth:setTotalLoadHours,3600,4,1,1,0x602|"+
    "r,meth:setMaintCounters,3600,24,1,1,0x604";
}
"""

#
#
#
def fetchControllerStates_body():
    return """/**

*/
return [
    { code: 0, label: "OFF" },
    { code: 1, label: "OFF - WAITING FOR NEXT WEEKLY TIMER INTERVAL" },
    { code: 2, label: "STARTING - WAITING FOR SAFETY TIME" },
    { code: 3, label: "ON" },
    { code: 4, label: "BLOCKED" },
];
"""
def fetchSlaveControllerStates_body():
    return """/**

*/
return [
    { code: 0, label: "RESET" },
    { code: 1, label: "OFF" },
    { code: 2, label: "STARTING" },
    { code: 3, label: "LOAD RUNNING" },
    { code: 4, label: "IDLE RUNNING" },
    { code: 5, label: "SAFETY TIME" },
    { code: 6, label: "UNDER MAINTENANCE" },
    { code: 7, label: "FAULT" },
];
"""
#
#
#
def fetchCompressorStates_body():
    return """/**

*/
return [
    { code: 0, label: "OFF" },
    { code: 1, label: "WAITING TO START" },
    { code: 2, label: "WAITING Pin" },
    { code: 3, label: "REMOTE STOP ACTIVE" },
    { code: 4, label: "STOP BY TIMER" },
    { code: 5, label: "STARTING" },
    { code: 6, label: "IDLE RUNNING" },
    { code: 7, label: "IDLE RUNNING STOPPING" },
    { code: 8, label: "PRESSURE IN SET, MOTOR IS OFF" },
    { code: 9, label: "LOAD RUNNING" },
    { code: 10, label: "SOFT BLOCK DELAY" },
    { code: 11, label: "BLOCK" },
    { code: 12, label: "INVERTER SETUP" },
    { code: 13, label: "OIL MANAGEMENT" },
    { code: 14, label: "FACTORY TEST" }
];
"""

#
#
#
def fetchCompressorStateTypes_body():
    return """/**
    Returns the compressor state types to calculate idle running time,
    load running time etc..
*/
return { IDLE_RUNNING: [ 6 ],
         LOAD_RUNNING: [ 9 ],
         PLANNED_STOPPAGES: [ 0, 14 ],
         UNPLANNED_STOPPAGES:[ 11 ]
};
"""

#
#
#
def hasInverter_body():
    return"""/**
@param value is the context
*/
const INVERTER = 'DANFOSS FC'
const CFG_DRIVE_PROTOCOL = 'configSwitches';

async function fn() {
    const context = value;

    const { value: propValue = {} } = await Device.api.getProperty(CFG_DRIVE_PROTOCOL);
    const hasInverter = propValue
        ? propValue.D0 === INVERTER
        : false;

    done(null, hasInverter);
}
fn();
"""

#
#
#
def makeCompressorCommand_body():
    return """/*
    Send compressor command to the gateway

    Valid commands are:
    
    STOP
    START
    ALARM_RESET
    ACK_RESET_ALL_ALARMS

    For example:

    { "value": "STOP" }
*/
const cmd = {
    START: Math.pow(2,0),
    STOP: Math.pow(2,1),
    ALARM_RESET: Math.pow(2,2),
    ACK_RESET_ALL_ALARMS: Math.pow(2,5),
}

if (!cmd[value]) throw value + " is not a valid command. See method description for valid commands.";

let tagValue = Device.makeWriteValue({ value: cmd[value], byteCount: 2 });
return "w," + tagValue.join(':') + ",2,0,1,0x418";
"""

#
#
#
def setRelayOutputs_body():
    return """/**
Bit mapped allocation: 
  0x0001 RL1
  0x0002 RL1
  0x0004 RL3
  0x0008 RL4 
  0x0010 RL5 
  0x0020 RL6 
  0x0040 RL7
*/
let outputMap = Device.convertToDec({ values: value, default: 0});

let result = [];
if (outputMap & 1) result.push("RL1");
if (outputMap & 2) result.push("RL2");
if (outputMap & 4) result.push("RL3");
if (outputMap & 8) result.push("RL4");
if (outputMap & 16) result.push("RL5");
if (outputMap & 32) result.push("RL6");
if (outputMap & 64) result.push("RL7");

if (result.length == 0) result = ["-"];

Device.api.setProperty("relayOutputs", {
    value: result.toString(),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#
#
#
def setDigitalInputs_body():
    return """/**
Bit mapped allocation: 
  0x0001 IN1
  0x0002 IN2
  0x0004 IN3
  0x0008 IN4
  0x0010 IN5
  0x0020 IN6
  0x0040 Phase R (Phase Check Unit Logika Control) 
  0x0080 Phase S (Phase Check Unit Logika Control) 
  0x0100 Phase T (Phase Check Unit Logika Control) 
  0x0200 Input for drive fault
  0x0400 PTC state
  0x0800 Phases Sequence Correct (Phase Check Unit Logika Control)

  Note that although the codes are same, meanings are different per controller. 
  See controller manuel.
*/

let outputMap = Device.convertToDec({ values: value, default: 0});

let result = [];
if (outputMap & 1) result.push("IN1");
if (outputMap & 2) result.push("IN2");
if (outputMap & 4) result.push("IN3");
if (outputMap & 8) result.push("IN4");
if (outputMap & 16) result.push("IN5");
if (outputMap & 32) result.push("IN6");
if (outputMap & 64) result.push("Phase R");
if (outputMap & 128) result.push("Phase S");
if (outputMap & 256) result.push("Phase T");
if (outputMap & 512) result.push("Input for drive fault");
if (outputMap & 1024) result.push("PTC state");
if (outputMap & 2048) result.push("Phases Sequence Correct");

if (result.length == 0) result = ["-"];

Device.api.setProperty("digitalInputs", {
    value: result.toString(),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""
#####################
#
#  Level1Password
#
#####################

def writeLevel1Password_body():
    return """/**
@value {{ x: integer, setValue: int[], byteCount: integer = 6 }}
Example:
Called as {"value": {"x": 1, "setValue":[5,9,5,4,6,6]} to set the level1Password to 59
Accepts 0...9 for each digit
*/
let args = {
  tagKey: "cfgLevel1Pwd",
  setValue: value.setValue,
  byteCount: value.byteCount || 6
};
try {
  let params = Device.fetchWriteRequest(args.tagKey);
  let tagValue = Device.makeWriteValue({ value: args.setValue, byteCount: args.byteCount });
  let tag_address = (parseInt(params.offset, 16) + (value.x - params.min)).toString();
  let req = { cmd: `w,${tagValue.join(':')},${args.byteCount},0,1,${tag_address}`, done: r => done(null, r) };
  Device.writeTag(req);
}
catch(e) {
  done(e);
}
"""

#####################
#
#  AmbientTemperature
#
#####################

def setAmbientTemperature_body():
    return """/**
*/

    const tagPropName = "AmbientTemperature";
    let AmbientTemperature = Device.convertToDec({ values: value }, -1);
    AmbientTemperature = AmbientTemperature / 10;
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.AmbientTemperature = AmbientTemperature.toString() +  ' °C';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

#####################
#
#  InternalVoltageVcc
#
#####################

def setInternalVoltageVcc_body():
    return """/**
*/

    const tagPropName = "InternalVoltageVcc";
    let InternalVoltageVcc = Device.convertToDec({ values: value }, -1);
    InternalVoltageVcc = InternalVoltageVcc / 10;
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.InternalVoltageVcc = InternalVoltageVcc.toString() + ' V';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

#####################
#
#  InternalVoltageVL
#
#####################

def setInternalVoltageVL_body():
    return """/**
*/

    const tagPropName = "InternalVoltageVL";
    let InternalVoltageVL = Device.convertToDec({ values: value }, -1);
    InternalVoltageVL = InternalVoltageVL / 10;
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.InternalVoltageVL = InternalVoltageVL.toString() + ' V';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

#####################
#
#  ResidualCompressorCapacity
#
#####################

def setResidualCompressorCapacity_body():
    return """/**
*/

    const tagPropName = "ResidualCompressorCapacity";
    let ResidualCompressorCapacity = Device.convertToDec({ values: value }, -1);
    ResidualCompressorCapacity = ResidualCompressorCapacity / 10;
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.ResidualCompressorCapacity = ResidualCompressorCapacity.toString() + ' Lit';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

#####################
#
#  ExcessCompressorCapacity
#
#####################

def setExcessCompressorCapacity_body():
    return """/**
*/

    const tagPropName = "ExcessCompressorCapacity";
    let ExcessCompressorCapacity = Device.convertToDec({ values: value }, -1);
    ExcessCompressorCapacity = ExcessCompressorCapacity / 10;
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.ExcessCompressorCapacity = ExcessCompressorCapacity.toString() + ' Lit';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

#####################
#
#  CurrentStopPressure
#
#####################

def setCurrentStopPressure_body():
    return """/**
*/

    const tagPropName = "CurrentStopPressure";
    let CurrentStopPressure = Device.convertToDec({ values: value }, -1);
    CurrentStopPressure = CurrentStopPressure / 10;
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.CurrentStopPressure = CurrentStopPressure.toString() + ' Bar';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

#####################
#
#  CurrentStartPressure
#
#####################

def setCurrentStartPressure_body():
    return """/**
*/

    const tagPropName = "CurrentStartPressure";
    let CurrentStartPressure = Device.convertToDec({ values: value }, -1);
    CurrentStartPressure = CurrentStartPressure / 10;
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.CurrentStartPressure = CurrentStartPressure.toString() + ' Bar';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

#####################
#
#  CurrentTotalPower
#
#####################

def setCurrentTotalPower_body():
    return """/**
*/

    const tagPropName = "CurrentTotalPower";
    let CurrentTotalPower = Device.convertToDec({ values: value }, -1);
    CurrentTotalPower = CurrentTotalPower * 10;
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.CurrentTotalPower = CurrentTotalPower.toString() + ' kW';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

#####################
#
#  AverageAirDelivery
#
#####################

def setAverageAirDelivery_body():
    return """/**
*/

    const tagPropName = "AverageAirDelivery";
    let AverageAirDelivery = Device.convertToDec({ values: value }, -1);
    AverageAirDelivery = AverageAirDelivery * 10;
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.AverageAirDelivery = AverageAirDelivery.toString() + ' Lit';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

#####################
#
#  CurrentTotalAirDelivery
#
#####################

def setCurrentTotalAirDelivery_body():
    return """/**
*/

    const tagPropName = "CurrentTotalAirDelivery";
    let CurrentTotalAirDelivery = Device.convertToDec({ values: value }, -1);
    CurrentTotalAirDelivery = CurrentTotalAirDelivery * 10;
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.CurrentTotalAirDelivery = CurrentTotalAirDelivery.toString() + ' Lit';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""


#####################
#
#  CompressorsConfigured
#
#####################

def setCompressorsConfigured_body():
    return """/**
*/
let data = Device.convertToDec({ values: value, default: 0});

let result = [];
if (data & 1) result.push("Compressor 0 Present");
if (data & 2) result.push("Compressor 1 Present");
if (data & 4) result.push("Compressor 2 Present");
if (data & 8) result.push("Compressor 3 Present");

if (result.length == 0) result = ["No Compressors Present"];

Device.api.setProperty("CompressorsConfigured", {
    value: result.toString(),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });

"""
#####################
#
#  CompressorsSlave
#
#####################

def setCompressorsSlave_body():
    return """/**
*/
let data = Device.convertToDec({ values: value, default: 0});

let result = [];
if (data & 1) result.push("Compressor 0 Controlled By Logik Controller");
else{
    result.push("Compressor 0 Controlled By Slave Device");
}
if (data & 2) result.push("Compressor 1 Controlled By Logik Controller");
else{
    result.push("Compressor 1 Controlled By Slave Device");
}
if (data & 4) result.push("Compressor 2 Controlled By Logik Controller");
else{
    result.push("Compressor 2 Controlled By Slave Device");
}
if (data & 8) result.push("Compressor 3 Controlled By Logik Controller");
else{
    result.push("Compressor 3 Controlled By Slave Device");
}

if (result.length == 0) result = ["-"];

Device.api.setProperty("CompressorsSlave", {
    value: result.toString(),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });

"""

#####################
#
#  CompressorsSetToMaintenance
#
#####################

def setCompressorsSetToMaintenance_body():
    return """/**
*/
let data = Device.convertToDec({ values: value, default: 0});

let result = [];
if (data & 1) result.push("Compressor 0 Set To Maintenance");
if (data & 2) result.push("Compressor 1 Set To Maintenance");
if (data & 4) result.push("Compressor 2 Set To Maintenance");
if (data & 8) result.push("Compressor 3 Set To Maintenance");

if (result.length == 0) result = ["No Compressors Set To Maintenance"];

Device.api.setProperty("CompressorsSetToMaintenance", {
    value: result.toString(),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });

"""

#####################
#
#  CompressorsAvailable
#
#####################

def setCompressorsAvailable_body():
    return """/**
*/
let data = Device.convertToDec({ values: value, default: 0});

let result = [];
if (data & 1) result.push("Compressor 0 Available");
if (data & 2) result.push("Compressor 1 Available");
if (data & 4) result.push("Compressor 2 Available");
if (data & 8) result.push("Compressor 3 Available");

if (result.length == 0) result = ["No Compressors Available"];

Device.api.setProperty("CompressorsAvailable", {
    value: result.toString(),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });

"""

#####################
#
#  CompressorsSelected
#
#####################

def setCompressorsSelected_body():
    return """/**
*/
let data = Device.convertToDec({ values: value, default: 0});

let result = [];
if (data & 1) result.push("Compressor 0 Selected");
if (data & 2) result.push("Compressor 1 Selected");
if (data & 4) result.push("Compressor 2 Selected");
if (data & 8) result.push("Compressor 3 Selected");

if (result.length == 0) result = ["No Compressors Selected"];

Device.api.setProperty("CompressorsSelected", {
    value: result.toString(),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });

"""

#####################
#
#  CompressorsOn
#
#####################

def setCompressorsOn_body():
    return """/**
*/
let data = Device.convertToDec({ values: value, default: 0});

let result = [];
if (data & 1) result.push("Compressor 0 Command To Load");
if (data & 2) result.push("Compressor 1 Command To Load");
if (data & 4) result.push("Compressor 2 Command To Load");
if (data & 8) result.push("Compressor 3 Command To Load");

if (result.length == 0) result = ["All Compressors Stopped or Running Idle"];

Device.api.setProperty("CompressorsSelected", {
    value: result.toString(),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });

"""

#####################
#
#  TotalEnergyConsumption
#
#####################
def setTotalEnergyConsumption_body():
    return """/**
*/

    const tagPropName = "TotalEnergyConsumption";
    let TotalEnergyConsumption = Device.convertToDec({ values: value }, -1);
    TotalEnergyConsumption = TotalEnergyConsumption / 10;
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.TotalEnergyConsumption = TotalEnergyConsumption.toString() + ' kWh';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""
def writeTotalEnergyConsumption_body():
    return """/**
*/

  let args = {
      tagKey: "TotalEnergyConsumption",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  AirProduced
#
#####################

def setAirProduced_body():
    return """/**
*/

    const tagPropName = "AirProduced";
    let AirProduced = Device.convertToDec({ values: value }, -1);
    AirProduced = AirProduced;
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.AirProduced = AirProduced.toString() + ' m^3';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""
def writeAirProduced_body():
    return """/**
*/

  let args = {
      tagKey: "AirProduced",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""
#####################
#
#  IOBoardFwVersion
#
#####################
def setIOBoardFwVersion_body():
    return '''/**
    value: [ 3, 1 ] => "1.3"
    */
    (async function f(major, minor) {
        let releaseNo = major.toString() + "." + minor.toString();
        
        await Device.api.setProperty("IOBoardFwVersion, {
            value: releaseNo,
            time: new Date().toISOString()
        });    
        done(null, releaseNo);    
    })(value[0], value[1]);
    '''

#####################
#
#  SlaveFwVersion
#
#####################
def setSlaveFwVersion_body(compressorNo):
    return '''/**
    value: [ 3, 1 ] => "1.3"
    */
    (async function f(major, minor) {
        let releaseNo = major.toString() + "." + minor.toString();
        
        await Device.api.setProperty("SlaveFwVersion_Comp''' + str(compressorNo) + ''', {
            value: releaseNo,
            time: new Date().toISOString()
        });    
        done(null, releaseNo);    
    })(value[0], value[1]);
    '''

#####################
#
#  SlaveControllerState
#
#####################
def setSlaveControllerState_body(compressorNo):
    return '''/**
    Sets controller state property
*/
let table = Device.fetchSlaveControllerStates();
let state = { code: -1, label: "NOT_SET" };
let code = Device.convertToDec({ values: value, default: -1 });

if (code >= 0 && code < table.length) {
  state = table[code];
  
  Device.api.getProperty("slaveControllerState_Comp''' + str(compressorNo) + '''").then( stateProp => {
    if (!stateProp.value || state.code !== stateProp.value.code) {
        Device.api.setProperty("slaveControllerState_Comp''' + str(compressorNo) + '''", {
            value: state,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, state);
        });
    }
    else{
        done(null, "nothing updated");
    }
  });
}
else {    
    done("invalid argument");
}
'''
#####################
#
#  SlaveControllerType
#
#####################

def setSlaveControllerType_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveControllerType_Comp''' + str(compressorNo) + '''";
let SlaveControllerType = Device.convertToDec({ values: value }, -1);
if (SlaveControllerType == 1) SlaveControllerType = "Slave";
else{SlaveControllerType = "Logik";}
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveControllerType = SlaveControllerType;
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveControllerType_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveControllerType_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveSelenoidDelay
#
#####################

def setSlaveSelenoidDelay_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveSelenoidDelay_Comp''' + str(compressorNo) + '''";
let SlaveSelenoidDelay = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveSelenoidDelay = SlaveSelenoidDelay.toString() + ' sec';
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveSelenoidDelay_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveSelenoidDelay_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveAirFlow
#
#####################
def setSlaveAirFlow_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveAirFlow_Comp''' + str(compressorNo) + '''";
let SlaveAirFlow = Device.convertToDec({ values: value }, -1);
SlaveAirFlow = SlaveAirFlow / 10;
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveAirFlow = SlaveAirFlow.toString() + ' Liters/min';
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveAirFlow_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveAirFlow_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""


#####################
#
#  SlaveRelativeSpeed
#
#####################
def setSlaveRelativeSpeed_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveRelativeSpeed_Comp''' + str(compressorNo) + '''";
let SlaveRelativeSpeed = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveRelativeSpeed = SlaveRelativeSpeed.toString();
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''
#####################
#
#  SlaveNominalPower
#
#####################

def setSlaveNominalPower_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveNominalPower_Comp''' + str(compressorNo) + '''";
let SlaveNominalPower = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveNominalPower = SlaveNominalPower.toString() + ' kW';
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveNominalPower_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveNominalPower_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveUnloadPower
#
#####################

def setSlaveUnloadPower_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveUnloadPower_Comp''' + str(compressorNo) + '''";
let SlaveUnloadPower = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveUnloadPower = SlaveUnloadPower.toString() + ' kW';
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveUnloadPower_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveUnloadPower_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlavePriorityInS0
#
#####################

def setSlavePriorityInS0_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlavePriorityInS0_Comp''' + str(compressorNo) + '''";
let SlavePriorityInS0 = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlavePriorityInS0 = SlavePriorityInS0.toString();
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlavePriorityInS0_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlavePriorityInS0_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""
#####################
#
#  SlavePriorityInS1
#
#####################

def setSlavePriorityInS1_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlavePriorityInS1_Comp''' + str(compressorNo) + '''";
let SlavePriorityInS1 = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlavePriorityInS1 = SlavePriorityInS1.toString();
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlavePriorityInS1_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlavePriorityInS1_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""
#####################
#
#  SlavePriorityInS2
#
#####################

def setSlavePriorityInS2_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlavePriorityInS2_Comp''' + str(compressorNo) + '''";
let SlavePriorityInS2 = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlavePriorityInS2 = SlavePriorityInS2.toString();
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlavePriorityInS2_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlavePriorityInS2_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""
#####################
#
#  SlavePriorityInS3
#
#####################

def setSlavePriorityInS3_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlavePriorityInS3_Comp''' + str(compressorNo) + '''";
let SlavePriorityInS3 = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlavePriorityInS3 = SlavePriorityInS3.toString();
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlavePriorityInS3_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlavePriorityInS3_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""
#####################
#
#  SlaveUnloadTime
#
#####################

def setSlaveUnloadTime_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveUnloadTime_Comp''' + str(compressorNo) + '''";
let SlaveUnloadTime = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveUnloadTime = SlaveUnloadTime.toString() + ' Sec';
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveUnloadTime_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveUnloadTime_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""
#####################
#
#  SlaveSafetyTime
#
#####################

def setSlaveSafetyTime_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveSafetyTime_Comp''' + str(compressorNo) + '''";
let SlaveSafetyTime = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveSafetyTime = SlaveSafetyTime.toString() + ' min';
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveSafetyTime_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveSafetyTime_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""
#####################
#
#  SlaveStartsHour
#
#####################

def setSlaveStartsHour_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveStartsHour_Comp''' + str(compressorNo) + '''";
let SlaveStartsHour = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveStartsHour = SlaveStartsHour.toString() + ' Sec';
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveStartsHour_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveStartsHour_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveAnalogInput
#
#####################

def setSlaveAnalogInput_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveAnalogInput_Comp''' + str(compressorNo) + '''";
let SlaveAnalogInput = Device.convertToDec({ values: value }, -1);
if (SlaveAnalogInput == 0) SlaveAnalogInput = "0/10V";
else{ SlaveAnalogInput = "4/20mA"; }
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveAnalogInput = SlaveAnalogInput;
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveAnalogInput_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveAnalogInput_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveExcludedForMaint
#
#####################

def setSlaveExcludedForMaint_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveExcludedForMaint_Comp''' + str(compressorNo) + '''";
let SlaveExcludedForMaint = Device.convertToDec({ values: value }, -1);
if (SlaveExcludedForMaint == 0) SlaveExcludedForMaint = "Controlled by Logik200";
else{ SlaveExcludedForMaint = "Forced to Work With Local Transducer"; }
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveExcludedForMaint = SlaveExcludedForMaint.toString();
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveExcludedForMaint_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveExcludedForMaint_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveEnableMaintenance
#
#####################

def setSlaveEnableMaintenance_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveEnableMaintenance_Comp''' + str(compressorNo) + '''";
let SlaveEnableMaintenance = Device.convertToDec({ values: value }, -1);
if (SlaveEnableMaintenance == 0) SlaveEnableMaintenance = "Maintenance Disabled";
else{ SlaveEnableMaintenance = "Maintenance Enabled"; }
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveEnableMaintenance = SlaveEnableMaintenance.toString();
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveEnableMaintenance_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveEnableMaintenance_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveChangeAirFilter
#
#####################

def setSlaveChangeAirFilter_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveChangeAirFilter_Comp''' + str(compressorNo) + '''";
let SlaveChangeAirFilter = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveChangeAirFilter = SlaveChangeAirFilter.toString() + "hours";
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveChangeAirFilter_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveChangeAirFilter_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveChangeOilFilter
#
#####################

def setSlaveChangeOilFilter_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveChangeOilFilter_Comp''' + str(compressorNo) + '''";
let SlaveChangeOilFilter = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveChangeOilFilter = SlaveChangeOilFilter.toString() + "hours";
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveChangeOilFilter_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveChangeOilFilter_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveChangeSeperatorFilter
#
#####################

def setSlaveChangeSeperatorFilter_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveChangeSeperatorFilter_Comp''' + str(compressorNo) + '''";
let SlaveChangeSeperatorFilter = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveChangeSeperatorFilter = SlaveChangeSeperatorFilter.toString() + "hours";
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveChangeSeperatorFilter_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveChangeSeperatorFilter_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveChangeOil
#
#####################

def setSlaveChangeOil_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveChangeOil_Comp''' + str(compressorNo) + '''";
let SlaveChangeOil = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveChangeOil = SlaveChangeOil.toString() + "hours";
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveChangeOil_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveChangeOil_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""
#####################
#
#  SlaveCheckCompressor
#
#####################

def setSlaveCheckCompressor_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveCheckCompressor_Comp''' + str(compressorNo) + '''";
let SlaveCheckCompressor = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveCheckCompressor = SlaveCheckCompressor.toString() + "hours";
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveCheckCompressor_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveCheckCompressor_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveBearingLubrication
#
#####################

def setSlaveBearingLubrication_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveBearingLubrication_Comp''' + str(compressorNo) + '''";
let SlaveBearingLubrication = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveBearingLubrication = SlaveBearingLubrication.toString() + "hours";
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveBearingLubrication_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveBearingLubrication_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveNumberOfTotalCompressorHours
#
#####################

def setSlaveNumberOfTotalCompressorHours_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveNumberOfTotalCompressorHours_Comp''' + str(compressorNo) + '''";
let SlaveNumberOfTotalCompressorHours = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveNumberOfTotalCompressorHours = SlaveNumberOfTotalCompressorHours.toString() + " Minutes";
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveNumberOfTotalCompressorHours_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveNumberOfTotalCompressorHours_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveNumberOfLoadCompresorHours
#
#####################

def setSlaveNumberOfLoadCompressorHours_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveNumberOfLoadCompressorHours_Comp''' + str(compressorNo) + '''";
let SlaveNumberOfLoadCompressorHours = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveNumberOfLoadCompressorHours = SlaveNumberOfLoadCompressorHours.toString().toString() + " Minutes";
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
'''

def writeSlaveNumberOfLoadCompressorHours_body(compressorNo):
    return """/**
*/

  let args = {
      tagKey: "SlaveNumberOfLoadCompressorHours_Comp""" + str(compressorNo) +"""",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }"""

#####################
#
#  SlaveMaintCounters
#
#####################

def setSlaveMaintCounters_body(compressorNo):
    return """/**
  24 bytes = long (4 byte) * 6
*/

const maintCountersPropName = 'SlaveMaintCounters_Comp +"""+ str(compressorNo) + """';
const maintLogPropName      = 'SlaveMaintenanceLog_Comp +"""+ str(compressorNo) + """';
const maintCostsPropName    = 'SlaveMaintenanceCostList_Comp +"""+ str(compressorNo) + """';

const maintTypes = [
  "airFilterChange",
  "oilFilterChange",
  "separatorFilterChange",
  "oilChange",
  "compressorCheck",
  "bearingLubrication"
];

const defaultMaintCosts = { 
    currencySymbol: "$",
    currency: "USD",
    airFilterChange: 0.0,
    oilChange: 0.0,  
    compressorCheck: 0.0, 
    oilFilterChange: 0.0, 
    separatorFilterChange : 0.0, 
    bearingLubrication: 0.0     
};

async function f(value) {
    let timeLeftInMinutes = {};
    for (var x = 0; x < maintTypes.length; x++) {
        timeLeftInMinutes[maintTypes[x]] = 0;
    }
    
    for (var i = 0; i < maintTypes.length*4; i+=4) {
        let minutes  = value.slice(i+0, i+1) << 24
            minutes |= value.slice(i+1, i+2) << 16;
            minutes |= value.slice(i+2, i+3) <<  8;
            minutes |= value.slice(i+3, i+4);
        
        timeLeftInMinutes[maintTypes[i/4]] = Math.floor(minutes / 60);
    }
    
    let currCounters = Object.assign({}, await Device.api.getProperty(maintCountersPropName).then(p => p ? p.value : undefined));
    
    let newMaintCounters = await Device.api.setProperty(maintCountersPropName, {
        value: timeLeftInMinutes,
        time: new Date().toISOString()
    })
     .then(property => property.value);
    
    
    try {
        // check if any maintenance counter is reset, then make a log
        if (currCounters) {
            let mcost = await Device.api.getProperty(maintCostsPropName).then(p=>p.value) || defaultMaintCosts;
            
            let maintenanceLog = { items: [] };
            for (var i = 0; i < maintTypes.length; i++) {
                if (newMaintCounters[maintTypes[i]] < currCounters[maintTypes[i]]) {
                    let item = { name: maintTypes[i], cost: mcost[maintTypes[i]], unit: mcost.currency };
                    maintenanceLog.items.push(item);
                }
            }
            
            if (maintenanceLog.items.length > 0) {
                await Device.api.setProperty(maintLogPropName, {
                        value: maintenanceLog,
                        time: new Date().toISOString()
                    });
            }
        }
    }
    catch (e) {
        await Device.api.log("error", e.toString());
    }
    
    done(null, null);
}

return f(value);
"""


#####################
#
#  R02
#
#####################

def setR02_body():
    return """/**
*/
const tagPropName = "Rx";
let R02 = Device.convertToDec({ values: value }, -1);
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.R02 = R02;
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
"""

def writeR02_body():
    return """/**
*/

  let args = {
      tagKey: "R02",
      x: value.x,
      setValue: value.setValue,
      byteCount: value.byteCount || 2
  };

  try {
      let req = Device.makeWriteRequest(args);
      req.done = r => done(null, r);

  Device.writeAndReadTag(req);
  }
  catch(e) {
      done(e);
  }
        """

#####################
#
#  V01
#
#####################

def setV01_body():
    return """/**
*/

    const tagPropName = "Vx";
    let V01 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.V01 = V01;
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeV01_body():
    return """/**
*/

        let args = {
            tagKey: "V01",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  WPx
#
#####################

def setWPx_body():
    return """/**
WP1			Bar
WP2			Bar x 10
WP3			Bar x 10
WP4			Bar x 10 
WP5			Bar x 10
WP6			Bar x 10
*/

const itemCount = 6;

let WPx = {};
for (var x = 0; x < itemCount; x++) {
    WPx['WP' + (x+1).toString()] = '-';
}

Device.api.log("info", "WPx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        if (i !=0){
        itemValue = itemValue / 10;
        }
        WPx['WP' + ((i/2)+1).toString()] = itemValue.toString() + ' Bar';
    }
    
    Device.api.setProperty("WPx", {
      value: WPx,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
"""

def writeWPx_body():
    return """/**
*/

        let args = {
            tagKey: "WPx",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  WTx
#
#####################

def setWTx_body():
    return """/**
WT1	R		°C x 10
WT2	R		°C x 10
WT3	R		°C x 10
WT4	R		°C x 10 
*/

const itemCount = 4;

let WTx = {};
for (var x = 0; x < itemCount; x++) {
    WTx['WT' + (x+1).toString()] = '-';
}

Device.api.log("info", "WTx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        itemValue = itemValue / 10;
        WTx['WT' + ((i/2)+1).toString()] = itemValue.toString() + ' °C';
    }
    
    Device.api.setProperty("WTx", {
      value: WTx,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
"""

def writeWTx_body():
    return """/**
*/

        let args = {
            tagKey: "WTx",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  V04
#
#####################

def setV04_body():
    return """/**
*/

    const tagPropName = "Vx";
    let V04 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.V04 = V04.toString() + '%';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeV04_body():
    return """/**
*/

        let args = {
            tagKey: "V04",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  V02_V03
#
#####################

def setV02_V03_body():
  return """/**
*/
const itemCount = 2;
const tagPropName = "Vx";
let Vx = {};
for (var x = 0; x < itemCount; x++) {
    Vx['v' + (x+2).toString()] = '-';
}
Device.api.log("debug", tagPropName + ": " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        Vx['V' + ((i/2)+2).toString()] = itemValue.toString();
    }
    
  Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.V02 = Vx[V2];
    property.value.V03 = Vx[V3];
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
 });"""

def writeV02_V03_body():
    return """/**
*/

        let args = {
            tagKey: "V02",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  V07
#
#####################

def setV07_body():
    return """/**
*/

    const tagPropName = "Vx";
    let V07 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.V07 = V07;
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeV07_body():
    return """/**
*/

        let args = {
            tagKey: "V07",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  S11
#
#####################

def setS11_body():
    return """/**
*/

    const tagPropName = "Sx";
    let S11 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.S11 = S11;
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeS11_body():
    return """/**
*/

        let args = {
            tagKey: "S11",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  T01
#
#####################

def setT01_body():
    return """/**
*/

    const tagPropName = "T01";
    let T01 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.T01 = T01;
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeT01_body():
    return """/**
*/

        let args = {
            tagKey: "T01",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  S14
#
#####################

def setS14_body():
    return """/**
*/

    const tagPropName = "Sx";
    let S14 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.S14 = S14;
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeS14_body():
    return """/**
*/

        let args = {
            tagKey: "S14",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  R01
#
#####################

def setR01_body():
    return """/**
*/

    const tagPropName = "Rx";
    let R01 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.R01 = R01;
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeR01_body():
    return """/**
*/

        let args = {
            tagKey: "R01",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  S00_S01_S02
#
#####################

def setS00_S01_S02_body():
    return """/**
*/
const itemCount = 3;
const tagPropName = "Sx";
let Sx = {};
for (var x = 0; x < itemCount; x++) {
    Sx['S' + (x).toString()] = '-';
}
Device.api.log("debug", tagPropName + ": " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        if(i/2 == 2){
            itemValue = itemValue *10;
        }
        Sx['S' + ((i/2)).toString()] = itemValue.toString();
    }
    
  Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.S00 = Sx[S0];
    property.value.S01 = Sx[S1];
    property.value.S02 = Sx[S2] + ' Liters';
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
 });"""

def writeS00_S01_S02_body():
    return """/**
*/

        let args = {
            tagKey: "S00",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  S09_S10
#
#####################

def setS09_S10_body():
    return """/**
*/
const itemCount = 2;
const tagPropName = "Sx";
let Sx = {};
for (var x = 0; x < itemCount; x++) {
    Sx['S' + (x+9).toString()] = '-';
}
Device.api.log("debug", tagPropName + ": " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        Sx['S' + ((i/2)+9).toString()] = itemValue.toString();
    }
    
  Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.S09 = Sx[S9];
    property.value.S10 = Sx[S10] + "Hours";
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
 });"""

def writeS09_S10_body():
    return """/**
*/

        let args = {
            tagKey: "S09",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  S06
#
#####################


def setS06_body():
    return """/**
*/

    const tagPropName = "Sx";
    let S06 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.S06 = S06;
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeS06_body():
    return """/**
*/

        let args = {
            tagKey: "S06",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """
#####################
#
#  S05
#
#####################

def setS05_body():
    return """/**
*/

    const tagPropName = "Sx";
    let S05 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.S05 = S05;
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeS05_body():
    return """/**
*/

        let args = {
            tagKey: "S05",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  S07_S08
#
#####################

def setS07_S08_body():
    return """/**
*/
const itemCount = 2;
const tagPropName = "Sx";
let Sx = {};
for (var x = 0; x < itemCount; x++) {
    Sx['S' + (x+7).toString()] = '-';
}
Device.api.log("debug", tagPropName + ": " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        Sx['S' + ((i/2)+7).toString()] = itemValue.toString();
    }
    
  Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.S07 = Sx[S7];
    property.value.S08 = Sx[S8];
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
 });"""

def writeS07_S08_body():
    return """/**
*/

        let args = {
            tagKey: "S07",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  S12_S13
#
#####################

def setS12_S13_body():
    return """/**
*/
const itemCount = 2;
const tagPropName = "Sx";
let Sx = {};
for (var x = 0; x < itemCount; x++) {
    Sx['S' + (x+12).toString()] = '-';
}
Device.api.log("debug", tagPropName + ": " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        Sx['S' + ((i/2)+12).toString()] = itemValue.toString();
    }
    
  Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.S12 = Sx[S12] + " Seconds";
    property.value.S13 = Sx[S13] + " Minutes";
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
 });"""

def writeS12_S13_body():
    return """/**
*/

        let args = {
            tagKey: "S12",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  S17
#
#####################

def setS17_body():
    return """/**
*/

    const tagPropName = "Sx";
    let S17 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.S17 = S17.toString() + ' %';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeS17_body():
    return """/**
*/

        let args = {
            tagKey: "S17",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  S16
#
#####################


def setS16_body():
    return """/**
*/

    const tagPropName = "Sx";
    let S16 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.S16 = S16.toString() + ' %';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeS16_body():
    return """/**
*/

        let args = {
            tagKey: "S16",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  S03_S04
#
#####################

def setS03_S04_body():
    return """/**
*/
const itemCount = 2;
const tagPropName = "Sx";
let Sx = {};
for (var x = 0; x < itemCount; x++) {
    Sx['S' + (x+3).toString()] = '-';
}
Device.api.log("debug", tagPropName + ": " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        Sx['S' + ((i/2)+3).toString()] = itemValue.toString();
    }
    
  Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.S03 = Sx[S3].toString() + ' Seconds';
    property.value.S04 = Sx[S4].toString() + ' Seconds';
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
 });"""

def writeS03_S04_body():
    return """/**
*/

        let args = {
            tagKey: "S03",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  S18_S19
#
#####################

def setS18_S19_body():
    return """/**
*/
const itemCount = 2;
const tagPropName = "Sx";
let Sx = {};
for (var x = 0; x < itemCount; x++) {
    Sx['S' + (x+18).toString()] = '-';
}
Device.api.log("debug", tagPropName + ": " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        Sx['S' + ((i/2)+18).toString()] = itemValue.toString();
    }
    
  Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.S18 = Sx[S18];
    property.value.S19 = Sx[S19];
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
 });"""

def writeS18_S19_body():
    return """/**
*/

        let args = {
            tagKey: "S18",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  S21
#
#####################

def setS21_body():
    return """/**
*/

    const tagPropName = "Sx";
    let S21 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.S21 = S21.toString() + ' Seconds';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeS21_body():
    return """/**
*/

        let args = {
            tagKey: "S21",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

#####################
#
#  S20
#
#####################

def setS20_body():
    return """/**
*/

    const tagPropName = "Sx";
    let S20 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.S20 = S20.toString() + ' Seconds';
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeS20_body():
    return """/**
*/

        let args = {
            tagKey: "S20",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """
#####################
#
#  S22
#
#####################

def setS22_body():
    return """/**
*/

    const tagPropName = "Sx";
    let S22 = Device.convertToDec({ values: value }, -1);
    Device.api.getProperty(tagPropName)
        .then(property => {
        property.value.S22 = S22;
        Device.api.setProperty(tagPropName, {
            value: property.value,
            time: new Date().toISOString()
        })
        .then(property => {
            done(null, property.value);
        });
    });
"""

def writeS22_body():
    return """/**
*/

        let args = {
            tagKey: "S22",
            x: value.x,
            setValue: value.setValue,
            byteCount: value.byteCount || 2
        };

        try {
            let req = Device.makeWriteRequest(args);
            req.done = r => done(null, r);

        Device.writeAndReadTag(req);
        }
        catch(e) {
            done(e);
        }
        """

