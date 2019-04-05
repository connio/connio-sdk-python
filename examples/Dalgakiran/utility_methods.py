# ~~ Utility/Helper methods ~~
#
# startStop(start or stop)
# sendCommand()
# init(inverterModel)
# getEmptyState()
# convertToHours()
# convertToDecimal()    
# makeWriteRequest()
# makeWriteValue()
# writeTagByAddress()
# readTagByAddress()
# getCompressorInfo()
# getDashboard()
# getLatestValues()

# getHistOEE
# getHistMttr
# getHistMtbf
# getHistEstimPowerConsumption()
# getHistEstimEnergyConsumption()

#
#
#
def startStop_body(startOrStop):
  if startOrStop == 0:
    return """
try {    
    let command = Device.makeCompressorCommand("STOP");
    
    let request = { cmd: command, done: r => done(null, r) };
    Device.writeTag(request);
}
catch(e) {
    done(e);
}
    """
  else:
    return """
try {    
    let command = Device.makeCompressorCommand("START");
    
    let request = { cmd: command, done: r => done(null, r) };
    Device.writeTag(request);
}
catch(e) {
    done(e);
}
    """

#
#
#
def sendCommand_body():
    return """/*
    Send compressor command to the gateway
*/

try {    
    let command = Device.makeCompressorCommand(value);
     
    let request = { cmd: command, done: r => done(null, r) };
    Device.writeTag(request);
}
catch(e) {
    done(e);
}
"""

#
#
#
def getInit_body():
    return """/**
  Initialize device `state` property with default values

  @value:
  { 
    "hasInverter": true, 
    "warrantyInMonth": 12,
    "icon": "inversys-15-plus-depolu.png",
    "elecCost": {
        "value": 0,     //cost of electricity KWh
        "unit": "USD"
    }
   }
*/

const defaultWarrantyInMonth = 12;

const defaultElecCost = { value: 0, unit: 'USD' };

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

let warrantyInMonth, hasInverter, elecCost;

({hasInverter, warrantyInMonth, elecCost} = value);

let settings = Device.fetchModbusSettings(hasInverter);

let state = Device.getEmptyState(elecCost || defaultElecCost);
state.hasInverter = hasInverter || false;

let now = new Date();
let warrantyExpiry = new Date(now.setMonth(now.getMonth() + (warrantyInMonth || defaultWarrantyInMonth)));

Device.api.setProperty("modbus_settings", {
  value: settings,
  time: new Date().toISOString()
}).
then(() => Device.api.setProperty('icon', {
    value: value.icon || "dk-default.png",
    time: new Date().toISOString()
})).
then(() => Device.api.setProperty('warrantyExpiryDate', {
    value: warrantyExpiry.toISOString(),
    time: new Date().toISOString()
})).
then(() => Device.api.setProperty('maintenanceCostList', {
        value: defaultMaintCosts,
        time: new Date().toISOString()
})).
then(() => Device.getCompressorInfo()).
then(st => {
    // Merge device info into state
    Object.assign(state, st);
    
    Device.api.setProperty('state', {
        value: state,
        time: new Date().toISOString()
    }).
    then(property => done(null, property.value));
});
"""

