# ~~ Common SET methods ~~
#
# setAny()
# setSerialNumber()
# setLogikaModel()
# setLogikaFwVersion()
# setLevelXPwd() -> where X is password level
# setAlarms()
# setNonAckAlarms()
# setControllerState()
# setCompressorState()
# setBlockingAlarm()
# setScrewTemperature()
# setWorkingPressure()
# setControllerSupplyVoltage()
# setMaintCycles()
# setTotalHours()
# setTotalLoadHours()
# setMaintCounters()
# setLoadPercInLast100h()
# setNbrOfStartsInLastHour()
# setControllerTime()

#
#
#
def setAny_body():
    return """/**
Used with readAnyTag() method to read any type of tag. 
The result is written into the 'tagValue' property.
*/

let readValue = Device.convertToDec({ values: value, default: 0 });

Device.api.setProperty("tagValue", {
    value: readValue.toString(),
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#
#
#
def setSerialNumber_body():
    return """/**
    input: [ 68, 69, 78, 69, 77, 69, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] => "Deneme"
    { "dps": [ 
    { "method": "setSerialNumber", "value": [ 68, 69, 78, 69, 77, 69, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] }          
    ]})
*/
function toSerNum(sn) {
    let flag = false;
    let serialNumber = "";
    
    for (let i = 0; i < sn.length; i++) {
      if ( sn[i] != 0 && !flag ) {
          serialNumber += String.fromCharCode(sn[i]);
      }
      else if ( sn[i] == 0 ) {
          flag = true;
      }
    }
    return serialNumber;
}
(async function f(serialNumber) {
    await Device.api.setProperty("cfgSerialNumber", {
        value: serialNumber,
        time: new Date().toISOString()
    });
    
    done(null, serialNumber);
    
})(toSerNum(value));
"""


#
#
#
def setLogikaModel_body():
    return """/**
    { "dps": [ 

    { "method": "setLogikaModel", "value": [ 2, 161 ]  }          

    ]})
    Result should be 673 (Dalgakiran)
*/
(async function f(modelNo) {
    
    await Device.api.setProperty("cfgLogikaModel", {
        value: "0x" + ("0000" + modelNo.toString(16)).slice(-4),
        time: new Date().toISOString()
    });    
    done(null, modelNo);    
})(Device.convertToDec({ values: value, default: -1}));"""

#
#
#
def setLogikaFwVersion_body():
    return """/**
    value: [ 3, 1 ] => "1.3"
*/
(async function f(major, minor) {
    let releaseNo = major.toString() + "." + minor.toString();
    
    await Device.api.setProperty("cfgLogikaFwVersion", {
        value: releaseNo,
        time: new Date().toISOString()
    });    
    done(null, releaseNo);    
})(value[0], value[1]);
"""

#
#
#
def setLevelXPwd_body(x):
    return """/**

*/
function toPassword(pwd) {
    let flag = false;
    let password = "";
    
    for (let i = 0; i < pwd.length; i++) {
      if ( pwd[i] != 0 && !flag ) {
          password += String.fromCharCode(pwd[i]);
      }
      else if ( pwd[i] == 0 ) {
          flag = true;
      }
    }
    return password;
}

(async function f(password) {
    await Device.api.setProperty("cfgLevel%sPwd", {
        value: password,
        time: new Date().toISOString()
    });
    
    //await Device.api.log("info", "Level %s password: " + password);

    done(null, password);
    
})(toPassword(value));
""" % (str(x), str(x))

#
#
#
def setAlarms_body():
    return """/**
    Sets compressor alarms
*/
const alarms = Device.fetchAlarmList();
const ALARM_LIST = alarms.list; 
const BLACK_OUT_CODE = alarms.blackOutCode; 
 
