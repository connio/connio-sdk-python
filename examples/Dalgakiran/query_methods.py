# Query methods
#
# buildAggregateQueries
# queryAggregates
# queryPropertySummary
# queryWarningAlarmSummary
# queryTimeToMaintenance
# queryUsageHours
# queryLoadRatio
#
# preaggregate
# calculateAll
# showOEE 
# processCompressorStates
# 
# queryEstimEnergyConsumption   - OBSOLETED
# queryEstimPowerConsumption    - OBSOLETED
# queryStoppages                - OBSOLETED
# queryEstimCostOfRunning       - OBSOLETED
# queryOEE                      - OBSOLETED
#

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
  Builds a summary/stats view of the given property from the timeseries database.
*/
async function f() {
    
    // Acquire property definition and historical data in parallel
    let [prop, stats] = await Promise.all([
        Device.api.getProperty(value.pname),
        Device.queryAggregates({ pname: value.pname, agg: value.agg })
    ]);

    let result = {
        value: prop.value,
        unit: value.unit
    };
    
    //default field name is `average`
    result[value.fname || 'average'] = stats.map(i => i);
    
    // Result may be requested as a member of a context object
    // such as in getDashboardParallel.
    if (value.asContextMember) {
        let context = {};
        context[value.asContextMember] = result;
        return context;
    }
    
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
        currency: "USD",
        airFilterChange: 0.0,
        oilChange: 0.0,  
        compressorCheck: 0.0, 
        oilFilterChange: 0.0, 
        separatorFilterChange : 0.0, 
        bearingLubrication: 0.0     
    };
    
    let defaultCycles = { 
        airFilterChange: 2997,
        oilChange: 3000,  
        compressorCheck: 3000, 
        oilFilterChange: 3000, 
        separatorFilterChange : 6000, 
        bearingLubrication: 29999     
    };
    
    let mcost = await Device.api.getProperty(maintCostsPropName).then(p=>p.value) || defaultMaintCosts;
    let mCycles = await Device.api.getProperty(maintCyclesPropName).then(p=>p.value) || defaultCycles;
    
    let plannedMaintenanceList = [ 
        { maintenance: "Bearing Lubrication", cost: mcost.bearingLubrication, hours: 0, days: undefined, cycle: Math.ceil(mCycles.bearingLubrication / 24) },
        { maintenance: "Air Filter Change", cost: mcost.airFilterChange, hours: 0, days: undefined, cycle: Math.ceil(mCycles.airFilterChange / 24) },
        { maintenance: "Oil Filter Change", cost: mcost.oilFilterChange, hours: 0, days: undefined, cycle: Math.ceil(mCycles.oilFilterChange / 24) },
        { maintenance: "Oil Change", cost: mcost.oilChange, hours: 0, days: undefined, cycle: Math.ceil(mCycles.oilChange / 24) },
        { maintenance: "Seperator Filter Change", cost: mcost.separatorFilterChange, hours: 0, days: undefined, cycle: Math.ceil(mCycles.separatorFilterChange / 24) },
        { maintenance: "Compressor Check", cost: mcost.compressorCheck, hours: 0, days: undefined, cycle: Math.ceil(mCycles.compressorCheck / 24) }
    ];

    // Hours left until the next maintenances by category
    let mCounters = await Device.api.getProperty(maintCountersPropName).then(p=>p.value);
    
    if ( mCounters ) {
        let hoursToBearingLub        = ((mCycles.bearingLubrication * 60)   - mCounters.bearingLubrication) / 60.0;
        let hoursToAirFilterChange   = ((mCycles.airFilterChange * 60)      - mCounters.airFilterChange) / 60.0;
        let hoursToOilFilterChange   = ((mCycles.oilFilterChange * 60)      - mCounters.oilFilterChange) / 60.0;
        let hoursToOilChange         = ((mCycles.oilChange * 60)            - mCounters.oilChange) / 60.0;
        let hoursToSepFilterChange   = ((mCycles.separatorFilterChange * 60) - mCounters.separatorFilterChange) / 60.0;
        let hoursToCompressorCheck   = ((mCycles.compressorCheck * 60)      - mCounters.compressorCheck) / 60.0;
        
        plannedMaintenanceList[0].hours = hoursToBearingLub;
        plannedMaintenanceList[0].days = Math.ceil(hoursToBearingLub / 24.0);
        plannedMaintenanceList[1].hours = hoursToAirFilterChange;
        plannedMaintenanceList[1].days = Math.ceil(hoursToAirFilterChange / 24.0);
        plannedMaintenanceList[2].hours = hoursToOilFilterChange;
        plannedMaintenanceList[2].days = Math.ceil(hoursToOilFilterChange / 24.0);
        plannedMaintenanceList[3].hours = hoursToOilChange;
        plannedMaintenanceList[3].days = Math.ceil(hoursToOilChange / 24.0);
        plannedMaintenanceList[4].hours = hoursToSepFilterChange;
        plannedMaintenanceList[4].days = Math.ceil(hoursToSepFilterChange / 24.0);
        plannedMaintenanceList[5].hours = hoursToCompressorCheck;
        plannedMaintenanceList[5].days = Math.ceil(hoursToCompressorCheck / 24.0);
        
        // sort the list ascending - next maintenance
        plannedMaintenanceList.sort(function(a, b) {
            return a.hours - b.hours;
        });
    }
    
    context['maintenance'] = {
        currencySymbol: mcost.currencySymbol,
        unit: mcost.currency,
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
            loadRatio.push((tLhMax - tLhMin) / totalH * 100);
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
def preaggregate_body():
    return """/**
*/
async function f(context) {
    
    // Call the methods below in parallel.
    // These methods do not have any dependence on other method output.
    let results = await Promise.all([
        Device.queryPropertySummary({ pname: "workingPressure", agg: "avg", unit: "bar", asContextMember: 'pressure' }),
        Device.queryPropertySummary({ pname: "screwTemperature", agg: "avg", unit: "°C", asContextMember: 'temperature' }),
        Device.queryLoadRatio(context),
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

def processCompressorState_body():
    return """/**
* This method processes compressor states and calculate operation times (i.e idle/load running, number of unplanned stops, etc..)
* Accepts number of months to process. Default is 13 for full year (yes it is 13 not 12 for a reason)
* Returns an array of 24hr periods with information needed to calculate operation times and OEE.
*
* TODO:
*  1. Handle states overlapping more than day - time window
*  2. Last 24hr calculation is missing - we calculate today
*  3. Also handle when $END$ is not within the same time window
*  4. 1 / 0.5 for counting won't work for states overlapping multiple days
*/

/* 
 * Formulas:
 * 
 * Availability = Wt / Lt where Wt is Working Time, Lt is Loaded Time
 * 
 * Lt (Loaded Time) = Load Running Duration + Idle Running Duration + Unplanned stopages Duration
 *
 * Wt (Working Time) = Load Running Duration + Idle Running Duration
 *
 * OEE = A x Perf x Q
 * 
 * MTbf = Lt / Nbr of unplanned stoppages
 * 
 * MTtr = Unplanned stoppages / Nbr of unplanned stoppages
 */
 
 function savePeriod(periods, period, twb, twe) {
    let Lt = period.idleRunningDur + period.loadRunningDur + period.unplannedDur;
    let Wt = period.idleRunningDur + period.loadRunningDur;
    
    period.Availability = Wt / Lt;
    period.Quality = 1.0;
    period.Perf = 1.0;
    
    let date = new Date(twe)
    period.date = `${date.getUTCFullYear()}-${date.getUTCMonth() + 1}-${date.getUTCDate()}`;
    
    period.tw_ends = new Date(twe).toISOString();
    period.tw_begins = new Date(twb).toISOString();
    
    periods.push(period);
 }
 

// Default is last 13 months
let q = { startRelative: { value: 13, unit: 'months' }, order: 'asc' };

let table = Device.fetchCompressorStates();
let stateTypes = Device.fetchCompressorStateTypes();

const SentinelCode = 999;
const timewindow = (24 * 60 * 60 * 1000); // 24 hours (1 day) time window by default 

let now = new Date();
now.setUTCMonth(now.getUTCMonth() - 12);

// twb time should be at 00:00:00.000Z and 
// twe time should be at 23:59:59.999Z to start time window at the top of the day
let twb = Date.parse(now.toISOString().split('T')[0] + "T00:00:00.000Z");
let twe = twb + timewindow - 1000; // minus 1 sec

return Device.api.readData('compressorState', q)
  .then(resultSet => {
    let periods = [];

    // add a sentinel value to calculate the last state properly
    if ( resultSet.results[0].values.length > 0) { 
        resultSet.results[0].values.push({ 
            v: { code: SentinelCode, label: '$END$'}, 
            t: new Date().toISOString() 
        });
    }
    
    let period = { unplannedStops: 0, plannedStops: 0, idleRunningDur: 0, loadRunningDur: 0, unplannedDur: 0 };
    
    let prevState;
    resultSet.results[0].values.forEach( s => {
        let stateTime = Date.parse(s.t); // number of milliseconds since the Unix Epoch
        
        if (s.v.code == SentinelCode) {
            /****
             * This is the last state processing case
             */ 
            
            if (stateTypes.UNPLANNED_STOPPAGES.includes(prevState.v.code)) period.unplannedStops += 1;
            if (stateTypes.PLANNED_STOPPAGES.includes(prevState.v.code)) period.plannedStops += 1;
            
            // convert from milliseconds to minutes
            let lastStateDuration = (stateTime - Date.parse(prevState.t)) / 1000 / 60 / 60;
            
            if (stateTypes.IDLE_RUNNING.includes(prevState.v.code)) {
                period.idleRunningDur += lastStateDuration;
            }
            else if (stateTypes.LOAD_RUNNING.includes(prevState.v.code)) {
                period.loadRunningDur += lastStateDuration;
            }
            else if (stateTypes.UNPLANNED_STOPPAGES.includes(prevState.v.code)) {
                period.unplannedDur += lastStateDuration;
            }
            
            // final record, save the period and quit
            savePeriod(periods, period, twb, twe);
        }
        else if (prevState && stateTime >= twb && stateTime < twe) {
            /****
             * This is the within state processing case
             */ 

            if (stateTypes.UNPLANNED_STOPPAGES.includes(prevState.v.code)) period.unplannedStops += 1;
            if (stateTypes.PLANNED_STOPPAGES.includes(prevState.v.code)) period.plannedStops += 1;
            
            // we don't want to account for durations taken place after date cut off
            let prevStateBeginning = Date.parse(prevState.t) < twb ? twb : Date.parse(prevState.t);
            // convert from milliseconds to minutes
            let prevStateDuration = (stateTime - prevStateBeginning) / 1000 / 60 / 60;
            
            if (stateTypes.IDLE_RUNNING.includes(prevState.v.code)) {
                period.idleRunningDur += prevStateDuration;
            }
            else if (stateTypes.LOAD_RUNNING.includes(prevState.v.code)) {
                period.loadRunningDur += prevStateDuration;
            }
            else if (stateTypes.UNPLANNED_STOPPAGES.includes(prevState.v.code)) {
                period.unplannedDur += prevStateDuration;
            }
        }
        else if (prevState && stateTime > twe) {
            /****
             * This is the overlapping state processing case
             */ 
        
            // This is an overlapping state; save the current period and create a new one
            if (stateTypes.UNPLANNED_STOPPAGES.includes(prevState.v.code)) period.unplannedStops += 1;
            if (stateTypes.PLANNED_STOPPAGES.includes(prevState.v.code)) period.plannedStops += 1;
     
            // add up residual prev state time
            let prevStateResidualDuration = (twe - Date.parse(prevState.t)) / 1000 / 60 / 60;
            
            if (stateTypes.IDLE_RUNNING.includes(prevState.v.code)) {
                period.idleRunningDur += prevStateResidualDuration;
            }
            else if (stateTypes.LOAD_RUNNING.includes(prevState.v.code)) {
                period.loadRunningDur += prevStateResidualDuration;
            }
            else if (stateTypes.UNPLANNED_STOPPAGES.includes(prevState.v.code)) {
                period.unplannedDur += prevStateResidualDuration;
            }
            
            savePeriod(periods, period, twb, twe);
            
            //+++++
            
            // reset period values and start a new window
            period = { unplannedStops: 0, plannedStops: 0, idleRunningDur: 0, loadRunningDur: 0, unplannedDur: 0 };
            
            // Overlapping states is counted as .5 
            // Do Math.ceil(x) when calculating daily average of MTbf and MTtr
            // Do Math.floor(x) when calculating larger range average - except do Math.ceil(x) for the very first record
            if (stateTypes.UNPLANNED_STOPPAGES.includes(prevState.v.code)) period.unplannedStops += 0.5;
            if (stateTypes.PLANNED_STOPPAGES.includes(prevState.v.code)) period.plannedStops += 0.5;
            
            // change period
            twb = twe + 1000; // add one sec to make it top of the hour
            twe = twe + timewindow;
            
            let prevStateOverlappingDuration = (stateTime - twb) / 1000 / 60 / 60;
            
            if (stateTypes.IDLE_RUNNING.includes(prevState.v.code)) {
                period.idleRunningDur += prevStateOverlappingDuration;
            }
            else if (stateTypes.LOAD_RUNNING.includes(prevState.v.code)) {
                period.loadRunningDur += prevStateOverlappingDuration;
            }
            else if (stateTypes.UNPLANNED_STOPPAGES.includes(prevState.v.code)) {
                period.unplannedDur += prevStateOverlappingDuration;
            }
        }
        else if (!prevState && stateTime > twe) {
            while(stateTime >= twe) {
                twb = twe + 1000;  // add one sec to make it top of the hour
                twe = twe + timewindow;
            }
        }
        prevState = s;
    });
    
    return periods;
  });
"""

def calculateAll_body():
    return """/**
  Calculates average OEE, MTtr, MTbf, Energy Consumption, Power Consumption, Cost of Running 
  and stoppages for 24hr, 7 days, 30 days and 1 year
*/


/**
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
    
function calc(periods, nbrOfDays, quality, perf) {
    let unplannedStops  = 0;
    let plannedStops    = 0;
    let idleRunningDur  = 0;
    let loadRunningDur  = 0;
    let unplannedDur    = 0;

    let offset = Math.max((periods.length - nbrOfDays), 0);
    for (let i = 0; (i+offset) < periods.length; i++) {
        let p = periods[i+offset];
        // do not count overlapping states twice
        // except the very first one
        unplannedStops  += (i == 0 ? Math.ceil(p.unplannedStops) : Math.floor(p.unplannedStops));
        plannedStops    += (i == 0 ? Math.ceil(p.plannedStops) : Math.floor(p.plannedStops));
        idleRunningDur  += p.idleRunningDur;
        loadRunningDur  += p.loadRunningDur;
        unplannedDur    += p.unplannedDur;
    }
    
    let Lt = idleRunningDur + loadRunningDur + unplannedDur;
    let Wt = idleRunningDur + loadRunningDur;
    
    return {
        OEE: Math.min(100, ((Wt / Lt * quality * perf) * 100)).toFixed(2),
        MTbf: (unplannedStops == 0 ? "-" : (Lt / unplannedStops).toFixed(2)),
        MTtr: (unplannedStops == 0 ? "-" : (unplannedDur / unplannedStops).toFixed(2)),
        idleRunningDur: idleRunningDur,
        loadRunningDur: loadRunningDur,
        unplannedStops: unplannedStops,
        plannedStops: plannedStops
        
    }
}


/**
 *
 */ 
async function f(context) {
    const ENERGY_CONSUMPTION_CONSTANT = 10.0 * 1.2;
    const ENERGY_IDLE_CONSUMPTION_RATIO = 0.27;
    
    const IDLE_PWR_MULTIPLIER = ENERGY_CONSUMPTION_CONSTANT * ENERGY_IDLE_CONSUMPTION_RATIO;
    const LOAD_PWR_MULTIPLIER = ENERGY_CONSUMPTION_CONSTANT;
    
    let p24hr = calc(context.periods, 1, 1, 1);
    let p7days = calc(context.periods, 7, 1, 1);
    let p30days = calc(context.periods, 30, 1, 1);
    let p1year = calc(context.periods, 365, 1, 1);
    
    context['oee'] = {
        performance: [ 1, 1, 1, 1 ],
        quality: [ 1, 1, 1, 1 ],
        average: [ p24hr.OEE, p7days.OEE, p30days.OEE, p1year.OEE ],
        unit: '%'
    };
    
    context['mtbf'] = {
        average: [ p24hr.MTbf, p7days.MTbf, p30days.MTbf, p1year.MTbf ],
        unit: 'h'
    };
    
    context['mttr'] = {
        average: [ p24hr.MTtr, p7days.MTtr, p30days.MTtr, p1year.MTtr ],
        unit: 'h'
    };
    
    context['energy'] = {
        value: [ 
            p24hr.loadRunningDur * LOAD_PWR_MULTIPLIER + p24hr.idleRunningDur * IDLE_PWR_MULTIPLIER,
            p7days.loadRunningDur * LOAD_PWR_MULTIPLIER + p7days.idleRunningDur * IDLE_PWR_MULTIPLIER,
            p30days.loadRunningDur * LOAD_PWR_MULTIPLIER + p30days.idleRunningDur * IDLE_PWR_MULTIPLIER,
            p1year.loadRunningDur * LOAD_PWR_MULTIPLIER + p1year.idleRunningDur * IDLE_PWR_MULTIPLIER,
        ],
        unit: 'kWh'
    };
    
    context['power'] = {
        value: [
            (p24hr.loadRunningDur * LOAD_PWR_MULTIPLIER + p24hr.idleRunningDur * IDLE_PWR_MULTIPLIER) / (p24hr.loadRunningDur + p24hr.idleRunningDur),
            (p7days.loadRunningDur * LOAD_PWR_MULTIPLIER + p7days.idleRunningDur * IDLE_PWR_MULTIPLIER) / (p7days.loadRunningDur + p7days.idleRunningDur),
            (p30days.loadRunningDur * LOAD_PWR_MULTIPLIER + p30days.idleRunningDur * IDLE_PWR_MULTIPLIER) / (p30days.loadRunningDur + p30days.idleRunningDur),
            (p1year.loadRunningDur * LOAD_PWR_MULTIPLIER + p1year.idleRunningDur * IDLE_PWR_MULTIPLIER) / (p1year.loadRunningDur + p1year.idleRunningDur),
        ],
        unit: 'kW'
    };
    
    const costOfkWh = validateCostOfkWhType(value['costOfkWh']) ? value['costOfkWh'] : COST_OF_KWH;;
    
    context['costOfRunning'] = {
        value: context.energy.value.map(i => i * costOfkWh.value),
        unit: costOfkWh.unit
    };
    
    
    let powercutCounts = await Device.queryAggregates({ pname: "powercutStops", agg: "count" });
    
    context["stoppages"] = {
        planned:  [
            p24hr.plannedStops, 
            p7days.plannedStops, 
            p30days.plannedStops, 
            p1year.plannedStops
        ],
        unplanned: [
            p24hr.unplannedStops, 
            p7days.unplannedStops, 
            p30days.unplannedStops, 
            p1year.unplannedStops
        ],
        powercut: powercutCounts.map(i => i || 0)
    };
    
    return context;
}

return Promise.resolve(f(value));
"""

def showOEE_body():
    return """/**
* Enter number of days to display OEE for each day and the aggregated OEE
*/    
Array.prototype.insert = function ( index, item ) {
    this.splice( index, 0, item );
};

let days = value || 7;

Device.processCompressorStates().then(periods => {
    
    let results = periods.map( p => {
        let OEE = ((p.Availability * p.Quality * p.Perf) * 100).toFixed(2);
        let MTbf = (Math.ceil(p.unplannedStops) == 0 
                    ? "-"
                    : ( (p.idleRunningDur + p.loadRunningDur + p.unplannedDur) / Math.ceil(p.unplannedStops) ).toFixed(2));
        let MTtr = (Math.ceil(p.unplannedStops) == 0 
                    ? "-"
                    : (p.unplannedDur / Math.ceil(p.unplannedStops)).toFixed(2));
        
        return `@${p.date} OEE: ${OEE}, MTbf: ${MTbf} hr, MTtr: ${MTtr} hr`;
    });
    
    let unplannedStops  = 0;
    let plannedStops    = 0;
    let idleRunningDur  = 0;
    let loadRunningDur  = 0;
    let unplannedDur    = 0;
    
    let offset = Math.max((periods.length - days), 0);
    for (let i = 0; (i+offset) < periods.length; i++) {
        let p = periods[i+offset];
        // do not count overlapping states twice
        // except the very first one
        unplannedStops  += (i == 0 ? Math.ceil(p.unplannedStops) : Math.floor(p.unplannedStops));
        plannedStops    += (i == 0 ? Math.ceil(p.plannedStops) : Math.floor(p.plannedStops));
        idleRunningDur  += p.idleRunningDur;
        loadRunningDur  += p.loadRunningDur;
        unplannedDur    += p.unplannedDur;
    }
  
    let Lt = idleRunningDur + loadRunningDur + unplannedDur;
    let Wt = idleRunningDur + loadRunningDur;
    
    let summary = `#unp: ${unplannedStops}, #pla: ${plannedStops}, Idle: ${idleRunningDur.toFixed(2)}h, Load: ${loadRunningDur.toFixed(2)}h, uPlan: ${unplannedDur.toFixed(2)}h`;
    
    let resultSet = results.reverse();

    resultSet.insert(0, `--OVERALL--` );
    resultSet.insert(1, `${summary}` );
    resultSet.insert(2, "OEE: " + ((Wt / Lt) * 100).toFixed(2)  +" %");
    resultSet.insert(3, "MTbf: " + (unplannedStops == 0 ? "-" : (Lt / unplannedStops).toFixed(2)  + " hr"));
    resultSet.insert(4, "MTtr: " + (unplannedStops == 0 ? "-" : (unplannedDur / unplannedStops).toFixed(2)  +" hr"));
    resultSet.insert(5, "--DAILY--");
        
    done(null, resultSet.slice(0, days + 6));
});
"""

#
#
#
def queryEstimEnergyConsumption_OLD_body():
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
def queryEstimPowerConsumption_OLD_body():
    return """/**
  @param value is the context
*/
let context = value;

const IDLE_RUNNING = 10;
const LOAD_RUNNING = 11;

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
    value: estimatedPowerUsageAvg.map(i => i),
    unit: 'kW'
};

