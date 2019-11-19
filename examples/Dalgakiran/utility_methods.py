# -*- coding: utf-8 -*-
# ~~ Utility/Helper methods ~~
#
# common
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
def common_body():
    return """/** @type {Object.<string, string|number>} */
const DEFAULT_MAINTENANCE_COST_LIST = {
  unit: 'USD',
  airFilterChange: 0.0,
  oilChange: 0.0,
  compressorCheck: 0.0,
  oilFilterChange: 0.0,
  separatorFilterChange: 0.0,
  bearingLubrication: 0.0,
};

/** @type {string} */
const Aggregator = {
  SUM: 'sum',
};

/** @type {string} */
const Connectivity = {
  OFFLINE: 'offline',
  ONLINE_ACTIVE: 'online-active',
  ONLINE_INACTIVE: 'online-inactive',
};

/** @enum {string} */
const Property = {
  ACTIVE_ALARMS: 'activeAlarms',
  ACTIVE: 'active',
  COMPRESSOR_STATE: 'compressorState',
  CONNECTION_STATUS: 'connectionStatus',
  DRIVE: 'driveMeasures',
  ICON: 'icon',
  LAST_ALARMS: 'lastAlarms',
  LAST_WARNINGS: 'lastWarnings',
  LOGIKA_FIRMWARE_VERSION: 'cfgLogikaFwVersion',
  LOGIKA_MODEL: 'cfgLogikaModel',
  MAINTENANCE_COST_LIST: 'maintenanceCostList',
  MAINTENANCE_COUNTERS: 'maintCounters',
  MAINTENANCE_CYCLES: 'cfgMaintCycles',
  MODBUS_SETTINGS: 'modbus_settings',
  MOTOR_CURRENT: 'motorCurrent',
  MOTOR_FREQUENCY: 'motorFrequency',
  MOTOR_SPEED: 'motorSpeed',
  NBR_OF_ALARMS: 'nbrOfAlarms',
  NBR_OF_WARNINGS: 'nbrOfWarnings',
  POWERCUT_STOPS: 'powercutStops',
  PRESSURE: 'workingPressure',
  SERIAL_NUMBER: 'cfgSerialNumber',
  STATE: 'state',
  TEMPERATURE: 'screwTemperature',
  WARRANTY_END_DATE: 'warrantyExpiryDate',
  WARRANTY_EXPIRY_DATE: 'warrantyExpiryDate',
};

/** @enum {string} */
const Context = {
  COST_OF_KWH: 'costOfkWh',
  COST_OF_RUNNING: 'costOfRunning',
  ENERGY: 'energy',
  MAINTENANCE: 'maintenance',
  MTBF: 'mtbf',
  MTTR: 'mttr',
  OEE: 'oee',
  POWER: 'power',
  STOPPAGES: 'stoppages',
};

/**
 * {@link https://github.com/lodash/lodash/blob/4.17.10/lodash.js#L11972 Lodash#isNil}
 * @param {any} x
 * @returns {boolean}
 */
const isNil = (x) => x == null;

/**
 * @param {any} x
 * @returns {boolean}
 */
const isNull = (x) => x === null;

/**
 * @param {*} x
 * @returns {boolean}
 */
const isNumber = (x) => typeof x === 'number';

/**
 * @param {*} x
 * @returns {boolean}
 */
const isString = (x) => typeof x === 'string';

/**
 * @param {string} name
 * @param {any} [defaultValue]
 * @return {Promise<any>}
 */
async function getPropertyValue(name, defaultValue) {
  const { value = defaultValue } = await Device.api.getProperty(name);

  return isNull(value) ? defaultValue : value;
}

/**
 * @param {string} x
 * @returns {boolean}
 */
const checkIsOffline = (x) => x === Connectivity.OFFLINE;

/**
 * @param {any} [x]
 * @param {any} [defaultValue]
 * @returns {any}
 */
function withDefaultValue(x, defaultValue) {
  if (isNil(x)) {
    return defaultValue;
  }

  return x;
}

return {
  DEFAULT_MAINTENANCE_COST_LIST,

  Aggregator,
  Connectivity,
  Context,
  Property,

  checkIsOffline,
  getPropertyValue,
  isNil,
  isNull,
  isNumber,
  isString,
  withDefaultValue,
};
"""

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
 * @namespace BaseLogikaProfile
 *
 * @public
 * @function init
 * @memberof BaseLogikaProfile
 * @desc Initialize device `state` property with default values
 * @param {Object} value
 * @param {boolean} value.hasInverter
 * @param {number} value.warrantyInMonth
 * @param {string} value.icon
 * @param {{ value: number, unit: string }} value.elecCost
 * @returns
 *
 * @requires Device/common
 *
 * @example value
 * {
 *   "hasInverter": true,
 *   "warrantyInMonth": 12,
 *   "icon": "inversys-15-plus-depolu.png",
 *   "elecCost": {
 *     "value": 0,  // cost of electricity KWh
 *     "unit": "USD"
 *   }
 * }
 */

