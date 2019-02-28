
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
 { byteNo: 1, type: 'alarm', bit: 0,             code: 'A00', label: "Setting Data Fault" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,1), code: 'A01', label: "Wrong Phase" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,2), code: 'A02', label: "High Screw Temperature" },
 { byteNo: 1, type: 'warning', bit: Math.pow(2,3), code: 'A03', label: "High Screw Temperature" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,4), code: 'A04', label: "Low Screw Temp" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,5), code: 'A05', label: "Temperature Probe Failure" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,6), code: 'A06', label: "Temperature Probe Disabled" },
 { byteNo: 1, type: 'alarm', bit: Math.pow(2,7), code: 'A07', label: "Low Voltage" },
 //
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,0), code: 'A08', label: "Max Starts Per Hour Reached" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,1), code: 'A09', label: "Input Power Fault" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,2), code: 'A10', label: "High Pressure" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,3), code: 'A11', label: "Transducer Failure" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,4), code: 'A12', label: "Emergency Stop" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,5), code: 'A13', label: "Motor Overload" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,6), code: 'A14', label: "Fan Overload" },
 { byteNo: 2, type: 'alarm', bit: Math.pow(2,7), code: 'A15', label: "Alarm OR" },
 //
 { byteNo: 3, type: 'warning', bit: Math.pow(2,0), code: 'A16', label: "Multi Unit Fault" },
 { byteNo: 3, type: 'warning', bit: Math.pow(2,1), code: 'A17', label: "Master/Slave Fault" },
 { byteNo: 3, type: 'alarm', bit: Math.pow(2,2), code: 'A18', label: "Security" },
 { byteNo: 3, type: 'warning', bit: Math.pow(2,3), code: 'A19', label: "Fieldbus Watchdog Error" },
 { byteNo: 3, type: 'alarm', bit: Math.pow(2,4), code: 'A20', label: "Air Filter Change" },
 { byteNo: 3, type: 'alarm', bit: Math.pow(2,5), code: 'A21', label: "Oil Filter Change" },
 { byteNo: 3, type: 'alarm', bit: Math.pow(2,6), code: 'A22', label: "Separator Change" },
 { byteNo: 3, type: 'alarm', bit: Math.pow(2,7), code: 'A23', label: "Oil Change" },
 //
 { byteNo: 4, type: 'alarm', bit: Math.pow(2,0), code: 'A24', label: "Compressor Check" },
 { byteNo: 4, type: 'alarm', bit: Math.pow(2,1), code: 'A25', label: "Bearing Maintenance" }
],
blackOutCode: 'A99' };
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
  cfgLevel1Pwd:         { request: "r,meth:setLevel1Pwd,-,4,-,1,0x100" },
  cfgLevel2Pwd:         { request: "r,meth:setLevel2Pwd,-,4,-,1,0x102" },
  relayOutputs:         { request: "r,meth:setRelayOutputs,-,2,-,1,0x403" },
  digitalInputs:        { request: "r,meth:setDigitalInputs,-,2,-,1,0x404" },
  cfgMaintCycles:       { request: "r,meth:setMaintCycles,-,12,-,1,0x518" },
  totalHours:           { request: "r,meth:setTotalHours,-,4,-,1,0x600" },
  totalLoadHours:       { request: "r,meth:setTotalLoadHours,-,4,-,1,0x602" },
  maintCounters:        { request: "r,meth:setMaintCounters,-,24,-,1,0x604" },
  controllerTime:       { request: "r,meth:setControllerTime,-,8,-,1,0x800" },
  // Controller specific
  P0:                   { request: "r,meth:setP0x,-,16,-,1,0x500" },
  H0:                   { request: "r,meth:setH0x,-,16,-,1,0x508" },
  t0:                   { request: "r,meth:sett0x,-,16,-,1,0x510" },
  PA:                   { request: "r,meth:setPAx,-,4,-,1,0x52A" },
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
    P0:  { rprop: "P0x", rcmd: "r,meth:setP0x,-,16,-,1,0x500", min: 0, max: 7, offset: "0x500", multiplier: 0.1 },
    H0:  { rprop: "H0x", rcmd: "r,meth:setH0x,-,16,-,1,0x508", min: 0, max: 7, offset: "0x508", multiplier: 1 },
    t0:  { rprop: "t0x", rcmd: "r,meth:sett0x,-,16,-,1,0x510", min: 1, max: 8, offset: "0x510", multiplier: 1 },
    PA:  { rprop: "PAx", rcmd: "r,meth:setPAx,-,4,-,1,0x52A", min: 1, max: 2, offset: "0x52A", multiplier: 1 },

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
"r,meth:setAlarms,5,4,1,1,0x200|"+
"r,meth:setNonAckAlarms,5,4,1,1,0x202|"+
"r,meth:setControllerState,5,2,1,1,0x400|"+
"r,meth:setCompressorState,5,2,1,1,0x401|"+
"r,meth:setBlockingAlarm,5,2,1,1,0x402|"+
"r,meth:setScrewTemperature,3,2,0,1,0x405|"+
"r,meth:setWorkingPressure,3,2,0,1,0x406|"+
"r,meth:setControllerSupplyVoltage,60,2,1,1,0x407|"+
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
    { code: 2, label: "DRYER DELAY" },
    { code: 3, label: "STARTING - MOTOR IN STAR CONNECTION" },
    { code: 4, label: "STARTING - WAIT START TO DELTA CONNECTION" },
    { code: 5, label: "STARTING - ACCELERATING IN DELTA CONNECTION" },
    { code: 6, label: "LOAD RUNNING" },
    { code: 7, label: "IDLE RUNNING - PRESSURE IN RANGE" },
    { code: 8, label: "IDLE RUNNING - STOPPING" },
    { code: 9, label: "BLOCKED BY FAULT" },
    { code: 10,label: "FACTORY TEST" }
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
    { code: 1, label: "REMOTE STOP ACTIVE" },
    { code: 2, label: "IDLE STOPPING BY REMOTE STOP" },
    { code: 3, label: "WAITING TO START" },
    { code: 4, label: "DRYER DELAY" },
    { code: 5, label: "STARTING" },
    { code: 6, label: "IDLE RUNNING" },
    { code: 7, label: "IDLE STOPPING" },
    { code: 8, label: "PRESSURE IN SET, MOTOR IS OFF" },
    { code: 9, label: "LOAD RUNNING" },
    { code: 10, label: "BLOCK" },
    { code: 11, label: "FACTORY TEST" }    
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
         PLANNED_STOPPAGES: [ 0, 11 ],
         UNPLANNED_STOPPAGES:[ 10 ]
};
"""

#
#
#
def hasInverter_body():
    return"""/**
* L9 doesn't have inverter
*/
return false;
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
    let command = "w," + tagValue.join(':') + ",2,0,1,0x408";
    
    let request = { cmd: command, done: r => done(null, r) };
    Device.writeTag(request);
}
catch(e) {
    done(e);
}"""

#####################
#
#  P0x
#
#####################

def setP0x_body():
    return """/**
    P01	RW	
    P02	RW	bar
    P03	RW	bar*10 (must be divided by 10)
    P04	RW	bar*10 (must be divided by 10)
    P05	RW	bar*10 (must be divided by 10)
    P06	RW	bar*10 (must be divided by 10)
    P07	RW	
*/

