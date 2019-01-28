import os
import time
import getopt
import operator
from six import u
import json
import datetime

import requests
from requests.auth import HTTPBasicAuth

import paho.mqtt.client as mqtt
from paho.mqtt.client import connack_string
from paho.mqtt.client import MQTTv311

from threading import Timer

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from connio.rest import Client
from connio.base.exceptions import ConnioRestException
from connio.rest.api.v3.account import UserInfo
from connio.rest.api.v3.account.method import MethodInstance

 # HOST = "https://api.connio.cloud"
HOST = "http://206.189.78.2:8081"
MQTT_BROKER = "206.189.78.2"

deviceId = None
deviceKeyId = None
deviceKeySecret = None
config = None
mytimer = None

config = { 'frequency': 5, 'forever': True, 'timeout': 15 }

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
def timeout():
    print("Timer timout!!")
    url = "https://hooks.slack.com/services/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"
    requests.post(url, json={ 'text': 'SYSTEM ERR: {} MQTT LOOPBACK TEST FAILED!'.format(MQTT_BROKER)}, verify=True)

#
#
#
def cleanup(sysclient):
    sortedAccountList = sorted(sysclient.accounts.list(), key = operator.itemgetter('date_created'))

    for sysaccount in sortedAccountList:
        if sysaccount.name == "uat":
            testAccount = sysclient.accounts.get(sysaccount.id).fetch()
            testAccount.delete(True)

#
#
#
def teardown(sysclient):
    """
    
    """

    testAccount = sysclient.accounts.get("UAT").fetch()
    testAccount.delete(True)
    print(teal("\n~~ALL TESTS PASSED~~\n"))
    print("Test account is deleted successfully.")

#
#
#
def create_account(sysclient):
    """
    
    """

    # List all system users - use existing one, if any
    sortedUserList = sorted(sysclient.users.list(), key = operator.itemgetter('date_created'))
    for sysusr in sortedUserList:
        if sysusr.status == 'confirmed' and sysusr.role == 'admin' and sysusr.email == 'admin@uat.com':
            return Client(username=sysusr.apikey.id, 
                            password=sysusr.apikey.secret,
                            host=HOST)
    
    # Create a USER ACCEPTANCE TEST account if doesn't exist
    token = sysclient.accounts.create(name="UAT", tags=['UAT'], userInfo=UserInfo(email="admin@uat.com", role='admin', name="admin"))
    admin = sysclient.api.helpers.activate(token['token'])

    # Wait until activation is propagated
    time.sleep(4)
    
    admin.update(password='password')
    print("Test account is created successfully.")

    return Client(username=admin.apikey.id, 
                  password=admin.apikey.secret,
                  host=HOST)