#
#
#
def getEmptyState_body():
    return """/**
    Creates an empty state for this device
    @value {{ value, unit }} cost of electricity KWh
*/
return {        
    costOfkWh: {
        value: value.value,
        unit: value.unit,
    },
    warnings: { last: [], asOf: "2019-01-01T00:00:00Z", total: [ 0, 0, 0, 0 ] },
    alarms: { last: [], asOf: "2019-01-01T00:00:00Z", total: [ 0, 0, 0, 0 ] },
    pressure: { value: 0, unit: "bar", average: [ 0, 0, 0, 0 ] },    
    temperature: { value: 0, unit: "°C", average: [ 0, 0, 0, 0 ] },
    maintenance: { upcoming: [
                { maintenance: "Bearing Lubrication", cost: 0, hours: 0, days: 0 },
                { maintenance: "Air Filter Change", cost: 0, hours: 0, days: 0 },
                { maintenance: "Oil Filter Change", cost: 0, hours: 0, days: 0 },
                { maintenance: "Oil Change", cost: 0, hours: 0, days: 0 },
                { maintenance: "Seperator Filter Change", cost: 0, hours: 0, days: 0 },
                { maintenance: "Compressor Check", cost: 0, hours: 0, days: 0 }
            ]
    },
    stoppages: { planned: [ 0, 0, 0, 0 ], unplanned: [ 0, 0, 0, 0 ], powercut: [ 0, 0, 0, 0 ] },
    loadRatio: { average: [ 0, 0, 0, 0 ], current: 0, unit: "%" },
    energy: { value: [ 0, 0, 0, 0 ], unit: "kWh" },        
    unplannedStoppageHours: [ 0, 0, 0, 0 ],
    loadRunningHours: [ 0, 0, 0, 0 ],        
    power: { value: [ 0, 0, 0, 0 ], unit: "kW" },                
    costOfRunning: { value: [ 0, 0, 0, 0 ], unit: "USD"},
    idleRunningHours: [ 0, 0, 0, 0 ],
    plannedStoppageHours: [ 0, 0, 0, 0 ],
    unplannedStoppageHours: [ 0, 0, 0, 0 ],
    loadRunningHours: [ 0, 0, 0, 0 ],
    totalHours: { last: 0, asOf: "2019-01-01T00:00:00.000Z", average: [ 0, 0, 0, 0 ] },
    totalLoadHours: { last: 0, asOf: "2019-01-01T00:00:00.000Z", average: [ 0, 0, 0, 0 ] },    
    oee: { availability: [ 0, 0, 0, 0 ], performance: [ 0, 0, 0, 0 ], quality: [ 0, 0, 0, 0 ], average: [ 0, 0, 0, 0 ], unit: '%' },
    mtbf: { average: [ 0, 0, 0, 0 ], unit: 'h' },
    mttr: { average: [ 0, 0, 0, 0 ], unit: 'h' },
    hasInverter: false, 
    motorSpeed: { current: 0, average: [ 0, 0, 0, 0 ], unit: 'RPM' },
    motorFrequency: { current: 0, average: [ 0, 0, 0, 0 ], unit: 'Hz' },
    motorCurrent: { current: 0, average: [ 0, 0, 0, 0 ], unit: 'A' },
    status: {
        code: 0,
    },
};
"""

#
#
#
def convertToHours_body(): 
    return """/**
    Converts given Logika hour representation to hours
    @value [word1, word2] 
*/
function convert(word1, word2) {
    var byte1 = (word2 & 255) << 24;
    var byte2 = (word2 >>> 8) << 16;
    var byte3 = (word1 & 255) << 8;
    var byte4 = (word1 >>> 8);
    
    // calculate and divide by 60 to convert minutes into hours        
    return (byte1 | byte2 | byte3 | byte4) / 60.0;
};
done(null, convert(value[0], value[1]));
"""

#
#
#
def convertToDec_body():
    return """/** 
    Converts given big-endien byte array to decimal values
    @value: {{ values: [b1, b2, b3, ..], default: x }}
*/

let values = value.values;
let defaultValue = value.default;

if (!Array.isArray(values) || values.length == 0) return defaultValue;

let result = 0;
let offset = 0;
for (var i = values.length - 1; i >= 0; i--) {
    result |= values[i] << (offset * 8);
    offset += 1;
}
return result;
"""