done(null, null);
"""

def writeP0x_body():
    return """/**
*/
let args = {
  tagKey: "P0",
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
#  H0x
#
#####################

def setH0x_body():
    return """/**
    H00
    H01 °C
    H02 °C
    H03 °C
    H04 °C
    H05 °C
    H06 °C
    H07
*/
done(null, null);
"""

def writeH0x_body():
    return """/**
*/
let args = {
  tagKey: "H0",
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
#  t0x
#
#####################

def sett0x_body():
    return """/**
    t1 sec
    t2 msec
    t3 sec
    t4 min
    t5 sec
    t6 hour
    t7 min
    t8
*/
done(null, null);
"""

def writet0x_body():
    return """/**
*/
let args = {
  tagKey: "t0",
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
#  PAx
#
#####################

def setPAx_body():
    return """/**
    PA1 Each nibble (4 bit) is a digit of the password (2 least significant nibbles)
    PA2 Each nibble (4 bit) is a digit of the password (3 least significant nibbles)
*/
done(null, null);
"""

def writePAx_body():
    return """/**
*/
let args = {
  tagKey: "PA",
  x: value.x,
  setValue: value.setPoint,
  byteCount: value.byteCount || 2
};

let req = Device.makeWriteRequest(args);
req.done = r => done(null, r);

Device.writeAndReadTag(req);
"""