const { Property, DEFAULT_MAINTENANCE_COST_LIST } = Device.common();

/** @type {string} */
const DEFAULT_ICON = 'dk-default.png';

/** @type {number} */
const DEFAULT_WARRANTY_IN_MONTH = 12;

/** @type {{ value: number, unit: string }} */
const DEFAULT_ELECTRICITY_COST = {
  value: 0,
  unit: 'USD',
};

let warrantyInMonth = void 0;
let hasInverter = void 0;
let elecCost = void 0;

({ hasInverter, warrantyInMonth, elecCost } = value);

const modbusSettings = Device.fetchModbusSettings(hasInverter);

const state = Object.assign(
  Device.getEmptyState(elecCost || DEFAULT_ELECTRICITY_COST),
  {
    hasInverter: !!hasInverter,
  },
);

const now = new Date();
const nowISO = now.toISOString();
const warrantyExpiry = new Date(
  now.setMonth(now.getMonth() + (warrantyInMonth || DEFAULT_WARRANTY_IN_MONTH)),
);

Device.api
  .setProperty(Property.MODBUS_SETTINGS, {
    value: modbusSettings,
    time: nowISO,
  })
  .then(() =>
    Device.api.setProperty(Property.ICON, {
      value: value.icon || DEFAULT_ICON,
      time: nowISO,
    }),
  )
  .then(() =>
    Device.api.setProperty(Property.WARRANTY_EXPIRY_DATE, {
      value: warrantyExpiry.toISOString(),
      time: nowISO,
    }),
  )
  .then(() =>
    Device.api.setProperty(Property.MAINTENANCE_COST_LIST, {
      value: DEFAULT_MAINTENANCE_COST_LIST,
      time: nowISO,
    }),
  )
  .then(Device.getCompressorInfo)
  .then((compressorInfo) => {
    /** @desc Merge device info into state  */
    Object.assign(state, compressorInfo);

    return Device.api.setProperty(Property.STATE, {
      value: state,
      time: nowISO,
    });
  })
  .then((property) => done(null, property.value));
"""

#
#
#
def getEmptyState_body():
    return """/**
 * @namespace BaseLogikaProfile
 *
 * @protected
 * @function getEmptyState
 * @memberof BaseLogikaProfile
 * @desc Creates an empty state for this device
 * @param {{ value: number, unit: string }} value cost of electricity KWh
 * @returns {Object}
 */

/** @type {number[]} */
const DEFAULT_ARRAY = [0, 0, 0, 0];

/** @type {number} */
const DEFAULT_VALUE = 0;