#
#
#
def makeWriteRequest_body():
    return """/**
    @param value.tagKey   (e.g. "WP")
    @param value.x        (e.g. 1 for WP1)
    @param value.setValue (e.g. 26.8)
    @param value.byteCount(default 2)
*/

// TODO: Test which statement works
if (!value.x || !value.setValue) throw `Given parameters are not correct. x: ${value.x}, setValue: ${value.setValue}`;
//if (value.x == null || value.setValue == null) throw `Given parameters are not correct. x: ${value.x}, setValue: ${value.setValue}`;

let params = Device.fetchWriteRequest(value.tagKey);
let byteCount = value.byteCount || 2;

let tag_address;
if (value.x > params.max || value.x < params.min) { 
    throw "Invalid tag index "+ value.tagKey + "("+ value.x.toString() +") should be between " + params.min.toString() + "-" + params.max.toString();
}
else {
    tag_address = parseInt(params.offset, 16) + (value.x - params.min);
}

// If multiplier is not specified default multiplier is 1;
// if multiplier is specified but no value specified for given index value (value.x), then default is 1
let multip = params.multiplier ? params.multiplier[value.x - params.min] || 1 : 1;

let tagValue = Device.makeWriteValue({ value: (value.setValue * multip), byteCount: byteCount });

return { writeRequest: "w," + tagValue.join(':') + "," + byteCount.toString() + ",0,1,0x" + tag_address.toString(16),
        readRequest: params.rcmd
        };"""

#
#
#
def makeWriteValue_body():
    return """/**
    @value {{ value, byteCount }}
*/
function convert(v, byteCount) {
    let hex = v.toString(16);
    if (hex.length % 2) hex = '0' + hex;
    
    // group chars by 2
    let hexArr = hex.match(/(.{2})/g);
    for (let x = hexArr.length; x < byteCount; x++) {
        hexArr.unshift('00');
    }
    
    return hexArr.map(x => x.split('').reduce((result, ch) => result * 16 + '0123456789abcdefgh'.indexOf(ch), 0));
}
return convert(value.value, value.byteCount);"""

#
#
#
def writeAnyTag_body():
    return """/**
@value {{ setValue, addr, size }}

e.g
{ 
  setValue: 13, 
  addr: "0x504", 
  size: 2 
}
*/

let tagValue = Device.makeWriteValue({ value: value.setValue, byteCount: value.size });
let req = { cmd: `w,${tagValue.join(':')},${value.size},0,1,${value.addr}`, done: r => done(null, r) };

Device.writeTag(req);
"""

#
#
#
def readAnyTag_body():
    return """/**
@value {{ addr, size }}

e.g
{ 
  addr: "0x504", 
  size: 2 
}

Writes result into the `tag` property.
*/

let req = { cmd: `r,meth:setAny,-,${value.size},-,1,${value.addr}`, done: r => done(null, r + " You can read the value in `tagValue` property") };
Device.readTag(req);
"""


#
#
#
def getCompressorInfo_body():
    return """/**
  Build a view of compressor details.
*/
const serNumPropName        = "cfgSerialNumber";
const modelPropName         = "cfgLogikaModel";
const fwVerPropName         = "cfgLogikaFwVersion";
const compStatePropName     = "compressorState";
const connStatusPropName    = "connectionStatus";
const activityPropName      = "active";
const warrantyEndDatePropName   = "warrantyExpiryDate";
const WarrantyPeriod        = 60;

function calcDateDiff(date1, date2) {
    var diff = Math.floor(date1.getTime() - date2.getTime());
    var day = 1000 * 60 * 60 * 24;

    var days = Math.floor(diff/day);
    var months = Math.floor(days/31);
    var years = Math.floor(months/12);

    return months;
}

async function f(warrantyPeriod) {    
    if (Device.customIds && !Device.customIds.sn) {
        Device.customIds.sn = await Device.api.getProperty(serNumPropName).then(p=>p.value || "-");
    }
    
    let logika_model = await Device.api.getProperty(modelPropName).then(p=>p.value  || "-");
    let logika_release = await Device.api.getProperty(fwVerPropName).then(p=>p.value  || "-");
    
    let status = await Device.api.getProperty(compStatePropName).then(p=>p.value  || "-");
    let connection = await Device.api.getProperty(connStatusPropName).then(p=>p.value  || "-");
    let active = await Device.api.getProperty(activityPropName).then(p=>p.value  || "-");
    
    let connectivity = "offline";
    if (connection === "online" && active == "active") {
        connectivity = "online-active";
    }
    else if (connection === "online") {
        connectivity = "online-inactive";
    }
    
    let now = new Date();
    let defaultWarrantyExpiry = new Date(now.setMonth(now.getMonth() + warrantyPeriod));

    let warrantyExpiry = await Device.api.getProperty(warrantyEndDatePropName).then(p => p.value ? Date.parse(p.value) : defaultWarrantyExpiry.toISOString());
    let timeToWarranty = calcDateDiff(new Date(warrantyExpiry), new Date());
    
    // In case that we use a counter to decrement the warranty time
    if (timeToWarranty < 0) {
        timeToWarranty = 0;
    }
    
    let device = {
        id: Device.id,
        name: Device.name,
        friendlyName: Device.friendlyName,
        customIds: Device.customIds || { sn: await Device.api.getProperty(serNumPropName).then(p=>p.value || "-") },
        logikaModel: logika_model,
        logikaRelease: logika_release,
        connectivity: connectivity,
        status: status,
        warrantyEnd: timeToWarranty + " months",
        warranty: { endsInMonths: timeToWarranty, periodInMonths: warrantyPeriod },
    };
    return device;
}
return Promise.resolve(f(value || WarrantyPeriod));
"""