#
#
#
def wireup(client):
     # Create new device profile
    devprof = client.account.deviceprofiles.create(name='TestProfile', 
                                                friendly_name='Test Profile',
                                                base_profile='Gateway',
                                                description='Some test profile',
                                                tags=['test', 'uat'],
                                                device_class='Test',
                                                product_name='Test01',
                                                vendor_name='Test01'
                                                )

    # Add property to the device profile
    client.account.properties(devprof.id).create(name='prop0', data_type='number', access_type='private', publish_type='never')
    client.account.properties(devprof.id).create(name='prop1', data_type='number', access_type='protected', publish_type='never')
    client.account.properties(devprof.id).create(name='prop2', data_type='string', access_type='protected', publish_type='never')
    client.account.properties(devprof.id).create(name='prop3', data_type='enum', access_type='protected', publish_type='never')
    client.account.properties(devprof.id).create(name='prop4', data_type='object', access_type='protected', publish_type='never')
    client.account.properties(devprof.id).create(name='prop5', data_type='blob', access_type='protected', publish_type='never')
    client.account.properties(devprof.id).create(name='prop6', data_type='waypoint', access_type='protected', publish_type='never')
    client.account.properties(devprof.id).create(name='prop7', data_type='boolean', access_type='protected', publish_type='never')
    client.account.properties(devprof.id).create(name='loopback-channel', data_type='number', access_type='public', publish_type='always')

    client.account.properties(devprof.id).create(name='config', data_type='object', access_type='public', publish_type='always', description='{ "frequency": 5, "forever": true, "timeout": 15 }')
    client.account.properties(devprof.id).create(name='text', data_type='string', access_type='public', publish_type='never')
    client.account.properties(devprof.id).create(name='bool', data_type='boolean', access_type='public', publish_type='never')
    client.account.properties(devprof.id).create(name='list1', data_type='enum', access_type='public', publish_type='never', boundaries={'set': ['opt1', 'opt2', 'opt3']})
    client.account.properties(devprof.id).create(name='list2', data_type='enum', access_type='public', publish_type='never', boundaries={'set': [1, 2, 3]})
    client.account.properties(devprof.id).create(name='loc', data_type='waypoint', access_type='public', publish_type='never')

    # Add method to the device profile
    impl1 = MethodInstance.MethodImplementation(body="let v = value * 2; Device.api.setProperty('prop2', { value: v.toString(), time: new Date().toISOString() }).then(property => {done(null, v.toString());});", lang="javascript")
    impl2 = MethodInstance.MethodImplementation(body="done(null, value * 2);", lang="javascript")
    impl3 = MethodInstance.MethodImplementation(body="Device.api.getProperty('prop0').then(p=>{done(null, p.value);})", lang="javascript")

    client.account.methods(devprof.id).create(name='method1', access_type='private', method_impl=impl1)
    client.account.methods(devprof.id).create(name='method2', access_type='protected', method_impl=impl2)
    client.account.methods(devprof.id).create(name='method3', access_type='public', method_impl=impl1)

    # Add alerts to the device profile
    # TBI

    # Create an app
    app = client.account.apps.create(name='TestApp',
                               profile='Sample',
                               friendly_name='My test app',
                               description='The test app',
                               tags=['test']
                              )

    # Create a provisioning key
    apicli = client.account.apiclients.create(name='ProvisioningClient',
                                    friendly_name='Provisioning Key',
                                    description='An API Client for device provisioning',
                                    tags=['provisioning'],
                                    context={'type': "app", 'ids': [app.id]},
                                    scope=['device:read'],
                                    )
    
    # Create new device
    for i in range(1, 5):
        device = client.account.devices.create(name='Device.{}'.format(i), 
                                            profile='testprofile',
                                            apps=[app.id],
                                            custom_ids={'sn': str(i)},
                                            status='debug'
                                            )                                
        print('New device: {}, {}'.format(device.id, device.name))

    for t in range(1, 2):
        new_devices = []
        for i in range(1, 1001):
            dev = { 'name': 'Device.Bulk.{}{}'.format(t,i),
                    'profile': 'testprofile',
                    'apps': [app.id],
                    'custom_ids': { 'sn': 'SN-{}-00{}'.format(t,i) }
                }
            new_devices.append(dev)

        client.account.devices.create_bulk(new_devices)
        print('Batch #{} created...'.format(t))
        time.sleep(.5) 

    # Wait until creation is complete
    print('Wait until device creation is complete...')
    time.sleep(5)            

    return apicli

