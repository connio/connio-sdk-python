
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
  // ---- Controller specific ----
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
  WP:                               { request: "r,meth:setWPx,-,12,-,1,0x504" },
  SP:                               { request: "r,meth:setSPx,-,8,-,1,0x50A" },
  SP5:                              { request: "r,meth:setSP5,-,2,-,1,0x542" },
  SP6:                              { request: "r,meth:setSP6,-,2,-,1,0x548" },
  //WPs:                              { request: "r,meth:setWPs,-,2,-,1,0x50E" },
  //WPS2P:                            { request: "r,meth:setWPS2Px,-,6,-,1,0x50F" },
  //WPS2Ps:                           { request: "r,meth:setWPS2Ps,-,2,-,1,0x512" },
  WT:                               { request: "r,meth:setWTx,-,14,-,1,0x513" },
  STA:                              { request: "r,meth:setSTAx,-,6,-,1,0x51A" },
  //ST3:                              { request: "r,meth:setST3,-,2,-,1,0x51C" },
  STT1:                             { request: "r,meth:setSTT1,-,2,-,1,0x51D" },
  STD1:                             { request: "r,meth:setSTD1,-,2,-,1,0x51E" },
  Wt:                               { request: "r,meth:setWtx_,-,20,-,1,0x522" },
  R0:                               { request: "r,meth:setR0x,-,4,-,1,0x53D" },
  R03:                              { request: "r,meth:setR03,-,2,-,1,0x502" },
  DS:                               { request: "r,meth:setDSx,-,12,-,1,0xA1B" },
  DA:                               { request: "r,meth:setDAx,-,28,-,1,0xA21" },
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
    WP:      { rprob: "WPx", rcmd: "r,meth:setWPx,-,12,-,1,0x504", min: 1, max: 6, offset:"0x504", multiplier: [,10,10,10,10,10] },
    SP:      { rprob: "SPx", rcmd: "r,meth:setSPx,-,8,-,1,0x50A", min: 1, max: 4, offset:"0x50A", multiplier: [,10,10,10] },
    SP5:     { rprob: "SP5", rcmd: "r,meth:setSP5,-,2,-,1,0x542", min: 5, max: 5, offset:"0x542", multiplier: [10] },
    SP6:     { rprob: "SP6", rcmd: "r,meth:setSP6,-,2,-,1,0x548", min: 6, max: 6, offset:"0x548", multiplier: [10] },
    //WPs:     { rprob: "WPs", rcmd: "r,meth:setWPs,-,2,-,1,0x50E", min: 1, max: 1, offset:"0x50E" },
    //WPS2P:   { rprob: "WPS2Px", rcmd: "r,meth:setWPS2Px,-,6,-,1,0x50F", min: 3, max: 5, offset:"0x50F" },
    //WPS2Ps:  { rprob: "WPS2Ps", rcmd: "r,meth:setWPS2Ps,-,2,-,1,0x512", min: 1, max: 1, offset:"0x512" },
    WT:      { rprob: "WTx", rcmd: "r,meth:setWTx,-,14,-,1,0x513", min: 1, max: 7, offset:"0x513", multiplier: [10,10,10,10,10,10,10] },
    STA:     { rprob: "STAx", rcmd: "r,meth:setSTAx,-,6,-,1,0x51A", min: 1, max: 3, offset:"0x51A", multiplier: [10,10,10] },
    //ST3:     { rprob: "ST3", rcmd: "r,meth:setST3,-,2,-,1,0x51C", min: 3, max: 3, offset:"0x51C" },
    STT1:    { rprob: "STT1", rcmd: "r,meth:setSTT1,-,2,-,1,0x51D", min: 1, max: 1, offset:"0x51D", multiplier: [10] },
    STD1:    { rprob: "STD1", rcmd: "r,meth:setSTD1,-,2,-,1,0x51E", min: 1, max: 1, offset:"0x51E", multiplier: [10] },
    Wt:      { rprob: "Wtx_", rcmd: "r,meth:setWtx_,-,20,-,1,0x522", min: 1, max: 10, offset:"0x522", multiplier: [,,,,,,,,,0.1] },
    R0:      { rprob: "R0x", rcmd: "r,meth:setR0x,-,4,-,1,0x53D", min: 1, max: 2, offset:"0x53D", multiplier: [10,0.1] },
    DS:      { rprob: "DSx", rcmd: "r,meth:setDSx,-,12,-,1,0xA1B", min: 1, max: 6, offset:"0xA1B", multiplier: [,,0.1,0.1,0.1,0.1] },
    DA:      { rprob: "DAx", rcmd: "r,meth:setDAx,-,28,-,1,0xA21", min: 0, max: 13, offset:"0xA21" },
    DF:      { rprob: "DFx", rcmd: "r,meth:setDFx,-,12,-,1,0xA2E", min: 1, max: 6, offset:"0xA2E", multiplier: [0.01,0.01,0.01,0.01,0.01,0.01] },
    //DF7:     { rprob: "DF7", rcmd: "r,meth:setDF7,-,2,-,1,0x541", min: 7, max: 7, offset:"0x541" },
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
    "r,meth:setNonAckAlarms,5,12,1,1,0x206|"+
    "r,meth:setControllerState,5,2,1,1,0x400|"+
    "r,meth:setCompressorState,5,2,1,1,0x401|"+
    "r,meth:setBlockingAlarm,5,2,1,1,0x402|"+
    "r,meth:setScrewTemperature,3,2,0,1,0x406|"+
    "r,meth:setWorkingPressure,3,2,0,1,0x407|"+
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
    "r,meth:setNonAckAlarms,5,12,1,1,0x206|"+
    "r,meth:setControllerState,5,2,1,1,0x400|"+
    "r,meth:setCompressorState,5,2,1,1,0x401|"+
    "r,meth:setBlockingAlarm,5,2,1,1,0x402|"+
    "r,meth:setScrewTemperature,3,2,0,1,0x406|"+
    "r,meth:setWorkingPressure,3,2,0,1,0x407|"+
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

