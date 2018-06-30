import paho.mqtt.client as mqtt
from paho.mqtt.client import connack_string
from paho.mqtt.client import MQTTv311
import json
import time
import numpy as np


MqttClientID="_dev_388993231801430353"
UserName="_key_388993231802932947"
Password="fe6359cc1d094a1cb2c60e55bf2d7b31"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + connack_string(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")
    client.subscribe("connio/data/in/devices/{}/#".format(MqttClientID))

def on_disconnect(client, userdata, rc):
    print("Connection is lost: " + connack_string(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):
    print('{}<-{}'.format(message.topic, str(message.payload)))
    # print("message topic=",message.topic)
    # print("message qos=",message.qos)
    # print("message retain flag=",message.retain)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscription is complete")

def on_publish(client, userdata, mid):
    print('{}. Publish is complete: {}'.format(mid, userdata))

client = mqtt.Client(client_id=MqttClientID, clean_session=True, userdata=None, protocol=MQTTv311)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_publish = on_publish

client.username_pw_set(username=UserName, password=Password)
client.connect_async("mqtt.connio.cloud", 1883, 60)

# client.loop_forever()

client.loop_start()

Fs = 8000
f = 5
sample = 8000
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)

for val in y:
    client.publish("connio/data/out/devices/{}/properties/temperature".format(MqttClientID), val)
    time.sleep(.5)

client.loop_stop()

client.disconnect()