
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
  cfgSerialNumber:      { request: "r,meth:setSerialNumber,-,20,-,1,0x00" },
  cfgLogikaModel :      { request: "r,meth:setModelNumber,-,2,-,1,0x0A" },
  cfgLogikaFwVersion:   { request: "r,meth:setReleaseNo,-,2,-,1,0x0B" },
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
  WP:                   { request: "r,meth:setWPx,-,12,-,1,0x509" },
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
    WP:  { rprop: "cfgWPx", rcmd: "r,meth:setWPx,-,12,-,1,0x509", min: 1, max: 6, offset: "0x509" },
    WT:  { rprop: "cfgWTx", rcmd: "r,meth:setWTx,-,16,-,1,0x50F", min: 0, max: 7, offset: "0x50F", multiplier: 1 },
    Wt:  { rprop: "cfgWtx_", rcmd: "r,meth:setWtx_,-,14,-,1,0x517", min: 1, max: 7, offset: "0x517", multiplier: 1 },
    C07_:{ rprop: "cfgC07_x", rcmd: "r,meth:setC07_x,-,4,-,1,0x51E", min: 1, max: 2, offset: "0x51E", multiplier: 1 },
    NAF: { rprop: "cfgNominalAirFlow", rcmd: "r,meth:setNominalAirFlow,-,2,-,1,0x528", min: 1, max: 1, offset: "0x528", multiplier: 0.1 },
    AP:  { rprop: "cfgAPx", rcmd: "r,meth:setAPx,-,10,-,1,0x529", min: 1, max: 3, offset: "0x529" },
    AP4: { rprop: "cfgAPx", rcmd: "r,meth:setAPx,-,10,-,1,0x529", min: 4, max: 4, offset: "0x52D" },
    C19_1:{ rprop:"cfgC19_x", rcmd: "r,meth:setC19_x,-,6,-,1,0x52C", min: 1, max: 1, offset: "0x52C", multiplier: 1 },
    C19_2:{ rprop:"cfgC19_x", rcmd: "r,meth:setC19_x,-,6,-,1,0x52C", min: 2, max: 2, offset: "0x52E", multiplier: 1 },
    PI:  { rprop: "cfgPIx", rcmd: "r,meth:setPIx,-,14,-,1,0x52F", min: 1, max: 7, offset: "0x52F" , multiplier: .01 }, 
    FR:  { rprop: "cfgFRx", rcmd: "r,meth:setFRx,-,4,-,1,0x536", min: 1, max: 2, offset: "0x536", multiplier: 1 },
    PT:  { rprop: "cfgPTx", rcmd: "r,meth:setPTx,-,6,-,1,0x538", min: 1, max: 3, offset: "0x538" },
    PM1: { rprop: "cfgPM1", rcmd: "r,meth:setPM1,-,2,-,1,0x53B", min: 1, max: 1, offset: "0x53B", multiplier: .01  },
    AO:  { rprop: "cfgAOx", rcmd: "r,meth:setAOx,-,8,-,1,0x53C", min: 1, max: 4, offset: "0x53C" },
    C20_:{ rprop:"cfgC20_x", rcmd: "r,meth:setC20_x,-,4,-,1,0x540", min: 1, max: 2, offset: "0x540", multiplier: 1 },
    C2:  { rprop: "cfgC2x", rcmd: "r,meth:setC2x,-,4,-,1,0x542", min: 2, max: 3, offset: "0x542", multiplier: 1 },
    DR:  { rprop: "cfgDRx", rcmd: "r,meth:setDriveProtocol,-,14,-,1,0x544", min: 0, max: 6, offset: "0x544", multiplier: 1 },
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
"r,meth:setAlarms,5,8,1,1,0x200|"+
"r,meth:setNonAckAlarms,5,8,1,1,0x204|"+
"r,meth:setControllerState,5,2,1,1,0x400|"+
"r,meth:setCompressorState,5,2,1,1,0x401|"+
"r,meth:setBlockingAlarm,5,2,1,1,0x402|"+
"r,meth:setScrewTemperature,3,2,0,1,0x405|"+
"r,meth:setWorkingPressure,3,2,0,1,0x406|"+
//"r,meth:setAuxiliaryPressure,3,2,0,1,0x407|"+
//"r,meth:setPTCInput,60,2,1,1,0x408|"+
"r,meth:setControllerSupplyVoltage,60,2,1,1,0x409|"+
//"r,meth:setAnalogOutFreqSet,60,2,1,1,0x40B|"+
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
    let command = "w," + tagValue.join(':') + ",2,0,1,0x40C";
    
    let request = { cmd: command, done: r => done(null, r) };
    Device.writeTag(request);
}
catch(e) {
    done(e);
}"""

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
done(null, "<NOT IMPLEMENTED>");
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
done(null, "<NOT IMPLEMENTED>");
"""

#####################
#
#  C07x
#
#####################

def setC07x_body():
    return """/**
*/
done(null, null);
"""

def writeC07x_body():
     return """/**
*/
done(null, "<NOT IMPLEMENTED>");
"""










#####################
#
#  
#
#####################

# NominalAirFlow
# AP1-3
# AP4
# C19_1
# C19_2
# PI1-7
# FR1-2
# PT1-3
# -PM1
# AO1-4
# C20_1, C20_2
# C22, C23
# DR0-6