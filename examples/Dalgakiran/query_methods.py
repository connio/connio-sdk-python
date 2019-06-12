# ~~ Query methods ~~
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
# processCompressorStates
# calculateAll
# showOEE 
# 
# getConnectivity
# getActiveAlarm
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
 * @namespace BaseLogikaProfile
 *
 * @private
 * @async
 * @function queryAggregates
 * @memberof BaseLogikaProfile
 * @desc Queries 4 different stats for given property
 * @param {{ agg: string, pname: string }} value
 * @returns {Promise<Array>}
 */

/**
 * @private
 * @param {{ results: { values: { v: any }[] }[] }} response
 * @returns {any}
 */
function extractValue(response) {
  if (
    response.results &&
    response.results.length &&
    response.results[0].values &&
    response.results[0].values.length
  ) {
    return response.results[0].values[0].v;
  }

  return void 0;
}

/**
 * @async
 * @param {{ agg: string, pname: string }} value
 * @returns {Promise<Array>}
 */
async function main(value) {
  const queries = Device.buildAggregateQueries(value.agg);
  const requests = queries.map((q) => Device.api.readData(value.pname, q));
  const responses = await Promise.all(requests);

  return responses.map(extractValue);
}

return main(value);
"""

#
#
#
def queryPropertySummary_body():
    return """/**
 * @namespace BaseLogikaProfile
 *
 * @protected
 * @async
 * @function queryPropertySummary
 * @memberof BaseLogikaProfile
 * @description
 * Builds a summary/stats view of the given property from the timeseries database
 * @param {Object} value
 * @param {string} value.pname
 * @param {string} value.agg
 * @param {string} value.unit
 * @param {string} value.asContextMember
 * @param {string} value.fname
 * @returns {Promise<Object>}
 */

/**
 * @async
 * @param {Object} value
 * @param {string} value.pname
 * @param {string} value.agg
 * @param {string} value.unit
 * @param {string} value.asContextMember
 * @param {string} [value.fname="average"]
 * @returns {Object}
 */
async function main(value) {
  /** @desc Acquire property definition and historical data in parallel */
  const [prop, stats] = await Promise.all([
    Device.api.getProperty(value.pname),
    Device.queryAggregates({ pname: value.pname, agg: value.agg }),
  ]);

  const result = {
    current: prop.value,
    unit: value.unit,
    /** @desc default field name is "average" */
    [value.fname || 'average']: stats.map((i) => i),
  };

  /**
   * @description
   * Result may be requested as a member of a context object
   * such as in getDashboardParallel
   */
  if (value.asContextMember) {
    return {
      [value.asContextMember]: result,
    };
  }

  return result;
}

return main(value);
"""

def queryWarningAlarmSummary_body():
    return """/**
 * @namespace BaseLogikaProfile
 *
 * @protected
 * @async
 * @function queryWarningAlarmSummary
 * @returns {Promise<Object>}
 *
 * @requires Device/common
 */

const { Aggregator, Property } = Device.common();

/**
 * @async
 * @returns {Object}
 */
async function main() {
  const requests = [
    Device.queryAggregates({
      pname: Property.NBR_OF_ALARMS,
      agg: Aggregator.SUM,
    }),
    Device.queryAggregates({
      pname: Property.NBR_OF_WARNINGS,
      agg: Aggregator.SUM,
    }),
    Device.api.getProperty(Property.LAST_ALARMS),
    Device.api.getProperty(Property.LAST_WARNINGS),
  ];

  const [
    nbrOfAlarms,
    nbrOfWarnings,
    lastAlarms,
    lastWarnings,
  ] = await Promise.all(requests);

  let lastAlarmItems = [];

  if (lastAlarms.value) {
    lastAlarmItems = lastAlarms.value.items || [];
  }

  let lastWarningItems = [];

  if (lastWarnings.value) {
    lastWarningItems = lastWarnings.value.items || [];
  }

  return {
    alarms: {
      last: lastAlarmItems,
      asOf: lastAlarms.time || new Date().toISOString(),
      total: nbrOfAlarms.map((x) => x || 0),
    },
    warnings: {
      last: lastWarningItems,
      asOf: lastWarnings.time || new Date().toISOString(),
      total: nbrOfWarnings.map((x) => x || 0),
    },
  };
}

