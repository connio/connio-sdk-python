import requests
from requests.auth import HTTPBasicAuth

import paho.mqtt.client as mqtt
from paho.mqtt.client import connack_string
from paho.mqtt.client import MQTTv311

from threading import Timer

import os
import time
import json
import datetime
from six import u

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from connio.rest import Client
from connio.rest.api.v3.account import UserInfo
from connio.rest.api.v3.account import AccountInstance
from connio.base.exceptions import ConnioException
from connio.base.exceptions import ConnioRestException
from connio.rest.api.v3.account.method import MethodInstance
from connio.rest.api.v3.account.alert import AlertInstance

# ConnioHost = "127.0.0.1"
# ConnioAPIEndpoint = "http://{}:8081".format(ConnioHost)

ConnioHost = "api.connio.cloud"
ConnioAPIEndpoint = "https://{}".format(ConnioHost)

ConnioMqttEndpoint = "{}".format(ConnioHost)

def red(words):
    return u("\033[31m\033[49m%s\033[0m") % words
def teal(words):
    return u("\033[36m\033[49m%s\033[0m") % words
def white(words):
    return u("\033[37m\033[49m%s\033[0m") % words
def blue(words):
    return u("\033[34m\033[49m%s\033[0m") % words

#
#
#        
def teardown(sysclient, accountName):
    testAccount = sysclient.accounts.get(accountName).fetch()
    testAccount.delete(True)

    print(blue("\n~~ALL TESTS PASSED~~\n"))
    print(teal("Test account is deleted successfully."))

#
#
#
def create_account(sysclient, accountName):
    print(teal("Creating test account...."))

    # Create an account if doesn't exist
    token = sysclient.accounts.create(name=accountName, tags=['test'], userInfo=UserInfo(email="admin@{}.com".format(accountName), role='admin', name="admin"))
    admin = sysclient.api.helpers.activate(token['token'])

    # Wait until activation is propagated
    print(teal("Waiting for activation to complete...."))
    # Wait until activation is propagated
    while(1):
        try:
            # setup a client with current admin credentials 
            admin.update(password='password')
            break
        except:
            time.sleep(1.5)
            continue
    
    print(teal("Account successfully activated"))
    
    while(1):
        try:
            admin = Client(username=admin.apikey.id, 
                        password=admin.apikey.secret,
                        host=ConnioAPIEndpoint)
            return admin
        # except ConnioRestException as ce:
        #     print(ce)
        except:
            time.sleep(1.5)
            continue

#
#
#
def wireup(client):
    print(teal("Wiring test account...."))

    # Create new device profile
    devprof = client.account.deviceprofiles.create(name='RemoteMonitor', 
                                                friendly_name='Test Profile',
                                                base_profile='Gateway',
                                                description='Some test profile',
                                                tags=['test'],
                                                device_class='Test',
                                                product_name='Test01',
                                                vendor_name='Test01'
                                                )

    # Create new device profile for child device
    sensorprof = client.account.deviceprofiles.create(name='Sensor', friendly_name='Sensor', base_profile='connecteddevice')
    client.account.properties(sensorprof.id).create(name='reading', data_type='number', access_type='protected', publish_type='never')

    print(teal("Device profile successfully created"))

    # Add property to the device profile
    client.account.properties(devprof.id).create(name='temperature', data_type='boolean', access_type='public', publish_type='never')

    print(teal("Properties successfully created"))

    impl = MethodInstance.MethodImplementation(body="Device.api.log('debug', eval(value).toString()).then(() => { done(null, 'Log written') }).catch((error) => { done(error, null); });", lang="javascript")
    method = client.account.methods(devprof.id).create(name='echo', access_type='protected', method_impl=impl)

    print(teal("Method successfully created"))

    notif = AlertInstance.Notification(name="makeCall", action='method', method=method.id, parameter='${value}')

    expr = AlertInstance.Condition.Expression(operation='always')
    hnd = AlertInstance.Condition.Handler(key='k1', notification='makeCall')
    condition = AlertInstance.Condition(severity='notification', expression=expr, handlers=[hnd])

    client.account.alerts(devprof.id).create(name='testAlert', trigger='temperature', metric='value', conditions=[condition], notifications=[notif])
    
    print(teal("Alert successfully created"))

    # Create an app
    app = client.account.apps.create(name='RemoteMonitorApp',
                               profile='Sample',
                               friendly_name='My app',
                               description='The app',
                               tags=['test']
                              )

    print(teal("App successfully created"))

    # Create a provisioning key
    apicli = client.account.apiclients.create(name='ProvisioningClient',
                                    friendly_name='Provisioning Key',
                                    description='An API Client for device provisioning',
                                    tags=['provisioning'],
                                    context={'type': "app", 'ids': [app.id]},
                                    scope=['device:read', 'device:write-data', 'device:read-data', 'device:execute'],
                                    )

    print(teal("ApiClient successfully created"))
    
    # Create new gateway device
    gw = client.account.devices.create(name='Gateway.1', 
                                        profile='RemoteMonitor',
                                        apps=[app.id],
                                        custom_ids={'sn': "SN-001-0023904"},
                                        status='debug'
                                        )
    # Create new child device
    child = client.account.devices.create(name='Sensor.1', profile='Sensor')
    global childDeviceId
    childDeviceId = child.id

    # Add child device to gateway
    gw.apikey.update(context={ 'type': 'device', 'ids': [gw.id, child.id] })

    print(teal("Device successfully created"))
    print(teal("Wiring successfully completed\n"))

    return apicli

if __name__ == '__main__':
    SYSTEMADMIN_USER = os.environ.get('CONNIO_SYSTEMADMIN_USER', 'user')
    SYSTEMADMIN_PWD = os.environ.get('CONNIO_SYSTEMADMIN_PWD', 'password')

    sysclient = Client(username=SYSTEMADMIN_USER, 
                    password=SYSTEMADMIN_PWD,
                    sysadmin=True,
                    host=ConnioAPIEndpoint)

    accountName = "acmeCo"

    # cleanup if exists
    try:
        testAccount = sysclient.accounts.get(accountName).fetch()
        testAccount.delete(True)
    except ConnioRestException as cre:
        if cre.code == 'ResourceNotFound':
            # test account doesn't exist
            pass
        else:
            print(cre)
            sys.exit(1)


    adminclient = None
    apiclient = None

    try:
        adminclient = create_account(sysclient, accountName)
    except Exception as e:
        print(red("Account creation: FAILED!"))
        print(e)
        sys.exit(1)

    apiclient = wireup(adminclient)

    try:
        pass
    except Exception as e:
        print(red("Account wiring: FAILED!"))
        print(e)
        sys.exit(1)

   
    # teardown(sysclient, accountName)