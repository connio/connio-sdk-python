import paho.mqtt.client as mqtt
from paho.mqtt.client import connack_string
from paho.mqtt.client import MQTTv311
import json


MqttClientID="_???_11111111111"
UserName="_key_382212017171338747"
Password="162d97594bb04b4db4bc8195b91e2949"


# INNOVA

# MqttClientID="_???_11111111111"
# UserName="_key_300296630590587668"
# Password="296582a04af241eb99fde15014423683"

# MqttClientID="_???_3bad22ba52ad482992"
# UserName="_key_359151487716885388"
# Password="6e9304012a024979b2a8db96e8043773"

# MqttClientID="_bridge_2345345435345"
# UserName="burrard"
# Password="burrard"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + connack_string(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")
    client.subscribe("connio/provisions/{}".format(MqttClientID))

def on_disconnect(client, userdata, rc):
    print("Connection is lost: " + connack_string(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" " + str(msg.payload))
    client.disconnect()

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscription is complete")

    payload = json.dumps({'mac': '16:b4:12:7d:5d:da'})

    #innova
    #payload = json.dumps({'mac': '2c:4d:54:42:f1:a8'})
    client.publish("connio/provisions", payload)

def on_publish(client, userdata, mid):
    print("Publish is complete")

client = mqtt.Client(client_id=MqttClientID, clean_session=True, userdata=None, protocol=MQTTv311)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_publish = on_publish

client.username_pw_set(username=UserName, password=Password)
client.connect_async("mqtt.connio.cloud", 1883, 60)

#Innova
#client.connect_async("mqtt3.inv.connio.net", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()