return main();
"""

#
#
#
def queryTimeToMaintenance_body():
    return """/**
 * @namespace BaseLogikaProfile
 *
 * @private
 * @async
 * @function queryTimeToMaintenance
 * @memberof BaseLogikaProfile
 * @param {Object} value context
 * @return {Promise<Object>}
 *
 * @requires Device/common
 */

const {
  getPropertyValue,
  Context,
  Property,
  DEFAULT_MAINTENANCE_COST_LIST,
} = Device.common();

/** @type {Object.<string, number>} */
const DEFAULT_MAINTENANCE_CYCLES = {
  airFilterChange: 2997,
  oilChange: 3000,
  compressorCheck: 3000,
  oilFilterChange: 3000,
  separatorFilterChange: 6000,
  bearingLubrication: 29999,
};

/** @enum {Object.<string, { id: string, name: string}>} */
const Maintenance = {
  BEARING_LUBRICATION: {
    id: 'bearingLubrication',
    name: 'Bearing Lubrication',
  },
  AIR_FILTER_CHANGE: {
    id: 'airFilterChange',
    name: 'Air Filter Change',
  },
  OIL_FILTER_CHANGE: {
    name: 'Oil Filter Change',
    id: 'oilFilterChange',
  },
  OIL_CHANGE: {
    name: 'Oil Change',
    id: 'oilChange',
  },
  SEPERATOR_FILTER_CHANGE: {
    name: 'Seperator Filter Change',
    id: 'separatorFilterChange',
  },
  COMPRESSOR_CHECK: {
    name: 'Compressor Check',
    id: 'compressorCheck',
  },
};

/** @type {{ name: string, id: string }[]} */
const MAINTENANCE_LIST = Object.values(Maintenance);

/**
 * @private
 * @param {{ costs: Object, cycles: Object, counters: Object}} params
 * @returns {(maintenance: string) => { cost: number, cycle: number } }
 */
function extractMaintenanceParams({ costs, cycles, counters }) {
  return function(maintenance) {
    return {
      cost: costs[maintenance],
      cycle: cycles[maintenance],
      counters: counters && counters[maintenance],
    };
  };
}

/**
 * @private
 * @param {Object} params
 * @param {string} params.name
 * @param {number} params.cost
 * @param {number} params.cycle
 * @param {number} [params.counters]
 * @returns {{ maintenance: string, cost: number, hours: number, days: number|void, cycle: number }}
 */
function makeMaintenance({ name, cost, cycle, counters }) {
  const hours = counters ? cycle - counters : 0;
  const days = counters ? Math.ceil(hours / 24) : void 0;

  return {
    maintenance: name,
    cost,
    hours,
    days,
    cycle: Math.ceil(cycle / 24),
  };
}

/**
 * @async
 * @param {Object} context
 * @returns {Object}
 */
async function main(context) {
  const requests = [
    getPropertyValue(
      Property.MAINTENANCE_COST_LIST,
      DEFAULT_MAINTENANCE_COST_LIST,
    ),
    getPropertyValue(Property.MAINTENANCE_CYCLES, DEFAULT_MAINTENANCE_CYCLES),
    getPropertyValue(Property.MAINTENANCE_COUNTERS),
  ];

  const [
    { unit, ...costs },
    cycles,
    /** @desc Hours left until the next maintenances by category */
    counters,
  ] = await Promise.all(requests);

  const extractParams = extractMaintenanceParams({
    costs,
    cycles,
    counters,
  });

  const upcomingMaintenanceList = MAINTENANCE_LIST.map(({ id, name }) =>
    makeMaintenance({
      name,
      ...extractParams(id),
    }),
  );

  context[Context.MAINTENANCE] = {
    unit,
    upcoming: counters
      ? upcomingMaintenanceList.sort((x, y) => x.hours - y.hours)
      : upcomingMaintenanceList,
  };

  return context;
}