#
#
#
def getDashboard_body():
    return """/**
*  Build the default dashboard view of the compressor.
*  Some information must be populated by calling `preaggregate()` method ahead of time.
*/

/** @desc Logika-Base */
const PRESSURE_PROPERTY = 'workingPressure';
/** @desc Logika-Base */
const TEMPERATURE_PROPERTY = 'screwTemperature';
/** @desc Logika-Base */
const COMPRESSOR_STATE_PROPERTY = 'compressorState';
/** @desc Logika-Base */
const DRIVE_PROPERTY = 'driveMeasures';


/** @desc Logika-Base */
const STATE_PROPERTY = 'state';

const OFFLINE = 'offline';

async function main(context) {
    Object.assign(context, {
        costOfkWh: value,
    });
    
    // Acquire temperature and pressure values in parallel
    let [pressureProp, temperatureProp, compressorStateProp, driveProp, periods] = await Promise.all([
       Device.api.getProperty(PRESSURE_PROPERTY),
       Device.api.getProperty(TEMPERATURE_PROPERTY),
       Device.api.getProperty(COMPRESSOR_STATE_PROPERTY),
       context.hasInverter ? Device.api.getProperty(DRIVE_PROPERTY) : Promise.resolve(undefined),
       Device.processCompressorStates(),
    ]);
    
    context.periods = periods;

    context.pressure.value = pressureProp.value || 0;
    context.pressure.unit = pressureProp.meta.measurement && pressureProp.meta.measurement.unit && pressureProp.meta.measurement.unit.symbol;

    if (pressureProp.meta.boundaries) {
        context.pressure.range = {
            min: pressureProp.meta.boundaries.min,
            max: pressureProp.meta.boundaries.max,
        };
    }
    
    context.temperature.value = temperatureProp.value || 0;
    context.temperature.unit = temperatureProp.meta.measurement && temperatureProp.meta.measurement.unit && temperatureProp.meta.measurement.unit.symbol;

    if (temperatureProp.meta.boundaries) {
        context.temperature.range = {
            min: temperatureProp.meta.boundaries.min,
            max: temperatureProp.meta.boundaries.max,
        };
    }
    else {
        context.temperature.range = {
            min: 0,
            max: 100,
        };
    }

    // Inverter motor information
    if (driveProp && driveProp.value) {
        context.motorSpeed.current = driveProp.value.rpm || 0;
        context.motorFrequency.current = driveProp.value.frequency || 0;
        context.motorCurrent.current = driveProp.value.current || 0;
    }

    // Call the methods below in parallel.
    // These methods do not have any dependence on other method output.
    let results = await Promise.all([
        Device.getCompressorInfo(),
        Device.queryWarningAlarmSummary(context),
    ]);
    
    // Clean all periods
    context.periods = undefined;
    
    // Merge results into context
    results.forEach(result => Object.assign(context, result));
    
    return {
        ...context,
        
        /** @desc Reset current values for offline compressor */
        pressure: {
            ...context.pressure,
            value: context.connectivity === OFFLINE ? 0 : context.pressure.value,
        },
        temperature: {
            ...context.temperature,
            value: context.connectivity === OFFLINE ? 0 : context.temperature.value,
        },
    };
};

Device.api.getProperty(STATE_PROPERTY)
 .then(property => property.value || Device.getEmptyView())
 .then(context => main(context))
 .then(context => done(null, context));
"""