#
#
#
def test_provisioning(apiclient):
    userName = apiclient.apikey.id
    password = apiclient.apikey.secret
    cidType = 'sn'
    cidVal = '1'
    MqttClientID = "_???_d111111111"

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connection returned result: " + connack_string(rc))
        print("    Session present: " + str(flags['session present']))
        print("    Connection result: " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        # client.subscribe("$SYS/#")
        client.subscribe("connio/provisions/{}".format(MqttClientID))

    def on_disconnect(client, userdata, rc):
        print("Connection is lost: " + connack_string(rc))
        client.loop_stop()

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        print("Message received: \n@" + msg.topic + "\n" + str(msg.payload))
        client.disconnect()    

        response = json.loads(msg.payload)

        global deviceId 
        global deviceKeyId
        global deviceKeySecret
        global config

        deviceId = response.get('deviceId')
        deviceKeyId = response.get('apiKeyId')
        deviceKeySecret = response.get('apiSecret')
        config = response.get('config')

    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscription is complete")

        payload = json.dumps({cidType: cidVal, 'configProperty': 'config'})   
        client.publish("connio/provisions", payload)

    def on_publish(client, userdata, mid):
        print("Publish is complete")

    client = mqtt.Client(client_id=MqttClientID, clean_session=True, userdata=None, protocol=MQTTv311)

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_publish = on_publish

    client.username_pw_set(username=userName, password=password)
    client.connect_async(MQTT_BROKER, 1883, 60)

    client.loop_forever()

#
#
#
def test_mqtt_connection(user):
    global mytimer
    global deviceId 
    global deviceKeyId
    global deviceKeySecret

    now = datetime.datetime.utcnow().replace(microsecond=0).replace(tzinfo=datetime.timezone.utc).isoformat()
    
    print('Connecting as....... {} : {} : {}'.format(deviceId, deviceKeyId, deviceKeySecret))

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, deviceId, flags, rc):       
        client.subscribe("connio/data/in/devices/{}/#".format(deviceId))

    def on_disconnect(client, userdata, rc):
        print("Connection is lost: " + connack_string(rc))

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        global config

        data = json.loads(str(msg.payload, 'utf-8'))
        print("Data received @ topic: ", str(msg.topic) + " <= ", str(data))

        prop = str(msg.topic).split('/')[-1]
        if (prop == 'config'):
            config = data
        elif (prop == 'loopback-channel'):            
            mytimer.cancel()           
            print("{} {}".format(now, str(data)))

    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscription is complete")

    def on_publish(client, userdata, mid):
        print("Data successfully sent")

    client = mqtt.Client(client_id=deviceId, clean_session=True, userdata=deviceId, protocol=MQTTv311)

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_publish = on_publish

    client.username_pw_set(username=deviceKeyId, password=deviceKeySecret)
    client.connect_async(MQTT_BROKER, 1883, 30)

    client.loop_start()

    time.sleep(1)

    while config['forever']:
        now = datetime.datetime.utcnow().replace(microsecond=0).replace(tzinfo=datetime.timezone.utc).isoformat()

        # duration is in seconds
        mytimer = Timer(config['timeout'], timeout)
        mytimer.start()

        url = "{0}/v3/data/devices/{1}/properties/loopback-channel".format(HOST, deviceId)
        res = requests.post(url, auth=HTTPBasicAuth(user.username, user.password), json={ 'dps': [ { 'v': 0, 't': now } ]}, verify=True)

        # For successful API call, response code will be 200 (OK)
        if(res.ok):
            time.sleep(config['frequency'])
        else:
            res.raise_for_status()

        data = json.dumps({'dps': [ 
            # { 'v':  '52.1', 't': '2000-00-00T00:00:00.786Z', 'prop': 'prop1' },
            { 'v':  '52.1', 't': now, 'prop': 'prop1' },
            { 'v':  52.1, 't': now, 'prop': 'prop1' }
        ]})

        client.publish("connio/data/out/devices/{}/json".format(deviceId), data)
        # client.publish("connio/data/out/devices/{}/json".format(deviceId), "{'t': }")

        data = json.dumps({'dps': [ 
            {'method': 'method3', 'value': 11 }
        ]})
        client.publish("connio/data/out/devices/{}/methods/json".format(deviceId), data)


        time.sleep(config['frequency'])

    client.loop_stop()