return context;
"""

#
#
#
def queryStoppages_OLD_body():
    return """/**
  @param value is the context
*/
let context = value;

return Promise.all([
    Device.queryAggregates({ pname: "plannedStops", agg: "count" }),
    Device.queryAggregates({ pname: "unplannedStops", agg: "count" }),
    Device.queryAggregates({ pname: "powercutStops", agg: "count" })
]).then(results => {
    context["stoppages"] = {
        planned:  results[0].map(i => i || 0),
        unplanned: results[1].map(i => i || 0),
        powercut: results[2].map(i => i || 0)
    };
    return context;
});
"""

#
#
#
def queryEstimCostOfRunning_OLD_body():
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
def queryOEE_OLD_body():
    return """/**
 * @param value is the context
 * 
 * 
 * Availability = Wt / Lt where Wt is Working Time, Lt is Loaded Time
 * 
 * Lt (Loaded Time) = Load Running Duration + Idle Running Duration + Unplanned stopages Duration
 *
 * Wt (Working Time) = Load Running Duration + Idle Running Duration
 *
 * OEE = A x Perf x Q
 * 
 * MTbf = Lt / Nbr of unplanned stoppages
 * 
 * MTtr = Unplanned stoppages / Nbr of unplanned stoppages
 */

let context = value;
const perf  = 1;
const quality = 1;

