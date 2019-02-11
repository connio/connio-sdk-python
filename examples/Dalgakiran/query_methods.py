# Query methods
#
# buildAggregateQueries
# queryAggregates
# queryPropertySummary
# queryWarningAlarmSummary
# queryTimeToMaintenance
# queryUsageHours
# queryEstimEnergyConsumption
# queryEstimPowerConsumption
# queryLoadRatio
# queryStoppages
# queryEstimCostOfRunning
# queryOEE
# queryMtbf
# queryMttr

#
#
#
def buildAggregateQueries_body():
    return """/**
    Builds time-series queries to collect 4 different stats for given property
*/
let q = [
        { startRelative: { value: 24, unit: 'hours' }, aggregators: [ {name: value, sampling: { value: 24, unit: 'hours'} } ] },
        { startRelative: { value: 7, unit: 'days' }, aggregators: [ {name: value, sampling: { value: 7, unit: 'days'} } ] },
        { startRelative: { value: 30, unit: 'days' }, aggregators: [ {name: value, sampling: { value: 30, unit: 'days'} } ] },
        { startRelative: { value: 12, unit: 'months' }, aggregators: [ {name: value, sampling: { value: 12, unit: 'months'} } ] }
    ];
return q;
"""


#
#
#
def queryAggregates_body():
    return """/**
    Queries 4 different stats for given property
*/
function cleanse(r) {
    if (r.results && r.results.length > 0 && r.results[0].values && r.results[0].values.length > 0) {
        return r.results[0].values[0].v;
    }
    return undefined;
}

let resultSet = [];
let q = Device.buildAggregateQueries(value.agg);

return Device.api.readData(value.pname, q[0])
    .then(r0 => { 
        resultSet.push(cleanse(r0));
        return Device.api.readData(value.pname, q[1]); 
     })
    .then(r1 => { 
        resultSet.push(cleanse(r1));
        return Device.api.readData(value.pname, q[2]);
     })
    .then(r2 => {
        resultSet.push(cleanse(r2));
        return Device.api.readData(value.pname, q[3]);
     })
     .then(r3 => { 
        resultSet.push(cleanse(r3));
        return resultSet;
    });
"""

#
#
#
def queryPropertySummary_body():
    return """/**
*/
async function f() {
    let prop = await Device.api.getProperty(value.pname);
    let stats = await Device.queryAggregates({ pname: value.pname, agg: value.agg });
    
    let result = { value: prop.value, unit: value.unit };
    //default field name is `average`
    result[value.fname || 'average'] = stats.map(i => i || undefined);
    
    return result;
}

return Promise.resolve(f());
"""

def queryWarningAlarmSummary_body():
    return """/**

*/
async function f() {
    let context = value;
    
    let nbrOfAlarms = await Device.queryPropertySummary({ pname: "nbrOfAlarms", agg: "sum", unit: "#", fname: 'total' });
    let nbrOfWarnings = await Device.queryPropertySummary({ pname: "nbrOfWarnings", agg: "sum", unit: "#", fname: 'total' });
    
    let lastAlarmsProp = await Device.api.getProperty("lastAlarms");
    let lastWarningsProp = await Device.api.getProperty("lastWarnings");
    
    let lastAlarmItems = [];
    if (lastAlarmsProp.value)
        lastAlarmItems = lastAlarmsProp.value.items || [];
        
    let lastWarningItems = [];
    if (lastWarningsProp.value)
        lastWarningItems = lastWarningsProp.value.items || [];
    
    context['alarms'] = { last: lastAlarmItems, asOf: lastAlarmsProp.time, total: nbrOfAlarms.total.map(i => i || 0) };
    context['warnings'] = { last: lastWarningItems, asOf: lastWarningsProp.time, total: nbrOfWarnings.total.map(i => i || 0) };
    
    return context;
}

return Promise.resolve(f());
"""

