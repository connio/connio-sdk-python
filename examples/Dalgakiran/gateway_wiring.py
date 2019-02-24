
# ~readTag()
# ~writeAndReadTag()
# ~writeTag()
# ~restart()
# ~setModbusSettings()

#
#
#
def readTag_body():
    return """/**
  Sends gateway a read tag request if gateway is connected.
*/
try {
    let request = Device.fetchReadRequest(value.requestKey)
    return Device.api.getProperty("connectionStatus").then(prop =>{
        if (prop.value !== "online") {
           throw Device.name + " is not online";
        }
        Device.api.setProperty("modbus_readrequest", {
          value: request,
          time: new Date().toISOString()
        }).then(prop => {
            value.done("Read request [" + request  + "] sent successfully; check " + value.requestKey  + " property shortly for gateway response");
        });
    });
}
catch(e) {
    done(e);
}
"""

#
#
#
def writeAndReadTag_body():
    return """/**
  Send given write request to the gateway, waits couple seconds and send a read requests for corresponding tag.
*/
const waitTime = value.waitTime || 1500; // in miliseconds
const commandPropertyName = "modbus_writerequest";

try {
    Device.api.getProperty("connectionStatus").then(prop =>{
        if (prop.value !== "online") {
           throw Device.name + " is not online";
        }
        
        Device.api.setProperty(commandPropertyName, {
          value: value.writeRequest,
          time: new Date().toISOString()
        }).then(property => {
            setTimeout(function() {
                // Device.readTag({ 
                //     tagReadRequest: value.readRequest, 
                //     tagProperty: value.readPropertyName,
                //     done: r => done(null, "Write request [" + value.writeRequest  +"] sent successfully")
                // }); 
                Device.api.setProperty("modbus_readrequest", {
                  value: value.readRequest,
                  time: new Date().toISOString()
                }).then(prop => {
                    value.done("Write request [" + value.writeRequest  +"] sent successfully");
                });
            }, waitTime);
        });
    });
}
catch(e) {
    done(e);
}
"""

#
#
#
def writeTag_body():
    return """/**
  Send given write request to the gateway.
*/
const commandPropertyName = "modbus_writerequest";

try {
    Device.api.getProperty("connectionStatus").then(prop =>{
        if (prop.value !== "online") {
           throw Device.name + " is not online";
        }
        Device.api.setProperty(commandPropertyName, {
            value: value.cmd,
            time: new Date().toISOString()
        }).then(property => {
            value.done("Write request [" + value.cmd  +"] sent successfully");
        });
    });
}
catch(e) {
    done(e);
}
"""

#
#
#
def restart_body():
    return """/**
  Restarts the gateway
*/
Device.api.setProperty("modbus_writerequest", {
    value: "RESET DEVICE",
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, "Reset request sent successfully");
 });
"""

#
#
#
def setModbusSettings_body():
    return """/**
  Set default modbus settings.
*/
const default_settings = 
    "/dev/ttyS1:9600:8:N:1|" +
    "g0:0,g1:3600,g2:60,g3:3,g4:5|" +
    "r,meth:setAlarms,5,8,1,1,0x200|" +
    "r,meth:setNonAckAlarms,5,8,1,1,0x204|" +
    "r,meth:setControllerState,5,2,1,1,0x400|" +
    "r,meth:setCompressorState,5,2,1,1,0x401|" +
    "r,meth:setBlockingAlarm,5,2,1,1,0x402|" +
    "r,meth:setScrewTemperature,3,2,0,1,0x405|" +
    "r,meth:setWorkingPressure,3,2,0,1,0x406|" +
    "r,meth:setAuxiliaryPressure,3,2,0,1,0x407|" +
    "r,meth:setPTCInput,60,2,1,1,0x408|" +
    "r,meth:setAnalogOutFreqSet,60,2,1,1,0x40B|" +
    "r,meth:setTotalHours,3600,4,1,1,0x600|" +
    "r,meth:setLoadHours,3600,4,1,1,0x602|" +
    "r,meth:setTimeToNextMaint,3600,24,1,1,0x604";

let settings = value == "" ? undefined : value;

 Device.api.setProperty("modbus_settings", {
  value: settings || default_settings,
  time: new Date().toISOString()
  }).
then(property => {
    done(null, property.value);
});
"""