if (!cmd[value]) throw value + " is not a valid command. See method description for valid commands.";

let tagValue = Device.makeWriteValue({ value: cmd[value], byteCount: 2 });
return "w," + tagValue.join(':') + ",2,0,1,0x40D";
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
#  WorkingFlags
#
#####################

def setWorkingFlags_body():
    return """/**
Bit mapped allocation:
0x0001 System Enable( ON state)
0x0002 Fan active
0x0004 Weekly timer bypassed by user forced start
0x0008 Start/stop remote active
0x0010 Master/slave role is master
0x0100 Second pressure set selected
0x2000 Load valve open
*/

let outputMap = Device.convertToDec({ values: value, default: 0});

let result = [];
if (outputMap & 1) result.push("System Enable( ON state)");
if (outputMap & 2) result.push("Fan active");
if (outputMap & 4) result.push("Weekly timer bypassed by user forced start");
if (outputMap & 8) result.push("Start/stop remote active");
if (outputMap & 16) result.push("Master/slave role is master");
if (outputMap & 256) result.push("Second pressure set selected");
if (outputMap & 8192) result.push("Load valve open");

Device.api.setProperty("workingFlags", {
    value: { switches: result },
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#####################
#
#  SecondTemperature
#
#####################

def setSecondTemperature_body():
    return """/**

*/
Device.api.setProperty("secondTemperature", {
    value: Device.convertToDec({ values: value, default: 0}) / 10.0,
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#####################
#
#  SecondPressure
#
#####################

def setSecondPressure_body():
    return """/**

*/
Device.api.setProperty("secondPressure", {
    value: Device.convertToDec({ values: value, default: 0}) / 10.0,
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#####################
#
#  Drive24VSupply
#
#####################

def setDrive24VSupply_body():
    return """/**

*/
Device.api.setProperty("drive24VSupply", {
    value: Device.convertToDec({ values: value, default: 0}) / 10.0,
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#####################
#
#  DriveAnalogInput
#
#####################

def setDriveAnalogInput_body():
    return """/**

*/
Device.api.setProperty("driveAnalogInput", {
    value: Device.convertToDec({ values: value, default: 0}) / 10.0,
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#####################
#
#  ConfigSwitches
#
#####################

def setConfigSwitches_body():
    return """/**
Bit mapped allocation (see menu Compressor Config): 0x0001 DST automatic adjust (menu 2 - Display Setup) 0x0002 P. S01 - Automatic Restart

1st Word:
0x0004 P. T01 - Start/stop by timer enabled
0x0008 Pressure in PSI (menu 2 - Display Setup)
0x0010 Temperature in Fahrenheit (menu 2 - Display Setup) 
0x0020 P. S03 - Fixed Timer Wt4
0x0040 P. S04 - Phase Check Active
0x0080 P. S05 - Security Active
0x0100 P. S06 - Low supply voltage check active
0x0200 P. MA1 – Multiunit slave maintenance mode
0x0400 P. D2 - Drive out4 current select
0x0800 P. D4 - Drive stop at min frequency
0x1000 P. S18 - Maintenance C_h blocking
0x2000 P. S17 - Second pressure set enabled
0x4000 P. S07-4 - M/S drive twin
0x8000 P. D5 - Drive put temp on out3 and out4

2nd Word:

0x0001 P. M08 Multiunit working hours alignment
0x0002 P. DF0 Enable PID for inverter driving fan motor
0x0004 P. D0 Variable speed compressor (star/delta vs inverter) 
0x0008 P. S19 RL1 ready function
0x0010 P. S20 PNP2 fan function

*/

let outputMap = Device.convertToDec({ values: value, default: 0});

let result = [];

// 1st word
if (outputMap & 4) result.push("T01 Start/stop by timer enabled");
if (outputMap & 8) result.push("Pressure in PSI");
if (outputMap & 16) result.push("Temperature in Fahrenheit");
if (outputMap & 32) result.push("S03 Fixed Timer Wt4");
if (outputMap & 64) result.push("S04 Phase Check Active");
if (outputMap & 128) result.push("S05 Security Active");
if (outputMap & 256) result.push("S06 Low supply voltage check active");
if (outputMap & 512) result.push("MA1 Multiunit slave maintenance mode");
if (outputMap & 1024) result.push("D2 Drive out4 current select");
if (outputMap & 2048) result.push("D4 Drive stop at min frequency");
if (outputMap & 4096) result.push("S18 Maintenance C_h blocking");
if (outputMap & 8192) result.push("S17 Second pressure set enabled");
if (outputMap & 16384) result.push("S07-4 M/S drive twin");
if (outputMap & 32768) result.push("D5 Drive put temp on out3 and out4");

let inverter = '';

// 2nd word
if (outputMap & 65536) result.push("M08 Multiunit working hours alignment");
if (outputMap & 131072) result.push("DF0 Enable PID for inverter driving fan motor");
if (outputMap & 262144) { 
    result.push("D0 Variable speed compressor (star/delta vs inverter)");
    // mark that this is a compressor with inverter
    // this value will be used by hasInverter() method
    inverter = 'DANFOSS FC';
}
if (outputMap & 524288) result.push("S19 RL1 ready function");
if (outputMap & 1048576) result.push("S20 PNP2 fan function");

//

Device.api.setProperty("configSwitches", {
    value: { 
      switches: result, 
      D0: inverter 
    },
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

def writeConfigSwitches_body():
    return """/**
*/
let args = {
  tagKey: "configSwitches",
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
#  DriveStatus
#
#####################

def setDriveStatus_body():
    return """/**
Bit mapped allocation:
  0x0001 Ready 
  0x0002 Running 
  0x0004 LowSpeed 
  0x0008 UnderFMin 
  0x0080 Alarm
  0x0100 Fault
*/
let outputMap = Device.convertToDec({ values: value, default: 0});

let result = [];
if (outputMap & 1) result.push("Ready");
if (outputMap & 2) result.push("Running");
if (outputMap & 4) result.push("LowSpeed");
if (outputMap & 8) result.push("UnderFMin");
if (outputMap & 128) result.push("Alarm");
if (outputMap & 256) result.push("Fault");

if (result.length == 0) result = ["-"];

Device.api.setProperty("driveStatus", {
    value: result.toString(),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#####################
#
#  DriveMeasures
#
#####################

def setDriveMeasures_body():
    return """/**
Elements contains (depends on drive selected):
  0-FREQ [Hz*10]
  1-POWER [kW*10 or %*10]
  2-CURRENT [A*10 or %*10]
  3-MOTOR_VOLTAGE [V or %] or for Emerson ENERGY METER L [KW*100] 
  4-DRIVE_TEMP [°C or %] or for Emerson ENERGY METER H [MW*10] 
  5-RPM [rpm]
  6-ENERGY(less significant 16bit) [kWh] 
  7-ENERGY(most significant 16bit) [kWh] 
  8-FMIN [Hz*10]
  9-FMAX [Hz*10]
*/

let frequency = Device.convertToDec({ values: value.splice(0, 2), default: 0});
let power = Device.convertToDec({ values: value.splice(2, 4), default: 0});
let current = Device.convertToDec({ values: value.splice(4, 6), default: 0});
let voltage = Device.convertToDec({ values: value.splice(6, 8), default: 0});
let temp = Device.convertToDec({ values: value.splice(8, 10), default: 0});
let rpm = Device.convertToDec({ values: value.splice(10, 12), default: 0});
let energy = Device.convertToDec({ values: value.splice(12, 16), default: 0});
let fmin = Device.convertToDec({ values: value.splice(16, 18), default: 0});
let fmax = Device.convertToDec({ values: value.splice(18), default: 0});

let drive = {
  frequency: frequency / 10,
  power: power / 10,
  current: current / 10,
  voltage: voltage,
  temp: temp,
  rpm: rpm,
  energy: energy,
  fmin: fmin / 10,
  fmax: fmax / 10
};

//let msg = `${drive.frequency}, ${drive.power}, ${drive.current}, ${drive.voltage}, ${drive.temp}, ${drive.rpm}, ${drive.energy}, ${drive.fmin}, ${drive.fmax}`;
//Device.api.log("info", msg).then(i => done(null, null));

Device.api.setProperty("driveMeasures", {
    value: drive,
    time: new Date().toISOString()
}).then(prop => {
   done(null, null);
});
"""

#####################
#
#  DriveFaultString
#
#####################

def setDriveFaultString_body():
    return """/**
ASCII string '\0' terminated
*/
function toFaultString(fault) {
    let flag = false;
    let faultString = "";
    
    for (let i = 0; i < fault.length; i++) {
      if ( fault[i] != 0 && !flag ) {
          faultString += String.fromCharCode(fault[i]);
      }
      else if ( fault[i] == 0 ) {
          flag = true;
      }
    }
    return faultString;
}
(async function f(faultString) {
    await Device.api.setProperty("driveFaultString", {
        value: faultString,
        time: new Date().toISOString()
    });
    
    done(null, faultString);
    
})(toFaultString(value));
"""

#####################
#
#  DriveCommands
#
#####################

def setDriveCommands_body():
    return """/**
Bit mapped allocation:
  0x0001 Enable
  0x0020 Run
  0x0040 Fixed frequency (minimum frequency) 
  0x0200 Force max speed
*/
let outputMap = Device.convertToDec({ values: value, default: 0});

let result = [];
if (outputMap & 1) result.push("Enable");
if (outputMap & 32) result.push("Run");
if (outputMap & 64) result.push("Fixed frequency");
if (outputMap & 512) result.push("Force max speed");

if (result.length == 0) result = ["-"];

Device.api.setProperty("driveCommands", {
    value: result.toString(),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""


#####################
#
#  WPx
#
#####################

def setWPx_body():
    return """/**
WP1	RW	bar
WP2	RW	bar*10 (must be divided by 10)
WP3	RW	bar*10 (must be divided by 10)
WP4	RW	bar*10 (must be divided by 10)
WP5	RW	bar*10 (must be divided by 10)
WP6	RW	bar*10 (must be divided by 10)
*/

const itemCount = 6;
const tagPropName = "WPx";

let WPx = {};
for (var x = 0; x < itemCount; x++) {
    WPx['WP' + (x+1).toString()] = '-';
}

Device.api.log("debug", tagPropName + ": " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        // Exception: WP1 is not x10 scale like other values
        if (i > 0) itemValue = itemValue / 10;
        WPx['WP' + ((i/2)+1).toString()] = itemValue.toString() + ' bar';
    }
    
    Device.api.setProperty(tagPropName, {
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
  tagKey: "WP",
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
#  SPx
#
#####################

def setSPx_body():
    return """/**
SP1	RW	bar
SP2	RW	bar*10 (must be divided by 10)
SP3	RW	bar*10 (must be divided by 10)
SP4	RW	bar*10 (must be divided by 10)
*/
const itemCount = 4;
const tagPropName = "SPx";

let SPx = {};
for (var x = 0; x < itemCount; x++) {
    SPx['SP' + (x+1).toString()] = '-';
}

Device.api.log("debug", tagPropName + ": " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        // Exception: SP1 is not x10 scale like other values
        if (i > 0) itemValue = itemValue / 10;
        SPx['SP' + ((i/2)+1).toString()] = itemValue.toString() + ' bar';
    }
    
    Device.api.setProperty(tagPropName, {
      value: SPx,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
"""

def writeSPx_body():
    return """/**
Writes given value into SPx tag.
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}

To write 8.7 into SP2:

    {
      "value": { "x": 2, "setValue": 8.7 }
    }
*/
let args = {
  tagKey: "SP",
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
#  SP5
#
#####################

def setSP5_body():
    return """/**
SP5	RW	bar*10 (must be divided by 10)
*/
const tagPropName = "SPx";

let SP5 = Device.convertToDec({ values: value }, -1);

Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SP5 = SP5;
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
"""

def writeSP5_body():
    return """/**
*/
let args = {
  tagKey: "SP5",
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
#  SP6
#
#####################

def setSP6_body():
    return """/**
SP6	RW	bar*10 (must be divided by 10)
*/
const tagPropName = "SPx";

let SP6 = Device.convertToDec({ values: value }, -1);

Device.api.getProperty(tagPropName)
  .then(property => {
    property.value.SP6 = SP6;
    Device.api.setProperty(tagPropName, {
      value: property.value,
      time: new Date().toISOString()
    })
    .then(property => {
      done(null, property.value);
    });
  });
"""

def writeSP6_body():
    return """/**
*/
let args = {
  tagKey: "SP6",
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
WT5	R		°C x 10
WT6	R		°C x 10
WT7	R		°C x 10
*/

const itemCount = 7;

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
  tagKey: "WT",
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
#  STAx
#
#####################

def setSTAx_body():
    return """/**
STA1	R		°C x 10
STA2	R		°C x 10
STA3	R		°C x 10
*/

const itemCount = 3;

let WTx = {};
for (var x = 0; x < itemCount; x++) {
    STAx['STA' + (x+1).toString()] = '-';
}

Device.api.log("info", "STAx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        itemValue = itemValue / 10;
        STAx['STA' + ((i/2)+1).toString()] = itemValue.toString() + ' °C';
    }
    
    Device.api.setProperty("STAx", {
      value: WTx,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
"""

def writeSTAx_body():
    return """/**
*/
let args = {
  tagKey: "STA",
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
#  STT1
#
#####################

def setSTT1_body():
    return """/**
STT1 or DF8 if S09=4
*/
const tagPropName = "STT1";

let STT1 = Device.convertToDec({ values: value }, -1);

Device.api.setProperty(tagPropName, {
  value: STT1,
  time: new Date().toISOString()
})
.then(property => {
  done(null, property.value);
});
"""

def writeSTT1_body():
    return """/**
*/
let args = {
  tagKey: "STT1",
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
#  STD1
#
#####################

def setSTD1_body():
    return """/**
STD1 or DF9 if S09=4
*/
const tagPropName = "STT1";

let STD1 = Device.convertToDec({ values: value }, -1);

Device.api.setProperty(tagPropName, {
  value: STD1,
  time: new Date().toISOString()
})
.then(property => {
  done(null, property.value);
});
"""

def writeSTD1_body():
    return """/**
*/
let args = {
  tagKey: "STD1",
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
#  Wtx
#
#####################

def setWtx_body():
    return """/**
Wt1	R		second
Wt2	R		millisecond
Wt3	R		second
Wt4	R		minutes
Wt5	R		second
Wt6	R		second
Wt7	R		minutes
Wt8 R   second
Wt9 R   second
Wt10 R  min / 10
*/

const itemCount = 10;

let Wtx = {};
for (var x = 0; x < itemCount; x++) {
    Wtx['Wt' + (x+1).toString()] = '-';
}

Device.api.log("debug", "Wtx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        if (i == 18) {
          itemValue = itemValue * 10;
        }
        
        let unit = ' seconds';
        if (i == 2) {
            unit = ' milliseconds';
        }
        else if (i == 6 || i == 12 || i == 18) {
            unit = ' minutes';
        }
        
        Wtx['Wt' + ((i/2) + 1).toString()] = itemValue.toString() + unit;
    }
    
    Device.api.setProperty("Wtx_", {
      value: Wtx,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
"""

def writeWtx_body():
    return """/**
*/
let args = {
  tagKey: "Wt",
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
#  R0x [NOT IMPLEMENTED]
#
#####################

def setR0x_body():
    return """/**
*/
const itemCount = 2;

let R0x = {};
for (var x = 0; x < itemCount; x++) {
    R0x['R0' + (x+1).toString()] = '-';
}

Device.api.log("debug", "R0x: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);

        let unit;
        if (i == 2) {
          itemValue = itemValue / 10;
          unit = "Power";
        }
        else {
          itemValue = itemValue * 10;
          unit = "L/min";
        }
        
        R0x['R0' + ((i/2) + 1).toString()] = itemValue.toString() + unit;
    }
    
    Device.api.setProperty("R0x", {
      value: R0x,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
"""

def writeR0x_body():
    return """/**
*/
let args = {
  tagKey: "R0",
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
#  DSx
#
#####################

def setDSx_body():
    return """/**
DS1	R		Hz
DS2	R		Hz
DS3	R		0.1 second
DS4	R		0.1 second
DS5	R		0.01 second
DS6	R		0.01 second
*/

const itemCount = 6;

let DSx = {};
for (var x = 0; x < itemCount; x++) {
    DSx['DS' + (x+1).toString()] = '-';
}

Device.api.log("debug", "DSx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);

        let unit = " Second";
        if (i == 0 || i == 2) {
          unit = " Hz";
        }
        else if (i == 8 || i == 10) {
          itemValue = itemValue * 100;
        }
        else {
          itemValue = itemValue * 10;
        }
        
        DSx['DS' + ((i/2) + 1).toString()] = itemValue.toString() + unit;
    }
    
    Device.api.setProperty("DSx", {
      value: DSx,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
"""

def writeDSx_body():
    return """/**
*/
let args = {
  tagKey: "DS",
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
#  DAx
#
#####################

def setDAx_body():
    return """/**
*/
const itemCount = 14;

let DAx = {};
for (var x = 0; x < itemCount; x++) {
    DAx['DA' + x.toString()] = '-';
}

Device.api.log("info", "DAx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);

        DAx['DA' + (i/2).toString()] = itemValue.toString();
    }
    
    Device.api.setProperty("DAx", {
      value: DAx,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
"""

def writeDAx_body():
    return """/**
*/
let args = {
  tagKey: "DA",
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
#  DFx
#
#####################

def setDFx_body():
    return """/**
Temperature PID proportional factor [0.01]
Temperature PID integration time [0.01s]
Temperature PID derivative time [0.01s]
Temperature PID scaling [0.01]
Temperature PID adder multiplier [0.01]
Temperature PID adder offset [0.01]
*/

const itemCount = 6;

let DFx = {};
for (var x = 0; x < itemCount; x++) {
    DFx['DF' + (x+1).toString()] = '-';
}

Device.api.log("debug", "DFx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);

        let unit = "";
        if (i == 2 || i == 4) {
          unit = " seconds";
        }

        DFx['DF' + ((i/2) + 1).toString()] = itemValue.toString() + unit;
    }
    
    Device.api.setProperty("DFx", {
      value: DFx,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
"""

def writeDFx_body():
    return """/**
*/
let args = {
  tagKey: "DF",
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
#  DF7 [NOT USED]
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