return main(value);
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
 * @namespace BaseLogikaProfile
 *
 * @public
 * @function preaggregate
 * @memberof BaseLogikaProfile
 * @returns {void}
 */

/**
 * @async
 * @param {Object} context
 * @returns {Promise<Object>} Modified context
 */
async function main(context) {
  const requests = [
    Device.queryPropertySummary({
      pname: 'workingPressure',
      agg: 'avg',
      unit: 'bar',
      asContextMember: 'pressure',
    }),
    Device.queryPropertySummary({
      pname: 'screwTemperature',
      agg: 'avg',
      unit: '°C',
      asContextMember: 'temperature',
    }),
    Device.queryLoadRatio(context),
    /**
     * @description
     * Calculates average OEE, MTtr, MTbf, Energy Consumption, Power Consumption, Cost of Running
     * and stoppages for 24hr, 7 days, 30 days and 1 year
     */
    Device.processCompressorStates().then((periods) => {
      context.periods = periods;

      Device.calculateAll(context);
    }),
    Device.queryTimeToMaintenance(context),
    Device.queryWarningAlarmSummary(),
  ];

  if (context.hasInverter) {
    requests.push(
      Device.queryPropertySummary({
        pname: 'motorSpeed',
        agg: 'avg',
        unit: 'rpm',
        asContextMember: 'motorSpeed',
      }),
      Device.queryPropertySummary({
        pname: 'motorCurrent',
        agg: 'avg',
        unit: 'A',
        asContextMember: 'motorCurrent',
      }),
      Device.queryPropertySummary({
        pname: 'motorFrequency',
        agg: 'avg',
        unit: 'Hz',
        asContextMember: 'motorFrequency',
      }),
    );
  }

  /**
   * @description
   * Call the methods below in parallel.
   * These methods do not have any dependence on other method output.
   */
  const results = await Promise.all(requests);

  /** @desc Merge results into context */
  results.forEach((result) => Object.assign(context, result));

  return context;
}

Device.api
  .getProperty('state')
  .then((property) => property.value || Device.getEmptyState())
  .then(main)
  .then((context) =>
    Device.api.setProperty('state', {
      value: context,
      time: new Date().toISOString(),
    }),
  )
  .then(() => done(null, null));
"""

#
#
#
def processCompressorStates_body():
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
    period.date = `${date.getUTCFullYear()}-${('0' + (date.getUTCMonth() + 1)).slice(-2)}-${ ('0' + date.getUTCDate()).slice(-2)}`;
    
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

#
#
#
def calculateAll_body():
    return """/**
 * @namespace BaseLogikaProfile
 *
 * @private
 * @async
 * @function calculateAll
 * @memberof BaseLogikaProfile
 * @description
 * Calculates average OEE, MTtr, MTbf, Energy Consumption, Power Consumption, Cost of Running
 * and stoppages for 24hr, 7 days, 30 days and 1 year
 * @param {Object} value
 * @returns {Promise<Object>}
 *
 * @requires Devices/common
 */

const { isNil, isNumber, isString, Context, Property } = Device.common();

/**
 * @param {{ value: number, unit: string}} x
 * @returns {boolean}
 */
const validateCostOfkWhType = (x) => {
  if (isNil(x)) return false;

  if (!isNumber(x.value) || !isString(x.unit)) return false;

  return true;
};

/**
 * @desc Default value of "costOfkWh"
 * @type {{ value: number, unit: string }}
 */
const COST_OF_KWH = {
  value: 0.0,
  unit: '',
};

/**
 * @param {any} periods
 * @param {any} nbrOfDays
 * @param {any} quality
 * @param {any} perf
 * @returns {Object}
 */