(async function f() {
    let prop = await Device.api.getProperty("activeAlarms");
    // Clone the property otherwise it will be updated when we set it.
    let activeAlarmProp = Object.assign({}, prop);
    
    // No alarm state
    let activeAlarms = { "items": [] };
    if (activeAlarmProp.value) {
      activeAlarms = activeAlarmProp.value;
    }
    
    let newAlarms = [];
    // All alarms sent in 8 bytes in total
    for (let i = 0; i < 8; i++) {
        let bitmap = value[i];
        let alarms = ALARM_LIST.filter( function(item) { return item.byteNo == i+1; } );
        
        alarms.forEach( (alarm) => {
          if (bitmap & alarm.bit) {
            newAlarms.push(alarm);
          }
        });
    }
    
    let newActivAlarmCodeList = newAlarms.map( ca => ca.code );
    let currActiveAlarmCodeList = activeAlarms.items.map( ea => ea.code );
    
    if (!(newActivAlarmCodeList.length == 0 && currActiveAlarmCodeList.length == 0) &&
        (newActivAlarmCodeList.length !== currActiveAlarmCodeList.length || 
        newActivAlarmCodeList.every((alarm, index) => !currActiveAlarmCodeList.includes(alarm)))
    ) {
        
        // For debugging purposes
        await Device.api.log('debug', "Alarm list changed; New: " + newActivAlarmCodeList.toString() + 
                                " - current: " + currActiveAlarmCodeList.toString());
        //

        // Write new list into the property
        await Device.api.setProperty("activeAlarms", {
                value: { items: newAlarms },
                time: new Date().toISOString()
            });
            
        let alarms = newAlarms.filter(aa => aa.type === 'alarm');
        let warnings = newAlarms.filter(aa => aa.type === 'warning');
        let blackOut = newAlarms.filter(aa => aa.code === BLACK_OUT_CODE);
        
        let nbrOfAlarms = alarms.length;
        let nbrOfWarnings = warnings.length;
        
        await Device.api.setProperty("nbrOfAlarms", {
                value: nbrOfAlarms,
                time: new Date().toISOString()
              });
                      
        await Device.api.setProperty("nbrOfWarnings", {
                value: nbrOfWarnings,
                time: new Date().toISOString()
              });
              
        // set last alarms and warnings if and only if there are alarms and warnings
        if (nbrOfAlarms > 0) {
            await Device.api.setProperty("lastAlarms", {
                    value: { items: alarms.map(a => { return { code: a.code, label: a.label }; }) },
                    time: new Date().toISOString()
                  });
        }
              
        if (nbrOfWarnings > 0) {
            await Device.api.setProperty("lastWarnings", {
                    value: { items: warnings.map(a => { return { code: a.code, label: a.label }; }) },
                    time: new Date().toISOString()
                  });
        }
        
        if (blackOut.length > 0) {
            await Device.api.setProperty("powercutStops", {
                        value: { blackOuts: blackOut },
                        time: new Date().toISOString()
                    });
        }
    }
    
    done(null, newAlarms);
})();
"""

#
#
#
def setNonAckAlarms_body():
    return """/**
    Sets Non acknowledged alarms
*/
const ALARM_LIST = Device.fetchAlarmList().list;
 
(async function f() {
    let prop = await Device.api.getProperty("activeAlarms");
    // Clone the property otherwise it will be updated when we set it.
    let activeAlarmProp = Object.assign({}, prop);
    
    // No alarm state
    let activeAlarms = { "items": [] };
    if (activeAlarmProp.value) {
      activeAlarms = activeAlarmProp.value;
    }
    
    let newAlarms = [];
    for (let i = 0; i < 8; i++) {
        let bitmap = value[i];
        let alarms = ALARM_LIST.filter( function(item) { return item.byteNo == i+1; } );
        
        alarms.forEach( (alarm) => {
          if (bitmap & alarm.bit) {
            newAlarms.push(alarm);
          }
        });
    }
        
    let currActivAlarmCodeList = newAlarms.map( ca => ca.code );
    let prevActiveAlarmCodeList = activeAlarms.items.map( ea => ea.code );
    
    if (!(currActivAlarmCodeList.length == 0 && prevActiveAlarmCodeList.length == 0) &&
        (currActivAlarmCodeList.length !== prevActiveAlarmCodeList.length || 
        currActivAlarmCodeList.every((value, index) => value !== prevActiveAlarmCodeList[index]))) {
        
        // Write new list into the property
        await Device.api.setProperty("activeAlarmsNonAck", {
                value: { items: newAlarms },
                time: new Date().toISOString()
            });
    }
    
    done(null, newAlarms);
})();
"""

#
#
#
def setControllerState_body():
    return """/**
    Sets controller state property
*/
let table = Device.fetchControllerStates();
let state = { code: -1, label: "NOT_SET" };
let code = Device.convertToDec({ values: value, default: -1 });

