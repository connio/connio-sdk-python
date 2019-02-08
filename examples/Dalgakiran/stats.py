

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