#
#
#
def getDashboard_OLD_body():
    return """/**
*  Build the default dashboard view of the compressor.
*  Some information must be populated by calling `preaggregate()` method ahead of time.
*/
/** @desc Logika-Base */
const PRESSURE_PROPERTY = 'workingPressure';
/** @desc Logika-Base */
const TEMPERATURE_PROPERTY = 'screwTemperature';
/** @desc Logika-Base */
const STATE_PROPERTY = 'state';

const OFFLINE = 'offline';

async function main(context) {
    Object.assign(context, {
        costOfkWh: value,
    });

    // Acquire temperature and pressure values in parallel
    let [pressureProp, temperatureProp] = await Promise.all([
       Device.api.getProperty(PRESSURE_PROPERTY),
       Device.api.getProperty(TEMPERATURE_PROPERTY)
    ]);

    context.pressure.value = pressureProp.value || 0;
    context.pressure.unit = pressureProp.meta.measurement && pressureProp.meta.measurement.unit && pressureProp.meta.measurement.unit.symbol;

    if (pressureProp.meta.boundaries) {
        context.pressure.range = {
            min: pressureProp.meta.boundaries.min,
            max: pressureProp.meta.boundaries.max,
        };
    }
    else {
        // in case that no boundary has been provided
        context.temperature.range = {
            min: 0,
            max: 100,
        };
    }
    
    context.temperature.value = temperatureProp.value || 0;
    context.temperature.unit = temperatureProp.meta.measurement && temperatureProp.meta.measurement.unit && temperatureProp.meta.measurement.unit.symbol;

    if (temperatureProp.meta.boundaries) {
        context.temperature.range = {
            min: temperatureProp.meta.boundaries.min,
            max: temperatureProp.meta.boundaries.max,
        };
    }
    else {
        // in case that no boundary has been provided
        context.temperature.range = {
            min: 0,
            max: 100,
        };
    }

    // Call the methods below in parallel.
    // These methods do not have any dependence on other method output.
    let results = await Promise.all([
        Device.getCompressorInfo(),
        Device.queryWarningAlarmSummary(context),
        Device.queryTimeToMaintenance(context),
        Device.hasInverter(context),
    ]);
    
    // Merge results into context
    results.forEach(result => Object.assign(context, result));
    
    return {
        ...context,
        
        /** @desc Reset current values for offline compressor */
        pressure: {
            ...context.pressure,
            value: context.connectivity === OFFLINE ? 0 : context.pressure.value,
        },
        temperature: {
            ...context.temperature,
            value: context.connectivity === OFFLINE ? 0 : context.temperature.value,
        },
    };
};

Device.api.getProperty(STATE_PROPERTY)
 .then(property => property.value || Device.getEmptyView())
 .then(main)
 .then(context => Device.api.setProperty(STATE_PROPERTY, { value: context, time: new Date().toISOString() }))
 .then(property => done(null, property.value));
"""

