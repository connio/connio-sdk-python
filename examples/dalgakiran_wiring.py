import os
import time

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from connio.rest import Client
from connio.rest.api.v3.account.propertyy import PropertyInstance
from connio.rest.api.v3.account.method import MethodInstance

def wire():
    ACCOUNT_KEYID = os.environ.get('CONNIO_ACCOUNT_KEYID')
    ACCOUNT_KEYSECRET = os.environ.get('CONNIO_ACCOUNT_KEYSECRET')

    client = Client(username=ACCOUNT_KEYID, 
                    password=ACCOUNT_KEYSECRET)


    # Get master account details
    master = client.accounts.get().fetch()    
    print('Master account: ' + master.name)
                                     
    # Create new device profile
    compressor = client.account.deviceprofiles.create(name='Logika-L26', 
                                                  friendly_name='[TEST] L26',
                                                  base_profile='ModbusGateway',
                                                  description='Industrial compressor',
                                                  tags=['test'],
                                                  device_class='compressor',
                                                  product_name='i4100',
                                                  vendor_name='Dalgakıran'
                                                )

    #------ Add properties to device profile

    client.account.properties(compressor.id).create(name='cfgSerialNumber', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='cfgModelNumber', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='cfgReleaseNo', data_type='number', access_type='protected', publish_type='never')    

    unit = PropertyInstance.MeasurementUnit('Hour', 'h')
    measurement = PropertyInstance.Measurement('time', unit)

    client.account.properties(compressor.id).create(name='cfgBearingLubrication', data_type='number', access_type='protected', publish_type='never', description='Check Bearings Lubrication Setting C-BL (hours)', measurement=measurement)
    client.account.properties(compressor.id).create(name='cfgChangeAirFilter', data_type='number', access_type='protected', publish_type='never', description='Change air filter setting CAF (hours)', measurement=measurement)
    client.account.properties(compressor.id).create(name='cfgChangeOil', data_type='number', access_type='protected', publish_type='never', description='Change oil setting C-- (hours)', measurement=measurement)
    client.account.properties(compressor.id).create(name='cfgChangeOilFilter', data_type='number', access_type='protected', publish_type='never', description='Change oil filter setting COF (hours)', measurement=measurement)
    client.account.properties(compressor.id).create(name='cfgChangeSeparatorFilter', data_type='number', access_type='protected', publish_type='never', description='Change Separator filter setting CSF (hours)', measurement=measurement)
    client.account.properties(compressor.id).create(name='cfgCheckCompressor', data_type='number', access_type='protected', publish_type='never', description='Check Compressor setting C--h (hours)', measurement=measurement)
    
    client.account.properties(compressor.id).create(name='cfgNominalAirFlow', data_type='number', access_type='protected', publish_type='never', description='Capacity (Nominal Air Flow) L/min *0.1 (C10) (Lt/min)')
    client.account.properties(compressor.id).create(name='cfgConfigurationSwitches', data_type='number', access_type='protected', publish_type='never', description='See documentation')
    client.account.properties(compressor.id).create(name='cfgConfigurationSelections1', data_type='number', access_type='protected', publish_type='never', description='See documentation')
    client.account.properties(compressor.id).create(name='cfgConfigurationSelections2', data_type='number', access_type='protected', publish_type='never', description='See documentation')

    #----

    client.account.properties(compressor.id).create(name='controller_state', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='compressor_state', data_type='object', access_type='protected', publish_type='never')
   
    unit = PropertyInstance.MeasurementUnit('Celsius', '°C')
    measurement = PropertyInstance.Measurement('temperature', unit)
    client.account.properties(compressor.id).create(name='screw_temperature', data_type='number', access_type='protected', publish_type='never', description='Main Screw Temperature (* 10)', measurement=measurement)

    unit = PropertyInstance.MeasurementUnit('Bar', 'bar')
    measurement = PropertyInstance.Measurement('pressure', unit)
    client.account.properties(compressor.id).create(name='auxiliary_pressure', data_type='number', access_type='protected', publish_type='never', description='Auxiliary Pressure (*10)', measurement=measurement)
    client.account.properties(compressor.id).create(name='working_pressure', data_type='number', access_type='protected', publish_type='never', description='Main Working Pressure (* 10)', measurement=measurement)

    unit = PropertyInstance.MeasurementUnit('Volt', 'V')
    measurement = PropertyInstance.Measurement('electricity', unit)
    client.account.properties(compressor.id).create(name='ptc_input', data_type='number', access_type='protected', publish_type='never', description='Positive Temperature Coefficient (in Volts)', measurement=measurement)

    unit = PropertyInstance.MeasurementUnit('Frequence', 'Hz')
    measurement = PropertyInstance.Measurement('custom', unit)
    client.account.properties(compressor.id).create(name='analog_out_freq', data_type='number', access_type='protected', publish_type='never', description='Analog Out Frequency in Hz', measurement=measurement)

    client.account.properties(compressor.id).create(name='active_alarms', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(compressor.id).create(name='active_alarms_nonack', data_type='object', access_type='protected', publish_type='never')
   
    client.account.properties(compressor.id).create(name='last_alarms', data_type='object', access_type='protected', publish_type='never', description='Last compressor alarms')
    client.account.properties(compressor.id).create(name='last_warnings', data_type='object', access_type='protected', publish_type='never', description='Last compressor warnings')
   
    unit = PropertyInstance.MeasurementUnit('Minute', 'min')
    measurement = PropertyInstance.Measurement('time', unit)
    client.account.properties(compressor.id).create(name='idle_running_minutes', data_type='number', access_type='protected', publish_type='never', description='Check Bearings Lubrication Setting C-BL (hours)', measurement=measurement)
    client.account.properties(compressor.id).create(name='load_running_minutes', data_type='number', access_type='protected', publish_type='never', description='Check Bearings Lubrication Setting C-BL (hours)', measurement=measurement)

    unit = PropertyInstance.MeasurementUnit('Hour', 'h')
    measurement = PropertyInstance.Measurement('time', unit)    
    client.account.properties(compressor.id).create(name='total_hours', data_type='number', access_type='protected', publish_type='never', description='Total hours compressor was working', measurement=measurement)
    client.account.properties(compressor.id).create(name='total_load_hours', data_type='number', access_type='protected', publish_type='never', description='Total hours compressor was on load', measurement=measurement)

    # NOT USED
    #pvOnLoadMinsLast100Hours	R	Total minutes the compressor was on load within the last 100 hrs
    #pvNumOfStartsInLastHour	R	Number of starts within the last hour
    #pvTimeKeeperErrs
   
    client.account.properties(compressor.id).create(name='maintenance_costs', data_type='object', access_type='public', publish_type='never', description='Maintenance Cost Tariff')
    client.account.properties(compressor.id).create(name='maintenance_log', data_type='object', access_type='protected', publish_type='never', description='Put maintenance log here')

    unit = PropertyInstance.MeasurementUnit('Count', '#')
    measurement = PropertyInstance.Measurement('custom', unit)    
    client.account.properties(compressor.id).create(name='nbr_of_alarms', data_type='number', access_type='protected', publish_type='never', description='Number of alarms', measurement=measurement)
    client.account.properties(compressor.id).create(name='nbr_of_warnings', data_type='number', access_type='protected', publish_type='never', description='Number of warning', measurement=measurement)

    client.account.properties(compressor.id).create(name='nbr_of_powercut_stoppages', data_type='number', access_type='protected', publish_type='never', description='Number of powercut stoppages', measurement=measurement)    
    client.account.properties(compressor.id).create(name='nbr_of_planned_stoppages', data_type='object', access_type='protected', publish_type='never', description='Number of planned stoppages')
    client.account.properties(compressor.id).create(name='nbr_of_unplanned_stoppages', data_type='object', access_type='protected', publish_type='never', description='Number of unplanned stoppages')
    
    unit = PropertyInstance.MeasurementUnit('Minute', 'min')
    measurement = PropertyInstance.Measurement('time', unit)
    client.account.properties(compressor.id).create(name='pland_stp_minutes', data_type='number', access_type='protected', publish_type='never', description='Planned stoppage total minutes', measurement=measurement)
    client.account.properties(compressor.id).create(name='unpland_stp_minutes', data_type='number', access_type='protected', publish_type='never', description='Unplanned stoppage total minutes', measurement=measurement)

    unit = PropertyInstance.MeasurementUnit('Month', 'months')
    measurement = PropertyInstance.Measurement('custom', unit)
    client.account.properties(compressor.id).create(name='time_to_end_of_warranty', data_type='number', access_type='protected', publish_type='never', description='Months to end of warranty', measurement=measurement)

    unit = PropertyInstance.MeasurementUnit('Hour', 'h')
    measurement = PropertyInstance.Measurement('time', unit)    
    client.account.properties(compressor.id).create(name='time_from_air_filter_change', data_type='number', access_type='protected', publish_type='never', measurement=measurement)
    client.account.properties(compressor.id).create(name='time_from_bearing_lubrication', data_type='number', access_type='protected', publish_type='never', measurement=measurement)
    client.account.properties(compressor.id).create(name='time_from_comp_check', data_type='number', access_type='protected', publish_type='never', measurement=measurement)
    client.account.properties(compressor.id).create(name='time_from_oil_change', data_type='number', access_type='protected', publish_type='never', measurement=measurement)
    client.account.properties(compressor.id).create(name='time_from_oil_filter_change', data_type='number', access_type='protected', publish_type='never', measurement=measurement)
    client.account.properties(compressor.id).create(name='time_from_sep_filter_change', data_type='number', access_type='protected', publish_type='never', measurement=measurement)

    #------ Add methods to device profile

    impl = MethodInstance.MethodImplementation(body="const ALARM_LIST = [ \n { wordNo: 1, type: 'alarm', bit: Math.pow(2,9), code: 'A01', label: \"Emergency Stop\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,10), code: 'A02', label: \"Motor Overheat\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,11), code: 'A03', label: \"Fan Overheat\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,12), code: 'A04', label: \"AC Phase Missing\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,13), code: 'A05', label: \"Phase Sequence Wrong\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,15), code: 'A07', label: \"Door Open\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,1), code: 'A09', label: \"Drive Fault\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,3), code: 'A11', label: \"High Work Press\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,4), code: 'A12', label: \"Screw Temp Fault\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,5), code: 'A13', label: \"High Screw Temp\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,6), code: 'A14', label: \"Low Screw Temp\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,7), code: 'A15', label: \"Aux Transd Sep Filter\" },\n //\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,10), code: 'A18', label: \"Black Out\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,12), code: 'A20', label: \"PTC Motor\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,13), code: 'A21', label: \"Input Common Missing\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,14), code: 'A22', label: \"Input7\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,1), code: 'A25', label: \"Separator Filter\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,2), code: 'A26', label: \"Work Press Fault\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,3), code: 'A27', label: \"Aux Press Fault\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,4), code: 'A28', label: \"Low Voltage\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,5), code: 'A29', label: \"Security\" },\n { wordNo: 2, type: 'warning', bit: Math.pow(2,6), code: 'A30', label: \"Screw Temp Warning\" },\n //\n { wordNo: 3, type: 'alarm', bit: Math.pow(2,9), code: 'A32', label: \"Maint C H Blk\" },\n { wordNo: 3, type: 'alarm', bit: Math.pow(2,10), code: 'A33', label: \"Fieldbus Error\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,12), code: 'A35', label: \"EEPROM Fault\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,13), code: 'A36', label: \"Air Filter\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,14), code: 'A37', label: \"Multi Unit Fault\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,15), code: 'A38', label: \"Aux Transd Sep Filter Warning\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,0), code: 'A39', label: \"Low Voltage Warning\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,1), code: 'A40', label: \"High Voltage\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,2), code: 'A41', label: \"Clock Failure\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,3), code: 'A42', label: \"RS232 Fault\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,4), code: 'A43', label: \"DST Adjusted\" },\n { wordNo: 3, type: 'alarm', bit: Math.pow(2,5), code: 'A44', label: \"Bearing High Temp\" },\n //\n { wordNo: 4, type: 'warning', bit: Math.pow(2,8), code: 'A47', label: \"Too Much Start\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,9), code: 'A48', label: \"Restart Changed to Manual\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,10), code: 'A49', label: \"Restart Changed to Auto\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,11), code: 'A50', label: \"Change Air Filter\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,12), code: 'A51', label: \"Change Oil Filter\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,13), code: 'A52', label: \"Change Sep Filter\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,14), code: 'A53', label: \"Change Oil\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,15), code: 'A54', label: \"Check Compressor\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,0), code: 'A55', label: \"Check Bearings\" },\n { wordNo: 4, type: 'alarm', bit: Math.pow(2,5), code: 'A60', label: \"Drive Fault\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,6), code: 'A61', label: \"Drive Warning\" },\n { wordNo: 4, type: 'alarm', bit: Math.pow(2,7), code: 'A62', label: \"Drive No Communication\" } ];\n \nconst BLACK_OUT_CODE = 'A18'; \n \nfunction createBinaryString(nMask) {\n  // nMask must be between -2147483648 and 2147483647\n  for (var nFlag = 0, nShifted = nMask, sMask = ''; nFlag < 32;\n       nFlag++, sMask += String(nShifted >>> 31), nShifted <<= 1);\n  return sMask;\n}\n\nfunction getActiveAlarms(activeAlarms, wordNo, bitmap) {\n    let modifiedActiveAlarms = activeAlarms.items.filter( function(item) { return item.wordNo != wordNo; } );\n    let alarms = ALARM_LIST.filter( function(item) { return item.wordNo == wordNo; } );\n    \n    alarms.forEach( (item) => {\n      if (bitmap & item.bit) {\n        modifiedActiveAlarms.push(item);\n      }\n    });\n    \n    return modifiedActiveAlarms;\n}\n\n(async function f() {\n    let prop = await Device.api.getProperty(\"active_alarms\");\n    // Clone the property otherwise it will be updated when we set it.\n    let activeAlarmProp = Object.assign({}, prop);\n    \n    // No alarm state\n    let activeAlarms = { \"items\": [] };\n    \n    if (activeAlarmProp.value) {\n      activeAlarms = activeAlarmProp.value;\n    }\n    \n    // Alarm data provided in 4 words\n    for (let i = 0; i < 4; i++) {\n        let wordNo = i+1;\n        let bitmap = value[i];\n        \n        let currActiveAlarms = getActiveAlarms(activeAlarms, wordNo, bitmap);\n    \n        let currActivAlarmCodeList = currActiveAlarms.map( ca => ca.code );\n        let extActiveAlarmCodeList = activeAlarms.items.map( ea => ea.code );\n        \n        if (!(currActivAlarmCodeList.length == 0 && extActiveAlarmCodeList.length == 0) &&\n            (currActivAlarmCodeList.length !== extActiveAlarmCodeList.length || \n            currActivAlarmCodeList.every((item, index) => !extActiveAlarmCodeList.includes(item)))\n        ) {\n            \n            // Write new list into the property\n            await Device.api.setProperty(\"active_alarms\", {\n                    value: { items: currActiveAlarms },\n                    time: new Date().toISOString()\n                });\n                \n            let alarms = currActiveAlarms.filter(aa => aa.type === 'alarm');\n            let warnings = currActiveAlarms.filter(aa => aa.type === 'warning');\n            let blackOut = currActiveAlarms.filter(aa => aa.code === BLACK_OUT_CODE);\n            \n            let nbrOfAlarms = alarms.length;\n            let nbrOfWarnings = warnings.length;\n            \n            await Device.api.setProperty(\"nbr_of_alarms\", {\n                    value: nbrOfAlarms,\n                    time: new Date().toISOString()\n                  });\n                          \n            await Device.api.setProperty(\"nbr_of_warnings\", {\n                    value: nbrOfWarnings,\n                    time: new Date().toISOString()\n                  });\n                  \n            // set last alarms and warnings if and only if there are alarms and warnings\n            if (nbrOfAlarms > 0) {\n                await Device.api.setProperty(\"last_alarms\", {\n                        value: { items: alarms.map(a => { return { code: a.code, label: a.label }; }) },\n                        time: new Date().toISOString()\n                      });\n            }\n                  \n            if (nbrOfWarnings > 0) {\n                await Device.api.setProperty(\"last_warnings\", {\n                        value: { items: warnings.map(a => { return { code: a.code, label: a.label }; }) },\n                        time: new Date().toISOString()\n                      });\n            }\n            \n            if (blackOut.length > 0) {\n                await Device.api.setProperty(\"nbr_of_powercut_stoppages\", {\n                            value: 1,\n                            time: new Date().toISOString()\n                        });\n            }\n        }\n        \n    }//end of for-loop\n    \n    done(null, null);\n})();\n\n", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setAlarms', access_type='public', method_impl=impl)
    #--
    impl = MethodInstance.MethodImplementation(body="const ALARM_LIST = [ \n { wordNo: 1, type: 'alarm', bit: Math.pow(2,9), code: 'A01', label: \"Emergency Stop\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,10), code: 'A02', label: \"Motor Overheat\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,11), code: 'A03', label: \"Fan Overheat\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,12), code: 'A04', label: \"AC Phase Missing\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,13), code: 'A05', label: \"Phase Sequence Wrong\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,15), code: 'A07', label: \"Door Open\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,1), code: 'A09', label: \"Drive Fault\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,3), code: 'A11', label: \"High Work Press\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,4), code: 'A12', label: \"Screw Temp Fault\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,5), code: 'A13', label: \"High Screw Temp\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,6), code: 'A14', label: \"Low Screw Temp\" },\n { wordNo: 1, type: 'alarm', bit: Math.pow(2,7), code: 'A15', label: \"Aux Transd Sep Filter\" },\n //\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,10), code: 'A18', label: \"Black Out\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,12), code: 'A20', label: \"PTC Motor\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,13), code: 'A21', label: \"Input Common Missing\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,14), code: 'A22', label: \"Input7\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,1), code: 'A25', label: \"Separator Filter\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,2), code: 'A26', label: \"Work Press Fault\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,3), code: 'A27', label: \"Aux Press Fault\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,4), code: 'A28', label: \"Low Voltage\" },\n { wordNo: 2, type: 'alarm', bit: Math.pow(2,5), code: 'A29', label: \"Security\" },\n { wordNo: 2, type: 'warning', bit: Math.pow(2,6), code: 'A30', label: \"Screw Temp Warning\" },\n //\n { wordNo: 3, type: 'alarm', bit: Math.pow(2,9), code: 'A32', label: \"Maint C H Blk\" },\n { wordNo: 3, type: 'alarm', bit: Math.pow(2,10), code: 'A33', label: \"Fieldbus Error\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,12), code: 'A35', label: \"EEPROM Fault\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,13), code: 'A36', label: \"Air Filter\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,14), code: 'A37', label: \"Multi Unit Fault\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,15), code: 'A38', label: \"Aux Transd Sep Filter Warning\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,0), code: 'A39', label: \"Low Voltage Warning\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,1), code: 'A40', label: \"High Voltage\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,2), code: 'A41', label: \"Clock Failure\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,3), code: 'A42', label: \"RS232 Fault\" },\n { wordNo: 3, type: 'warning', bit: Math.pow(2,4), code: 'A43', label: \"DST Adjusted\" },\n { wordNo: 3, type: 'alarm', bit: Math.pow(2,5), code: 'A44', label: \"Bearing High Temp\" },\n //\n { wordNo: 4, type: 'warning', bit: Math.pow(2,8), code: 'A47', label: \"Too Much Start\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,9), code: 'A48', label: \"Restart Changed to Manual\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,10), code: 'A49', label: \"Restart Changed to Auto\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,11), code: 'A50', label: \"Change Air Filter\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,12), code: 'A51', label: \"Change Oil Filter\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,13), code: 'A52', label: \"Change Sep Filter\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,14), code: 'A53', label: \"Change Oil\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,15), code: 'A54', label: \"Check Compressor\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,0), code: 'A55', label: \"Check Bearings\" },\n { wordNo: 4, type: 'alarm', bit: Math.pow(2,5), code: 'A60', label: \"Drive Fault\" },\n { wordNo: 4, type: 'warning', bit: Math.pow(2,6), code: 'A61', label: \"Drive Warning\" },\n { wordNo: 4, type: 'alarm', bit: Math.pow(2,7), code: 'A62', label: \"Drive No Communication\" } ];\n \nfunction createBinaryString(nMask) {\n  // nMask must be between -2147483648 and 2147483647\n  for (var nFlag = 0, nShifted = nMask, sMask = ''; nFlag < 32;\n       nFlag++, sMask += String(nShifted >>> 31), nShifted <<= 1);\n  return sMask;\n}\n\nfunction getActiveAlarms(activeAlarms, wordNo, bitmap) {\n    let modifiedActiveAlarms = activeAlarms.items.filter( function(item) { return item.wordNo != wordNo; } );\n    let alarms = ALARM_LIST.filter( function(item) { return item.wordNo == wordNo; } );\n    \n    alarms.forEach( (item) => {\n      if (bitmap & item.bit) {\n        modifiedActiveAlarms.push(item);\n      }\n    });\n    \n    return modifiedActiveAlarms;\n}\n\n(async function f() {\n    let prop = await Device.api.getProperty(\"active_alarms_nonack\");\n    // Clone the property otherwise it will be updated when we set it.\n    let activeAlarmProp = Object.assign({}, prop);\n    \n    // No alarm state\n    let activeAlarms = { \"items\": [] };\n    \n    if (activeAlarmProp.value) {\n      activeAlarms = activeAlarmProp.value;\n    }\n    \n    // Non Ack Alarm data provided in 4 words\n    for (let i = 0; i < 4; i++) {\n        \n        let wordNo = i+1;\n        let bitmap = value[i];\n        \n        let currActiveAlarms = getActiveAlarms(activeAlarms, wordNo, bitmap);\n    \n        let currActivAlarmCodeList = currActiveAlarms.map( ca => ca.code );\n        let extActiveAlarmCodeList = activeAlarms.items.map( ea => ea.code );\n        \n        if (!(currActivAlarmCodeList.length == 0 && extActiveAlarmCodeList.length == 0) &&\n            (currActivAlarmCodeList.length !== extActiveAlarmCodeList.length || \n            currActivAlarmCodeList.every((value, index) => value !== extActiveAlarmCodeList[index]))) {\n            \n            // Write new list into the property\n            await Device.api.setProperty(\"active_alarms_nonack\", {\n                    value: { items: currActiveAlarms },\n                    time: new Date().toISOString()\n                });\n        }\n        \n    }//end of for-loop\n    \n    done(null, null);\n})();\n\n", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setNonAckAlarms', access_type='public', method_impl=impl)
    #--
    impl = MethodInstance.MethodImplementation(body="let table = [\n    { code: 0, label: \"OFF\" },\n    { code: 1, label: \"INTERNAL PRESS TOO HIGH, WAITING\" },\n    { code: 2, label: \"REMOTE STOP ACTIVE\" },\n    { code: 3, label: \"STOP BY TIMER\" },\n    { code: 4, label: \"IDLE STOPPING\" },\n    { code: 5, label: \"IDLE STOPPING BYREMOTE STOP\" },\n    { code: 6, label: \"IDLE STOPPING BY TIMER\" },\n    { code: 7, label: \"PRESSURE IN SET, MOTOR IS OFF\" },\n    { code: 8, label: \"WAITING TO START\" },\n    { code: 9, label: \"MOTOR STARTING\" },\n    { code: 10, label: \"IDLE RUNNING\" },\n    { code: 11, label: \"LOAD RUNNING\" },\n    { code: 12, label: \"SOFT BLOCK DELAY\" },\n    { code: 13, label: \"BLOCK\" },\n    { code: 14, label: \"FACTORY TEST\" }\n    ];\n    \nconst IDLE_RUNNING = 10;\nconst LOAD_RUNNING = 11;\n\nconst PLANNED_STOPPAGES = [ 0, 14 ];\nconst UNPLANNED_STOPPAGES = [ 13 ];\n\nlet newState = { code: -1, label: \"-\" };\nif (typeof value != 'undefined' && value >= 0 && value < 15) {\n    newState = table[value | 0];\n}\n\n(async function f() {\n    let prop = await Device.api.getProperty(\"compressor_state\");\n    \n    if (!prop.value) {\n        await Device.api.setProperty(\"compressor_state\", {\n                value: newState,\n                time: new Date().toISOString()\n            });\n            \n        done(null, prop);\n    }\n    else {\n        // Clone the property otherwise it will be updated when we set it.\n        let currProp_ = Object.assign({}, prop);\n        \n        if (newState.code !== currProp_.value.code) {\n            var modifiedProp = await Device.api.setProperty(\"compressor_state\", {\n                    value: newState,\n                    time: new Date().toISOString()\n                });\n                \n            if (PLANNED_STOPPAGES.includes(newState.code)) {\n                await Device.api.setProperty(\"nbr_of_planned_stoppages\", {\n                        value: newState,\n                        time: new Date().toISOString()\n                    });\n            }\n            else if (UNPLANNED_STOPPAGES.includes(newState.code)) {\n                await Device.api.setProperty(\"nbr_of_unplanned_stoppages\", {\n                        value: newState,\n                        time: new Date().toISOString()\n                    });\n            }\n                \n            // Calculate load & idle running durations\n            // \n            if (!currProp_.value && currProp_.value.code === LOAD_RUNNING && modifiedProp.value.code !== LOAD_RUNNING) {\n                var lr = await Device.api.setProperty(\"load_running_minutes\", {\n                        value: (Date.parse(modifiedProp.time) - Date.parse(currProp_.time)) / (1000 * 60),\n                        time: new Date().toISOString()\n                    });\n            }\n            else if (!currProp_.value && currProp_.value.code === IDLE_RUNNING && modifiedProp.value.code !== IDLE_RUNNING) {\n                var ir = await Device.api.setProperty(\"idle_running_minutes\", {\n                        value: (Date.parse(modifiedProp.time) - Date.parse(currProp_.time)) / (1000 * 60),\n                        time: new Date().toISOString()\n                    });\n            }\n            \n            // Calculate unplanned & planned stoppage durations\n            //\n            if (!currProp_.value && UNPLANNED_STOPPAGES.includes(currProp_.value.code) && !UNPLANNED_STOPPAGES.includes(modifiedProp.value.code)) {\n                // Unplanned stoppage is over\n                await Device.api.setProperty(\"unpland_stp_minutes\", {\n                        value: (Date.parse(modifiedProp.time) - Date.parse(currProp_.time)) / (1000 * 60),\n                        time: new Date().toISOString()\n                    });\n            }\n            else if (!currProp_.value && PLANNED_STOPPAGES.includes(currProp_.value.code) && !PLANNED_STOPPAGES.includes(modifiedProp.value.code)) {\n                // Planned stoppage is over\n                await Device.api.setProperty(\"pland_stp_minutes\", {\n                        value: (Date.parse(modifiedProp.time) - Date.parse(currProp_.time)) / (1000 * 60),\n                        time: new Date().toISOString()\n                    });\n            }\n            \n            done(null, modifiedProp);\n        }\n        else {\n            done(null, currProp_)\n        }\n    }\n})();\n", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setCompressorState', access_type='public', method_impl=impl)
    #--
    impl = MethodInstance.MethodImplementation(body="let table = [\n    { code: 0, label: \"RESET\" },\n    { code: 1, label: \"OFF\" },\n    { code: 2, label: \"STARTING - MOTOR IN STAR CONNECTION\" },\n    { code: 3, label: \"STARTING - PAUSE START TO DELTA CONNECTION\" },\n    { code: 4, label: \"STARTING - ACCELERATING IN DELTA CONNECTION\" },\n    { code: 5, label: \"LOAD RUNNING\" },\n    { code: 6, label: \"IDLE RUNNING - PRESSURE IN RANGE\" },\n    { code: 7, label: \"IDLE RUNNING - STOPPING\" },\n    { code: 8, label: \"INVERTER ON\" },\n    { code: 9, label: \"INVERTER SETUP\" },\n    { code: 10, label: \"BLOCKED BY FAULT\" },\n    { code: 11, label: \"FACTORY TEST\" }\n    ];\n\n\nlet state = { code: -1, label: \"NOT_SET\" };\nif (value !== undefined && value >= 0 && value < 12) {\n    state = table[value | 0];\n}\n\nDevice.api.getProperty(\"controller_state\").then( stateProp => {\n    if (!stateProp.value || state.code !== stateProp.value.code) {\n        Device.api.setProperty(\"controller_state\", {\n            value: state,\n            time: new Date().toISOString()\n        })\n        .then(property => {\n            done(null, state);\n        });\n    }\n    else{\n        done(null, \"noop\");\n    }\n});\n\n\n", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setControllerState', access_type='public', method_impl=impl)
    #--
    impl = MethodInstance.MethodImplementation(body="Device.api.setProperty(\"auxiliary_pressure\", {\n    value: value / 10.0,\n    time: new Date().toISOString()\n })\n .then(property => {\n    done(null, value / 10.0);\n });", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setAuxiliaryPressure', access_type='public', method_impl=impl)
    #--
    impl = MethodInstance.MethodImplementation(body="Device.api.setProperty(\"working_pressure\", {\n    value: value / 10.0,\n    time: new Date().toISOString()\n })\n .then(property => {\n    done(null, value / 10.0);\n });", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setWorkingPressure', access_type='public', method_impl=impl)    
    #--
    impl = MethodInstance.MethodImplementation(body="Device.api.setProperty(\"screw_temperature\", {\n    value: value / 10.0,\n    time: new Date().toISOString()\n })\n .then(property => {\n    done(null, value / 10.0);\n });", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setScrewTemperature', access_type='public', method_impl=impl)
    #--
    impl = MethodInstance.MethodImplementation(body="Device.convertToHours(value, (error, hours) => {\n    if (error) {\n        done(error, null);\n    }\n    else {\n        // Update the output property with the actual hours value\n        Device.api.setProperty(\"total_load_hours\", {\n          value: hours,\n          time: new Date().toISOString()\n          }).\n        then(property => {\n            done(null, property.value);\n        });   \n    }\n});", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setLoadHours', access_type='public', method_impl=impl)
    #--
    impl = MethodInstance.MethodImplementation(body="Device.convertToHours(value, (error, hours) => {\n    if (error) {\n        done(error, null);\n    }\n    else {\n        // Update the output property with the actual hours value\n        Device.api.setProperty(\"total_hours\", {\n          value: hours,\n          time: new Date().toISOString()\n          }).\n        then(property => {\n            done(null, property.value);\n        });   \n    }\n});", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setTotalHours', access_type='public', method_impl=impl)
    #--
    impl = MethodInstance.MethodImplementation(body="done(null, value);", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setAirFilterMaintCounter', access_type='public', method_impl=impl)
    #--
    impl = MethodInstance.MethodImplementation(body="done(null, value);", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setOilFilterMaintCounter', access_type='public', method_impl=impl)
    #--
    impl = MethodInstance.MethodImplementation(body="done(null, value);", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setSepFilterMaintCounter', access_type='public', method_impl=impl)
    #--
    impl = MethodInstance.MethodImplementation(body="done(null, value);", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setOilChangeMaintCounter', access_type='public', method_impl=impl)
    #--
    impl = MethodInstance.MethodImplementation(body="done(null, value);", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setCompCheckMaintCounter', access_type='public', method_impl=impl)
    #--
    impl = MethodInstance.MethodImplementation(body="done(null, value);", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='setBearingLubMaintCounter', access_type='public', method_impl=impl)

    #--
    impl = MethodInstance.MethodImplementation(body="function convert(word1, word2) {\n    var byte1 = (word2 & 255) << 24;\n    var byte2 = (word2 >>> 8) << 16;\n    var byte3 = (word1 & 255) << 8;\n    var byte4 = (word1 >>> 8);\n    \n    // calculate and divide by 60 to convert minutes into hours        \n    return (byte1 | byte2 | byte3 | byte4) / 60.0;\n};\n\ndone(null, convert(value[0], value[1]));\n\n", 
                                               lang="javascript")
    client.account.methods(compressor.id).create(name='convertToHours', access_type='private', method_impl=impl)

    


    # Add property to the device profile
    # client.account.properties(compressor.id).create(name='ActiveAlarms1', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='ActiveAlarms2', data_type='number', access_type='protected', publish_type='always')

    # for i in range(1, 11):
    #     client.account.properties(compressor.id).create(name='AlarmRecords' + str(i), data_type='number', access_type='protected', publish_type='always')

    # for i in range(1, 5):
    #     client.account.properties(compressor.id).create(name='AO' + str(i), data_type='string', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='AP3', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='AP4', data_type='string', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='bL', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='BlockingStates', data_type='number', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='C02', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='C07_1', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='C07_2', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='C08', data_type='string', access_type='protected', publish_type='always')
    
    # client.account.properties(compressor.id).create(name='C10', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='C19_1', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='C19_2', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='C20_1', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='C20_2', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='C22', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='C23', data_type='string', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='C__', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='C_H', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='CAF', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='CDF', data_type='number', access_type='protected', publish_type='always')

    # for i in range(1, 11):
    #     client.account.properties(compressor.id).create(name='Cntrl_Identifier' + str(i), data_type='number', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='con', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='ControlCommand', data_type='number', access_type='public', publish_type='always')
    # client.account.properties(compressor.id).create(name='CSF', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='DigitalInputs', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='DisplayedState', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='DisplayState1', data_type='number', access_type='protected', publish_type='always')

    # for i in range(0, 7):
    #     client.account.properties(compressor.id).create(name='DR' + str(i), data_type='number', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='drY', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='FAd', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='FR1', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='FR2', data_type='number', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='GatewayError', data_type='object', access_type='protected', publish_type='always')

    # for i in range(0, 8):
    #     client.account.properties(compressor.id).create(name='H0' + str(i), data_type='number', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='ln2', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='ln3', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='ln4', data_type='number', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='Indexes', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='initialState', data_type='number', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='Level1Password1', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='Level1Password2', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='Level2Password1', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='Level2Password2', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='Level3Password1', data_type='string', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='Level3Password2', data_type='string', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='LoadHours1', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='LoadHours2', data_type='number', access_type='protected', publish_type='always')
    
    # for i in range(1, 13):
    #     client.account.properties(compressor.id).create(name='MaintenanceHours' + str(i), data_type='number', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='Modbus_Release', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='ModelNumber', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='nc', data_type='number', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='NonAcknowledgedActiveAlarms1', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='NonAcknowledgedActiveAlarms2', data_type='number', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='OFL', data_type='number', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='PA1', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='PA2', data_type='number', access_type='protected', publish_type='always')

    # for i in range(0, 8):
    #     client.account.properties(compressor.id).create(name='P0' + str(i), data_type='number', access_type='protected', publish_type='always')

    # for i in range(1, 8):
    #     client.account.properties(compressor.id).create(name='PI' + str(i), data_type='number', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='PM1', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='PT1', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='PT2', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='PT3', data_type='number', access_type='protected', publish_type='always')
    
    # client.account.properties(compressor.id).create(name='r__', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='RelayOuts', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='Release_No', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='rL5', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='S__', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='S_h', data_type='number', access_type='protected', publish_type='always')

    # client.account.properties(compressor.id).create(name='ScrewTemp1', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='SupplyVoltage', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='TotalHours1', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='TotalHours2', data_type='number', access_type='protected', publish_type='always')
    # client.account.properties(compressor.id).create(name='WorkingPress1', data_type='number', access_type='protected', publish_type='always')

    # for i in range(1, 9):
    #     client.account.properties(compressor.id).create(name='t0' + str(i), data_type='number', access_type='protected', publish_type='always')

    # for i in range(1, 7):
    #     client.account.properties(compressor.id).create(name='WP' + str(i), data_type='number', access_type='protected', publish_type='always')

    # for i in range(1, 8):
    #     client.account.properties(compressor.id).create(name='WT' + str(i), data_type='number', access_type='protected', publish_type='always')






    # Create new app profile
    # client.account.appprofiles.create(name='CompressorManagement',                                                   
    #                                               friendly_name='Compressor Management App',
    #                                               description='Dalgakıran compressor management application',
    #                                               tags=['compressor'],
    #                                               version='1.0',
    #                                               product_name='i4100',
    #                                               vendor_name='Dalgakıran',
    #                                               system=[{'deviceProfileId': compressor.id, 'cardinality': 0}]
    #                                             )
    
    # Create an app
    # compressorApp = client.account.apps.create(name='CompressorManager',
    #                            profile='CompressorManagement',
    #                            friendly_name='Compressor Manager',
    #                            description='Unit of Compressor Management App',
    #                            tags=['compressor']
    #                           )

    # device = client.account.devices.create(name='i4100_demo', 
    #                                        profile='i4100',
    #                                        custom_ids={'mac': '06:ac:58:7f:6d:35'},
    #                                        apps=[compressorApp.id]
    #                                       )

    # Create a provisioning key
    # client.account.apiclients.create(name='ProvisioningClient2',
    #                                 friendly_name='Provisioning Key',
    #                                 description='An API Client for device provisioning',
    #                                 tags=['provisioning'],
    #                                 context={'type': 'app', 'ids': [compressorApp.id]},
    #                                 scope=['device:read'],
    #                                 )
    
if __name__ == '__main__':
    wire()
