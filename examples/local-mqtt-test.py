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

ConnioHost = "127.0.0.1"

ConnioAPIEndpoint = "http://{}:8081".format(ConnioHost)
ConnioMqttEndpoint = "{}".format(ConnioHost)

cidType = 'sn'
cid = os.environ.get("CONNIO_DEVICE_CID", 'SN-001-0023904')

deviceId = None
deviceKeyId = None
deviceKeySecret = None
TOTAL_TRIES = 3
testCounter = TOTAL_TRIES
childDeviceId = None

mytimer = None

config = { 'frequency': 5, 'forever': True, 'timeout': 10 }

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
def provision(userName, password, cidType, cidVal):
    MqttClientID = "_???_mnv2"

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        # client.subscribe("$SYS/#")
        client.subscribe("connio/provisions/{}".format(MqttClientID))

    def on_disconnect(client, userdata, rc):
        # print("Connection is lost: " + connack_string(rc))
        client.loop_stop()

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        # print("Message received: \n@" + msg.topic + "\n" + str(msg.payload, 'utf-8'))
        client.disconnect()    

        response = json.loads(str(msg.payload, 'utf-8'))

        global deviceId 
        global deviceKeyId
        global deviceKeySecret
        global config

        deviceId = response.get('deviceId')
        deviceKeyId = response.get('apiKeyId')
        deviceKeySecret = response.get('apiSecret')
        config = response.get('config') or config

        mytimer.cancel()
        print(blue("Provisioning: PASSED"))

    def on_subscribe(client, userdata, mid, granted_qos):
        # print("Subscription is complete")

        payload = json.dumps({cidType: cidVal, 'configProperty': 'config'})   
        client.publish("connio/provisions", payload)

    def on_publish(client, userdata, mid):
        # print("Publish is complete")
        pass

    client = mqtt.Client(client_id=MqttClientID, clean_session=True, userdata=None, protocol=MQTTv311)

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_publish = on_publish

    client.username_pw_set(username=userName, password=password)
    client.connect_async(ConnioMqttEndpoint, 1883, 60)

    client.loop_forever()

#
#
#
def provisioning_timeout():
    print(red("Provisioning: FAILED! [Timeout]"))

#
#
#
def sending_timeout():
    print(red("Sending data to devices over MQTT: FAILED!"))
    # url = "https://hooks.slack.com/services/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"
    # requests.post(url, json={ 'text': 'SYSTEM ERR!'}, verify=True)