def getLatestValues_body():
    return """/**
*  Returns the most recent values of compressor pressure and temperature.
*/
const PRESSURE_PROPERTY     = 'workingPressure';
const TEMPERATURE_PROPERTY  = 'screwTemperature';
const DRIVE_PROPERTY        = 'driveMeasures';


async function getValues() {
    let state = await Device.api.getProperty("state").then(prop => prop.value);
    
    let calls = [
        Device.api.getProperty(PRESSURE_PROPERTY), 
        Device.api.getProperty(TEMPERATURE_PROPERTY)
    ];
    
    // Get inverter info if compressor comes with inverter
    if (state.hasInverter) {
        req.push(Device.api.getProperty(DRIVE_PROPERTY));
    }
    
    let [pressureProp, temperatureProp, driveProp] = await Promise.all(calls);
    
    const result = {
        pressure: pressureProp.value || 0,
        temperature: temperatureProp.value || 0,
    };

    // Inverter motor information - if any
    if (driveProp && driveProp.value) {
        result.motorSpeed = { current: driveProp.value.rpm || 0 };
        result.motorFrequency = { current: driveProp.value.frequency || 0 };
        result.motorCurrent = { current: driveProp.value.current || 0 };
    }

    return done(null, result);
};

getValues();
"""

def getHistOEE_body():
    return """/**
*  Gets historical OEE
*/

let query = value;

const reducer = (yearly, daily) => {
    if (yearly.length == 0) {
        yearly.push(daily);
    }
    else if (new Date(yearly[yearly.length-1].date).getUTCMonth() == new Date(daily.date).getUTCMonth()) {
        yearly[yearly.length-1].idleRunningDur += daily.idleRunningDur;
        yearly[yearly.length-1].loadRunningDur += daily.loadRunningDur;
        yearly[yearly.length-1].unplannedDur += daily.unplannedDur;
    }
    else {
        yearly.push({ 
            idleRunningDur: daily.idleRunningDur,
            loadRunningDur: daily.loadRunningDur,
            unplannedDur: daily.unplannedDur,
            date: daily.date
        });
    }
    return yearly;
}

let now = new Date();
let startMonth = now.setUTCMonth(now.getUTCMonth() - 12);

Device.processCompressorStates().then(periods => {
    if (query.from.unit == 'DAYS' || query.from.unit == 'WEEKS' || query.from.unit == 'MONTHS') {
        let results = periods.map( p => {
            return {
                v: ((p.Availability * p.Quality * p.Perf) * 100),
                t: p.date + "T23:59:59.999Z"
            }
        });
        done(null, results.reverse().slice(0, 30));
    }
    else {
        // Yearly
        let results = periods
                        .filter(p => Date.parse(p.date) > startMonth)
                        .reduce(reducer, [])
                        .map( p => {
                            let Lt = p.idleRunningDur + p.loadRunningDur + p.unplannedDur;
                            let Wt = p.idleRunningDur + p.loadRunningDur;
    
                            let availability = Wt / Lt;
                            
                            return {
                                v: ((availability * 1.0 * 1.0) * 100),
                                t: p.date + "T23:59:59.999Z"
                            }
                        });
        done(null, results.reverse().slice(0, 12));
    }
});
"""

def getHistMtbf_body():
    return """/**
 * Gets historical Mean time between failures
 */ 
let query = value;

const reducer = (yearly, daily) => {
    if (yearly.length == 0) {
        yearly.push(daily);
    }
    else if (new Date(yearly[yearly.length-1].date).getUTCMonth() == new Date(daily.date).getUTCMonth()) {
        yearly[yearly.length-1].idleRunningDur += daily.idleRunningDur;
        yearly[yearly.length-1].loadRunningDur += daily.loadRunningDur;
        yearly[yearly.length-1].unplannedDur += daily.unplannedDur;
        yearly[yearly.length-1].unplannedStops += daily.unplannedStops;
    }
    else {
        yearly.push({ 
            idleRunningDur: daily.idleRunningDur,
            loadRunningDur: daily.loadRunningDur,
            unplannedDur: daily.unplannedDur,
            unplannedStops: daily.unplannedStops,
            date: daily.date
        });
    }
    return yearly;
}

let now = new Date();
let startMonth = now.setUTCMonth(now.getUTCMonth() - 12);

Device.processCompressorStates().then(periods => {
    if (query.from.unit == 'DAYS' || query.from.unit == 'WEEKS' || query.from.unit == 'MONTHS') {
        let results = periods.map( p => {
            let Lt = p.idleRunningDur + p.loadRunningDur + p.unplannedDur;
            let mtbf = (p.unplannedStops == 0 ? NaN : (Lt / p.unplannedStops));
            
            return {
                v: mtbf,
                t: p.date + "T23:59:59.999Z"
            }
        });
        done(null, results.reverse().slice(0, 30));
    }
    else {
        // Yearly
        let results = periods
                        .filter(p => Date.parse(p.date) > startMonth)
                        .reduce(reducer, [])
                        .map( p => {
                            let Lt = p.idleRunningDur + p.loadRunningDur + p.unplannedDur;
                            let mtbf = (p.unplannedStops == 0 ? NaN : (Lt / p.unplannedStops));
                            
                            return {
                                v: mtbf,
                                t: p.date + "T23:59:59.999Z"
                            }
                        });
        done(null, results.reverse().slice(0, 12));
    }
});
"""

