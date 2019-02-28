
# ~fetchAlarmList()
# ~fetchReadRequestList()
# ~fetchWriteRequestList()
# ~fetchModbusSettings()
# ~fetchControllerStates()
# ~fetchCompressorStates()
# ~fetchCompressorStateTypes()

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
  cfgLogikaModel:                   { request: "r,meth:setModelNumber,-,2,-,1,0x0A" },
  cfgLogikaFwVersion:               { request: "r,meth:setReleaseNo,-,2,-,1,0x0B" },
  cfgLevel1Pwd:                     { request: "r,meth:setLevel1Pwd,-,6,-,1,0x100" },
  cfgLevel2Pwd:                     { request: "r,meth:setLevel2Pwd,-,6,-,1,0x103" },
  cfgLevel3Pwd:                     { request: "r,meth:setLevel3Pwd,-,6,-,1,0x106" },
  relayOutputs:                     { request: "r,meth:setRelayOutputs,-,2,-,1,0x404" },
  digitalInputs:                    { request: "r,meth:setDigitalInputs,-,2,-,1,0x405" },
  cfgMaintCycles:                   { request: "r,meth:setMaintCycles,-,12,-,1,0x52C" },
  totalHours:                       { request: "r,meth:setTotalHours,-,4,-,1,0x600" },
  totalLoadHours:                   { request: "r,meth:setTotalLoadHours,-,4,-,1,0x602" },
  maintCounters:                    { request: "r,meth:setMaintCounters,-,24,-,1,0x604" },
  loadPercInLast100h:               { request: "r,meth:setLoadPercInLast100h,-,2,-,1,0x610" },
  nbrOfStartsInLastHour:            { request: "r,meth:setNbrOfStartsInLastHour,-,2,-,1,0x611" },
  controllerTime:                   { request: "r,meth:setControllerTime,-,8,-,1,0x800" },
  // Controller specific
  DisplayedState:                   { request: "r,meth:setDisplayedState,-,2,-,1,0x403" },
  SecondTemperature:                { request: "r,meth:setSecondTemperature,-,2,-,1,0x408" },
  SecondPressure:                   { request: "r,meth:setSecondPressure,-,2,-,1,0x409" },
  Drive24VSupply:                   { request: "r,meth:setDrive24VSupply,-,2,-,1,0x40B" },
  DriveAnalogInput:                 { request: "r,meth:setDriveAnalogInput,-,2,-,1,0x40C" },
  ConfigurationSwitches:            { request: "r,meth:setConfigurationSwitches,-,4,-,1,0x500" },
  Language:                         { request: "r,meth:setLanguage,-,2,-,1,0x503" },
  ClockTimers:                      { request: "r,meth:setClockTimers,-,84,-,1,0x700" },
  PressureSelectionBits:            { request: "r,meth:setPressureSelectionBits,-,4,-,1,0x72A" },
  DaylightSavingTimeAdjustment:     { request: "r,meth:setDaylightSavingTimeAdjustment,-,2,-,1,0x804" },
  Indexes:                          { request: "r,meth:setIndexes,-,2,-,1,0x900" },
  MaintenanceOperationRecords:      { request: "r,meth:setMaintenanceOperationRecords,-,120,-,1,0x901" },
  DriveStatus:                      { request: "r,meth:setDriveStatus,-,2,-,1,0xA00" },
  DriveMeasures:                    { request: "r,meth:setDriveMeasures,-,20,-,1,0xA01" },
  DriveFaultString:                 { request: "r,meth:setDriveFaultString,-,26,-,1,0xA0B" },
  DriveCommands:                    { request: "r,meth:setDriveCommands,-,2,-,1,0xA18" },
  //
  WP:                               { request: "r,meth:setWPx,-,12,-,1,0x504" },
  SP:                               { request: "r,meth:setSPx,-,8,-,1,0x50A" },
  SP5:                              { request: "r,meth:setSP5,-,2,-,1,0x542" },
  SP6:                              { request: "r,meth:setSP6,-,2,-,1,0x548" },
  WPs:                              { request: "r,meth:setWPs,-,2,-,1,0x50E" },
  WPS2P:                            { request: "r,meth:setWPS2Px,-,6,-,1,0x50F" },
  WPS2Ps:                           { request: "r,meth:setWPS2Ps,-,2,-,1,0x512" },
  WT:                               { request: "r,meth:setWTx,-,14,-,1,0x513" },
  STA:                              { request: "r,meth:setSTAx,-,4,-,1,0x51A" },
  ST3:                              { request: "r,meth:setST3,-,2,-,1,0x51C" },
  STT1:                             { request: "r,meth:setSTT1,-,2,-,1,0x51D" },
  STD1:                             { request: "r,meth:setSTD1,-,2,-,1,0x51E" },
  Wt:                               { request: "r,meth:setWtx,-,20,-,1,0x522" },
  R0:                               { request: "r,meth:setR0x,-,4,-,1,0x53D" },
  R03:                              { request: "r,meth:setR03,-,2,-,1,0x502" },
  DS:                               { request: "r,meth:setDSx,-,12,-,1,0xA1B" },
  DA:                               { request: "r,meth:setDAx,-,26,-,1,0xA22" },
  DF:                               { request: "r,meth:setDFx,-,12,-,1,0xA2E" },
  DF7:                              { request: "r,meth:setDF7,-,2,-,1,0x541" },
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
    RelativeSpeed:                  { rprob: "RelativeSpeed", rcmd: "r,meth:setRelativeSpeed,-,0,1,0x40E", min: 1, max: 1, offset:"0x40E" },
    ConfigurationSwitches:          { rprob: "ConfigurationSwitches", rcmd: "r,meth:setConfigurationSwitches,-,4,-,1,0x500", min: 1, max: 2, offset:"0x500" },
    Language:                       { rprob: "Language", rcmd: "r,meth:setLanguage,-,2,-,1,0x503", min: 1, max: 1, offset:"0x503" },
    ClockTimers:                    { rprob: "ClockTimers", rcmd: "r,meth:setClockTimers,-,84,-,1,0x700", min: 1, max: 1, offset:"0x700" },
    PressureSelectionBits:          { rprob: "PressureSelectionBits", rcmd: "r,meth:setPressureSelectionBits,-,4,-,1,0x72A", min: 1, max: 1, offset:"0x72A" },
    Indexes:                        { rprob: "Indexes", rcmd: "r,meth:setIndexes,-,2,-,1,0x900", min: 1, max: 1, offset:"0x900" },
    MaintenanceOperationRecords:    { rprob: "MaintenanceOperationRecords", rcmd: "r,meth:setMaintenanceOperationRecords,-,120,-,1,0x901", min: 1, max: 1, offset:"0x901" },
    //
    WPx:                            { rprob: "WPx", rcmd: "r,meth:setWPx,-,12,-,1,0x504", min: 1, max: 6, offset:"0x504" },
    SPx:                            { rprob: "SPx", rcmd: "r,meth:setSPx,-,8,-,1,0x50A", min: 1, max: 4, offset:"0x50A" },
    SP5:                            { rprob: "SP5", rcmd: "r,meth:setSP5,-,2,-,1,0x542", min: 5, max: 5, offset:"0x542" },
    SP6:                            { rprob: "SP6", rcmd: "r,meth:setSP6,-,2,-,1,0x548", min: 6, max: 6, offset:"0x548" },
    WPs:                            { rprob: "WPs", rcmd: "r,meth:setWPs,-,2,-,1,0x50E", min: 1, max: 1, offset:"0x50E" },
    WPS2Px:                         { rprob: "WPS2Px", rcmd: "r,meth:setWPS2Px,-,6,-,1,0x50F", min: 3, max: 5, offset:"0x50F" },
    WPS2Ps:                         { rprob: "WPS2Ps", rcmd: "r,meth:setWPS2Ps,-,2,-,1,0x512", min: 1, max: 1, offset:"0x512" },
    WTx:                            { rprob: "WTx", rcmd: "r,meth:setWTx,-,14,-,1,0x513", min: 1, max: 7, offset:"0x513" },
    STAx:                           { rprob: "STAx", rcmd: "r,meth:setSTAx,-,4,-,1,0x51A", min: 1, max: 2, offset:"0x51A" },
    ST3:                            { rprob: "ST3", rcmd: "r,meth:setST3,-,2,-,1,0x51C", min: 3, max: 3, offset:"0x51C" },
    STT1:                           { rprob: "STT1", rcmd: "r,meth:setSTT1,-,2,-,1,0x51D", min: 1, max: 1, offset:"0x51D" },
    STD1:                           { rprob: "STD1", rcmd: "r,meth:setSTD1,-,2,-,1,0x51E", min: 1, max: 1, offset:"0x51E" },
    Wtx:                            { rprob: "Wtx", rcmd: "r,meth:setWtx,-,20,-,1,0x522", min: 1, max: 10, offset:"0x522" },
    R0x:                            { rprob: "R0x", rcmd: "r,meth:setR0x,-,4,-,1,0x53D", min: 1, max: 2, offset:"0x53D" },
    R03:                            { rprob: "R03", rcmd: "r,meth:setR03,-,2,-,1,0x502", min: 3, max: 3, offset:"0x502" },
    DSx:                            { rprob: "DSx", rcmd: "r,meth:setDSx,-,12,-,1,0xA1B", min: 1, max: 6, offset:"0xA1B" },
    DAx:                            { rprob: "DAx", rcmd: "r,meth:setDAx,-,26,-,1,0xA22", min: 0, max: 12, offset:"0xA22" },
    DFx:                            { rprob: "DFx", rcmd: "r,meth:setDFx,-,12,-,1,0xA2E", min: 1, max: 6, offset:"0xA2E" },
    DF7:                            { rprob: "DF7", rcmd: "r,meth:setDF7,-,2,-,1,0x541", min: 7, max: 7, offset:"0x541" },
    
};
return requests[value];
"""

#
#
#
def fetchModbusSettings_body():
    return """/**
*/
return "/dev/ttyS1:9600:8:N:1|"+
"g0:0,g1:3600,g2:60,g3:3,g4:5|"+
"r,meth:setAlarms,5,12,1,1,0x200|"+
"r,meth:setNonAckAlarms,5,12,1,1,0x204|"+
"r,meth:setControllerState,5,2,1,1,0x400|"+
"r,meth:setCompressorState,5,2,1,1,0x401|"+
"r,meth:setBlockingAlarm,5,2,1,1,0x402|"+
"r,meth:setScrewTemperature,3,2,0,1,0x406|"+
"r,meth:setWorkingPressure,3,2,0,1,0x407|"+
"r,meth:setControllerSupplyVoltage,60,2,1,1,0x40A|"+
"r,meth:setTotalHours,3600,4,1,1,0x600|"+
"r,meth:setTotalLoadHours,3600,4,1,1,0x602|"+
"r,meth:setMaintCounters,3600,24,1,1,0x604"
"""

#
#
#
def fetchControllerStates_body():
    return """/**

*/
return [
    { code: 0, label: "RESET" },
    { code: 1, label: "OFF" },
    { code: 2, label: "STARTING - MOTOR IN STAR CONNECTION" },
    { code: 3, label: "STARTING - PAUSE START TO DELTA CONNECTION" },
    { code: 4, label: "STARTING - ACCELERATING IN DELTA CONNECTION" },
    { code: 5, label: "LOAD RUNNING" },
    { code: 6, label: "IDLE RUNNING - PRESSURE IN RANGE" },
    { code: 7, label: "IDLE RUNNING - STOPPING" },
    { code: 8, label: "INVERTER START" },
    { code: 9, label: "INVERTER ACCELERATING" },
    { code: 10, label: "INVERTER LOAD" },
    { code: 11, label: "INVERTER IDLE RUNNING, PRESSURE IN RANGE" },
    { code: 12, label: "INVERTER IDLE, STOPPING" },
    { code: 13, label: "INVERTER STOP PAUSE" },
    { code: 14, label: "INVERTER SETUP" },
    { code: 15, label: "INVERTER POWER ON" },
    { code: 16, label: "OIL MANAGEMENT" },
    { code: 17, label: "BLOCKED BY FAULT" },
    { code: 18, label: "FACTORY TEST" }
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
// TODO
done(null, null);
"""

#
#
#
def sendCommand_body():
    return """/*
    Send compressor command to the gateway

    Valid commands are:
    
    STOP
    START
    ALARM_RESET
    START_BYPASS_WTIMER
    STOP_BYPASS_WTIMER 
    ACK_RESET_ALL_ALARMS
    RESET_AIR_FILTER_MAINT_COUNTER
    RESET_OIL_FILTER_MAINT_COUNTER
    RESET_SEP_FILTER_MAINT_COUNTER
    RESET_OIL_CHNG_MAINT_COUNTER
    RESET_COMP_MAINT_COUNTER
    RESET_BEAR_MAINT_COUNTER

    For example:

    { "value": "STOP" }
*/
const cmd = {
    START: Math.pow(2,0),
    STOP: Math.pow(2,1),
    ALARM_RESET: Math.pow(2,2),
    START_BYPASS_WTIMER: Math.pow(2,3),
    STOP_BYPASS_WTIMER: Math.pow(2,4),
    ACK_RESET_ALL_ALARMS: Math.pow(2,5),
    RESET_AIR_FILTER_MAINT_COUNTER: Math.pow(2,8),
    RESET_OIL_FILTER_MAINT_COUNTER: Math.pow(2,9),
    RESET_SEP_FILTER_MAINT_COUNTER: Math.pow(2,10),
    RESET_OIL_CHNG_MAINT_COUNTER: Math.pow(2,11),
    RESET_COMP_MAINT_COUNTER: Math.pow(2,12),
    RESET_BEAR_MAINT_COUNTER: Math.pow(2,13),
}

try {    
    if (!cmd[value]) throw value + " is not a valid command. See method description for valid commands.";
     
    let tagValue = Device.makeWriteValue({ value: cmd[value], byteCount: 2 });
    let command = "w," + tagValue.join(':') + ",2,0,1,0x40D";
    
    let request = { cmd: command, done: r => done(null, r) };
    Device.writeTag(request);
}
catch(e) {
    done(e);
}"""

#####################
#
#  DisplayedState
#
#####################

def setDisplayedState_body():
    return """/**
*/
done(null, null);
"""

#####################
#
#  SecondTemperature
#
#####################

def setSecondTemperature_body():
    return """/**
*/
done(null, null);
"""

#####################
#
#  SecondPressure
#
#####################

def setSecondPressure_body():
    return """/**
*/
done(null, null);
"""

#####################
#
#  Drive24VSupply
#
#####################

def setDrive24VSupply_body():
    return """/**
*/
done(null, null);
"""

#####################
#
#  DriveAnalogInput
#
#####################

def setDriveAnalogInput_body():
    return """/**
*/
done(null, null);
"""

#####################
#
#  DriveStatus
#
#####################

def setDriveStatus_body():
    return """/**
*/
done(null, null);
"""

#####################
#
#  DriveMeasures
#
#####################

def setDriveMeasures_body():
    return """/**
*/
done(null, null);
"""

#####################
#
#  DriveFaultString
#
#####################

def setDriveFaultString_body():
    return """/**
*/
done(null, null);
"""

#####################
#
#  DriveCommands
#
#####################

def setDriveCommands_body():
    return """/**
*/
done(null, null);
"""

#####################
#
#  DaylightSavingTimeAdjustment
#
#####################

def setDaylightSavingTimeAdjustment_body():
    return """/**
*/
done(null, null);
"""

#####################
#
#  RelativeSpeed
#
#####################

def setRelativeSpeed_body():
    return """/**
*/
done(null, null);
"""

def writeRelativeSpeed_body():
    return """/**
*/
let args = {
  tagKey: "RelativeSpeed",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  ConfigurationSwitches
#
#####################

def setConfigurationSwitches_body():
    return """/**
*/
done(null, null);
"""

def writeConfigurationSwitches_body():
    return """/**
*/
let args = {
  tagKey: "ConfigurationSwitches",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  Language
#
#####################

def setLanguage_body():
    return """/**
*/
done(null, null);
"""

def writeLanguage_body():
    return """/**
*/
let args = {
  tagKey: "Language",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  ClockTimers
#
#####################

def setClockTimers_body():
    return """/**
*/
done(null, null);
"""

def writeClockTimers_body():
    return """/**
*/
let args = {
  tagKey: "PTClockTimers",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  PressureSelectionBits
#
#####################

def setPressureSelectionBits_body():
    return """/**
*/
done(null, null);
"""

def writePressureSelectionBits_body():
    return """/**
*/
let args = {
  tagKey: "PressureSelectionBits",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  Indexes
#
#####################

def setIndexes_body():
    return """/**
*/
done(null, null);
"""

def writeIndexes_body():
    return """/**
*/
let args = {
  tagKey: "Indexes",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  MaintenanceOperationRecords
#
#####################

def setMaintenanceOperationRecords_body():
    return """/**
*/
done(null, null);
"""

def writeMaintenanceOperationRecords_body():
    return """/**
*/
let args = {
  tagKey: "MaintenanceOperationRecords",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  WPx
#
#####################

def setWPx_body():
    return """/**
*/
done(null, null);
"""

def writeWPx_body():
    return """/**
*/
let args = {
  tagKey: "WP",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  SPx
#
#####################

def setSPx_body():
    return """/**
*/
done(null, null);
"""

def writeSPx_body():
    return """/**
*/
let args = {
  tagKey: "SP",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  SP5
#
#####################

def setSP5_body():
    return """/**
*/
done(null, null);
"""

def writeSP5_body():
    return """/**
*/
let args = {
  tagKey: "SP5",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  SP6
#
#####################

def setSP6_body():
    return """/**
*/
done(null, null);
"""

def writeSP6_body():
    return """/**
*/
let args = {
  tagKey: "SP6",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  ST3
#
#####################

def setST3_body():
    return """/**
*/
done(null, null);
"""

def writeST3_body():
    return """/**
*/
let args = {
  tagKey: "ST3",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  WPs
#
#####################

def setWPs_body():
    return """/**
*/
done(null, null);
"""

def writeWPs_body():
    return """/**
*/
let args = {
  tagKey: "WPs",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  WPS2Px
#
#####################

def setWPS2Px_body():
    return """/**
*/
done(null, null);
"""

def writeWPS2Px_body():
    return """/**
*/
let args = {
  tagKey: "WPS2P",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  WPS2Ps
#
#####################

def setWPS2Ps_body():
    return """/**
*/
done(null, null);
"""

def writeWPS2Ps_body():
    return """/**
*/
let args = {
  tagKey: "WPS2Ps",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  WTx
#
#####################

def setWTx_body():
    return """/**
*/
done(null, null);
"""

def writeWTx_body():
    return """/**
*/
let args = {
  tagKey: "WT",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  STAx
#
#####################

def setSTAx_body():
    return """/**
*/
done(null, null);
"""

def writeSTAx_body():
    return """/**
*/
let args = {
  tagKey: "STA",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  STT1
#
#####################

def setSTT1_body():
    return """/**
*/
done(null, null);
"""

def writeSTT1_body():
    return """/**
*/
let args = {
  tagKey: "STT1",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  STD1
#
#####################

def setSTD1_body():
    return """/**
*/
done(null, null);
"""

def writeSTD1_body():
    return """/**
*/
let args = {
  tagKey: "STD1",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  Wtx
#
#####################

def setWtx_body():
    return """/**
*/
done(null, null);
"""

def writeWtx_body():
    return """/**
*/
let args = {
  tagKey: "Wt",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  R0x
#
#####################

def setR0x_body():
    return """/**
*/
done(null, null);
"""

def writeR0x_body():
    return """/**
*/
let args = {
  tagKey: "R0",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  R03
#
#####################

def setR03_body():
    return """/**
*/
done(null, null);
"""

def writeR03_body():
    return """/**
*/
let args = {
  tagKey: "R03",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  DSx
#
#####################

def setDSx_body():
    return """/**
*/
done(null, null);
"""

def writeDSx_body():
    return """/**
*/
let args = {
  tagKey: "DS",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  DAx
#
#####################

def setDAx_body():
    return """/**
*/
done(null, null);
"""

def writeDAx_body():
    return """/**
*/
let args = {
  tagKey: "DA",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  DFx
#
#####################

def setDFx_body():
    return """/**
*/
done(null, null);
"""

def writeDFx_body():
    return """/**
*/
let args = {
  tagKey: "DF",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""

#####################
#
#  DF7
#
#####################

def setDF7_body():
    return """/**
*/
done(null, null);
"""

def writeDF7_body():
    return """/**
*/
let args = {
  tagKey: "DF7",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""
