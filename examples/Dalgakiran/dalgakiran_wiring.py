import os
import time

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir + '/../') 

from connio.rest import Client
from connio.rest.api.v3.account.propertyy import PropertyInstance
from connio.rest.api.v3.account.method import MethodInstance

from utility_methods import *
from set_methods import *
from readwrite_methods import *
from query_methods import *

import L9_wiring as L9c
import L26_wiring as L26c
import L33_wiring as L33c
import L200_wiring as L200c

from gateway_wiring import *
import app_wiring as app

 ######
#      #
 ######
def wireApp(client):
  # Create compressor app profile
  compressorManager = client.account.appprofiles.create(name='CompressorManager',
                                                friendly_name='Compressor Manager',
                                                description='Dalgakıran Compressor Management App',
                                                version='1.0',
                                                vendor_name='Dalgakıran'
                                              )

    #------ Add profile properties

  unit = PropertyInstance.MeasurementUnit('', 'TL')
  measurement = PropertyInstance.Measurement('currency', unit)    
  client.account.properties(compressorManager.id).create(name='electric_cost_per_kWh', data_type='number', access_type='public', publish_type='never', measurement=measurement)

  #------ Add profile methods

  client.account.methods(compressorManager.id).create(name='getDashboard', method_impl= MethodInstance.MethodImplementation(app.getDashboard_body()), access_type='public')
  client.account.methods(compressorManager.id).create(name='getElectricCostPerkWh', method_impl= MethodInstance.MethodImplementation(app.getElectricCostPerkWh_body()), access_type='public')

  # Create compressor app profile
  compressorManagerApp = client.account.apps.create(name='CompressorManager',
                                                friendly_name='Compressor Manager',
                                                profile='CompressorManager',
                                                tags=['icon:cogs:#0077c3']
                                              )

 ######
#      #
 ######
def wireGw(client, name="ModbusGateway", friendly="Generic Modbus Gateway"):
  # Create new Minova Gateway profile
  compressor = client.account.deviceprofiles.create(name=name, 
                                                friendly_name=friendly,
                                                base_profile='Gateway',
                                                description='Modbus gateway',
                                                tags=['gw'],
                                                device_class='gateway',
                                                product_name='MiTrack-Q',
                                                vendor_name='Minova'
                                              )

  #------ Add profile properties
  
  client.account.properties(compressor.id).create(name='gateway_info', data_type='object', access_type='protected', publish_type='never')
  client.account.properties(compressor.id).create(name='modbus_errors', data_type='string', access_type='protected', publish_type='never')
  client.account.properties(compressor.id).create(name='modbus_readrequest', data_type='string', access_type='public', publish_type='always')    
  client.account.properties(compressor.id).create(name='modbus_settings', data_type='string', access_type='public', publish_type='always')
  client.account.properties(compressor.id).create(name='modbus_writerequest', data_type='string', access_type='public', publish_type='always')
  
  #------ Add profile methods

  client.account.methods(compressor.id).create(name='readTagByPropKey', method_impl= MethodInstance.MethodImplementation(readTagByPropKey_body()), access_type='protected')
  client.account.methods(compressor.id).create(name='readTag', method_impl= MethodInstance.MethodImplementation(readTag_body()), access_type='protected')
  client.account.methods(compressor.id).create(name='writeAndReadTag', method_impl= MethodInstance.MethodImplementation(writeAndReadTag_body()), access_type='protected')
  client.account.methods(compressor.id).create(name='writeTag', method_impl= MethodInstance.MethodImplementation(writeTag_body()), access_type='protected')
  client.account.methods(compressor.id).create(name='restart', method_impl= MethodInstance.MethodImplementation(restart_body()), access_type='public')
  client.account.methods(compressor.id).create(name='setModbusSettings', method_impl= MethodInstance.MethodImplementation(setModbusSettings_body()), access_type='public')

 ######
#      #
 ######