#
#
#
def queryTimeToMaintenance_body():
    return """/**
@param value is the context
*/
const maintCostsPropName    = "maintenanceCostList";
const maintCountersPropName = "maintCounters";
const maintCyclesPropName   = "cfgMaintCycles";

async function f() {
    let context = value;
    
    let defaultMaintCosts = { 
        currencySymbol: "$",
        airFilterChange: 0.0,
        oilChange: 0.0,  
        compressorCheck: 0.0, 
        oilFilterChange: 0.0, 
        separatorFilterChange : 0.0, 
        bearingLubrication: 0.0     
    };
    
    let defaultCycles = { 
        airFilterChange: 0,
        oilChange: 0,  
        compressorCheck: 0, 
        oilFilterChange: 0, 
        separatorFilterChange : 0, 
        bearingLubrication: 0     
    };
    
    let mcost = await Device.api.getProperty(maintCostsPropName).then(p=>p.value) || defaultMaintCosts;
    let mCycles = await Device.api.getProperty(maintCyclesPropName).then(p=>p.value) || defaultCycles;
    // Hours left until the next maintenances by category
    let mCounters = await Device.api.getProperty(maintCountersPropName).then(p=>p.value) || defaultCycles;
    
    let hoursToBearingLub        = ((mCycles.bearingLubrication * 60)   - mCounters.bearingLubrication) / 60.0;
    let hoursToAirFilterChange   = ((mCycles.airFilterChange * 60)      - mCounters.airFilterChange) / 60.0;
    let hoursToOilFilterChange   = ((mCycles.oilFilterChange * 60)      - mCounters.oilFilterChange) / 60.0;
    let hoursToOilChange         = ((mCycles.oilChange * 60)            - mCounters.oilChange) / 60.0;
    let hoursToSepFilterChange   = ((mCycles.separatorFilterChange * 60) - mCounters.separatorFilterChange) / 60.0;
    let hoursToCompressorCheck   = ((mCycles.compressorCheck * 60)      - mCounters.compressorCheck) / 60.0;
    
    let plannedMaintenanceList = [ 
        { maintenance: "Bearing Lubrication", cost: mcost.bearingLubricator, hours: hoursToBearingLub, days: Math.ceil(hoursToBearingLub / 24.0) },
        { maintenance: "Air Filter Change", cost: mcost.airFilterChange, hours: hoursToAirFilterChange, days: Math.ceil(hoursToAirFilterChange / 24.0) },
        { maintenance: "Oil Filter Change", cost: mcost.oilFilterChange, hours: hoursToOilFilterChange, days: Math.ceil(hoursToOilFilterChange / 24.0) },
        { maintenance: "Oil Change", cost: mcost.oilChange, hours: hoursToOilChange, days: Math.ceil(hoursToOilChange / 24.0) },
        { maintenance: "Seperator Filter Change", cost: mcost.separatorFilterChange, hours: hoursToSepFilterChange, days: Math.ceil(hoursToSepFilterChange / 24.0) },
        { maintenance: "Compressor Check", cost: mcost.compressorCheck, hours: hoursToCompressorCheck, days: Math.ceil(hoursToCompressorCheck / 24.0) }
    ];
    
    // sort the list ascending - next maintenance
    plannedMaintenanceList.sort(function(a, b) {
        return a.hours - b.hours;
    });
    
    context['maintenance'] = {
        /** @deprecated */
        currencySymbol: mcost.currencySymbol,

        unit: mcost.currencySymbol,
        upcoming: plannedMaintenanceList
    };    
    return context;
}
return Promise.resolve(f());
"""

#
#
#
def queryUsageHours_body():
    return """/**
@param value is the context
*/
let context = value;

return Device.api.getProperty("totalLoadHours")
 .then(prop => {
     context['totalLoadHours'] = { last: prop.value, asOf: prop.time };
     return Device.api.getProperty("totalHours");
})
 .then(prop => {
     context['totalHours'] = { last: prop.value, asOf: prop.time };
     return context;
});
"""

