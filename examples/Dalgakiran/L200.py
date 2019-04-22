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
blackOutCode: 'A04' };
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
  AmbientTemperature:               { request: "r,meth:setAmbientTemperature,-,2,-,1,0x405" },
  InternalVoltageVcc:               { request: "r,meth:setInternalVoltageVcc,-,2,-,1,0x406" },
  InternalVoltageVL:                { request: "r,meth:setInternalVoltageVL,-,2,-,1,0x407" },
  ResidualCompressorCapacity:       { request: "r,meth:setResidualCompressorCapacity,-,2,-,1,0x408" },
  ExcessCompressorCapacity:         { request: "r,meth:setExcessCompressorCapacity,-,2,-,1,0x409" },
  CurrentStopPressure:              { request: "r,meth:setCurrentStopPressure,-,2,-,1,0x40A" },
  CurrentStartPressure:             { request: "r,meth:setCurrentStartPressure,-,2,-,1,0x40B" },
  CurrentTotalPower:                { request: "r,meth:setCurrentTotalPower,-,4,-,1,0x40C" },
  AverageAirDelivery:               { request: "r,meth:setAverageAirDelivery,-,4,-,1,0x40E" },
  CurrentTotalAirDelivery:          { request: "r,meth:setCurrentTotalAirDelivery,-,4,-,1,0x410" },
  CompressorsConfigured:            { request: "r,meth:setCompressorsConfigured,-,2,-,1,0x412" },
  CompressorsSlave:                 { request: "r,meth:setCompressorsSlave,-,2,-,1,0x413" },
  CompressorsSetToMaintenance:      { request: "r,meth:setCompressorsSetToMaintenance,-,2,-,1,0x414" },
  CompressorsAvailable:             { request: "r,meth:setCompressorsAvailable,-,2,-,1,0x415" },
  CompressorsSelected:              { request: "r,meth:setCompressorsSelected,-,2,-,1,0x416" },
  CompressorsOn:                    { request: "r,meth:setCompressorsOn,-,2,-,1,0x417" },
  TotalEnergyConsumption:           { request: "r,meth:setTotalEnergyConsumption,-,4,-,1,0x600" },
  AirProduced:                      { request: "r,meth:setAirProduced,-,4,-,1,0x602" },
  //Slave Read Tags
  SlaveFwVersion_Comp0:             { request: "r,meth:setSlaveFwVersion_Comp0,-,2,-,1,0x1000" },
  SlaveFwVersion_Comp1:             { request: "r,meth:setSlaveFwVersion_Comp1,-,2,-,1,0x1100" },
  SlaveFwVersion_Comp2:             { request: "r,meth:setSlaveFwVersion_Comp2,-,2,-,1,0x1200" },
  SlaveFwVersion_Comp3:             { request: "r,meth:setSlaveFwVersion_Comp3,-,2,-,1,0x1300" },
  SlaveControllerState_Comp0:       { request: "r,meth:setSlaveControllerState_Comp0,-,2,-,1,0x1001" },
  SlaveControllerState_Comp1:       { request: "r,meth:setSlaveControllerState_Comp1,-,2,-,1,0x1101" },
  SlaveControllerState_Comp2:       { request: "r,meth:setSlaveControllerState_Comp2,-,2,-,1,0x1201" },
  SlaveControllerState_Comp3:       { request: "r,meth:setSlaveControllerState_Comp3,-,2,-,1,0x1301" },
  SlaveRelativeSpeed_Comp0:         { request: "r,meth:setSlaveRelativeSpeed_Comp0,-,2,-,1,0x1002" },
  SlaveRelativeSpeed_Comp1:         { request: "r,meth:setSlaveRelativeSpeed_Comp1,-,2,-,1,0x1102" },
  SlaveRelativeSpeed_Comp2:         { request: "r,meth:setSlaveRelativeSpeed_Comp2,-,2,-,1,0x1202" },
  SlaveRelativeSpeed_Comp3:         { request: "r,meth:setSlaveRelativeSpeed_Comp3,-,2,-,1,0x1302" },
  SlaveControllerType_Comp0:        { request: "r,meth:setSlaveControllerType_Comp0,-,2,-,1,0x1004" },
  SlaveControllerType_Comp1:        { request: "r,meth:setSlaveControllerType_Comp1,-,2,-,1,0x1104" },
  SlaveControllerType_Comp2:        { request: "r,meth:setSlaveControllerType_Comp2,-,2,-,1,0x1204" },
  SlaveControllerType_Comp3:        { request: "r,meth:setSlaveControllerType_Comp3,-,2,-,1,0x1304" },
  SlaveSelenoidDelay_Comp0:         { request: "r,meth:setSlaveSelenoidDelay_Comp0,-,2,-,1,0x1005" },
  SlaveSelenoidDelay_Comp1:         { request: "r,meth:setSlaveSelenoidDelay_Comp1,-,2,-,1,0x1105" },
  SlaveSelenoidDelay_Comp2:         { request: "r,meth:setSlaveSelenoidDelay_Comp2,-,2,-,1,0x1205" },
  SlaveSelenoidDelay_Comp3:         { request: "r,meth:setSlaveSelenoidDelay_Comp3,-,2,-,1,0x1305" },
  SlaveAirFlow_Comp0:               { request: "r,meth:setSlaveAirFlow_Comp0,-,2,-,1,0x1006" },
  SlaveAirFlow_Comp1:               { request: "r,meth:setSlaveAirFlow_Comp1,-,2,-,1,0x1106" },
  SlaveAirFlow_Comp2:               { request: "r,meth:setSlaveAirFlow_Comp2,-,2,-,1,0x1206" },
  SlaveAirFlow_Comp3:               { request: "r,meth:setSlaveAirFlow_Comp3,-,2,-,1,0x1306" },
  SlaveNominalPower_Comp0:          { request: "r,meth:setSlaveNominalPower_Comp0,-,2,-,1,0x1008" },
  SlaveNominalPower_Comp1:          { request: "r,meth:setSlaveNominalPower_Comp1,-,2,-,1,0x1108" },
  SlaveNominalPower_Comp2:          { request: "r,meth:setSlaveNominalPower_Comp2,-,2,-,1,0x1208" },
  SlaveNominalPower_Comp3:          { request: "r,meth:setSlaveNominalPower_Comp3,-,2,-,1,0x1308" },
  SlaveUnloadPower_Comp0:           { request: "r,meth:setSlaveUnloadPower_Comp0,-,2,-,1,0x1009" },
  SlaveUnloadPower_Comp1:           { request: "r,meth:setSlaveUnloadPower_Comp1,-,2,-,1,0x1109" },
  SlaveUnloadPower_Comp2:           { request: "r,meth:setSlaveUnloadPower_Comp2,-,2,-,1,0x1209" },
  SlaveUnloadPower_Comp3:           { request: "r,meth:setSlaveUnloadPower_Comp3,-,2,-,1,0x1309" },
  SlavePriorityInS0_Comp0:          { request: "r,meth:setSlavePriorityInS0_Comp0,-,2,-,1,0x100A" },
  SlavePriorityInS0_Comp1:          { request: "r,meth:setSlavePriorityInS0_Comp1,-,2,-,1,0x110A" },
  SlavePriorityInS0_Comp2:          { request: "r,meth:setSlavePriorityInS0_Comp2,-,2,-,1,0x120A" },
  SlavePriorityInS0_Comp3:          { request: "r,meth:setSlavePriorityInS0_Comp3,-,2,-,1,0x130A" },
  SlavePriorityInS1_Comp0:          { request: "r,meth:setSlavePriorityInS1_Comp0,-,2,-,1,0x100B" },
  SlavePriorityInS1_Comp1:          { request: "r,meth:setSlavePriorityInS1_Comp1,-,2,-,1,0x110B" },
  SlavePriorityInS1_Comp2:          { request: "r,meth:setSlavePriorityInS1_Comp2,-,2,-,1,0x120B" },
  SlavePriorityInS1_Comp3:          { request: "r,meth:setSlavePriorityInS1_Comp3,-,2,-,1,0x130B" },
  SlavePriorityInS2_Comp0:          { request: "r,meth:setSlavePriorityInS2_Comp0,-,2,-,1,0x100C" },
  SlavePriorityInS2_Comp1:          { request: "r,meth:setSlavePriorityInS2_Comp1,-,2,-,1,0x110C" },
  SlavePriorityInS2_Comp2:          { request: "r,meth:setSlavePriorityInS2_Comp2,-,2,-,1,0x120C" },
  SlavePriorityInS2_Comp3:          { request: "r,meth:setSlavePriorityInS2_Comp3,-,2,-,1,0x130C" },
  SlavePriorityInS3_Comp0:          { request: "r,meth:setSlavePriorityInS3_Comp0,-,2,-,1,0x100D" },
  SlavePriorityInS3_Comp1:          { request: "r,meth:setSlavePriorityInS3_Comp1,-,2,-,1,0x110D" },
  SlavePriorityInS3_Comp2:          { request: "r,meth:setSlavePriorityInS3_Comp2,-,2,-,1,0x120D" },
  SlavePriorityInS3_Comp3:          { request: "r,meth:setSlavePriorityInS3_Comp3,-,2,-,1,0x130D" },
  C00x:            { request: "r,meth:setC00x,-,8,-,1,0x100E" },
  C01x:            { request: "r,meth:setC01x,-,8,-,1,0x110E" },
  C02x:            { request: "r,meth:setC02x,-,8,-,1,0x120E" },
  C03x:            { request: "r,meth:setC03x,-,8,-,1,0x130E" },
  M00x:      { request: "r,meth:setM00x,-,16,-,1,0x1012" },
  M01x:      { request: "r,meth:setM01x,-,16,-,1,0x1112" },
  M02x:      { request: "r,meth:setM02x,-,16,-,1,0x1212" },
  M03x:      { request: "r,meth:setM03x,-,16,-,1,0x1312" },
  SlaveNumberOfTotalCompressorHours_Comp0:    { request: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp0,-,4,-,1,0x101A" },
  SlaveNumberOfTotalCompressorHours_Comp1:    { request: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp1,-,4,-,1,0x111A" },
  SlaveNumberOfTotalCompressorHours_Comp2:    { request: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp2,-,4,-,1,0x121A" },
  SlaveNumberOfTotalCompressorHours_Comp3:    { request: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp3,-,4,-,1,0x131A" },
  SlaveNumberOfLoadCompressorHours_Comp0:     { request: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp0,-,4,-,1,0x101C" },
  SlaveNumberOfLoadCompressorHours_Comp1:     { request: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp1,-,4,-,1,0x111C" },
  SlaveNumberOfLoadCompressorHours_Comp2:     { request: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp2,-,4,-,1,0x121C" },
  SlaveNumberOfLoadCompressorHours_Comp3:     { request: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp3,-,4,-,1,0x131C" },
  SlaveMaintCounters_Comp0:                   { request: "r,meth:setSlaveMaintCounters_Comp0,-,24,-,1,0x101E" },
  SlaveMaintCounters_Comp1:                   { request: "r,meth:setSlaveMaintCounters_Comp1,-,24,-,1,0x111E" },
  SlaveMaintCounters_Comp2:                   { request: "r,meth:setSlaveMaintCounters_Comp2,-,24,-,1,0x121E" },
  SlaveMaintCounters_Comp3:                   { request: "r,meth:setSlaveMaintCounters_Comp3,-,24,-,1,0x131E" },
  //Clock Timers
  ClockTimer0:     { request: "r,meth:setClockTimer0,-,6,-,1,0x700" },
  ClockTimer1:     { request: "r,meth:setClockTimer1,-,6,-,1,0x703" },
  ClockTimer2:     { request: "r,meth:setClockTimer2,-,6,-,1,0x706" },
  ClockTimer3:     { request: "r,meth:setClockTimer3,-,6,-,1,0x709" },
  ClockTimer4:     { request: "r,meth:setClockTimer4,-,6,-,1,0x70C" },
  ClockTimer5:     { request: "r,meth:setClockTimer5,-,6,-,1,0x70F" },
  ClockTimer6:     { request: "r,meth:setClockTimer6,-,6,-,1,0x712" },
  ClockTimer7:     { request: "r,meth:setClockTimer7,-,6,-,1,0x715" },
  ClockTimer8:     { request: "r,meth:setClockTimer8,-,6,-,1,0x718" },
  ClockTimer9:     { request: "r,meth:setClockTimer9,-,6,-,1,0x71B" },
  ClockTimer10:    { request: "r,meth:setClockTimer10,-,6,-,1,0x71E" },
  ClockTimer11:    { request: "r,meth:setClockTimer11,-,6,-,1,0x721" },
  ClockTimer12:    { request: "r,meth:setClockTimer12,-,6,-,1,0x724" },
  ClockTimer13:    { request: "r,meth:setClockTimer13,-,6,-,1,0x727" },
  ClockTimer14:    { request: "r,meth:setClockTimer14,-,6,-,1,0x72A" },
  ClockTimer15:    { request: "r,meth:setClockTimer15,-,6,-,1,0x72D" },
  ClockTimer16:    { request: "r,meth:setClockTimer16,-,6,-,1,0x730" },
  ClockTimer17:    { request: "r,meth:setClockTimer17,-,6,-,1,0x733" },
  ClockTimer18:    { request: "r,meth:setClockTimer18,-,6,-,1,0x736" },
  ClockTimer19:    { request: "r,meth:setClockTimer19,-,6,-,1,0x739" },
  ClockTimer20:    { request: "r,meth:setClockTimer20,-,6,-,1,0x73C" },
  //
  R02:                               { request: "r,meth:setR02,-,2,-,1,0x500" },
  V01:                               { request: "r,meth:setV01,-,2,-,1,0x501" },
  WPx:                               { request: "r,meth:setWPx,-,12,-,1,0x502" },
  WTx:                               { request: "r,meth:setWTx,-,8,-,1,0x508" },
  V04:                               { request: "r,meth:setV04,-,2,-,1,0x50C" },
  V02:                               { request: "r,meth:setV02_V03,-,4,-,1,0x50D" },
  V07:                               { request: "r,meth:setV07,-,2,-,0x50F" },
  S11:                               { request: "r,meth:setS11,-,2,-,0x510" },
  T01:                               { request: "r,meth:setT01,-,2,-,0x511" },
  S14:                               { request: "r,meth:setS14,-,2,-,0x512" },
  R01:                               { request: "r,meth:setR01,-,2,-,0x513" },
  S00:                               { request: "r,meth:setS00_S01_S02, -,6,-,0x514" },
  S09:                               { request: "r,meth:setS09_S10,-,4,-,0x517" },
  S06:                               { request: "r,meth:setS06,-,2,-,0x519" },
  S05:                               { request: "r,meth:setS05,-,2,-,0x51A" },
  S07:                               { request: "r,meth:setS07_S08,-,4,-,0x51B" },
  S12:                               { request: "r,meth:setS12_S13,-,4,-,0x51D" },
  S17:                               { request: "r,meth:setS17,-,2,-,0x51F" },
  S16:                               { request: "r,meth:setS16,-,2,-,0x520" },
  S03:                               { request: "r,meth:setS03_S04,-,4,-,0x521" },
  S18:                               { request: "r,meth:setS18_S19,-,4,-,0x523" },
  S21:                               { request: "r,meth:setS21,-,2,-,0x525" },
  S20:                               { request: "r,meth:setS20,-,2,-,0x526" },
  S22:                               { request: "r,meth:setS22,-,2,-,0x527" },
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
    TotalEnergyConsumption:                     { rprop:"TotalEnergyConsumption", rcmd: "r,meth:setTotalEnergyConsumption,-,4,-,1,0x600", min: 1, max: 1, offset: "0X600", multiplier: [10] },
    AirProduced:                                { rprop:"AirProduced", rcmd: "r,meth:setAirProduced,-,4,-,1,0x602", min: 1, max: 1, offset: "0x602"},
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
    C00:                      { rprob: "C00x", rcmd: "r,meth:setC00x,-,8,-,0x100E", min: 2, max: 5, offset:"0x100E" },
    C01:                      { rprob: "C01x", rcmd: "r,meth:setC01x,-,8,-,0x110E", min: 2, max: 5, offset:"0x110E" },
    C02:                      { rprob: "C02x", rcmd: "r,meth:setC02x,-,8,-,0x120E", min: 2, max: 5, offset:"0x120E" },
    C03:                      { rprob: "C03x", rcmd: "r,meth:setC03x,-,8,-,0x130E", min: 2, max: 5, offset:"0x130E" },
    M00:                { rprob: "M00x", rcmd: "r,meth:setM00x,-,16,-,0x1012", min: 0, max: 7, offset:"0x1012" },
    M01:                { rprob: "M01x", rcmd: "r,meth:setM01x,-,16,-,0x1112", min: 0, max: 7, offset:"0x1112" },
    M02:                { rprob: "M02x", rcmd: "r,meth:setM02x,-,16,-,0x1212", min: 0, max: 7, offset:"0x1212" },
    M03:                { rprob: "M03x", rcmd: "r,meth:setM03x,-,16,-,0x1312", min: 0, max: 7, offset:"0x1312" },
    SlaveNumberOfTotalCompressorHours_Comp0:    { rprob: "SlaveNumberOfTotalCompressorHours_Comp0", rcmd: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp0,-,4,-,0x101A", min: 1, max: 1, offset:"0x101A" , multiplier: [60] },
    SlaveNumberOfTotalCompressorHours_Comp1:    { rprob: "SlaveNumberOfTotalCompressorHours_Comp1", rcmd: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp1,-,4,-,0x111A", min: 1, max: 1, offset:"0x111A" , multiplier: [60] },
    SlaveNumberOfTotalCompressorHours_Comp2:    { rprob: "SlaveNumberOfTotalCompressorHours_Comp2", rcmd: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp2,-,4,-,0x121A", min: 1, max: 1, offset:"0x121A" , multiplier: [60] },
    SlaveNumberOfTotalCompressorHours_Comp3:    { rprob: "SlaveNumberOfTotalCompressorHours_Comp3", rcmd: "r,meth:setSlaveNumberOfTotalCompressorHours_Comp3,-,4,-,0x131A", min: 1, max: 1, offset:"0x131A" , multiplier: [60] },
    SlaveNumberOfLoadCompressorHours_Comp0:     { rprob: "SlaveNumberOfLoadCompressorHours_Comp0", rcmd: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp0,-,4,-,0x101C", min: 1, max: 1, offset:"0x101C" , multiplier: [60] },
    SlaveNumberOfLoadCompressorHours_Comp1:     { rprob: "SlaveNumberOfLoadCompressorHours_Comp1", rcmd: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp1,-,4,-,0x111C", min: 1, max: 1, offset:"0x111C" , multiplier: [60] },
    SlaveNumberOfLoadCompressorHours_Comp2:     { rprob: "SlaveNumberOfLoadCompressorHours_Comp2", rcmd: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp2,-,4,-,0x121C", min: 1, max: 1, offset:"0x121C" , multiplier: [60] },
    SlaveNumberOfLoadCompressorHours_Comp3:     { rprob: "SlaveNumberOfLoadCompressorHours_Comp3", rcmd: "r,meth:setSlaveNumberOfLoadCompressorHours_Comp3,-,4,-,0x131C", min: 1, max: 1, offset:"0x131C" , multiplier: [60] },

    
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
    "r,meth:setSlaveControllerState_Comp0,5,2,1,1,0x1001|"+
    "r,meth:setSlaveControllerState_Comp1,5,2,1,1,0x1101|"+
    "r,meth:setSlaveControllerState_Comp2,5,2,1,1,0x1201|"+
    "r,meth:setSlaveControllerState_Comp3,5,2,1,1,0x1301|"+
    "r,meth:setBlockingAlarm,5,2,1,1,0x401|"+
    "r,meth:setWorkingPressure,3,2,0,1,0x404|"+
    "r,meth:setSlaveMaintCounters_Comp0,3600,24,1,1,0x101E|"+
    "r,meth:setSlaveMaintCounters_Comp1,3600,24,1,1,0x111E|"+
    "r,meth:setSlaveMaintCounters_Comp2,3600,24,1,1,0x121E|"+
    "r,meth:setSlaveMaintCounters_Comp3,3600,24,1,1,0x131E|"+
    "r,meth:setSlaveNumberOfTotalCompressorHours_Comp0,3600,4,1,1,0x101A|"+
    "r,meth:setSlaveNumberOfTotalCompressorHours_Comp1,3600,4,1,1,0x111A|"+
    "r,meth:setSlaveNumberOfTotalCompressorHours_Comp2,3600,4,1,1,0x121A|"+
    "r,meth:setSlaveNumberOfTotalCompressorHours_Comp3,3600,4,1,1,0x131A|"+
    "r,meth:setSlaveNumberOfLoadCompressorHours_Comp0,3600,4,1,1,0x101C|"+
    "r,meth:setSlaveNumberOfLoadCompressorHours_Comp1,3600,4,1,1,0x111C|"+
    "r,meth:setSlaveNumberOfLoadCompressorHours_Comp2,3600,4,1,1,0x121C|"+
    "r,meth:setSlaveNumberOfLoadCompressorHours_Comp3,3600,4,1,1,0x131C|";
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
        
        await Device.api.setProperty("IOBoardFwVersion", {
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
        
        await Device.api.setProperty("SlaveFwVersion_Comp''' + str(compressorNo) + '''", {
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
#  C0Xx
#
#####################
def setC0Xx_body(compressorNo):
    return '''/**
*/
const itemCount = 4;

let C0''' + str(compressorNo) + '''x = {};
for (var x = 0; x < itemCount; x++) {
    C0''' + str(compressorNo) + '''x['C0''' + str(compressorNo) + '''_' + (x+2).toString()] = '-';
}

Device.api.log("info", "C0''' + str(compressorNo) + '''x: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        itemValue = itemValue.toString();
        C0''' + str(compressorNo) + '''x['C0''' + str(compressorNo) + '''' + ((i/2)+2).toString()] = itemValue;
    }
    
    Device.api.setProperty("C0''' + str(compressorNo) + '''x", {
      value:  C0''' + str(compressorNo) + '''x,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
'''

def writeC0Xx_body(compressorNo):
    return """/**
*/

let args = {
    tagKey: "C0 ''' + str(compressorNo) + '''x",
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
#  M0Xx
#
#####################

def setM0Xx_body(compressorNo):
    return '''/**
*/

const itemCount = 8;

let M0''' + str(compressorNo) + '''x = {};
for (var x = 0; x < itemCount; x++) {
    M0''' + str(compressorNo) + '''x['M0''' + str(compressorNo) + '''_' + (x).toString()] = '-';
}

Device.api.log("info", "M0''' + str(compressorNo) + '''x: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);

        if (i > 2) itemValue = itemValue.toString() + " hours";
        else itemValue = itemValue.toString();
        M0''' + str(compressorNo) + '''x['M0''' + str(compressorNo) + '''' + ((i/2)).toString()] = itemValue;
    }
    
    Device.api.setProperty("M0''' + str(compressorNo) + '''x", {
      value:  M0''' + str(compressorNo) + '''x,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
'''

def writeM0Xx_body(compressorNo):
    return """/**
*/

let args = {
    tagKey: "M0 ''' + str(compressorNo) + '''x",
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
#  SlaveNumberOfTotalCompressorHours
#
#####################

def setSlaveNumberOfTotalCompressorHours_body(compressorNo):
    return '''/**
*/
const tagPropName = "SlaveNumberOfTotalCompressorHours_Comp''' + str(compressorNo) + '''";
let SlaveNumberOfTotalCompressorHours = Device.convertToDec({ values: value }, -1);
SlaveNumberOfTotalCompressorHours = SlaveNumberOfTotalCompressorHours / 60;
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveNumberOfTotalCompressorHours = SlaveNumberOfTotalCompressorHours.toString() + " Hours";
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
SlaveNumberOfLoadCompressorHours = SlaveNumberOfLoadCompressorHours / 60;
Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SlaveNumberOfLoadCompressorHours = SlaveNumberOfLoadCompressorHours.toString() + " Hours";
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

#####################
#
#  ClockTimer
#
#####################
def setClockTimer_body(timerNo):
    return '''/**
Bit mapped:
-bit9..bit0:  10 bits, setpoint pressure [0.1bar], from 0.0bar=0 to 60.0bar=600 
-bit14..bit10: 5 bits, delta pressure [0.1bar], from 0.2bar=2 to 3.0bar=30
-bit19..bit15: 5 bits, on hour, from 0 to 23, 31 to disable this timer
-bit25..bit20: 6 bits, on minute, from 0 to 59 -bit30..bit26: 5 bits, off hour, from 0 to 23
-bit36..bit31: 6 bits, off minute, from 0 to 59
-bit40..bit37: 4 bits, day of week, 0=monday, 1=tuesday, ..,6=sunday, 7 monday to friday, 8 saturday and sunday, 9 all days, 10 monday to saturday, 11 tuesday to thursday
-bit42..bit41: 2 bits, priority set, from 0 to 3
-bit47..bit43: 5 bits, always set to 0

*/ 
const tagPropName = "ClockTimer''' + str(timerNo) + '''";

let myvalue = { values: value };
let first4Bytes = myvalue.slice(0,4);
let last3Bytes = myvalue.slice(3,6);
let first4BytesInDecimal = Device.convertToDec(first4Bytes,-1);
let last3BytesInDecimal = Device.convertToDec(last3Bytes,-1);

let clockTimer = {};
let setPointPressure = (first4BytesInDecimal >> 22) / 10;
clockTimer.setPointPressure = setPointPressure;

let deltaPressure = ((first4BytesInDecimal >> 17) & 31) / 10;
clockTimer.deltaPressure = deltaPressure;

let onHour = ((first4BytesInDecimal >> 12) & 31);
let onMinutes = ((first4BytesInDecimal >> 6) & 63);
clockTimer.onTime = onHours.toString() + ":" + onMinutes.toString();

let offHours = ((first4BytesInDecimal >> 1) & 31);
let offMinutes = ((last3BytesInDecimal >> 11) & 63);
clockTimer.offTime = offHours.toString() + ":" + offMinutes.toString();

let daysOfWeek = ((last3BytesInDecimal >> 7) & 15);
clockTimer.daysOfWeek = daysOfWeek;

let prioritySet = ((last3BytesInDecimal >> 5) & 3);
clockTimer.prioritySet = prioritySet;

let startPressure = setPointPressure - deltaPressure;
clockTimer.startPressure = startPressure;

let stopPressure = setPointPressure + deltaPressure;
clockTimer.stopPressure = stopPressure;

Device.api.setProperty(tagPropName, {
    value: clockTimer,
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
'''