def wireBase(client, name="BaseLogikaProfile", friendly="Logika Base", base='ModbusGateway'):
    # Create new Logika base profile
    compressor = client.account.deviceprofiles.create(name=name, 
                                                  friendly_name=friendly,
                                                  base_profile=base,
                                                  description='Logika controller base profile',
                                                  tags=['logika', 'base'],
                                                  device_class='controller',
                                                  product_name='LSeries',
                                                  vendor_name='Logika'
                                                )

    #------ Add base profile properties
    
    client.account.properties(compressor.id).create(name='tagValue', data_type='string', access_type='protected', publish_type='never')

    client.account.properties(compressor.id).create(name='cfgSerialNumber', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='cfgLogikaModel', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='cfgLogikaFwVersion', data_type='string', access_type='protected', publish_type='never')    
    client.account.properties(compressor.id).create(name='cfgLevel1Pwd', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='cfgLevel2Pwd', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='cfgLevel3Pwd', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='activeAlarms', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='activeAlarmsNonAck', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='controllerState', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='compressorState', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='blockingAlarm', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='relayOutputs', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='digitalInputs', data_type='string', access_type='protected', publish_type='never')
    unit = PropertyInstance.MeasurementUnit('Celsius', '°C')
    measurement = PropertyInstance.Measurement('temperature', unit)
    client.account.properties(compressor.id).create(name='screwTemperature', data_type='number', access_type='protected', publish_type='never', 
        description='Main Screw Temperature (°C * 10)', measurement=measurement, boundaries={'min': -10, 'max': 125})
    
    unit = PropertyInstance.MeasurementUnit('Bar', 'bar')
    measurement = PropertyInstance.Measurement('pressure', unit)
    client.account.properties(compressor.id).create(name='workingPressure', data_type='number', access_type='protected', publish_type='never', 
        description='Main Working Pressure (Bar * 10)', measurement=measurement, boundaries={'min': 0, 'max': 16})
    
    unit = PropertyInstance.MeasurementUnit('Volt', 'V')
    measurement = PropertyInstance.Measurement('electricity', unit)
    client.account.properties(compressor.id).create(name='controllerSupplyVoltage', data_type='number', access_type='protected', publish_type='never', 
        description='Main Screw Temperature (V * 10)', measurement=measurement, boundaries={'min': 0, 'max': 300})
    
    client.account.properties(compressor.id).create(name='cfgMaintCycles', data_type='object', access_type='protected', publish_type='never')
    
    unit = PropertyInstance.MeasurementUnit('Hour', 'h')
    measurement = PropertyInstance.Measurement('time', unit)    
    client.account.properties(compressor.id).create(name='totalHours', data_type='number', access_type='protected', publish_type='never', description='Total hours compressor was working', measurement=measurement)
    
    client.account.properties(compressor.id).create(name='totalLoadHours', data_type='number', access_type='protected', publish_type='never', 
        description='Total hours compressor was on load', measurement=measurement)
    client.account.properties(compressor.id).create(name='maintCounters', data_type='object', access_type='protected', publish_type='never', description='Time from the last maintenance in minutes')
    client.account.properties(compressor.id).create(name='maintenanceLog', data_type='object', access_type='protected', publish_type='never', description='Log of compressor maintenances')
    
    unit = PropertyInstance.MeasurementUnit('Percentage', '%')
    measurement = PropertyInstance.Measurement('percentage', unit)    
    client.account.properties(compressor.id).create(name='loadPercInLast100h', data_type='number', access_type='protected', publish_type='never', 
        description="On load minutes in last 100 hours of motor running (100% is 6000)", measurement=measurement, boundaries={'min': 0, 'max': 100})
    
    unit = PropertyInstance.MeasurementUnit('Count', '#')
    measurement = PropertyInstance.Measurement('custom', unit)
    client.account.properties(compressor.id).create(name='nbrOfStartsInLastHour', data_type='number', access_type='protected', publish_type='never', measurement=measurement)
    client.account.properties(compressor.id).create(name='controllerTime', data_type='string', access_type='protected', publish_type='never')
    
    # derived properties
    client.account.properties(compressor.id).create(name='lastAlarms', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='lastWarnings', data_type='object', access_type='protected', publish_type='never')
    unit = PropertyInstance.MeasurementUnit('Count', '#')
    measurement = PropertyInstance.Measurement('custom', unit)
    client.account.properties(compressor.id).create(name='nbrOfAlarms', data_type='number', access_type='protected', publish_type='never', measurement=measurement)
    client.account.properties(compressor.id).create(name='nbrOfWarnings', data_type='number', access_type='protected', publish_type='never', measurement=measurement)
    
    client.account.properties(compressor.id).create(name='powercutStops', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='plannedStops', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='unplannedStops', data_type='object', access_type='protected', publish_type='never')
    
    unit = PropertyInstance.MeasurementUnit('Minute', 'min')
    measurement = PropertyInstance.Measurement('time', unit)
    client.account.properties(compressor.id).create(name='idleRunningMinutes', data_type='number', access_type='protected', publish_type='never', measurement=measurement)
    client.account.properties(compressor.id).create(name='loadRunningMinutes', data_type='number', access_type='protected', publish_type='never', measurement=measurement)
    client.account.properties(compressor.id).create(name='unplannedStopsMinutes', data_type='number', access_type='protected', publish_type='never', measurement=measurement)
    client.account.properties(compressor.id).create(name='plannedStopsMinutes', data_type='number', access_type='protected', publish_type='never', measurement=measurement)

    # settings
    # unit = PropertyInstance.MeasurementUnit('Month', 'months')
    # measurement = PropertyInstance.Measurement('custom', unit)    
    # client.account.properties(compressor.id).create(name='warrantyExpiresIn', data_type='number', access_type='public', publish_type='never', measurement=measurement)

    client.account.properties(compressor.id).create(name='warrantyExpiryDate', data_type='string', access_type='public', publish_type='never')
    client.account.properties(compressor.id).create(name='icon', data_type='string', access_type='public', publish_type='never')
    
    # This can go to app maybe?
    description = """
Asagidaki sekilde bakim ucretlerini girebilirsiniz:
{
  "currencySymbol": "$",
  "currency": "USD",  
  "oilFilterChange": 0,
  "oilChange": 0,
  "bearingLubrication": 0,
  "compressorCheck": 0,
  "airFilterChange": 0,
  "separatorFilterChange": 0
}
"""
    client.account.properties(compressor.id).create(name='maintenanceCostList', data_type='object', access_type='public', publish_type='never', 
      description=description)

    # Views
    condition = PropertyInstance.Condition(when=PropertyInstance.Condition.ConditionType.ALWAYS)
    retention = PropertyInstance.Retention(type=PropertyInstance.Retention.RetentionType.MOSTRECENT, context=PropertyInstance.Context(type='default'), capacity='0', condition=condition)
    client.account.properties(compressor.id).create(name='state', data_type='object', access_type='protected', publish_type='never', retention=retention)
   
    #------ Add base profile methods
    
    client.account.methods(compressor.id).create(name='init', method_impl= MethodInstance.MethodImplementation(getInit_body()), access_type='public', description="""e.g. 
{ 
  "hasInverter": false, 
  "warrantyInMonth": 12,
  "icon": "inversys-15-plus-depolu.png",
  "elecCost": {
    "value": 0, 
    "unit": "USD"
  }
}
    
    hasInverter: kompresorun inverter'u varsa 'true' yoksa 'false' olmalidir - default deger 'false'
    warrantyInMonth: kompresorun garanti suresini belirtir - default deger 12
    icon: kompresor resim dosyasinin adi
    elecCost: kompresorun kullanildigi bolgedeki elektrik birim fiyati ve para birimi
    """)
    client.account.methods(compressor.id).create(name='getDashboard', method_impl= MethodInstance.MethodImplementation(getDashboard_body()), access_type='public', description="""
Build the default dashboard view of the compressor. Some information must be populated by calling `preaggregate()` method ahead of time.""")
    client.account.methods(compressor.id).create(name='getLatestValues', method_impl= MethodInstance.MethodImplementation(getLatestValues_body()), access_type='public')
    client.account.methods(compressor.id).create(name='preaggregate', method_impl= MethodInstance.MethodImplementation(preaggregate_body()), access_type='public')

    client.account.methods(compressor.id).create(name='showOEE', method_impl= MethodInstance.MethodImplementation(showOEE_body()), access_type='public')
    client.account.methods(compressor.id).create(name='getHistOEE', method_impl= MethodInstance.MethodImplementation(getHistOEE_body()), access_type='public', description="""{
 "value": {
  "from": { "unit": "WEEKS", "value":	1 }, 
  "sampling": { "unit": "HOURS", "value": 1 }
  }
}""")
    client.account.methods(compressor.id).create(name='getHistMttr', method_impl= MethodInstance.MethodImplementation(getHistMttr_body()), access_type='public', description="""{
 "value": {
  "from": { "unit": "WEEKS", "value":	1 }, 
  "sampling": { "unit": "HOURS", "value": 1 }
  }
}""")
    client.account.methods(compressor.id).create(name='getHistMtbf', method_impl= MethodInstance.MethodImplementation(getHistMtbf_body()), access_type='public', description="""{
 "value": {
  "from": { "unit": "WEEKS", "value":	1 }, 
  "sampling": { "unit": "HOURS", "value": 1 }
  }
}""")
    client.account.methods(compressor.id).create(name='getHistEstimPowerConsumption', method_impl= MethodInstance.MethodImplementation(getHistEstimPowerConsumption_body()), access_type='public', description="""{
 "value": {
  "from": { "unit": "WEEKS", "value":	1 }, 
  "sampling": { "unit": "HOURS", "value": 1 }
  }
}""")
    client.account.methods(compressor.id).create(name='getHistEstimEnergyConsumption', method_impl= MethodInstance.MethodImplementation(getHistEstimEnergyConsumption_body()), access_type='public', description="""{
 "value": {
  "from": { "unit": "WEEKS", "value":	1 }, 
  "sampling": { "unit": "HOURS", "value": 1 }
  }
}""")

    accessLevel1 = 'protected'
    accessLevel1_1 = 'private'

    client.account.methods(compressor.id).create(name='getEmptyState', method_impl= MethodInstance.MethodImplementation(getEmptyState_body()), access_type=accessLevel1, description="e.g. { 'value': 0, 'unit': '$' }")
    client.account.methods(compressor.id).create(name='getCompressorInfo', method_impl= MethodInstance.MethodImplementation(getCompressorInfo_body()), access_type=accessLevel1)
    
    # dashboarding
    client.account.methods(compressor.id).create(name='buildAggregateQueries', method_impl= MethodInstance.MethodImplementation(buildAggregateQueries_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='queryAggregates', method_impl= MethodInstance.MethodImplementation(queryAggregates_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='queryPropertySummary', method_impl= MethodInstance.MethodImplementation(queryPropertySummary_body()), access_type=accessLevel1)
    client.account.methods(compressor.id).create(name='queryWarningAlarmSummary', method_impl= MethodInstance.MethodImplementation(queryWarningAlarmSummary_body()), access_type=accessLevel1)
    client.account.methods(compressor.id).create(name='queryTimeToMaintenance', method_impl= MethodInstance.MethodImplementation(queryTimeToMaintenance_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='queryLoadRatio', method_impl= MethodInstance.MethodImplementation(queryLoadRatio_body()), access_type=accessLevel1_1)

    client.acocunt.methods(compressor.id).create(name='getActiveAlarm', method_impl= MethodInstance.MethodImplementation(getActiveAlarm_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='getConnectivity', method_impl= MethodInstance.MethodImplementation(getConnectivity_body()), access_type=accessLevel1_1, description="""
/** @enum {string} */
Connectivity = {
  OFFLINE: 'offline',
  ONLINE_ACTIVE: 'online-active',
  ONLINE_INACTIVE: 'online-inactive',
};""")
    client.account.methods(compressor.id).create(name='common', method_impl= MethodInstance.MethodImplementation(common_body()), access_type=accessLevel1_1, description="""
Common utils, constants, enums, etc""")

    client.account.methods(compressor.id).create(name='processCompressorStates', method_impl= MethodInstance.MethodImplementation(processCompressorStates_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='calculateAll', method_impl= MethodInstance.MethodImplementation(calculateAll_body()), access_type=accessLevel1_1)

    client.account.methods(compressor.id).create(name='convertToHours', method_impl= MethodInstance.MethodImplementation(convertToHours_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='convertToDec', method_impl= MethodInstance.MethodImplementation(convertToDec_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='makeWriteRequest', method_impl= MethodInstance.MethodImplementation(makeWriteRequest_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='makeWriteValue', method_impl= MethodInstance.MethodImplementation(makeWriteValue_body()), access_type=accessLevel1_1)

    client.account.methods(compressor.id).create(name='setAny', method_impl= MethodInstance.MethodImplementation(setAny_body()), access_type=accessLevel1_1)

    client.account.methods(compressor.id).create(name='setSerialNumber', method_impl= MethodInstance.MethodImplementation(setSerialNumber_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setLogikaModel', method_impl= MethodInstance.MethodImplementation(setLogikaModel_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setLogikaFwVersion', method_impl= MethodInstance.MethodImplementation(setLogikaFwVersion_body()), access_type=accessLevel1_1)
    
    client.account.methods(compressor.id).create(name='setLevel1Pwd', method_impl= MethodInstance.MethodImplementation(setLevelXPwd_body(1)), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setLevel2Pwd', method_impl= MethodInstance.MethodImplementation(setLevelXPwd_body(2)), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setLevel3Pwd', method_impl= MethodInstance.MethodImplementation(setLevelXPwd_body(3)), access_type=accessLevel1_1)

    client.account.methods(compressor.id).create(name='setAlarms', method_impl= MethodInstance.MethodImplementation(setAlarms_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setNonAckAlarms', method_impl= MethodInstance.MethodImplementation(setNonAckAlarms_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setControllerState', method_impl= MethodInstance.MethodImplementation(setControllerState_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setCompressorState', method_impl= MethodInstance.MethodImplementation(setCompressorState_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setBlockingAlarm', method_impl= MethodInstance.MethodImplementation(setBlockingAlarm_body()), access_type=accessLevel1_1)

    client.account.methods(compressor.id).create(name='setScrewTemperature', method_impl= MethodInstance.MethodImplementation(setScrewTemperature_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setWorkingPressure', method_impl= MethodInstance.MethodImplementation(setWorkingPressure_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setControllerSupplyVoltage', method_impl= MethodInstance.MethodImplementation(setControllerSupplyVoltage_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setMaintCycles', method_impl= MethodInstance.MethodImplementation(setMaintCycles_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setTotalHours', method_impl= MethodInstance.MethodImplementation(setTotalHours_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setTotalLoadHours', method_impl= MethodInstance.MethodImplementation(setTotalLoadHours_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setMaintCounters', method_impl= MethodInstance.MethodImplementation(setMaintCounters_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setLoadPercInLast100h', method_impl= MethodInstance.MethodImplementation(setLoadPercInLast100h_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setNbrOfStartsInLastHour', method_impl= MethodInstance.MethodImplementation(setNbrOfStartsInLastHour_body()), access_type=accessLevel1_1)
    client.account.methods(compressor.id).create(name='setControllerTime', method_impl= MethodInstance.MethodImplementation(setControllerTime_body()), access_type=accessLevel1_1)

    accessLevel2 = 'public'

    client.account.methods(compressor.id).create(name='sendCommand', method_impl= MethodInstance.MethodImplementation(sendCommand_body()), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='start', method_impl= MethodInstance.MethodImplementation(startStop_body(1)), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='stop', method_impl= MethodInstance.MethodImplementation(startStop_body(0)), access_type=accessLevel2)

    client.account.methods(compressor.id).create(name='writeAnyTag', method_impl= MethodInstance.MethodImplementation(writeAnyTag_body()), access_type=accessLevel2, description="""
Bu method ile herhangi bir tag'i yazabilirsiniz. Gereken parametreler sunlar:

- setValue: Yazilacak deger
- addr: Tag'in modbus adresi
- size: Yazilacak tag'in uzunlugu - default 2 (word)

Ornegin:

{ "setValue": 13, "addr": "0x401", "size": 2 } 
""")
    client.account.methods(compressor.id).create(name='readAnyTag', method_impl= MethodInstance.MethodImplementation(readAnyTag_body()), access_type=accessLevel2, description="""
 Bu method ile herhangi bir tag'i okumak icin gateway'e komut gonderebilirsiniz. Okunan deger tagValue isimli property icine yailir. 
 Gereken parametreler sunlar:

- addr: Tag'in modbus adresi
- size: Okunacak tag'in uzunlugu - default 2 (word)

Ornegin:

{ "addr": "0x401", "size": 2 } 
""")

    client.account.methods(compressor.id).create(name='readSerialNumber', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('cfgSerialNumber')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readLogikaModel', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('cfgLogikaModel')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readLogikaFwVersion', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('cfgLogikaFwVersion')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readLevel1Pwd', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('cfgLevel1Pwd')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readLevel2Pwd', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('cfgLevel2Pwd')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readLevel3Pwd', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('cfgLevel3Pwd')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readRelayOutputs', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('relayOutputs')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readDigitalInputs', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('digitalInputs')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readMaintCycles', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('cfgMaintCycles')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readMaintCounters', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('maintCounters')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readTotalHours', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('totalHours')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readTotalLoadHours', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('totalLoadHours')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readLoadPercInLast100h', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('loadPercInLast100h')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readNbrOfStartsInLastHour', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('nbrOfStartsInLastHour')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='readControllerTime', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('controllerTime')), access_type=accessLevel2)

    client.account.methods(compressor.id).create(name='writeChangeAirFilter', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('writeChangeAirFilter_body')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='writeChangeOilFilter', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('writeChangeOilFilter_body')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='writeChangeOil', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('writeChangeOil_body')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='writeChangeSeperatorFilter', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('writeChangeSeperatorFilter_body')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='writeCheckCompressor', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('writeCheckCompressor_body')), access_type=accessLevel2)
    client.account.methods(compressor.id).create(name='writeBearingLubrication', method_impl= MethodInstance.MethodImplementation(readTagIntoProperty_body('writeBearingLubrication_body')), access_type=accessLevel2)


def wire(keyID, keySecret):
    start = time.time()

    client = Client(username=keyID, 
                    password=keySecret)

    # Get master account details
    # master = client.accounts.get().fetch()    
    # print('Master account: ' + master.name)

    print('Creating the system.....')

    wireApp(client)
    wireGw(client)
    wireBase(client)
    
    # Wire different controller types
    L9c.wire(client)
    L26c.wire(client)
    L33c.wire(client)
    # L200c.wire(client)

    # wireGw(client, 'ModbusGatewayXX', 'Modbus Gateway XX')
    # wireBase(client, 'BaseLogikaProfileXX', 'Logika Base XX', 'ModbusGatewayXX')
    # L9c.wire(client, 'LogikaL9XX', 'Logika L9 XX', 'BaseLogikaProfileXX')
    # L26c.wire(client, 'LogikaL26XX', 'Logika L26 XX', 'BaseLogikaProfileXX')
    # L33c.wire(client, 'LogikaL33XX', 'Logika L33 XX', 'BaseLogikaProfileXX')

    print('System is created successfully in %.2f seconds' % (time.time() - start))

if __name__ == '__main__':

    # DK
    # keyID = os.environ.get('DK_ACCOUNT_KEYID', '_key_597863750116322358') 
    # keySecret = os.environ.get('DK_ACCOUNT_KEYSECRET', '3de1070b75f945c5a2406557ea29affc')

    #Sub account 1
    # keyID = os.environ.get('DK_ACCOUNT_KEYID', '_key_591833232575364370')
    # keySecret = os.environ.get('DK_ACCOUNT_KEYSECRET', 'dafaeeb4b14a41ecbe438b29d9d93b2e')

    # DEMO ICIN
    keyID = os.environ.get('DK_ACCOUNT_KEYID', '_key_642643305188058986')
    keySecret = os.environ.get('DK_ACCOUNT_KEYSECRET', '747f95c9b6a54e7d91811f810436a01e')

    if len(sys.argv) == 3:
        keyID = sys.argv[1]
        keySecret = sys.argv[2]

    wire(keyID, keySecret)



#DK TEST 1
#  IMEI: 869867035753377

#test26s
#  IMEI: 869867036043836
#  frecon-5-plus-depolu

#DK TEST 3
#  MAC: 00:1e:c0:91:97:f3

#L33S TEST
#  MAC: 00:1e:c0:91:aa:b2

#test33
#  SN: 987654321

# ---

# Some sample device info
#Mac 16:b4:12:7d:5d:da

# IMEI: 869867036043836
# IMEI: 869867035753377
# MAC 00:1e:c0:91:97:f3

#Device IMEI: 861359035276375
#Device name: DK.Test.Cihaz.1
#Device friendly name: DK Test 1 [GSM]
#Description: >FTPUPDATE,0001,IP=107.170.178.138;PORT=21;APN=internet;USER=mitrackftp;PASS=mitrack2017;PATH=/files/;FILE=MITRACK_Q_DAL.bin;

#Device IMEI: 869867035753377
#Device name: DK.Test.Cihaz.2
#Device friendly name: DK Test 2 [ETHER]

#Device MAC:  00:1e:c0:91:8c:8f
#Device name: DK.Test.Cihaz.3
#Device friendly name: DK Test 3 [ETHER]
# 40.36666, 49.83518

#Device SN:  SN-001-001
#Device name: DK.Cihaz.Simul
#Device friendly name: DK Cihaz Simul