def getHistMttr_body():
    return """/**
* Gets historical MTtr values
*/ 
let query = value;

const reducer = (yearly, daily) => {
    if (yearly.length == 0) {
        yearly.push(daily);
    }
    else if (new Date(yearly[yearly.length-1].date).getUTCMonth() == new Date(daily.date).getUTCMonth()) {
        yearly[yearly.length-1].idleRunningDur += daily.idleRunningDur;
        yearly[yearly.length-1].loadRunningDur += daily.loadRunningDur;
        yearly[yearly.length-1].unplannedDur += daily.unplannedDur;
        yearly[yearly.length-1].unplannedStops += daily.unplannedStops;
    }
    else {
        yearly.push({ 
            idleRunningDur: daily.idleRunningDur,
            loadRunningDur: daily.loadRunningDur,
            unplannedDur: daily.unplannedDur,
            unplannedStops: daily.unplannedStops,
            date: daily.date
        });
    }
    return yearly;
}

let now = new Date();
let startMonth = now.setUTCMonth(now.getUTCMonth() - 12);

Device.processCompressorStates().then(periods => {
    if (query.from.unit == 'DAYS' || query.from.unit == 'WEEKS' || query.from.unit == 'MONTHS') {
        let results = periods.map( p => {
            let mttr = (p.unplannedStops == 0 ? NaN : (p.unplannedDur / p.unplannedStops));
            
            return {
                v: mttr,
                t: p.date + "T23:59:59.999Z"
            }
        });
        done(null, results.reverse().slice(0, 30));
    }
    else {
        // Yearly
        let results = periods
                        .filter(p => Date.parse(p.date) > startMonth)
                        .reduce(reducer, [])
                        .map( p => {
                            let mttr = (p.unplannedStops == 0 ? NaN : (p.unplannedDur / p.unplannedStops));
                            
                            return {
                                v: mttr,
                                t: p.date + "T23:59:59.999Z"
                            }
                        });
        done(null, results.reverse().slice(0, 12));
    }
});
"""