#
#
#
def queryEstimEnergyConsumption_body():
    return """/**
@param value is the context
*/
let context = value;

const ENERGY_CONSUMPTION_CONSTANT = 10.0 * 1.2;
const ENERGY_IDLE_CONSUMPTION_RATIO = 0.27;

const IDLE_PWR_MULTIPLIER = ENERGY_CONSUMPTION_CONSTANT * ENERGY_IDLE_CONSUMPTION_RATIO;
const LOAD_PWR_MULTIPLIER = ENERGY_CONSUMPTION_CONSTANT;

/*
 * Formula:
 *  x =  
 *   (load_running_hours_total * LOAD_PWR_MULTIPLIER) + (idle_running_hours_total * IDLE_PWR_MULTIPLIER)
 *
 *  result = x
 */

let estimatedEnergyAvg = [];

// For 4 periods: 24h, 7d, 1m, 1y 
for (let i = 0; i < 4; i++) {
   let x = context.loadRunningHours[i] * LOAD_PWR_MULTIPLIER + context.idleRunningHours[i] * IDLE_PWR_MULTIPLIER;
   estimatedEnergyAvg.push(x);
}

context['energy'] = {
    value: estimatedEnergyAvg.map(i => i || 0),
    unit: 'kWh'
};
                                                                

return context;
"""

#
#
#
def queryEstimPowerConsumption_body():
    return """/**
@param value is the context
*/
let context = value;

const ENERGY_CONSUMPTION_CONSTANT = 10.0 * 1.1;
const ENERGY_IDLE_CONSUMPTION_RATIO = 0.27;

const IDLE_PWR_MULTIPLIER = ENERGY_CONSUMPTION_CONSTANT * ENERGY_IDLE_CONSUMPTION_RATIO;
const LOAD_PWR_MULTIPLIER = ENERGY_CONSUMPTION_CONSTANT;

/*
 * Formula:
 *  x =  
 *   (load_running_hours_total * LOAD_PWR_MULTIPLIER) + (idle_running_hours_total * IDLE_PWR_MULTIPLIER)
 *  y = 
 *   (load_running_hours_totol + idle_running_hours_total)
 *
 *  result = x / y;
 */

let estimatedPowerUsageAvg = [];

// For 4 periods: 24h, 7d, 1m, 1y 
for (let i = 0; i < 4; i++) {
   let x = context.loadRunningHours[i] * LOAD_PWR_MULTIPLIER + context.idleRunningHours[i] * IDLE_PWR_MULTIPLIER;
   let y = context.loadRunningHours[i] + context.idleRunningHours[i];
   estimatedPowerUsageAvg.push(x/y);
}

context['power'] = {
    value: estimatedPowerUsageAvg.map(i => i || 0),
    unit: 'kW'
};
                                                                
return context;
"""

#
#
#
def queryLoadRatio_body():
    return """/**
@param value is the context
*/
let context = value;

let totalHoursMaxP = Device.queryAggregates({ pname: "totalHours", agg: "max" });
let totalHoursMinP = Device.queryAggregates({ pname: "totalHours", agg: "min" });
let totalLoadHoursMaxP = Device.queryAggregates({ pname: "totalLoadHours", agg: "max" });
let totalLoadHoursMinP = Device.queryAggregates({ pname: "totalLoadHours", agg: "min" });

return Promise.all([totalHoursMaxP, totalHoursMinP, totalLoadHoursMaxP, totalLoadHoursMinP]).then( results => {
    let loadRatio = [];
    
    context.totalHours['average'] = [];
    context.totalLoadHours['average'] = [];
    
    // For 4 periods: 24h, 7d, 30d, 1y 
    for (var i = 0; i < 4; i++) {
        let tLhMax = results[2][i] || 0;
        let tLhMin = results[3][i] || 0;
        let thMax  = results[0][i] || 0;
        let thMin  = results[1][i] || 0;
        
        context.totalHours['average'].push(thMax-thMin);
        context.totalLoadHours['average'].push(tLhMax-tLhMin);
            
        let totalH = thMax - thMin;
        if (totalH == 0) {
            loadRatio.push(0);
        }
        else {
            loadRatio.push((tLhMax - tLhMin) / totalH);
        }
    }
    
    context['loadRatio'] = {
        average: loadRatio,
        // calculate with the most recent values
        current: context.totalLoadHours.last / context.totalHours.last, 
        unit: "%"
    };
    
    return context;
});
"""