#
#
#
def test_rest_datawrite_compact(client):
    try:
        url = "{0}/v3/data/devices/{1}".format(HOST, 'Device.1')
        cfg = { 'frequency': 5, 'forever': True, 'timeout': 15 }
        payload = { 
            'config': cfg,
            'text': 'Hello World!',
            'bool': True,
            'list1': 'opt1',
            'list2': 1,
            'loc': { 'zone': 'Home'}
        }
        res = requests.post(url, auth=HTTPBasicAuth(client.username, client.password), json=payload, verify=True)

        # For successful API call, response code will be 200 (OK)
        if(not res.ok):
            res.raise_for_status()

        res = requests.get(url, auth=HTTPBasicAuth(client.username, client.password))

        # For successful API call, response code will be 200 (OK)
        if(not res.ok):
            res.raise_for_status()
        else:
            dev = res.json()
            assert (dev['config'] == payload['config']), red("** Assertion failed when comparing device data")
            assert (dev['text'] == payload['text']), red("** Assertion failed when comparing device data")
            assert (dev['bool'] == payload['bool']), red("** Assertion failed when comparing device data")
            assert (dev['loc'] == payload['loc']), red("** Assertion failed when comparing device data")
            assert (dev['list1'] == payload['list1']), red("** Assertion failed when comparing device data")
            assert (dev['list2'] == payload['list2']), red("** Assertion failed when comparing device data")
    except AssertionError as ae:
        print(ae)
        sys.exit(1)
    except ConnioRestException as ce:
        print(ce)
        sys.exit(1)

#
#
#
def test_rest_datawrite_feed(client):
    try:
        now = datetime.datetime.utcnow().replace(microsecond=0).replace(tzinfo=datetime.timezone.utc).isoformat()

        url = "{0}/v3/data/devices/{1}/properties".format(HOST, 'Device.1')
        cfg = { 'frequency': 5, 'forever': True, 'timeout': 15 }

        data = {'dps': [         
            { 'v':  cfg, 't': now, 'prop': 'config' },
            { 'v':  "Hello World!", 't': now, 'prop': 'text' },
            { 'v':  True, 't': now, 'prop': 'bool' },
            { 'v':  "opt1", 't': now, 'prop': 'list1' },
            { 'v':  1, 't': now, 'prop': 'list2' },
            { 'v':  { 'zone': 'Home'}, 't': now, 'prop': 'loc' }
        ]}

        res = requests.post(url, auth=HTTPBasicAuth(client.username, client.password), json=data, verify=True)

        # For successful API call, response code will be 200 (OK)
        if(not res.ok):
            res.raise_for_status()

        # res = requests.get(url, auth=HTTPBasicAuth(client.username, client.password))

        # # For successful API call, response code will be 200 (OK)
        # if(not res.ok):
        #     res.raise_for_status()
        # else:
        #     dev = res.json()
        #     assert (dev['config'] == data['dps'][0]['v']), red("** Assertion failed when comparing device data")
        #     assert (dev['text'] == data['dps'][1]['v']), red("** Assertion failed when comparing device data")
        #     assert (dev['bool'] == data['dps'][2]['v']), red("** Assertion failed when comparing device data")
        #     assert (dev['loc'] == data['dps'][3]['v']), red("** Assertion failed when comparing device data")
        #     assert (dev['list1'] == data['dps'][4]['v']), red("** Assertion failed when comparing device data")
        #     assert (dev['list2'] == data['dps'][5]['v']), red("** Assertion failed when comparing device data")
    except AssertionError as ae:
        print(ae)
        sys.exit(1)
    except ConnioRestException as ce:
        print(ce)
        sys.exit(1)

if __name__ == '__main__':
    SYSTEMADMIN_USER = os.environ.get('CONNIO_SYSTEMADMIN_USER', 'user')
    SYSTEMADMIN_PWD = os.environ.get('CONNIO_SYSTEMADMIN_PWD', 'password')

    sysclient = Client(username=SYSTEMADMIN_USER, 
                    password=SYSTEMADMIN_PWD,
                    sysadmin=True,
                    host=HOST)

    cleanup(sysclient)

    print(teal("~~ STARTING DATA API TESTS ~~"))

    client = create_account(sysclient)

    apiclient = wireup(client)

    test_rest_datawrite_compact(client)

    test_rest_datawrite_feed(client)

    test_provisioning(apiclient)

    test_mqtt_connection(client)

    # test_subaccount_operations(client)

    # test_user_operations(client)

    # test_deviceprofile_operations(client)

    # test_device_operations(client)

    # test_appprofile_operations(client)

    # test_app_operations(client)

    teardown(sysclient)
