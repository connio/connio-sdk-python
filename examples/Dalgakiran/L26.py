
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
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,4), code: 'A04', label: "AC Phase Missing" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,5), code: 'A05', label: "Phase Sequence Wrong" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,7), code: 'A07', label: "Door Open" },
 //
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,1), code: 'A09', label: "Drive Fault" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,3), code: 'A11', label: "High Work Press" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,4), code: 'A12', label: "Screw Temperature Fault" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,5), code: 'A13', label: "High Screw Temperature" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,6), code: 'A14', label: "Low Screw Temperature" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,7), code: 'A15', label: "Aux Transd Sep Filter" },
 //
 { byteNo: 3, type: 'alarm', bit: Math.pow(2,2), code: 'A18', label: "Black Out" },
 { byteNo: 3, type: 'alarm', bit: Math.pow(2,4), code: 'A20', label: "PTC Motor" },
 { byteNo: 3, type: 'alarm', bit: Math.pow(2,5), code: 'A21', label: "Input Common Missing" },
 { byteNo: 3, type: 'alarm', bit: Math.pow(2,6), code: 'A22', label: "Input7" },
 //
 { byteNo: 4, type: 'alarm', bit: Math.pow(2,1), code: 'A25', label: "Separator Filter" },
 { byteNo: 4, type: 'alarm', bit: Math.pow(2,2), code: 'A26', label: "Work Press Fault" },
 { byteNo: 4, type: 'alarm', bit: Math.pow(2,3), code: 'A27', label: "Aux Press Fault" },
 { byteNo: 4, type: 'alarm', bit: Math.pow(2,4), code: 'A28', label: "Low Voltage" },
 { byteNo: 4, type: 'alarm', bit: Math.pow(2,5), code: 'A29', label: "Security" },
 { byteNo: 4, type: 'warning', bit: Math.pow(2,6), code: 'A30', label: "Screw Temperature Warning" },
 //
 { byteNo: 5, type: 'alarm', bit: Math.pow(2,0), code: 'A32', label: "Maint C H Blk" },
 { byteNo: 5, type: 'alarm', bit: Math.pow(2,1), code: 'A33', label: "Fieldbus Error" },
 { byteNo: 5, type: 'warning', bit: Math.pow(2,3), code: 'A35', label: "EEPROM Fault" },
 { byteNo: 5, type: 'warning', bit: Math.pow(2,4), code: 'A36', label: "Air Filter" },
 { byteNo: 5, type: 'warning', bit: Math.pow(2,5), code: 'A37', label: "Multi Unit Fault" },
 { byteNo: 5, type: 'warning', bit: Math.pow(2,6), code: 'A38', label: "Aux Transd Sep Filter Warning" },
 { byteNo: 5, type: 'warning', bit: Math.pow(2,7), code: 'A39', label: "Low Voltage Warning" },
 //
 { byteNo: 6, type: 'warning', bit: Math.pow(2,0), code: 'A40', label: "High Voltage" },
 { byteNo: 6, type: 'warning', bit: Math.pow(2,1), code: 'A41', label: "Clock Failure" },
 { byteNo: 6, type: 'warning', bit: Math.pow(2,2), code: 'A42', label: "RS232 Fault" },
 { byteNo: 6, type: 'warning', bit: Math.pow(2,3), code: 'A43', label: "DST Adjusted" },
 { byteNo: 6, type: 'alarm', bit: Math.pow(2,4), code: 'A44', label: "Bearing High Temp" },
 { byteNo: 6, type: 'warning', bit: Math.pow(2,7), code: 'A47', label: "Too Much Start" },
 //
 { byteNo: 7, type: 'warning', bit: Math.pow(2,0), code: 'A48', label: "Restart Changed to Manual" },
 { byteNo: 7, type: 'warning', bit: Math.pow(2,1), code: 'A49', label: "Restart Changed to Auto" },
 { byteNo: 7, type: 'warning', bit: Math.pow(2,2), code: 'A50', label: "Change Air Filter" },
 { byteNo: 7, type: 'warning', bit: Math.pow(2,3), code: 'A51', label: "Change Oil Filter" },
 { byteNo: 7, type: 'warning', bit: Math.pow(2,4), code: 'A52', label: "Change Sep Filter" },
 { byteNo: 7, type: 'warning', bit: Math.pow(2,5), code: 'A53', label: "Change Oil" },
 { byteNo: 7, type: 'warning', bit: Math.pow(2,6), code: 'A54', label: "Check Compressor" },
 { byteNo: 7, type: 'warning', bit: Math.pow(2,7), code: 'A55', label: "Check Bearings" },
 //
 { byteNo: 8, type: 'alarm', bit: Math.pow(2,5), code: 'A60', label: "Drive Fault" },
 { byteNo: 8, type: 'warning', bit: Math.pow(2,6), code: 'A61', label: "Drive Warning" },
 { byteNo: 8, type: 'alarm', bit: Math.pow(2,7), code: 'A62', label: "Drive No Communication" } 
],
blackOutCode: 'A18' };
"""

#
#
#
def fetchReadRequest_body():
    return """/**

*/
const requests = {
  cfgSerialNumber:      { request: "r,meth:setSerialNumber,-,20,-,1,0x000" },
  cfgLogikaModel :      { request: "r,meth:setLogikaModel,-,2,-,1,0x0A" },
  cfgLogikaFwVersion:   { request: "r,meth:setLogikaFwVersion,-,2,-,1,0x0B" },
  cfgLevel1Pwd:         { request: "r,meth:setLevel1Pwd,-,6,-,1,0x100" },
  cfgLevel2Pwd:         { request: "r,meth:setLevel2Pwd,-,6,-,1,0x103" },
  cfgLevel3Pwd:         { request: "r,meth:setLevel3Pwd,-,6,-,1,0x106" },
  relayOutputs:         { request: "r,meth:setRelayOutputs,-,2,-,1,0x403" },
  digitalInputs:        { request: "r,meth:setDigitalInputs,-,2,-,1,0x404" },
  cfgMaintCycles:       { request: "r,meth:setMaintCycles,-,12,-,1,0x520" },
  totalHours:           { request: "r,meth:setTotalHours,-,4,-,1,0x600" },
  totalLoadHours:       { request: "r,meth:setTotalLoadHours,-,4,-,1,0x602" },
  maintCounters:        { request: "r,meth:setMaintCounters,-,24,-,1,0x604" },
  loadPercInLast100h:   { request: "r,meth:setLoadPercInLast100h,-,2,-,1,0x610" },
  nbrOfStartsInLastHour:{ request: "r,meth:setNbrOfStartsInLastHour,-,2,-,1,0x611" },
  controllerTime:       { request: "r,meth:setControllerTime,-,8,-,1,0x800" },
  // Controller specific
  auxPressure:          { request: "r,meth:setAuxPressure,3,2,0,1,0x407" },
  ptcInput:             { request: "r,meth:setPTCInput,60,2,1,1,0x408" },
  analogueOut:          { request: "r,meth:setAnalogueOutFreq,60,2,1,1,0x40B" },
  configSwitches:       { request: "r,meth:setConfigSwitches,-,2,-,1,0x500" },
  configSelections:     { request: "r,meth:setConfigSelections,-,4,-,1,0x501" },
  driveStatus:          { request: "r,meth:setDriveStatus,-,2,-,1,0xC00" },
  driveMeasures:        { request: "r,meth:setDriveMeasures,-,20,-,1,0xC01" },
  driveFaultString:     { request: "r,meth:setDriveFaultString,-,26,-,1,0xC0B" },
  //
  WP:                   { request: "r,meth:setWPx,-,12,-,1,0x509" },
  WT:                   { request: "r,meth:setWTx,-,16,-,1,0x50F" },
  Wt:                   { request: "r,meth:setWtx_,-,14,-,1,0x517" },
  C07:                  { request: "r,meth:setC07_x,-,4,-,1,0x51E" },
  C02:                  { request: "r,meth:setC02,-,2,-,1,0x527" },
  C10:                  { request: "r,meth:setC10,-,2,-,1,0x528" },
  AP:                   { request: "r,meth:setAPx,-,10,-,1,0x529" },
  C19:                  { request: "r,meth:setC19_x,-,6,-,1,0x52C" },
  PI:                   { request: "r,meth:setPIx,-,14,-,1,0x52F" },
  FR:                   { request: "r,meth:setFRx,-,4,-,1,0x536" },
  PT:                   { request: "r,meth:setPTx,-,6,-,1,0x538" },
  PM1:                  { request: "r,meth:setPM1,-,2,-,1,0x53B" },
  AO:                   { request: "r,meth:setAOx,-,8,-,1,0x53C" },
  C20:                  { request: "r,meth:setC20_x,-,4,-,1,0x540" },
  C22:                  { request: "r,meth:setC22,-,4,-,1,0x542" },
  DR:                   { request: "r,meth:setDRx,-,14,-,1,0x544" },
  DA:                   { request: "r,meth:setDAx,-, 20,-,1,0x54B"}
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
    changeAirFilter: { rprop: "cfgMaintCycles", rcmd: "r,meth:setMaintCycles,-,12,-,1,0x520", min: 1, max: 1, offset: "0x520" },
    changeOilFilter:{ rprop: "cfgMaintCycles", rcmd: "r,meth:setMaintCycles,-,12,-,1,0x520", min: 1, max: 1, offset: "0x521" },
    changeSeperatorFilter:{ rprop: "cfgMaintCycles", rcmd: "r,meth:setMaintCycles,-,12,-,1,0x520", min: 1, max: 1, offset: "0x522" },
    changeOil:{ rprop: "cfgMaintCycles", rcmd: "r,meth:setMaintCycles,-,12,-,1,0x520", min: 1, max: 1, offset: "0x523" },
    checkCompressor:{ rprop: "cfgMaintCycles", rcmd: "r,meth:setMaintCycles,-,12,-,1,0x520", min: 1, max: 1, offset: "0x524" },
    bearingLubrication:{ rprop: "cfgMaintCycles", rcmd: "r,meth:setMaintCycles,-,12,-,1,0x520", min: 1, max: 1, offset: "0x525" },
    WP:  { rprop: "WPx", rcmd: "r,meth:setWPx,-,12,-,1,0x509", min: 1, max: 6, offset: "0x509", multiplier: [,10,10,10,10,10] },
    WT:  { rprop: "WTx", rcmd: "r,meth:setWTx,-,16,-,1,0x50F", min: 0, max: 7, offset: "0x50F" },
    Wt:  { rprop: "Wtx_", rcmd: "r,meth:setWtx_,-,14,-,1,0x517", min: 1, max: 7, offset: "0x517" },
    C07: { rprop: "C07_x", rcmd: "r,meth:setC07_x,-,4,-,1,0x51E", min: 1, max: 2, offset: "0x51E" },
    C02: { rprop: "C02", rcmd: "r,meth:setC02,-,2,-,1,0x527", min: 1, max: 1, offset: "0x527" },
    C10: { rprop: "C10", rcmd: "r,meth:setC10,-,2,-,1,0x528", min: 1, max: 1, offset: "0x528", multiplier: [0.1] },
    AP:  { rprop: "APx", rcmd: "r,meth:setAPx,-,10,-,1,0x529", min: 1, max: 3, offset: "0x529", multiplier: [10,10,10] },
    AP4: { rprop: "APx", rcmd: "r,meth:setAPx,-,10,-,1,0x529", min: 4, max: 4, offset: "0x52D", multiplier: [10] },
    C19_1:{ rprop:"C19_x", rcmd: "r,meth:setC19_x,-,6,-,1,0x52C", min: 1, max: 1, offset: "0x52C" },
    C19_2:{ rprop:"C19_x", rcmd: "r,meth:setC19_x,-,6,-,1,0x52C", min: 2, max: 2, offset: "0x52E" },
    PI:  { rprop: "PIx", rcmd: "r,meth:setPIx,-,14,-,1,0x52F", min: 1, max: 7, offset: "0x52F", multiplier: [0.01,0.01,0.01,0.01,0.01,0.01,0.01] }, 
    FR:  { rprop: "FRx", rcmd: "r,meth:setFRx,-,4,-,1,0x536", min: 1, max: 2, offset: "0x536" },
    PT:  { rprop: "PTx", rcmd: "r,meth:setPTx,-,6,-,1,0x538", min: 1, max: 3, offset: "0x538", multiplier: [10,10,10] },
    PM1: { rprop: "PM1", rcmd: "r,meth:setPM1,-,2,-,1,0x53B", min: 1, max: 1, offset: "0x53B", multiplier: [.01]  },
    AO:  { rprop: "AOx", rcmd: "r,meth:setAOx,-,8,-,1,0x53C", min: 1, max: 4, offset: "0x53C", multiplier: [10,10,10,10] },
    C20: { rprop:"C20_x", rcmd: "r,meth:setC20_x,-,4,-,1,0x540", min: 1, max: 2, offset: "0x540" },
    C22: { rprop: "C22", rcmd: "r,meth:setC2x,-,4,-,1,0x542", min: 2, max: 3, offset: "0x542" },
    DR:  { rprop: "DRx", rcmd: "r,meth:setDRx,-,14,-,1,0x544", min: 0, max: 6, offset: "0x544", multiplier: [,,,0.1,0.1,0.01,0.01] },
    DA:  { rprop: "DAx", rcmd: "r,meth:setDAx,-,20,-,1,0x54B", min: 0, max: 9, offset: "0x54B", multiplier: [10,,,10,10,10,100,,10,100]},
    
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
    "r,meth:setAlarms,5,8,1,1,0x200|"+
    "r,meth:setNonAckAlarms,5,8,1,1,0x204|"+
    "r,meth:setControllerState,5,2,1,1,0x400|"+
    "r,meth:setCompressorState,5,2,1,1,0x401|"+
    "r,meth:setBlockingAlarm,5,2,1,1,0x402|"+
    "r,meth:setScrewTemperature,3,2,0,1,0x405|"+
    "r,meth:setWorkingPressure,3,2,0,1,0x406|"+
    "r,meth:setAuxPressure,3,2,0,1,0x407|"+
    "r,meth:setPTCInput,60,2,1,1,0x408|"+
    "r,meth:setControllerSupplyVoltage,60,2,1,1,0x409|"+
    "r,meth:setAnalogueOutFreq,60,2,1,1,0x40B|"+
    "r,meth:setDRx,60,14,1,1,0x544|"+
    "r,meth:setTotalHours,3600,4,1,1,0x600|"+
    "r,meth:setTotalLoadHours,3600,4,1,1,0x602|"+
    "r,meth:setMaintCounters,3600,24,1,1,0x604|"+
    "r,meth:setDriveStatus,60,2,0,1,0xC00|"+
    "r,meth:setDriveMeasures,5,20,0,1,0xC01";
}
else {
  return "/dev/ttyS1:9600:8:N:1|"+
    "g0:0,g1:3600,g2:60,g3:3,g4:5|"+
    "r,meth:setAlarms,5,8,1,1,0x200|"+
    "r,meth:setNonAckAlarms,5,8,1,1,0x204|"+
    "r,meth:setControllerState,5,2,1,1,0x400|"+
    "r,meth:setCompressorState,5,2,1,1,0x401|"+
    "r,meth:setBlockingAlarm,5,2,1,1,0x402|"+
    "r,meth:setScrewTemperature,3,2,0,1,0x405|"+
    "r,meth:setWorkingPressure,3,2,0,1,0x406|"+
    "r,meth:setAuxPressure,3,2,0,1,0x407|"+
    "r,meth:setPTCInput,60,2,1,1,0x408|"+
    "r,meth:setControllerSupplyVoltage,60,2,1,1,0x409|"+
    "r,meth:setAnalogueOutFreq,60,2,1,1,0x40B|"+
    "r,meth:setDRx,60,14,1,1,0x544|"+
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
    { code: 8, label: "INVERTER ON" },
    { code: 9, label: "INVERTER SETUP" },
    { code: 10, label: "BLOCKED BY FAULT" },
    { code: 11, label: "FACTORY TEST" }
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
    { code: 1, label: "INTERNAL PRESS TOO HIGH, WAITING" },
    { code: 2, label: "REMOTE STOP ACTIVE" },
    { code: 3, label: "STOP BY TIMER" },
    { code: 4, label: "IDLE STOPPING" },
    { code: 5, label: "IDLE STOPPING BY REMOTE STOP" },
    { code: 6, label: "IDLE STOPPING BY TIMER" },
    { code: 7, label: "PRESSURE IN SET, MOTOR IS OFF" },
    { code: 8, label: "WAITING TO START" },
    { code: 9, label: "MOTOR STARTING" },
    { code: 10, label: "IDLE RUNNING" },
    { code: 11, label: "LOAD RUNNING" },
    { code: 12, label: "SOFT BLOCK DELAY" },
    { code: 13, label: "BLOCK" },
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
return { IDLE_RUNNING: [ 10 ],
         LOAD_RUNNING: [ 11 ],
         PLANNED_STOPPAGES: [ 0, 14 ],
         UNPLANNED_STOPPAGES:[ 13 ]
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
const CFG_DRIVE_PROTOCOL = 'DRx';

async function fn() {
    const context = value;

    const { value: propValue = {} } = await Device.api.getProperty(CFG_DRIVE_PROTOCOL);
    const hasInverter = propValue
        ? propValue.DR0 === INVERTER
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
return "w," + tagValue.join(':') + ",2,0,1,0x40C";
"""

#
#
#
def setRelayOutputs_body():
    return """/**
Bit mapped allocation:
    0x0001: RL1
    0x0002: RL2
    0x0004: RL3
    0x0008: RL4
    0x0010: RL5
    0x0020: RL6
    0x0040: RL7
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
Bit mapped allocation (below L26):
  0x0001: IN1
  0x0002: IN2
  0x0004: IN3
  0x0008: IN4
  0x0010: IN5
  0x0020: IN6
  0x0040: IN7
  0x0080: Phase R (Phase Check Unit Logika Control)
  0x0100: Phase S (Phase Check Unit Logika Control)
  0x0200: Phase T (Phase Check Unit Logika Control)
  0x0400: INVERTER FAULT INPUT
  0x0800: PTC state
  0x1000: Phases Sequence Correct (Phase Check Unit Logika Control)

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
if (outputMap & 64) result.push("IN7");
if (outputMap & 128) result.push("Phase R");
if (outputMap & 256) result.push("Phase S");
if (outputMap & 512) result.push("Phase T");
if (outputMap & 1024) result.push("INVERTER FAULT INPUT");
if (outputMap & 2048) result.push("PTC state");
if (outputMap & 4096) result.push("Phases Sequence Correct");

if (result.length == 0) result = ["-"];

Device.api.setProperty("digitalInputs", {
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
def setAuxPressure_body():
    return """/**
*/
Device.api.setProperty("auxPressure", {
    value: Device.convertToDec({ values: value, default: 0}) / 10.0,
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#
#
#
def setPTCInput_body():
    return """/**
*/
Device.api.setProperty("ptcInput", {
    value: Device.convertToDec({ values: value, default: 0}),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#
#
#
def setAnalogueOutFreq_body():
    return """/**
*/
Device.api.setProperty("analogueOutFreq", {
    value: Device.convertToDec({ values: value, default: 0}),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#
#
#
def setConfigSwitches_body():
    return """/**
0x0001: C01 – Automatic Restart
0x0002: C03 – Fixed Timer Wt4
0x0004: C04 – Phase Check Active
0x0008: C05 – Security Active
0x0010: C06 – Low supply voltage check active
0x0020: C11 – PTC input enabled
0x0040: Temperature in Fahrenheit (menu M1-3)
0x0080: Pressure in PSI (menu M1-3)
0x0100: DST automatic adjust (menu M1-3)
0x0200: T01 - Start/stop by weekly timer enabled
0x0400: C17 – Block compressor on expiring of C–H maintenance
0x0800: C07.3 – Maintenance mode when working under multiunit
0x1000: C07.4 – Both inverter varying speed when master/slave new is active
*/

let outputMap = Device.convertToDec({ values: value, default: 0});

let result = [];
if (outputMap & 1) result.push("C01 – Automatic Restart");
if (outputMap & 2) result.push("C03 – Fixed Timer Wt4");
if (outputMap & 4) result.push("C04 – Phase Check Active");
if (outputMap & 8) result.push("C05 – Security Active");
if (outputMap & 16) result.push("C06 – Low supply voltage check active");
if (outputMap & 32) result.push("C11 – PTC input enabled");
if (outputMap & 64) result.push("Temperature in Fahrenheit (menu M1-3)");
if (outputMap & 128) result.push("Pressure in PSI (menu M1-3)");
if (outputMap & 256) result.push("DST automatic adjust (menu M1-3)");
if (outputMap & 512) result.push("T01 - Start/stop by weekly timer enabled");
if (outputMap & 1024) result.push("C17 – Block compressor on expiring of C–H maintenance");
if (outputMap & 2048) result.push("C07.3 – Maintenance mode when working under multiunit");
if (outputMap & 4096) result.push("C07.4 – Both inverter varying speed when master/slave new is active");

Device.api.setProperty("configSwitches", {
    value: { switches: result },
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#
#
#
def setConfigSelections_body():
    return """/**
Bit mapped allocation (see menu Compressor Config):

1st WORD

Bit0..Bit2: C19 – AUX PRESS INPUT
0 disabled, 1 delta pressure, 2 power from drive, 3 current from drive, 4 temperature from drive

Bit3..Bit4: C07 – MULTIUNIT
0 no multiunit or master/slave, 1 master/slave, 2 master/slave new, 3 multiunit slave

Bit5..Bit6: C18 – ANALOG OUTPUT MODE 
0 not used, 1 regulate on pressure, 2 regulate on temperature

Bit7..Bit9: C12 – IN7 CONFIGURATION
0 disabled, 1 door, 2 control phase relay, 3 generic alarm, 4 bearing high temp alarm

Bit10..Bit11: C21 – INVERTER FAULT INPUT
0 disabled, 1 normally open, 2 normally closed

2nd WORD

Bit0..Bit3: C13 - RL2 mode:
Bit4..Bit7: C14 - RL5 mode:
Bit8..Bit11: C15 - RL6 mode
Bit12..Bit15: C16 - RL7 mode

0 default, 1 fan, 2 drain, 3 state, 4 alarm, 5 motor, 6 load,
7 lubricate, 8 null, 9 PORO, 10 PORO + Alarm, 11 Enabled
*/

function getC19Mode(v) {
  let result = 'disabled';
  switch (v) {
    case 1: result = 'delta pressure';break;
    case 2: result = 'power from drive';break;
    case 3: result = 'current from drive';break;
    case 4: result = 'temperature from drive';break;
    default: result = 'Unknown';break;
  }
  return result;
}

function getC07Mode(v) {
  let result = 'no multiunit or master/slave';
  switch (v) {
    case 1: result = 'master/slave';break;
    case 2: result = 'master/slave new';break;
    case 3: result = 'multiunit slave';break;
    default: result = 'Unknown';break;
  }
  return result;
}

function getC18Mode(v) {
  let result = 'not used';
  switch (v) {
    case 1: result = 'regulate on pressure';break;
    case 2: result = 'regulate on temperature';break;
    default: result = 'Unknown';break;
  }
  return result;
}

function getC12Mode(v) {
  let result = 'disabled';
  switch (v) {
    case 1: result = 'door';break;
    case 2: result = 'control phase relay';break;
    case 3: result = 'generic alarm';break;
    case 4: result = 'bearing high temp alarm';break;
    default: result = 'Unknown';break;
  }
  return result;
}

function getC21Mode(v) {
  let result = 'disabled';
  switch (v) {
    case 1: result = 'normally open';break;
    case 2: result = 'normally closed';break;
    default: result = 'Unknown';break;
  }
  return result;
}

function get2ndWordMode(v) {
  let result = 'default';
  switch (v) {
    case 1: result = 'fan';break;
    case 2: result = 'drain';break;
    case 3: result = 'state';break;
    case 4: result = 'alarm';break;
    case 5: result = 'motor';break;
    case 6: result = 'load';break;
    case 7: result = 'lubricate';break;
    case 8: result = 'null';break;
    case 9: result = 'PORO';break;
    case 10: result = 'PORO + Alarm';break;
    case 11: result = 'enabled';break;
    default: result = 'Unknown';break;
  }
  return result;
}

let outputMap = Device.convertToDec({ values: value, default: 0});

let result = [];

// 1st word
if (outputMap & 7) result.push(`C19 – AUX PRESS INPUT: ${getC19Mode(outputMap & 7)}`);
if (outputMap & (3 << 3)) result.push(`C07 – MULTIUNIT: ${getC07Mode(outputMap & (3 << 3))}`);
if (outputMap & (3 << 5)) result.push(`C18 – ANALOG OUTPUT MODE : ${getC18Mode(outputMap & (3 << 5))}`);
if (outputMap & (7 << 7)) result.push(`C12 – IN7 CONFIGURATION: ${getC12Mode(outputMap & (7 << 7))}`);
if (outputMap & (3 << 10)) result.push(`C21 – INVERTER FAULT INPUT: ${getC21Mode(outputMap & (3 << 10))}`);

// 2nd word
if (outputMap & (31 << 16)) result.push(`C13 - RL2 mode: ${get2ndWordMode(outputMap & (31 << 16))}`);
if (outputMap & (31 << 20)) result.push(`C14 - RL5 mode: ${get2ndWordMode(outputMap & (31 << 20))}`);
if (outputMap & (31 << 24)) result.push(`C15 - RL6 mode: ${get2ndWordMode(outputMap & (31 << 24))}`);
if (outputMap & (31 << 28)) result.push(`C16 - RL7 mode: ${get2ndWordMode(outputMap & (31 << 28))}`);

Device.api.setProperty("configSelections", {
    value: { selections: result },
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
 });"""

def writeWPx_body():
    return """/**
Writes given value into WPx tag.
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}

To write 8.7 into WP2:

    {
      "value": { "x": 2, "setValue": 8.7 }
    }
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
#  WTx
#
#####################

def setWTx_body():
    return """/**
WT0	R	    0: Disable, 1: KTY, 2: NTC	N/A
WT1	R		°C
WT2	R		°C
WT3	R		°C
WT4	R		°C
WT5	R		°C
WT6	R		°C
WT7	R		°C
*/

const itemCount = 8;

let WTx = {};
for (var x = 0; x < itemCount; x++) {
    WTx['WT' + x.toString()] = '-';
}

Device.api.log("info", "WTx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        if (i == 0 && itemValue == 0) {
            WTx['WT0'] = 'Disable';
        }
        else if (i == 0 && itemValue == 1) { 
            WTx['WT0'] = 'KTY';
        }
        else if (i == 0 && itemValue == 2) { 
            WTx['WT0'] = 'NTC';
        }
        else {
            WTx['WT' + (i/2).toString()] = itemValue.toString() + '°C';    
        }
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
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}

To write 8.7 into WT2:

    {
      "value": { "x": 2, "setValue": 8.7 }
    }
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
*/

const itemCount = 7;

let Wtx = {};
for (var x = 0; x < itemCount; x++) {
    Wtx['Wt' + (x+1).toString()] = '-';
}

Device.api.log("debug", "Wtx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        
        let unit = ' seconds';
        if (i == 2) {
            unit = ' milliseconds';
        }
        else if (i == 6 || i == 12) {
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
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
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
#  C07x
#
#####################

def setC07x_body():
    return """/**
C07_1	R		hours
C07_2	R		minutes
*/

const itemCount = 2;

let C07_x = {};
for (var x = 0; x < itemCount; x++) {
    C07_x['C07_' + (x+1).toString()] = '-';
}

Device.api.log("debug", "C07_x: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        if (i == 0) C07_x['C07_' + ((i/2)+1).toString()] = itemValue.toString() + ' hours';
        if (i == 2) C07_x['C07_' + ((i/2)+1).toString()] = itemValue.toString() + ' minutes';
    }
    
    Device.api.setProperty("C07_x", {
      value: C07_x,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });

"""

def writeC07x_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "C07",
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
#  C02
#
#####################

def setC02_body():
    return """/**
Max starts per hour
*/
Device.api.setProperty("C02", {
    value: Device.convertToDec({ values: value, default: 0}),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

def writeC02_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "C02",
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
#  C10
#
#####################

def setC10_body():
    return """/**
NominalAirFlow	R	Capacity (Nominal Air Flow) L/min *0.1 (C10)	Lt/min
*/
let setValue = Device.convertToDec({ values: value, default: 0}) * 10.0;
Device.api.setProperty("C10", {
    value: setValue,
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

def writeC10_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "C10",
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
#  APx (1-3)
#
#####################

def setAPx_body():
    return """/**
AP1	R	bar * 10 (must be divided by 10)	bar
AP2	R	bar * 10 (must be divided by 10)	bar
AP3	R	bar * 10 (must be divided by 10)	bar
---skip this element--
AP4	R	bar * 10 (must be divided by 10)	bar
*/

const itemCount = 5;

let APx = {};
let idx = 1;
for (var x = 0; x < itemCount; x++) {
    if (x != 3) {
      APx['AP' + idx.toString()] = '-';
      idx += 1;
    }
}

Device.api.log("debug", "APx: " + value.toString())
 .then(p => {
    let idx = 1;
    for (var i = 0; i < itemCount * 2; i+=2) {
        // Skip element no 4
        if (i != 6) {
          let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1) / 10;
          APx['AP' + idx.toString()] = itemValue.toString() + ' bar';
          idx += 1;
        }
    }
    
    Device.api.setProperty("APx", {
      value: APx,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
"""

def writeAPx_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "AP",
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
#  AP4
#
#####################

def writeAP4_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "AP4",
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
#  C19x
#
#####################

def setC19x_body():
    return """/**
C19_1	R		second
---skip these 2 bytes--
C19_2	R		Range analog input
*/

const itemCount = 3;

let C19_x = {};
let y = 1;
for (var x = 0; x < itemCount; x+=2) {
    C19_x['C19_' + y.toString()] = '-';
    y += 1;
}

Device.api.log("debug", "C19_x: " + value.toString())
 .then(p => {
    let y = 1;
    for (var i = 0; i < itemCount * 2; i+=2) {
        if (i != 2) {
            let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
            C19_x['C19_' + y.toString()] = itemValue.toString();
            y+=1;
        }
    }
    
    Device.api.setProperty("C19_x", {
      value: C19_x,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });

"""

#####################
#
#  C19_1
#
#####################

def writeC19_1_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "C19_1",
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
#  C19_2
#
#####################

def writeC19_2_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "C19_2",
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
#  PIx
#
#####################

def setPIx_body():
    return """/**
*/
const itemCount = 7;

let PIx = {};
for (var x = 0; x < itemCount; x++) {
    PIx['PI' + (x+1).toString()] = '-';
}

Device.api.log("debug", "PIx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = (Device.convertToDec({ values: value.slice(i,i+2) }, -1) * 100.00).toFixed(2);
        PIx['PI' + ((i/2)+1).toString()] = itemValue.toString();
    }
    
    Device.api.setProperty("PIx", {
      value: PIx,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });

"""

def writePIx_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "PI",
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
#  FRx
#
#####################

def setFRx_body():
    return """/**
FR1	Hz
FR2 Hz
*/
const itemCount = 2;

let FRx = {};
for (var x = 0; x < itemCount; x++) {
    FRx['FR' + (x+1).toString()] = '-';
}

Device.api.log("debug", "FRx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        FRx['FR' + ((i/2)+1).toString()] = itemValue.toString() + ' Hz';
    }
    
    Device.api.setProperty("FRx", {
      value: FRx,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });

"""

def writeFRx_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "FR",
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
#  PTx
#
#####################

def setPTx_body():
    return """/**
PT1	R	seconds * 10 (must be divided by 10)	second
PT2	R	seconds * 10 (must be divided by 10)	second
PT3	R	seconds * 10 (must be divided by 10)	second
*/
const itemCount = 3;

let PTx = {};
for (var x = 0; x < itemCount; x++) {
    PTx['PT' + (x+1).toString()] = '-';
}

Device.api.log("info", "PTx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1) / 10;
        PTx['PT' + ((i/2)+1).toString()] = itemValue.toString() + ' seconds';
    }
    
    Device.api.setProperty("PTx", {
      value: PTx,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
"""

def writePTx_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "PT",
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
#  PM1
#
#####################

def setPM1_body():
    return """/**
0.01
*/
let setValue = Device.convertToDec({ values: value, default: 0}) * 100;
Device.api.setProperty("PM1", {
    value: setValue,
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

def writePM1_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "PM1",
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
#  AOx
#
#####################

def setAOx_body():
    return """/**
AO1	R	bar * 10 (must be divided by 10)	bar
AO2	R	bar * 10 (must be divided by 10)	bar
AO3	R	A *10	N/A
AO4	R	A *10	N/A
*/
const itemCount = 4;

let AOx = {};
for (var x = 0; x < itemCount; x++) {
    AOx['AO' + (x+1).toString()] = '-';
}

Device.api.log("debug", "AOx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1) / 10;
        
        let unit = ' bar'
        if (i >= 4) unit = ' A';
        AOx['AO' + ((i/2)+1).toString()] = itemValue.toString() + unit;
    }
    
    Device.api.setProperty("AOx", {
      value: AOx,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });

"""

def writeAOx_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "AO",
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
#  C20x
#
#####################

def setC20x_body():
    return """/**
C20_1	R		second
C20_2	R		second
*/

const itemCount = 2;

let C20_x = {};
for (var x = 0; x < itemCount; x++) {
    C20_x['C20_' + (x+1).toString()] = '-';
}

Device.api.log("debug", "C20_x: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        C20_x['C20_' + ((i/2)+1).toString()] = itemValue.toString() + ' seconds';
    }
    
    Device.api.setProperty("C20_x", {
      value: C20_x,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
"""

def writeC20x_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "C20",
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
#  C22/3
#
#####################

def setC22_body():
    return """/**
C22	    R		seconds
C23 	R		minutes
*/

const itemCount = 2;

let C2x = {};
for (var x = 0; x < itemCount; x++) {
    C2x['C2' + (x+2).toString()] = '-';
}

Device.api.log("debug", "C22: " + value.toString())
 .then(p => {
    let unit = ' seconds';
    let multiplier = 1;
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        if (i > 0) unit = ' minutes';
        //if (i > 0) multiplier = 10;
        //C2x['C2' + ((i/2)+2).toString()] = (itemValue * multiplier).toString() + unit;
        C2x['C2' + ((i/2)+2).toString()] = itemValue.toString() + unit;
    }
    
    Device.api.setProperty("C22", {
      value: C2x,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });
"""

def writeC22_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "C22",
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
#  DRx
#
#####################

def setDRx_body():
    return """/**
DR0	R	"Drive protocol:0: NO INVERTER CONNECTED ON SECOND RS485 1: DANFOSS FC"
DR1	R	
DR2	R	
DR3	R	0.1 sec
DR4	R	0.1 sec
DR5	R	0.01
DR6	R	0.01
*/

const itemCount = 7;

let DR = {};
for (var x = 0; x < itemCount; x++) {
    DR['DR' + x.toString()] = '-';
}

Device.api.log("debug", "DRx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        if (i == 0 && itemValue == 0) itemValue = 'NO INVERTER CONNECTED ON SECOND RS485';
        else if (i == 0 && itemValue == 1) itemValue = 'DANFOSS FC';
        else if (i == 6 || i == 8) itemValue = (itemValue / 10).toFixed(1);
        else if (i == 10 || i == 12) itemValue = (itemValue / 100).toFixed(2);
        DR['DR' + (i/2).toString()] = itemValue.toString();
    }
    
    Device.api.setProperty("DRx", {
      value: DR,
      time: new Date().toISOString()
      }).
    then(property => {
        done(null, property.value);
    });
 });

"""

def writeDRx_body():
     return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "DR",
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
const itemCount = 10;

let DAx = {};
for (var x = 0; x < itemCount; x++) {
    DAx['DA' + (x).toString()] = '-';
}

Device.api.log("debug", "DAx: " + value.toString())
 .then(p => {
    for (var i = 0; i < itemCount * 2; i+=2) {
        let itemValue = Device.convertToDec({ values: value.slice(i,i+2) }, -1);
        if(i == 6 || i == 0 || i == 10 || i== 8|| i == 16) itemValue = (itemValue/10).toFixed(1);
        else if(i == 12 || i == 18 ) itemValue = (itemValue/100).toFixed(2);
        DAx['DA' + ((i/2)).toString()] = itemValue.toString();
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
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
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

let frequency = Device.convertToDec({ values: value.slice(0, 2), default: 0});
let power = Device.convertToDec({ values: value.slice(2, 4), default: 0});
let current = Device.convertToDec({ values: value.slice(4, 6), default: 0});
let voltage = Device.convertToDec({ values: value.slice(6, 8), default: 0});
let temp = Device.convertToDec({ values: value.slice(8, 10), default: 0});
let rpm = Device.convertToDec({ values: value.slice(10, 12), default: 0});
let energy = Device.convertToDec({ values: value.slice(12, 16), default: 0});
let fmin = Device.convertToDec({ values: value.slice(16, 18), default: 0});
let fmax = Device.convertToDec({ values: value.slice(18), default: 0});

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
}).then(prop =>
   Device.api.setProperty("motorSpeed", {
    value: drive.rpm,
    time: new Date().toISOString()
})).then(prop =>
   Device.api.setProperty("motorFrequency", {
    value: drive.frequency,
    time: new Date().toISOString()
})).then(prop =>
   Device.api.setProperty("motorCurrent", {
    value: drive.current,
    time: new Date().toISOString()
})).then(prop => done(null, null));

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
