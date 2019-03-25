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