/** @enum {string} */
const PropertyUnit = {
  COST_OF_RUNNING: 'USD',
  ENERGY: 'kWh',
  LOAD_RATIO: '%',
  MOTOR_CURRENT: 'A',
  MOTOR_FREQUENCY: 'Hz',
  MOTOR_SPEED: 'RPM',
  MTBF: 'h',
  MTTR: 'h',
  OEE: '%',
  POWER: 'kW',
  PRESSURE: 'bar',
  TEMPERATURE: '°C',
};

/** @enum {string} */
const Maintenance = {
  AIR_FILTER_CHANGE: 'Air Filter Change',
  BEARING_LUBRICATION: 'Bearing Lubrication',
  COMPRESSOR_CHECK: 'Compressor Check',
  OIL_CHANGE: 'Oil Change',
  OIL_FILTER_CHANGE: 'Oil Filter Change',
  SEPERATOR_FILTER_CHANGE: 'Seperator Filter Change',
};

/**
 * @param {string} unit
 * @returns {{ current: number, unit: string, average: number[] }}
 */
function makeEmptyProperty(unit) {
  return {
    current: DEFAULT_VALUE,
    unit,
    average: DEFAULT_ARRAY,
  };
}

/**
 * @param {string} unit
 * @returns {{ unit: string, average: number[] }}
 */
function makeEmptyAverageProperty(unit) {
  return {
    unit,
    average: DEFAULT_ARRAY,
  };
}

/**
 * @param {string} unit
 * @returns {{ unit: string, total: number[] }}
 */
function makeEmptyTotalProperty(unit) {
  return {
    unit,
    total: DEFAULT_ARRAY,
  };
}

/**
 * @returns {{ last: Array, asOf: string, total: number[] }}
 */
function makeEmptyTotal() {
  return {
    last: [],
    asOf: '2019-01-01T00:00:00Z',
    total: DEFAULT_ARRAY,
  };
}

/**
 * @returns {{ last: number, asOf: string, average: number[] }}
 */
function makeEmptyAverage() {
  return {
    last: DEFAULT_VALUE,
    asOf: '2019-01-01T00:00:00.000Z',
    average: DEFAULT_ARRAY,
  };
}

/**
 * @param {string} maintenance
 * @returns {{ maintenance: string, cost: number, hours: number, days: number }}
 */
function makeMaintenance(maintenance) {
  return {
    maintenance,
    cost: DEFAULT_VALUE,
    hours: DEFAULT_VALUE,
    days: DEFAULT_VALUE,
  };
}