let oee = [];
let mtbf = [];
let mttr = [];

let availability = 1;

let durationCeiling = [24, 24 * 7, 24 * 30, 24 * 365];

// For 4 periods: 24h, 7d, 1m, 1y 
for (let i = 0; i < 4; i++) {
   
   // Make sure not to exceed period duration if state duration is longer 
   let ceiling = durationCeiling[i];
   
   let Lt = Math.min(context.loadRunningHours[i], ceiling) + Math.min(context.idleRunningHours[i], ceiling) + Math.min(context.unplannedStoppageHours[i], ceiling);
   let Wt = Math.min(context.loadRunningHours[i], ceiling) + Math.min(context.idleRunningHours[i], ceiling);

   availability = Wt / Lt;
   
   oee.push(availability * perf * quality);
   
  let mtbfi = Lt / context.stoppages.unplanned[i];
  mtbf.push(mtbfi);
   
  let mttri = Math.min(context.unplannedStoppageHours[i], ceiling) / context.stoppages.unplanned[i];
  mttr.push(mttri)
}

context['oee'] = {
    performance: [ 1, 1, 1, 1 ],
    quality: [ 1, 1, 1, 1 ],
    average: oee.map(i => i * 100 || 0),
    unit: '%'
};

context['mtbf'] = {
    average: mtbf.map(i => i || 0),
    unit: 'h'
};