#
#
#
def connectConnio(apiclient, adminKeyId, adminSecret):
    global mytimer
    global deviceId 
    global deviceKeyId
    global deviceKeySecret
    
    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, deviceId, flags, rc):       
        client.subscribe("connio/data/in/devices/{}/#".format(deviceId))

        # Wait a little for connection message to be delivered
        time.sleep(2)

        # Make sure that Gateway is in connected status
        url = "{0}/v3/data/devices/{1}".format(ConnioAPIEndpoint, deviceId)
        res = requests.get(url, auth=HTTPBasicAuth(apiclient.apikey.id, apiclient.apikey.secret), verify=True)

        body = json.loads(str(res.content, 'utf-8'))
        if not (res.ok and body['connectionStatus'] == "online"):
            print(red("Gateway online status update: FAILED!"))
            sys.exit(1)
        else:
            print(blue("Gateway online status update: PASSED"))

        # Make sure that Sensor is in connected status as well
        url = "{0}/v3/data/devices/{1}".format(ConnioAPIEndpoint, 'Sensor.1')
        res = requests.get(url, auth=HTTPBasicAuth(adminKeyId, adminSecret), verify=True)

        body = json.loads(str(res.content, 'utf-8'))
        if not (res.ok and body['connectionStatus'] == "online"):
            print(red("Sensor online status update: FAILED!"))
            sys.exit(1)
        else:
            print(blue("Sensor online status update: PASSED"))

    def on_disconnect(client, userdata, rc):
        # Wait a little for connection message to be delivered
        time.sleep(1.5)

        # Make sure that Gateway is in connected status
        url = "{0}/v3/data/devices/{1}".format(ConnioAPIEndpoint, deviceId)
        res = requests.get(url, auth=HTTPBasicAuth(apiclient.apikey.id, apiclient.apikey.secret), verify=True)

        body = json.loads(str(res.content, 'utf-8'))
        if not (res.ok and body['connectionStatus'] == "offline"):
            print(red("Gateway offline status update: FAILED!"))
            sys.exit(1)
        else:
            print(blue("Gateway offline status update: PASSED"))

        # Make sure that Sensor is in connected status
        url = "{0}/v3/data/devices/{1}".format(ConnioAPIEndpoint, 'Sensor.1')
        res = requests.get(url, auth=HTTPBasicAuth(adminKeyId, adminSecret), verify=True)

        body = json.loads(str(res.content, 'utf-8'))
        if not (res.ok and body['connectionStatus'] == "offline"):
            print(red("Sensor offline status update: FAILED!"))
            sys.exit(1)
        else:
            print(blue("Sensor offline status update: PASSED"))

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        global config
        global testCounter

        data = json.loads(str(msg.payload, 'utf-8'))
        # print("Data received @ topic: ", str(msg.topic) + " <= ", str(data))

        prop = str(msg.topic).split('/')[-1]
        if (prop == 'config'):
            config = data
        elif (prop == 'command' and data == 'run'):
            mytimer.cancel()
            print(blue("Sending data to device over MQTT: PASSED {}/{}".format((TOTAL_TRIES + 1) - testCounter, TOTAL_TRIES)))
            testCounter -= 1
            
            # now = datetime.datetime.utcnow().replace(microsecond=0).replace(tzinfo=datetime.timezone.utc).isoformat()
            # print("{} {}".format(now, str(data)))

    def on_subscribe(client, userdata, mid, granted_qos):
        # print("Subscription is complete")
        pass

    def on_publish(client, userdata, mid):
        # print("Data successfully sent")
        pass

    client = mqtt.Client(client_id=deviceId, clean_session=True, userdata=deviceId, protocol=MQTTv311)

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_publish = on_publish

    client.username_pw_set(username=deviceKeyId, password=deviceKeySecret)
    client.connect_async(ConnioMqttEndpoint, 1883, 30)

    client.loop_start()

    time.sleep(5)

    while config['forever']:
        now = datetime.datetime.utcnow().replace(microsecond=0).replace(tzinfo=datetime.timezone.utc).isoformat()

        data = json.dumps({'dps': [ 
            { 'method': 'mkSqThenStr', 'value': [4,45] },
            { 'method': 'mkStr', 'value': 4 }
        ]})
        client.publish("connio/data/out/devices/{}/methods/json".format(deviceId), data)

        # # Test writing multiple data points in JSON encoding
        # data = json.dumps({'dps': [ 
        #     { 'v': 52.1, 't': now, 'prop': 'reading' },
        #     { 'v': '52.1', 't': now, 'prop': 'reading' },
        # ]})
        # client.publish("connio/data/out/devices/{}/json".format(deviceId), data)

        # # Test writing single data point into single property
        # client.publish("connio/data/out/devices/{}/properties/reading".format(deviceId), 60.1)

        # # Test that invalid packets/data doesn't break mqtt streams
        # data = json.dumps({'dps': [ 
        #     { 'v': 52.1, 't': '2000-00-00T00:00:00.786Z', 'prop': 'reading' }
        # ]})
        # client.publish("connio/data/out/devices/{}/json".format(deviceId), data)

        # # Test method execution over mqtt
        # client.publish("connio/data/out/devices/{}/methods/mkSqThenStr".format(deviceId), 7)

        # # Test method execution over mqtt using JSON encoding
        # data = json.dumps({'dps': [ 
        #     { 'method': 'mkSqThenStr', 'value': 6 }
        # ]})
        # client.publish("connio/data/out/devices/{}/methods/json".format(deviceId), data)

        # # Test wether Gateway can write on behalf of child device
        # client.publish("connio/data/out/devices/{}/properties/reading".format(childDeviceId), 6.9)

        # if testCounter > 0:
        #     # duration is in seconds
        #     mytimer = Timer(config['timeout'], sending_timeout)
        #     mytimer.start()

        #     url = "{0}/v3/data/devices/{1}/properties/command".format(ConnioAPIEndpoint, deviceId)
        #     res = requests.post(url, auth=HTTPBasicAuth(apiclient.apikey.id, apiclient.apikey.secret), json={ 'dps': [ { 'v':  'run', 't': now } ]}, verify=True)

        #     # For successful API call, response code will be 200 (OK)
        #     body = json.loads(str(res.content, 'utf-8'))
        #     if (res.ok and body['accepted'] == 1):                
        #         print(teal('Command successfully sent'))
        #     else:
        #         res.raise_for_status()
        #         sys.exit(1)

        # elif testCounter == 0:
        #     url = "{0}/v3/devices/{1}".format(ConnioAPIEndpoint, deviceId)
        #     res = requests.put(url, auth=HTTPBasicAuth(adminKeyId, adminSecret), json={ 'status': 'disabled' }, verify=True)
        #     if (res.ok):
        #         print(teal('Device disabled'))
        #         break
        #     else:
        #         print(red('Device disabling: FAILED!'))
        #         res.raise_for_status()
        #         sys.exit(1)

        time.sleep(config['frequency'])

    client.loop_stop()
    client.disconnect()

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
    token = sysclient.accounts.create(name=accountName, tags=['test'], userInfo=UserInfo(email="admin4884848@{}.com".format(accountName), role='admin', name="admin"))
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
        except ConnioRestException as ce:
            print(ce)
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
                                                tags=['test', 'mqtt'],
                                                device_class='Test',
                                                product_name='Test01',
                                                vendor_name='Test01'
                                                )

    # Create new device profile for child device
    sensorprof = client.account.deviceprofiles.create(name='Sensor', friendly_name='Sensor', base_profile='connecteddevice')
    client.account.properties(sensorprof.id).create(name='reading', data_type='number', access_type='protected', publish_type='never')

    print(teal("Device profile successfully created"))

    # Add property to the device profile
    client.account.properties(devprof.id).create(name='config', data_type='object', access_type='public', publish_type='always', description='{ "frequency": 5, "forever": true, "timeout": 15 }')
    client.account.properties(devprof.id).create(name='reading', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(devprof.id).create(name='readingSq', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(devprof.id).create(name='command', data_type='enum', access_type='public', publish_type='always', boundaries={'set': ['run', 'stop', 'idle']})

    print(teal("Properties successfully created"))

    # Add method to the device profile
    impl = MethodInstance.MethodImplementation(body="let v = value[0] * value[1]; Device.api.setProperty('readingSq', { value: v.toString(), time: new Date().toISOString() }).then(property => {done(null, v.toString());});", lang="javascript")    
    impl2 = MethodInstance.MethodImplementation(body="let v = value; Device.api.setProperty('readingSq', { value: v.toString(), time: new Date().toISOString() }).then(property => {done(null, v.toString());});", lang="javascript")    
    client.account.methods(devprof.id).create(name='mkSqThenStr', access_type='protected', method_impl=impl)
    client.account.methods(devprof.id).create(name='mkStr', access_type='private', method_impl=impl2)

    print(teal("Method successfully created"))

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

    try:
        apiclient = wireup(adminclient)
    except Exception as e:
        print(red("Account wiring: FAILED!"))
        print(e)
        sys.exit(1)

    try:
        # duration is in seconds
        mytimer = Timer(10, provisioning_timeout)
        mytimer.start()
        provision(apiclient.apikey.id, apiclient.apikey.secret, cidType, cid)
    except Exception as e:
        print(red("Provisioning: FAILED!"))
        print(e)
        sys.exit(1)

    connectConnio(apiclient, adminclient.username, adminclient.password)

    # Make sure that device is in connected status
    url = "{0}/v3/data/devices/{1}".format(ConnioAPIEndpoint, deviceId)
    res = requests.get(url, auth=HTTPBasicAuth(apiclient.apikey.id, apiclient.apikey.secret), verify=True)

    body = json.loads(str(res.content, 'utf-8'))
    if not (res.ok and body['connectionStatus'] == "offline"):
        print(red("Device status check: FAILED! [Offline status expected]"))
        sys.exit(1)

    teardown(sysclient, accountName)