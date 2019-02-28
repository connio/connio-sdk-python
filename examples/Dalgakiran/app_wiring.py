
# ~getDashboard()
# ~getElectricCostPerkWh()

#
#
#
def getDashboard_body():
    return """/**
  
*/
const extractResultField = ({ result }) => result;
const getDeviceDashboard = d => App.api.executeDeviceMethod(d, 'getDashboard', value);

const getDevices = async (devices) => {
    const requests = devices.map(getDeviceDashboard);
    const result = await Promise.all(requests);

    return result.map(extractResultField);
}

App.api.findDevices({})
  .then(getDevices)
  .then((devices) => { 
    const dashboard = {
      devices,
      totalAlarms: [100, 40, 100, 400],
      warnings: [ 8, 30, 60, 300 ],
      alarms: [ 2, 10, 40, 100 ],
      oee: [ 45, 44, 47, 87, 77, 76 ],
      energy: [ 383, 333, 343, 234, 577, 346 ],
      mtbf: [ 45, 44, 47, 87, 77, 76 ],
      mttr: [ 45, 44, 47, 87, 77, 76 ], 
      connectivity: { idle: 1, connected: 2, sendingData: 1 },
      status: { idle: 1, active: 1, maintenance: 1 }  
    };

    done(null, dashboard);
  })
  .catch(error => done(error, null));
"""

#
#
#
def getElectricCostPerkWh_body():
    return """/**
  
*/
(async function () {
    const ELECTRIC_COST_PER_KWH = 'electric_cost_per_kWh';
    const electric_cost_per_kWh = await App.api.getProperty(ELECTRIC_COST_PER_KWH);
    
    done(null, {
        unit: electric_cost_per_kWh.meta.measurement.unit.symbol,
        value: electric_cost_per_kWh.value || 0,
    });
})();
"""