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
config = { 'frequency': 10, 'forever': True }

BROKER_ADDR = "mqtt.connio.cloud"
# BROKER_ADDR = "localhost"
BROKER_PORT = 1883

def provision(userName, password, cidType, cidVal):
    MqttClientID = "_???_SAA345678987654321"

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connection returned result: " + connack_string(rc))
        print("    Session present: " + str(flags['session present']))
        print("    Connection result: " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("connio/provisions/{}".format(MqttClientID))

    def on_disconnect(client, userdata, rc):
        print("Connection is lost: " + connack_string(rc))
        client.loop_stop()

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        print("Message received: \n@" + msg.topic + "\n" + str(msg.payload))
        
        response = json.loads(msg.payload.decode("utf8"))

        global deviceId 
        global deviceKeyId
        global deviceKeySecret
        global config

        deviceId = response.get('deviceId')
        deviceKeyId = response.get('apiKeyId')
        deviceKeySecret = response.get('apiSecret')
        config = response.get('config')

        client.disconnect()

    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscription is complete")

        # payload = json.dumps({cidType: cidVal, 'configProperty': 'config'})
        payload = json.dumps({cidType: cidVal})   
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
    client.connect_async(BROKER_ADDR, BROKER_PORT, 60)

    client.loop_forever()

#
#
#

def connect():    
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
        elif (prop == 'message' or prop == 'cmd'):
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
        print("Subscription is complete with QoS level {}".format(granted_qos))

    def on_publish(client, userdata, mid):
        print("Data successfully sent")

    client = mqtt.Client(client_id=deviceId, clean_session=True, userdata=deviceId, protocol=MQTTv311)

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_publish = on_publish

    client.username_pw_set(username=deviceKeyId, password=deviceKeySecret)
    client.connect_async(BROKER_ADDR, BROKER_PORT, 30)

    client.loop_start()

    global config

    if config is None:
        config = { 'forever': True, 'frequency': 10 }

    while config.get('forever', True):
        time.sleep(config.get('frequency', 5))

    client.loop_stop()
        
if __name__ == '__main__':    
    provisioningKeyId = os.environ.get("CONNIO_PROVISION_KEY_ID", "_key_499569128223998049")
    provisioningKeySecret = os.environ.get("CONNIO_PROVISION_KEY_SECRET", "0af19086c6a1485e890b996776bb58f0")
    
    cidType = os.environ.get("CONNIO_DEVICE_CID_TYPE", 'mac')
    cid = os.environ.get("CONNIO_DEVICE_CID_VALUE", '00:1e:c0:91:6e:0c')

    provision(provisioningKeyId, provisioningKeySecret, cidType, cid)
    connect()