#
#
#
def queryStoppages_body():
    return """/**
@param value is the context
*/
async function f() {
    let context = value;

    let nbrOfPlanned = await Device.queryAggregates({ pname: "plannedStops", agg: "count" });
    let nbrOfUnplanned = await Device.queryAggregates({ pname: "unplannedStops", agg: "count" });
    let nbrOfPowerCut = await Device.queryAggregates({ pname: "powercutStops", agg: "count" });

    context["stoppages"] = {
        planned:  nbrOfPlanned.map(i => i || 0),
        unplanned: nbrOfUnplanned.map(i => i || 0),
        powercut: nbrOfPowerCut.map(i => i || 0)
    };

    return context;
}
return Promise.resolve(f()); 
"""

#
#
#
def queryEstimCostOfRunning_body():
    return """/**
 * {@link https://github.com/lodash/lodash/blob/4.17.10/lodash.js#L11972 Lodash#isNil}
 * @param {*} x
 * @returns {boolean}
 */
const isNil = x => x == null;

/**
 * @param {*} x
 * @returns {boolean}
 */
const isNumber = x => typeof x === 'number';

/**
 * @param {*} x
 * @returns {boolean}
 */
const isString = x => typeof x === 'string';

/**
 * @param {{ value: number, unit: string}} x
 * @returns {boolean}
 */
const validateCostOfkWhType = x => {
 if (isNil(x)) return false;
 
 if (!isNumber(x.value) || !isString(x.unit)) return false;
 
 return true;
}

/**
 * @desc Default value of "costOfkWh"
 * @type {{ value: number, unit: string }}
 */
const COST_OF_KWH = {
    value: 0.0,
    unit: '',
};

async function f() {
    let context = value;

    const costOfkWh = validateCostOfkWhType(value['costOfkWh']) ? value['costOfkWh'] : COST_OF_KWH;;

    context['costOfRunning'] = {
        value: context.energy.value.map(i => i * costOfkWh.value),
        unit: costOfkWh.unit
    };   
    return context;
}
return Promise.resolve(f());
"""

#
#
#
def queryOEE_body():
    return """/**
* Availability = Wt / Lt where Wt is Working Time, Lt is Loaded Time
* 
* LoadedTime = period - (total hours - unplanned stoppage duration)
*
* WorkingTime = Total hours
*
* OEE = A x Perf x Q
* 
* MTbf = Lt / Nbr of unplanned stoppages
* 
* MTtr = Unplanned stoppages / Nbr of unplanned stoppages
*/

let query = value;

const PNAME = "non-existing-prop-name";

let q = { startRelative: { value: query.from.value, unit: query.from.unit }, aggregators: [ {name: 'sum', sampling: { value: query.sampling.value, unit: query.sampling.unit } } ] };

Device.api.readData(PNAME, q)
    .then(resultSet => { 
        let items = resultSet.results[0].values.map(obj => {
            return obj;
        });
        done(null, items);
     });
"""

#
#
#
def queryMtbf_body():
    return """/**
* Availability = Wt / Lt where Wt is Working Time, Lt is Loaded Time
* 
* LoadedTime = period - (total hours - unplanned stoppage duration)
*
* WorkingTime = Total hours
*
* OEE = A x Perf x Q
* 
* MTbf = Lt / Nbr of unplanned stoppages
* 
* MTtr = Unplanned stoppages / Nbr of unplanned stoppages
*/

let query = value;

const PNAME = "non-existing-prop-name";

let q = { startRelative: { value: query.from.value, unit: query.from.unit }, aggregators: [ {name: 'sum', sampling: { value: query.sampling.value, unit: query.sampling.unit } } ] };

Device.api.readData(PNAME, q)
    .then(resultSet => { 
        let items = resultSet.results[0].values.map(obj => {
            return obj;
        });
        done(null, items);
     });
"""