function calc(periods, nbrOfDays, quality, perf) {
  let unplannedStops = 0;
  let plannedStops = 0;
  let idleRunningDur = 0;
  let loadRunningDur = 0;
  let unplannedDur = 0;

  let offset = Math.max(periods.length - nbrOfDays, 0);

  for (let i = 0; i + offset < periods.length; i++) {
    let p = periods[i + offset];
    // do not count overlapping states twice
    // except the very first one
    unplannedStops +=
      i == 0 ? Math.ceil(p.unplannedStops) : Math.floor(p.unplannedStops);
    plannedStops +=
      i == 0 ? Math.ceil(p.plannedStops) : Math.floor(p.plannedStops);
    idleRunningDur += p.idleRunningDur;
    loadRunningDur += p.loadRunningDur;
    unplannedDur += p.unplannedDur;
  }

  let Lt = idleRunningDur + loadRunningDur + unplannedDur;
  let Wt = idleRunningDur + loadRunningDur;

  return {
    OEE: Math.min(100, (Wt / Lt) * quality * perf * 100),
    Availability: Math.min(100, (Wt / Lt) * 100),
    MTbf: unplannedStops == 0 ? NaN : Lt / unplannedStops,
    MTtr: unplannedStops == 0 ? NaN : unplannedDur / unplannedStops,
    idleRunningDur: idleRunningDur,
    loadRunningDur: loadRunningDur,
    unplannedStops: unplannedStops,
    plannedStops: plannedStops,
  };
}

/**
 * @async
 * @param {Object} context
 * @returns {Object}
 */
async function main(context) {
  const ENERGY_CONSUMPTION_CONSTANT = 10.0 * 1.2;
  const ENERGY_IDLE_CONSUMPTION_RATIO = 0.27;

  const IDLE_PWR_MULTIPLIER =
    ENERGY_CONSUMPTION_CONSTANT * ENERGY_IDLE_CONSUMPTION_RATIO;
  const LOAD_PWR_MULTIPLIER = ENERGY_CONSUMPTION_CONSTANT;

  let p24hr = calc(context.periods, 1, 1, 1);
  let p7days = calc(context.periods, 7, 1, 1);
  let p30days = calc(context.periods, 30, 1, 1);
  let p1year = calc(context.periods, 365, 1, 1);

  context[Context.OEE] = {
    performance: [100, 100, 100, 100],
    quality: [100, 100, 100, 100],
    availability: [
      p24hr.Availability,
      p7days.Availability,
      p30days.Availability,
      p1year.Availability,
    ],
    average: [p24hr.OEE, p7days.OEE, p30days.OEE, p1year.OEE],
    unit: '%',
  };

  context[Context.MTBF] = {
    average: [p24hr.MTbf, p7days.MTbf, p30days.MTbf, p1year.MTbf],
    unit: 'h',
  };

  context[Context.MTTR] = {
    average: [p24hr.MTtr, p7days.MTtr, p30days.MTtr, p1year.MTtr],
    unit: 'h',
  };

  context[Context.ENERGY] = {
    total: [
      p24hr.loadRunningDur * LOAD_PWR_MULTIPLIER +
        p24hr.idleRunningDur * IDLE_PWR_MULTIPLIER,
      p7days.loadRunningDur * LOAD_PWR_MULTIPLIER +
        p7days.idleRunningDur * IDLE_PWR_MULTIPLIER,
      p30days.loadRunningDur * LOAD_PWR_MULTIPLIER +
        p30days.idleRunningDur * IDLE_PWR_MULTIPLIER,
      p1year.loadRunningDur * LOAD_PWR_MULTIPLIER +
        p1year.idleRunningDur * IDLE_PWR_MULTIPLIER,
    ],
    unit: 'kWh',
  };

  context[Context.POWER] = {
    average: [
      (p24hr.loadRunningDur * LOAD_PWR_MULTIPLIER +
        p24hr.idleRunningDur * IDLE_PWR_MULTIPLIER) /
        (p24hr.loadRunningDur + p24hr.idleRunningDur),
      (p7days.loadRunningDur * LOAD_PWR_MULTIPLIER +
        p7days.idleRunningDur * IDLE_PWR_MULTIPLIER) /
        (p7days.loadRunningDur + p7days.idleRunningDur),
      (p30days.loadRunningDur * LOAD_PWR_MULTIPLIER +
        p30days.idleRunningDur * IDLE_PWR_MULTIPLIER) /
        (p30days.loadRunningDur + p30days.idleRunningDur),
      (p1year.loadRunningDur * LOAD_PWR_MULTIPLIER +
        p1year.idleRunningDur * IDLE_PWR_MULTIPLIER) /
        (p1year.loadRunningDur + p1year.idleRunningDur),
    ],
    unit: 'kW',
  };

  const costOfkWh = validateCostOfkWhType(value[Context.COST_OF_KWH])
    ? value[Context.COST_OF_KWH]
    : COST_OF_KWH;

  context[Context.COST_OF_RUNNING] = {
    total: context[Context.ENERGY].total.map((i) => i * costOfkWh.value),
    unit: costOfkWh.unit,
  };

  const powercutCounts = await Device.queryAggregates({
    pname: Property.POWERCUT_STOPS,
    agg: 'count',
  });

  context[Context.STOPPAGES] = {
    planned: [
      p24hr.plannedStops,
      p7days.plannedStops,
      p30days.plannedStops,
      p1year.plannedStops,
    ],
    unplanned: [
      p24hr.unplannedStops,
      p7days.unplannedStops,
      p30days.unplannedStops,
      p1year.unplannedStops,
    ],
    powercut: powercutCounts.map((i) => i || 0),
  };

  return context;
}