def getHistEstimPowerConsumption_body():
    return """/**
*  Returns the historical power consumption values based on the given query.
*/
let query = value;

const ENERGY_CONSUMPTION_CONSTANT = 10.0 * 1.2;
const ENERGY_IDLE_CONSUMPTION_RATIO = 0.27;

const IDLE_PWR_MULTIPLIER = ENERGY_CONSUMPTION_CONSTANT * ENERGY_IDLE_CONSUMPTION_RATIO;
const LOAD_PWR_MULTIPLIER = ENERGY_CONSUMPTION_CONSTANT;

const reducer = (yearly, daily) => {
    if (yearly.length == 0) {
        yearly.push(daily);
    }
    else if (new Date(yearly[yearly.length-1].date).getUTCMonth() == new Date(daily.date).getUTCMonth()) {
        yearly[yearly.length-1].idleRunningDur += daily.idleRunningDur;
        yearly[yearly.length-1].loadRunningDur += daily.loadRunningDur;
        yearly[yearly.length-1].unplannedDur += daily.unplannedDur;
    }
    else {
        yearly.push({ 
            idleRunningDur: daily.idleRunningDur,
            loadRunningDur: daily.loadRunningDur,
            unplannedDur: daily.unplannedDur,
            date: daily.date
        });
    }
    return yearly;
}

let now = new Date();
let startMonth = now.setUTCMonth(now.getUTCMonth() - 12);

Device.processCompressorStates().then(periods => {
    if (query.from.unit == 'DAYS' || query.from.unit == 'WEEKS' || query.from.unit == 'MONTHS') {
        let results = periods.map( p => {
            return {
                v: (( (p.loadRunningDur * LOAD_PWR_MULTIPLIER) + (p.idleRunningDur * IDLE_PWR_MULTIPLIER) ) / 
                    (p.loadRunningDur + p.idleRunningDur) ) || 0,
                t: p.date + "T23:59:59.999Z"
            }
        });
        done(null, results.reverse().slice(0, 30));
    }
    else {
        // Yearly
        let results = periods
                        .filter(p => Date.parse(p.date) > startMonth)
                        .reduce(reducer, [])
                        .map( p => {
                            return {
                                v: (( (p.loadRunningDur * LOAD_PWR_MULTIPLIER) + (p.idleRunningDur * IDLE_PWR_MULTIPLIER) ) / 
                                    (p.loadRunningDur + p.idleRunningDur) ) || 0,
                                t: p.date + "T23:59:59.999Z"
                            }
                        });
        done(null, results.reverse().slice(0, 12));
    }
});
"""

def getHistEstimEnergyConsumption_body():
    return """/**
*  Returns the historical energy consumption values based on the given query.
*/
let query = value;

const ENERGY_CONSUMPTION_CONSTANT = 10.0 * 1.2;
const ENERGY_IDLE_CONSUMPTION_RATIO = 0.27;

const IDLE_PWR_MULTIPLIER = ENERGY_CONSUMPTION_CONSTANT * ENERGY_IDLE_CONSUMPTION_RATIO;
const LOAD_PWR_MULTIPLIER = ENERGY_CONSUMPTION_CONSTANT;

const reducer = (yearly, daily) => {
    if (yearly.length == 0) {
        yearly.push(daily);
    }
    else if (new Date(yearly[yearly.length-1].date).getUTCMonth() == new Date(daily.date).getUTCMonth()) {
        yearly[yearly.length-1].idleRunningDur += daily.idleRunningDur;
        yearly[yearly.length-1].loadRunningDur += daily.loadRunningDur;
        yearly[yearly.length-1].unplannedDur += daily.unplannedDur;
    }
    else {
        yearly.push({ 
            idleRunningDur: daily.idleRunningDur,
            loadRunningDur: daily.loadRunningDur,
            unplannedDur: daily.unplannedDur,
            date: daily.date
        });
    }
    return yearly;
}

let now = new Date();
let startMonth = now.setUTCMonth(now.getUTCMonth() - 12);

Device.processCompressorStates().then(periods => {
    if (query.from.unit == 'DAYS' || query.from.unit == 'WEEKS' || query.from.unit == 'MONTHS') {
        let results = periods.map( p => {
            return {
                v: ((p.loadRunningDur * LOAD_PWR_MULTIPLIER) + (p.idleRunningDur * IDLE_PWR_MULTIPLIER)) || 0,
                t: p.date + "T23:59:59.999Z"
            }
        });
        done(null, results.reverse().slice(0, 30));
    }
    else {
        // Yearly
        let results = periods
                        .filter(p => Date.parse(p.date) > startMonth)
                        .reduce(reducer, [])
                        .map( p => {
                            return {
                                v: ((p.loadRunningDur * LOAD_PWR_MULTIPLIER) + (p.idleRunningDur * IDLE_PWR_MULTIPLIER)) || 0,
                                t: p.date + "T23:59:59.999Z"
                            }
                        });
        done(null, results.reverse().slice(0, 12));
    }
});
"""