#
#
#
def queryMttr_body():
    return """/**
* Availability = Wt / Lt where Wt is Working Time, Lt is Loaded Time
* 
* LoadedTime = period - (total hours - unplanned stoppage duration)
*
* WorkingTime = Total hours
*
* OEE = A x Perf x Q
* 
* MTbf = Lt / Nbr of unplanned stoppages
* 
* MTtr = Unplanned stoppages / Nbr of unplanned stoppages
*/

let query = value;

const PNAME = "non-existing-prop-name";

let q = { startRelative: { value: query.from.value, unit: query.from.unit }, aggregators: [ {name: 'sum', sampling: { value: query.sampling.value, unit: query.sampling.unit } } ] };

Device.api.readData(PNAME, q)
    .then(resultSet => { 
        let items = resultSet.results[0].values.map(obj => {
            return obj;
        });
        done(null, items);
     });
"""

#
#
#
def preaggregate_body():
    return """/**
*/
async function f(context) {
    // Call the methods below in parallel.
    // These methods do not have any dependence on other method output.
    let results = await Promise.all([
    	Device.queryPropertySummary({ pname: "idleRunningMinutes", agg: "sum", unit: "min", fname: 'total', asContextMember: '_idleMinutes' }),
    	Device.queryPropertySummary({ pname: "loadRunningMinutes", agg: "sum", unit: "min", fname: 'total', asContextMember: '_loadMinutes' }),
    	Device.queryPropertySummary({ pname: "unplannedStopsMinutes", agg: "sum", unit: "min", fname: 'total', asContextMember: '_unplndStopMinutes' }),
    	Device.queryPropertySummary({ pname: "plannedStopsMinutes", agg: "sum", unit: "min", fname: 'total', asContextMember: '_plndStopMinutes' }),
        Device.queryPropertySummary({ pname: "workingPressure", agg: "avg", unit: "bar", asContextMember: 'pressure' }),
        Device.queryPropertySummary({ pname: "screwTemperature", agg: "avg", unit: "°C", asContextMember: 'temperature' }),
    ]);
    
    // Merge results into context
    results.forEach(result => Object.assign(context, result));
    
    // Perform calculations using intermediary fields and place them into context
    context.idleRunningHours = context._idleMinutes ? context._idleMinutes.total.map(i => (i || 0) / 60.0) : 0;
    context.loadRunningHours = context._loadMinutes ? context._loadMinutes.total.map(i => (i || 0) / 60.0) : 0;
    context.unplannedStoppageHours = context._unplndStopMinutes ? context._unplndStopMinutes.total.map(i => (i || 0) / 60.0) : 0;
    context.plannedStoppageHours = context._plndStopMinutes ? context._plndStopMinutes.total.map(i => (i || 0) / 60.0) : 0;
    
    // Call the methods below in parallel.
    // These methods are dependent on the data produced by previously called methods.
    results = await Promise.all([
        Device.queryEstimEnergyConsumption(context),
        Device.queryEstimPowerConsumption(context),
        Device.queryUsageHours(context),
        // Device.queryLoadRatio(context),
        // Device.queryStoppages(context),
        // Device.queryEstimCostOfRunning(context),
        // Device.queryOEE(context),
        // Device.queryMtbf(context),
        // Device.queryMttr(context)
    ]);

    // Merge results into context
    results.forEach(result => Object.assign(context, result));
    return context;
};

Device.api.getProperty("state")
 .then( prop => prop.value || Device.getEmptyView() )
 .then( context => f(context) )
 .then( context => Device.api.setProperty("state", { value: context, time: new Date().toISOString() }) )
 .then( property => done(null, null) );
"""