return main(value);
"""

#
#
#
def showOEE_body():
    return """/**
* Enter number of days to display OEE for each day and the aggregated OEE
*/    
Array.prototype.insert = function ( index, item ) {
    this.split( index, 0, item );
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
def getConnectivity_body():
    return """/**
 * @namespace BaseLogikaProfile
 *
 * @private
 * @async
 * @function getLatestValues
 * @memberof BaseLogikaProfile
 * @returns {Promise<string>}
 *
 * @requires Device/common
 */

const { getPropertyValue, Property } = Device.common();

/** @enum {string} */
const Connectivity = {
  OFFLINE: 'offline',
  ONLINE_ACTIVE: 'online-active',
  ONLINE_INACTIVE: 'online-inactive',
};

/** @enum {string} */
const Connection = {
  ONLINE: 'online',
  OFFLINE: 'offline',
};

/** @enum {string} */
const Activity = {
  ACTIVE: 'active',
  INACTIVE: 'inactive',
};

/** @type {string} */
const EMPTY_VALUE = '—';

/**
 * @param {Object} params
 * @param {string} params.connection
 * @param {string} params.activity
 * @returns {string}
 */
function getConnectivity({ connection, activity }) {
  if (connection === Connection.ONLINE && activity === Activity.ACTIVE) {
    return Connectivity.ONLINE_ACTIVE;
  } else if (connection === Connection.ONLINE) {
    return Connectivity.ONLINE_INACTIVE;
  }

  return Connectivity.OFFLINE;
}

/**
 * @async
 * @returns {Promise<string>}
 */
async function main() {
  const requests = [
    getPropertyValue(Property.CONNECTION_STATUS, EMPTY_VALUE),
    getPropertyValue(Property.ACTIVE, EMPTY_VALUE),
  ];

  const [connection, active] = await Promise.all(requests);

  return getConnectivity({ connection, activity: active });
}

return main();
"""

def getActiveAlarm_body():
  return """/**
 * @namespace BaseLogikaProfile
 *
 * @private
 * @function getActiveAlarm
 * @returns {Object|void}
 *
 * @requires Device/common
 */

const { getPropertyValue, Property } = Device.common();

/** @type {Object} */
const DEFAULT_PROPERTY_VALUE = {};

/**
 * @async
 * @returns {Object|void}
 */
async function main() {
  const { items: [activeAlarm] = [] } = await getPropertyValue(
    Property.ACTIVE_ALARMS,
    DEFAULT_PROPERTY_VALUE,
  );

  return activeAlarm;
}

return main();
"""