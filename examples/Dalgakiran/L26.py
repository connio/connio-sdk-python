
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
  auxPressure:          { request: "r,meth:setAuxPressure,3,2,0,1,0x407" },
  ptcInput:             { request: "r,meth:setPTCInput,60,2,1,1,0x408" },
  analogueOut:          { request: "r,meth:setAnalogOutFreq,60,2,1,1,0x40B" },
  configSwitches:       { request: "r,meth:setConfigSwitches,-,2,-,1,0x500" },
  configSelections:     { request: "r,meth:setConfigSelections,-,4,-,1,0x501" },
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
    C07: { rprop: "cfgC07_x", rcmd: "r,meth:setC07_x,-,4,-,1,0x51E", min: 1, max: 2, offset: "0x51E", multiplier: 1 },
    C10: { rprop: "cfgNominalAirFlow", rcmd: "r,meth:setNominalAirFlow,-,2,-,1,0x528", min: 1, max: 1, offset: "0x528", multiplier: 0.1 },
    AP:  { rprop: "cfgAPx", rcmd: "r,meth:setAPx,-,10,-,1,0x529", min: 1, max: 3, offset: "0x529" },
    AP4: { rprop: "cfgAPx", rcmd: "r,meth:setAPx,-,10,-,1,0x529", min: 4, max: 4, offset: "0x52D" },
    C19_1:{ rprop:"cfgC19_x", rcmd: "r,meth:setC19_x,-,6,-,1,0x52C", min: 1, max: 1, offset: "0x52C", multiplier: 1 },
    C19_2:{ rprop:"cfgC19_x", rcmd: "r,meth:setC19_x,-,6,-,1,0x52C", min: 2, max: 2, offset: "0x52E", multiplier: 1 },
    PI:  { rprop: "cfgPIx", rcmd: "r,meth:setPIx,-,14,-,1,0x52F", min: 1, max: 7, offset: "0x52F" , multiplier: .01 }, 
    FR:  { rprop: "cfgFRx", rcmd: "r,meth:setFRx,-,4,-,1,0x536", min: 1, max: 2, offset: "0x536", multiplier: 1 },
    PT:  { rprop: "cfgPTx", rcmd: "r,meth:setPTx,-,6,-,1,0x538", min: 1, max: 3, offset: "0x538" },
    PM1: { rprop: "cfgPM1", rcmd: "r,meth:setPM1,-,2,-,1,0x53B", min: 1, max: 1, offset: "0x53B", multiplier: .01  },
    AO:  { rprop: "cfgAOx", rcmd: "r,meth:setAOx,-,8,-,1,0x53C", min: 1, max: 4, offset: "0x53C" },
    C20: { rprop:"cfgC20_x", rcmd: "r,meth:setC20_x,-,4,-,1,0x540", min: 1, max: 2, offset: "0x540", multiplier: 1 },
    C22: { rprop: "cfgC2x", rcmd: "r,meth:setC2x,-,4,-,1,0x542", min: 2, max: 3, offset: "0x542", multiplier: 1 },
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
"r,meth:setAuxPressure,3,2,0,1,0x407|"+
"r,meth:setPTCInput,60,2,1,1,0x408|"+
"r,meth:setControllerSupplyVoltage,60,2,1,1,0x409|"+
"r,meth:setAnalogueOutFreq,60,2,1,1,0x40B|"+
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
def hasInverter_body():
    return"""/**
@param value is the context
*/
const INVERTER = 'DANFOSS FC'
const CFG_DRIVE_PROTOCOL = 'C10';

async function fn() {
    const context = value;

    const { value: propValue = {} } = await Device.api.getProperty(CFG_DRIVE_PROTOCOL);
    const hasInverter = propValue
        ? propValue.DR0 === INVERTER
        : false;

    return Object.assign(context, {
        hasInverter,
    });
}
return Promise.resolve(fn())
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
Device.api.setProperty("analogOutFreq", {
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
*/
// TODO: Implement this
Device.api.setProperty("configSelections", {
    value: { selections: "Not Implemented" },
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
*/
let args = {
  tagKey: "C07",
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
#  C02
#
#####################

def setC02_body():
    return """/**
*/
done(null, null);
"""

def writeC02_body():
     return """/**
*/
done(null, "NOT IMPLEMENTED");
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
Device.api.setProperty("C10", {
    value: Device.convertToDec({ values: value, default: 0}) * 10.0,
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

def writeC10_body():
     return """/**
*/
let args = {
  tagKey: "C10",
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
*/
let args = {
  tagKey: "AP",
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
#  AP4
#
#####################

def writeAP4_body():
     return """/**
*/
let args = {
  tagKey: "AP4",
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
*/
let args = {
  tagKey: "C19_1",
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
#  C19_2
#
#####################

def writeC19_2_body():
     return """/**
*/
let args = {
  tagKey: "C19_2",
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
*/
let args = {
  tagKey: "PI",
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
*/
let args = {
  tagKey: "FR",
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
*/
let args = {
  tagKey: "PT",
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
#  PM1
#
#####################

def setPM1_body():
    return """/**
*/
done(null, null);
"""

def writePM1_body():
     return """/**
*/
let args = {
  tagKey: "PM1",
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
*/
let args = {
  tagKey: "AO",
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
*/
let args = {
  tagKey: "C20",
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
*/
let args = {
  tagKey: "C22",
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
        if (i == 0 && itemValue == 1) itemValue = 'DANFOSS FC';
        
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
*/
let args = {
  tagKey: "DR",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""