context['mttr'] = {
    average: mttr.map(i => i || 0),
    unit: 'h'
};

return context;
"""
#
#
#
def preaggregate_OLD_body():
    return """/**
*/
/**
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
    
    // Get compressor state to add duration of the current state to timings
    let compressorStateProp = await Device.api.getProperty("compressorState");
    if (compressorStateProp.value) {
        let stateTypes = Device.fetchCompressorStateTypes();
        
        let deltaInMinutes = (Date.now() - Date.parse(compressorStateProp.time)) / (1000 * 60);
        
        if (stateTypes.LOAD_RUNNING.includes(compressorStateProp.value.code) && context._loadMinutes) {
            context._loadMinutes.total[0] =  (context._loadMinutes.total[0] || 0) + deltaInMinutes;
        }
        else if (stateTypes.IDLE_RUNNING.includes(compressorStateProp.value.code) && context._idleMinutes) {
            context._idleMinutes.total[0] =  (context._idleMinutes.total[0] || 0) + deltaInMinutes;
        }
        else if (stateTypes.UNPLANNED_STOPPAGES.includes(compressorStateProp.value.code) && context._unplndStopMinutes) {
            context._unplndStopMinutes.total[0] =  (context._unplndStopMinutes.total[0] || 0) + deltaInMinutes;
        }
        else if (stateTypes.PLANNED_STOPPAGES.includes(compressorStateProp.value.code) && context._plndStopMinutes) {
            context._plndStopMinutes.total[0] =  (context._plndStopMinutes.total[0] || 0) + deltaInMinutes;
        }
    }
    
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
        //Device.queryUsageHours(context),
        Device.queryLoadRatio(context),
        Device.queryStoppages(context),
        Device.queryEstimCostOfRunning(context),
        Device.queryOEE(context),
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