if (code >= 0 && code < table.length) {
  state = table[code];
  
  Device.api.getProperty("controllerState").then( stateProp => {
    if (!stateProp.value || state.code !== stateProp.value.code) {
        Device.api.setProperty("controllerState", {
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
"""

#
#
#
def setCompressorState_body():
    return """/**
  Sets compressor state property
  Byte encoding [ 0, 13 ] => Code 13
*/

const compressorStatePropName       = "compressorState";
const loadRunningMinutesPropName    = "loadRunningMinutes";
const idleRunningMinutesPropName    = "idleRunningMinutes";
const plannedStopsMinutesPropName   = "plannedStopsMinutes";
const unplannedStopsMinutesPropName = "unplannedStopsMinutes";
const plannedStopsPropName          = "plannedStops";
const unplannedStopsPropName        = "unplannedStops";

async function process(newState, stateTypes) {
    let prop = await Device.api.getProperty(compressorStatePropName);
    
    if (!prop.value) {
        await Device.api.setProperty(compressorStatePropName, {
                value: newState,
                time: new Date().toISOString()
            });
            
        done(null, newState);
    }
    else {
        // Clone the property otherwise it will be updated when we set it.
        let currProp = Object.assign({}, prop);
        
        if (newState.code !== currProp.value.code) {
            var modifiedProp = await Device.api.setProperty(compressorStatePropName, {
                    value: newState,
                    time: new Date().toISOString()
                });
                
            if (stateTypes.PLANNED_STOPPAGES.includes(newState.code)) {
                await Device.api.setProperty(plannedStopsPropName, {
                        value: newState,
                        time: new Date().toISOString()
                    });
            }
            else if (stateTypes.UNPLANNED_STOPPAGES.includes(newState.code)) {
                await Device.api.setProperty(unplannedStopsPropName, {
                        value: newState,
                        time: new Date().toISOString()
                    });
            }
                
            // Calculate load & idle running durations
            // 
            if (currProp.value && stateTypes.LOAD_RUNNING.includes(currProp.value.code ) &&  !stateTypes.LOAD_RUNNING.includes(modifiedProp.value.code)) {
                var lr = await Device.api.setProperty(loadRunningMinutesPropName, {
                        value: (Date.parse(modifiedProp.time) - Date.parse(currProp.time)) / (1000 * 60),
                        time: new Date().toISOString()
                    });
            }
            else if (currProp.value && stateTypes.IDLE_RUNNING.includes(currProp.value.code) &&  !stateTypes.IDLE_RUNNING.includes(modifiedProp.value.code)) {
                var ir = await Device.api.setProperty(idleRunningMinutesPropName, {
                        value: (Date.parse(modifiedProp.time) - Date.parse(currProp.time)) / (1000 * 60),
                        time: new Date().toISOString()
                    });
            }
            
            // Calculate unplanned & planned stoppage durations
            //
            if (currProp.value && stateTypes.UNPLANNED_STOPPAGES.includes(currProp.value.code) && !stateTypes.UNPLANNED_STOPPAGES.includes(modifiedProp.value.code)) {
                // Unplanned stoppage is over
                await Device.api.setProperty(unplannedStopsMinutesPropName, {
                        value: (Date.parse(modifiedProp.time) - Date.parse(currProp.time)) / (1000 * 60),
                        time: new Date().toISOString()
                    });
            }
            else if (currProp.value && stateTypes.PLANNED_STOPPAGES.includes(currProp.value.code) && !stateTypes.PLANNED_STOPPAGES.includes(modifiedProp.value.code)) {
                // Planned stoppage is over
                await Device.api.setProperty(plannedStopsMinutesPropName, {
                        value: (Date.parse(modifiedProp.time) - Date.parse(currProp.time)) / (1000 * 60),
                        time: new Date().toISOString()
                    });
            }
            
            done(null, newState);
        }
        else {
            done(null, "noop")
        }
    }
};

let table = Device.fetchCompressorStates();
let stateTypes = Device.fetchCompressorStateTypes();

let state = { code: -1, label: "NOT_SET" };
let code = Device.convertToDec({ values: value, default: -1})

if (code >= 0 && code < table.length) {
  state = table[code];
  process(state, stateTypes);
}
else {
  done("invalid argument");
}
"""

#
#
#
def setBlockingAlarm_body():
    return """/**
    Sets blocking alarm tag value into property
*/
let code = Device.convertToDec({ values: value, default: 0});
    
let blockingAlarm = "-";
if (code > 0) {
    blockingAlarm = 'A' + code.toString();
}

Device.api.setProperty("blockingAlarm", {
    value: blockingAlarm,
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#
#
#
def setScrewTemperature_body():
    return """/**

*/
Device.api.setProperty("screwTemperature", {
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
def setWorkingPressure_body():
    return """/**

*/
Device.api.setProperty("workingPressure", {
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
def setControllerSupplyVoltage_body():
    return """/**

*/
Device.api.setProperty("controllerSupplyVoltage", {
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
def setMaintCycles_body():
    return """/**

*/
const maintTypes = [
  "airFilterChange",
  "oilFilterChange",
  "separatorFilterChange",
  "oilChange",
  "compressorCheck",
  "bearingLubrication"
];

let schedule = {};
for (var x = 0; x < maintTypes.length; x++) {
    schedule[maintTypes[x]] = 0;
}

for (var i = 0; i < maintTypes.length*2; i+=2) {
    // convert to word
    let hours = (value.slice(i, i+1) << 8) | value.slice(i+1, i+2);
    schedule[maintTypes[i/2]] = Math.floor(hours);
}

// Update maintenance cycles (in hours)
Device.api.setProperty("cfgMaintCycles", {
  value: schedule,
  time: new Date().toISOString()
  }).
then(property => {
    done(null, property.value);
});
"""

#
#
#
def setTotalHours_body():
    return """/**

*/
let minutes  = value[0] << 24
    minutes |= value[1] << 16;
    minutes |= value[2] <<  8;
    minutes |= value[3];
    
let hours = Math.floor(minutes / 60);

// Update the output property with the actual hours value
Device.api.setProperty("totalHours", {
  value: hours,
  time: new Date().toISOString()
  }).
then(property => {
    done(null, property.value);
});
"""

#
#
#
def setTotalLoadHours_body():
    return """/**

*/
let minutes  = value[0] << 24
    minutes |= value[1] << 16;
    minutes |= value[2] <<  8;
    minutes |= value[3];
    
let hours = Math.floor(minutes / 60);

// Update the output property with the total load hours value
Device.api.setProperty("totalLoadHours", {
  value: hours,
  time: new Date().toISOString()
  }).
then(property => {
    done(null, property.value);
});
"""

#
#
#
def setMaintCounters_body():
    return """/**
  24 bytes = long (4 byte) * 6
*/

const maintCountersPropName = 'maintCounters';
const maintLogPropName      = 'maintenanceLog';
const maintCostsPropName    = 'maintenanceCostList';

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

#
#
#
def setLoadPercInLast100h_body():
    return """/**
    On load minutes in last 100 hours of motor running (100% is 6000)
*/
Device.api.setProperty("loadPercInLast100h", {
    value: (Device.convertToDec({ values: value, default: 0}) / 6000) * 100.0,
    time: new Date().toISOString()
 })
 .then(property => {
    done(null, property.value);
 });
"""

#
#
#
def setNbrOfStartsInLastHour_body():
    return """/**

*/
Device.api.setProperty("nbrOfStartsInLastHour", {
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
def setControllerTime_body():
    return """/**

*/
function pad(n, width, z) {
  z = z || '0';
  n = n + '';
  return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}

let seconds     = value[0];
let minutes     = value[1];
let hours       = value[2];
let dayOfWeek   = value[3];
let dayOfMonth  = value[4];
let month       = value[5];
let year        = value[6];

let time = '20' + pad(year,2) + '-' + 
            pad(month,2) + '-' + 
            pad(dayOfMonth,2) + ' ' + 
            pad(hours,2) + ':' + 
            pad(minutes,2) + ':' + 
            pad(seconds,2);

Device.api.setProperty("controllerTime", {
  value: time,
  time: new Date().toISOString()
  }).
then(property => {
    done(null, property.value);
});
"""