return {
  costOfkWh: value,
  warnings: makeEmptyTotal(),
  alarms: makeEmptyTotal(),
  pressure: makeEmptyProperty(PropertyUnit.PRESSURE),
  temperature: makeEmptyProperty(PropertyUnit.TEMPERATURE),
  maintenance: {
    upcoming: [
      makeMaintenance(Maintenance.BEARING_LUBRICATION),
      makeMaintenance(Maintenance.AIR_FILTER_CHANGE),
      makeMaintenance(Maintenance.OIL_FILTER_CHANGE),
      makeMaintenance(Maintenance.OIL_CHANGE),
      makeMaintenance(Maintenance.SEPERATOR_FILTER_CHANGE),
      makeMaintenance(Maintenance.COMPRESSOR_CHECK),
    ],
  },
  stoppages: {
    planned: DEFAULT_ARRAY,
    unplanned: DEFAULT_ARRAY,
    powercut: DEFAULT_ARRAY,
  },
  loadRatio: makeEmptyProperty(PropertyUnit.LOAD_RATIO),
  energy: makeEmptyTotalProperty(PropertyUnit.ENERGY),
  unplannedStoppageHours: DEFAULT_ARRAY,
  loadRunningHours: DEFAULT_ARRAY,
  power: makeEmptyAverageProperty(PropertyUnit.POWER),
  costOfRunning: makeEmptyTotalProperty(PropertyUnit.COST_OF_RUNNING),
  idleRunningHours: DEFAULT_ARRAY,
  plannedStoppageHours: DEFAULT_ARRAY,
  unplannedStoppageHours: DEFAULT_ARRAY,
  loadRunningHours: DEFAULT_ARRAY,
  totalHours: makeEmptyAverage(),
  totalLoadHours: makeEmptyAverage(),
  oee: {
    availability: DEFAULT_ARRAY,
    performance: DEFAULT_ARRAY,
    quality: DEFAULT_ARRAY,
    average: DEFAULT_ARRAY,
    unit: PropertyUnit.OEE,
  },
  mtbf: makeEmptyAverageProperty(PropertyUnit.MTBF),
  mttr: makeEmptyAverageProperty(PropertyUnit.MTTR),
  hasInverter: false,
  status: {
    code: 0,
    label: '',
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
 * @namespace BaseLogikaProfile
 *
 * @public
 * @async
 * @function getCompressorInfo
 * @memberof BaseLogikaProfile
 * @desc Build a view of compressor details
 * @param {number} value Warranty period
 * @returns {Promise<Object>}
 *
 * @requires Device/common
 */

const { getPropertyValue, Property } = Device.common();

/** @type {number} */
const WARRANTY_PERIOD = 60;

/** @type {string} */
const EMPTY_VALUE = '—';

/** @type {{ code: number }} */
const EMPTY_STATUS = { code: 0, label: '' };

/**
 * @param {Date} date1
 * @param {Date} date2
 * @returns {number}
 */
function calcDateDiff(date1, date2) {
  const diff = Math.floor(date1.getTime() - date2.getTime());
  const day = 1000 * 60 * 60 * 24;

  const days = Math.floor(diff / day);
  const months = Math.floor(days / 31);
  const years = Math.floor(months / 12);

  return months;
}

/**
 * @param {number} warrantyPeriod
 * @returns {{ endsInMonths: number, periodInMonths: number }}
 */
async function getWarranty(warrantyPeriod) {
  const now = new Date();

  const defaultWarrantyExpiry = new Date(
    now.setMonth(now.getMonth() + warrantyPeriod),
  );

  const warrantyExpiry = await Device.api
    .getProperty(Property.WARRANTY_END_DATE)
    .then((p) =>
      p.value ? Date.parse(p.value) : defaultWarrantyExpiry.toISOString(),
    );

  let timeToWarranty = calcDateDiff(new Date(warrantyExpiry), new Date());

  /** @desc In case that we use a counter to decrement the warranty time */
  if (timeToWarranty < 0) {
    timeToWarranty = 0;
  }

  return {
    endsInMonths: timeToWarranty,
    periodInMonths: warrantyPeriod,
  };
}

/**
 * @async
 * @param {number} warrantyPeriod
 * @returns {Promise<Object>}
 */
async function main(warrantyPeriod = WARRANTY_PERIOD) {
  if (!Device.customIds || (Device.customIds && !Device.customIds.sn)) {
    const sn = await getPropertyValue(Property.SERIAL_NUMBER, EMPTY_VALUE);

    Device.customIds = {
      ...Device.customIds,
      sn,
    };
  }

  const [
    logikaModel,
    logikaRelease,
    status,
    icon,
    warranty,
    connectivity,
  ] = await Promise.all([
    getPropertyValue(Property.LOGIKA_MODEL, EMPTY_VALUE),
    getPropertyValue(Property.LOGIKA_FIRMWARE_VERSION, EMPTY_VALUE),
    getPropertyValue(Property.COMPRESSOR_STATE, EMPTY_STATUS),
    getPropertyValue(Property.ICON),
    getWarranty(warrantyPeriod),
    Device.getConnectivity(),
  ]);

  return {
    id: Device.id,
    name: Device.name,
    friendlyName: Device.friendlyName,
    customIds: Device.customIds,
    connectivity,
    icon,
    logikaModel,
    logikaRelease,
    status,
    warranty,
  };
}

return main(value);
"""

#
#
#
def getDashboard_body():
    return """/**
 * @namespace BaseLogikaProfile
 *
 * @public
 * @function getDashboard
 * @description
 * Build the default dashboard view of the compressor.
 * Some information must be populated by calling `preaggregate()` method ahead of time.
 * @param {{ unit: string, value: number }} value costOfkWh
 * @returns {void}
 *
 * @requires Device/common
 */

const {
  checkIsOffline,
  getPropertyValue,
  Property,
  withDefaultValue,
} = Device.common();

/** @type {number} */
const DEFAULT_PROPERTY_VALUE = 0;

/**
 *
 * @param {Object} params
 * @param {any} [params.value]
 * @param {Object} [params.meta={}]
 * @param {{ unit?: { symbol?: string }}} [params.meta.measurement]
 * @param {{ min?: number, max?: number }} [params.meta.boundaries]
 * @returns {{ value: number, unit: string, range: { min: number, max: number }}}
 */
function makeUIProperty({ value, meta: { measurement, boundaries } = {} }) {
  const _value = withDefaultValue(value, DEFAULT_PROPERTY_VALUE);

  const unit = measurement && measurement.unit && measurement.unit.symbol;

  const range = boundaries && {
    min: (boundaries && boundaries.min) || 0,
    max: (boundaries && boundaries.max) || 100,
  };

  return {
    current: _value,
    unit,
    range,
  };
}

/**
 * @async
 * @param {Object} context
 * @returns {Object}
 */
async function main(context) {
  Object.assign(context, {
    costOfkWh: value,
  });

  const requests = [
    Device.getCompressorInfo(),
    Device.getActiveAlarm(),
    Device.api.getProperty(Property.PRESSURE),
    Device.api.getProperty(Property.TEMPERATURE),
  ];

  if (context.hasInverter) {
    requests.push(
      Device.api.getProperty(Property.DRIVE),
      Device.api.getProperty(Property.MOTOR_SPEED),
      Device.api.getProperty(Property.MOTOR_FREQUENCY),
      Device.api.getProperty(Property.MOTOR_CURRENT),
    );
  }

  const [
    compressorInfo,
    activeAlarm,
    pressure,
    temperature,

    drive,
    motorSpeed,
    motorFrequency,
    motorCurrent,
  ] = await Promise.all(requests);

  const isOffline = checkIsOffline(compressorInfo.connectivity);

  context.pressure = {
    ...context.pressure,
    ...makeUIProperty(pressure),
  };

  context.temperature = {
    ...context.temperature,
    ...makeUIProperty(temperature),
  };

  Object.assign(context, {
    ...compressorInfo,

    activeAlarm,

    /** @desc A leftover from `preaggregate → processCompressorStates` */
    periods: void 0,

    /** @desc Unused / deprecated fields */
    idleRunningHours: void 0,
    loadRunningHours: void 0,
    plannedStoppageHours: void 0,
    totalHours: void 0,
    totalLoadHours: void 0,
    unplannedStoppageHours: void 0,

    /**
     * @desc Reset current values for offline compressor
     */
    pressure: {
      ...context.pressure,
      current: isOffline ? DEFAULT_PROPERTY_VALUE : context.pressure.current,
    },
    temperature: {
      ...context.temperature,
      current: isOffline ? DEFAULT_PROPERTY_VALUE : context.temperature.current,
    },
  });

  /** @desc Inverter motor information */
  if (drive) {
    context.motorSpeed = {
      ...context.motorSpeed,
      ...makeUIProperty({
        value: drive.value && drive.value.rpm,
        ...motorSpeed,
      }),
    };

    context.motorFrequency = {
      ...context.motorFrequency,
      ...makeUIProperty({
        value: drive.value && drive.value.frequency,
        ...motorFrequency,
      }),
    };

    context.motorCurrent = {
      ...context.motorCurrent,
      ...makeUIProperty({
        value: drive.value && drive.value.current,
        ...motorCurrent,
      }),
    };

    Object.assign(context, {
      /** @desc Reset current values for offline compressor */
      motorSpeed: {
        ...context.motorSpeed,
        current: isOffline
          ? DEFAULT_PROPERTY_VALUE
          : context.motorSpeed.current,
      },
      motorFrequency: {
        ...context.motorFrequency,
        current: isOffline
          ? DEFAULT_PROPERTY_VALUE
          : context.motorFrequency.current,
      },
      motorCurrent: {
        ...context.motorCurrent,
        current: isOffline
          ? DEFAULT_PROPERTY_VALUE
          : context.motorCurrent.current,
      },
    });
  }

  return context;
}

Device.api
  .getProperty(Property.STATE)
  .then((property) => property.value || Device.getEmptyState(value))
  .then(main)
  .then(currencyAdapter)
  .then((context) => done(null, context));

/**
 * @param {Object} property
 * @param {string} currency
 * @returns {Object}
 */
function updateCurrency(property, currency) {
  return {
    ...property,
    unit: currency,
  };
}

/**
 * @param {Object} ctx context
 * @returns {Object} Context with unified currencies
 */
function currencyAdapter(ctx) {
  const { unit: currency } = ctx.costOfkWh;
  const _updateCurrency = (x) => updateCurrency(x, currency);

  return {
    ...ctx,
    costOfRunning: _updateCurrency(ctx.costOfRunning),
    maintenance: _updateCurrency(ctx.maintenance),
  };
}
"""

#
#
#
def getLatestValues_body():
    return """/**
 * @namespace BaseLogikaProfile
 *
 * @public
 * @async
 * @function getLatestValues
 * @memberof BaseLogikaProfile
 * @description
 * Returns the most recent values of compressor pressure and temperature.
 * @returns {void}
 *
 * @requires Device/common
 */

const { getPropertyValue, checkIsOffline, Property } = Device.common();

/** @type {number} */
const DEFAULT_PROPERTY_VALUE = 0;

/**
 *
 * @param {Object} params
 * @param {string} params.property
 * @param {any} params.defaultValue
 * @param {boolean} [params.isOffline=false]
 * @returns {Promise<any>}
 */
async function getLatestValue({ property, defaultValue, isOffline = false }) {
  if (isOffline) {
    return defaultValue;
  }

  const value = await getPropertyValue(property, defaultValue);

  return value;
}

(async function main() {
  const [state, connectivity] = await Promise.all([
    getPropertyValue(Property.STATE),
    Device.getConnectivity(),
  ]);

  const isOffline = checkIsOffline(connectivity);

  const requests = [
    getLatestValue({
      property: Property.PRESSURE,
      defaultValue: DEFAULT_PROPERTY_VALUE,
      isOffline,
    }),
    getLatestValue({
      property: Property.TEMPERATURE,
      defaultValue: DEFAULT_PROPERTY_VALUE,
      isOffline,
    }),
  ];

  /** @desc Get inverter info if compressor comes with inverter */
  if (state.hasInverter) {
    requests.push(
      getLatestValue({
        property: Property.DRIVE,
        defaultValue: {
          rpm: DEFAULT_PROPERTY_VALUE,
          frequency: DEFAULT_PROPERTY_VALUE,
          current: DEFAULT_PROPERTY_VALUE,
        },
        isOffline,
      }),
    );
  }

  const [pressure, temperature, driveMeasures] = await Promise.all(requests);

  const result = {
    pressure,
    temperature,
  };

  /** @desc Inverter motor information - if any */
  if (driveMeasures) {
    Object.assign(result, {
      motorSpeed: driveMeasures.rpm,
      motorFrequency: driveMeasures.frequency,
      motorCurrent: driveMeasures.current,
    });
  }

  return done(null, result);
})();
"""

#
#
#
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

#
#
#
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

#
#
#
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

#
#
#
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

#
#
#
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