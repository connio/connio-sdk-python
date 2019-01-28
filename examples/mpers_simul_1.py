import paho.mqtt.client as mqtt
from paho.mqtt.client import connack_string
from paho.mqtt.client import MQTTv311

import json
import datetime
import os
import time
import pytz

deviceId = None
deviceKeyId = None
deviceKeySecret = None

# Connio master
# ConnioMqttBroker = "mqtt.connio.cloud"

# Connio new branch
ConnioMqttBroker = "206.189.78.2"

config = { 'frequency': 3, 'fall_detected': False, 'within_coordinates': True, 'forever': True }

def provision(userName, password, cidType, cidVal):
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
        #config = response.get('config')

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
    client.connect_async(ConnioMqttBroker, 1883, 60)

    client.loop_forever()

#
#
#

in_coordinates = [ { 'lon': -123.09333086013793, 'lat': 49.341845664081426 },
                    { 'lon': -123.09131383895873, 'lat': 49.34385883346321 },
                    { 'lon': -123.08987617492676, 'lat': 49.34623538575055 },
                    { 'lon': -123.08820247650146, 'lat': 49.34897526827763 },
                    { 'lon': -123.09189319610596, 'lat': 49.349646236657904 },
                    { 'lon': -123.0951976776123, 'lat': 49.349674193475146 },
                    { 'lon': -123.09536933898926, 'lat': 49.348304290746306 },
                    { 'lon': -123.09536933898926, 'lat': 49.346906391497846 },
                    { 'lon': -123.09279441833496, 'lat': 49.34687843310774 },
                    { 'lon': -123.09399604797363, 'lat': 49.345396615697574 },
                    { 'lon': -123.09511184692383, 'lat': 49.344194353686056 }
     ]

out_coordinates = [ { 'lon': -123.18042755126952, 'lat': 49.34067127723991 } ]

def connectConnio():
    print('Connecting as....... {} : {} : {}'.format(deviceId, deviceKeyId, deviceKeySecret))

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, deviceId, flags, rc):       
        client.subscribe("connio/data/in/devices/{}/#".format(deviceId))

    def on_disconnect(client, userdata, rc):
        print("Connection is lost: " + connack_string(rc))

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        global config

        data = json.loads(msg.payload)
        print("Data received @ topic: ", str(msg.topic) + " <= ", str(data))

        prop = str(msg.topic).split('/')[-1]
        if (prop == 'config'):
            config = data
        elif (prop == 'signage'):
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~                                              ~")
            print("~                                              ~")
            print("~                                              ~")
            print("\t{}".format(str(data)))
            print("~                                              ~")
            print("~                                              ~")
            print("~                                              ~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

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
    client.connect_async(ConnioMqttBroker, 1883, 30)

    client.loop_start()

    time.sleep(10)

    counter = 0
    while config['forever']:
        #now = datetime.datetime.now(pytz.timezone('UTC')).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        now = datetime.datetime.utcnow().replace(microsecond=0).replace(tzinfo=datetime.timezone.utc).isoformat()

        # currCoord = out_coordinates[0]
        # if config['within_coordinates'] == True:
        #     currCoord = in_coordinates[counter % len(in_coordinates)]
        #     counter += 1

        # geo = { 'zone': 'Fall location', 'geo': {'lat': currCoord['lat'], 'lon': currCoord['lon']} }

        # #if fall detected send the location info
        # if config['fall_detected'] == True:
        #     data = json.dumps({'dps': [ 
        #         { 'v':  config['fall_detected'], 't': now, 'loc': geo, 'prop': 'fall_detected' },
        #         { 'v':  geo, 't': now, 'prop': 'coordinates' }
        #     ]})
        # else:
        #     data = json.dumps({'dps': [ 
        #         { 'v':  config['fall_detected'], 't': now, 'prop': 'fall_detected' },
        #         { 'v':  geo, 't': now, 'prop': 'coordinates' }
        #     ]})


        data = json.dumps({'dps': [ 
            { 'v':  52.1, 't': now, 'prop': 'temperature' }
        ]})

        # data = json.dumps({'dps': [ 
        #     { 'v':  '52.1', 't': '2000-00-00T00:00:00.786Z', 'prop': 'screw_temperature' }
        # ]})

        client.publish("connio/data/out/devices/{}/json".format(deviceId), data)
        time.sleep(config['frequency'])

    client.loop_stop()
        
#  # get the current date and time and set the publish payload
#  now = datetime.datetime.now(pytz.timezone(timezone)).strftime('%Y-%m-%dT%H:%M:%S.%f%z')
#  payload = json.dumps({'uid' : hexUID, 'name' : name, 'raceTime' : completionTime, 'createdDateTime' : now })

if __name__ == '__main__':        
    #cidType = 'imei'
    # cidType = 'mac'
    cidType = 'sn'

    # Connio master branch
    # userName = os.environ.get("CONNIO_PROVISION_KEY_ID", "_key_382212017171338747")         
    # password = os.environ.get("CONNIO_PROVISION_KEY_SECRET", "162d97594bb04b4db4bc8195b91e2949")

    # New branch Connio
    userName = os.environ.get("CONNIO_PROVISION_KEY_ID", "_key_490018762486950775")
    password = os.environ.get("CONNIO_PROVISION_KEY_SECRET", "a38af4722e314ce5975dc2373f53b3a9")

    cid = os.environ.get("CONNIO_DEVICE_CID", '1')
    # cid = os.environ.get("MAC_ADDRESS", "16:b4:12:7d:5d:da")
    # cid = os.environ.get("MAC_ADDRESS", "de:5b:53:76:9d:94")
    
    
    # ConnioMqttBroker = "127.0.0.1"
    # cidType = 'sn'
    # userName = os.environ.get("CONNIO_PROVISION_KEY_ID", "_key_428802386592272237")
    # password = os.environ.get("CONNIO_PROVISION_KEY_SECRET", "09e4b149a8b34a3c8c8a1a3d20258b55")
    # cid = os.environ.get("CONNIO_DEVICE_CID", 'SN-001-0023904')

    provision(userName, password, cidType, cid)
    connectConnio()

