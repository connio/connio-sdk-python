
# Copyright (c) 2014-2018 Connio Inc.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# and Eclipse Distribution License v1.0 which accompany this distribution.
#
# The Eclipse Public License is available at
#    http://www.eclipse.org/legal/epl-v10.html
# and the Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Connio SDK Team

"""
This is a Connio MQTT v3.1 client module. MQTT is a lightweight pub/sub messaging
protocol that is easy to implement and suitable for low powered devices.
"""

import paho.mqtt.client as mqtt
from paho.mqtt.client import connack_string
from paho.mqtt.client import MQTTv311

import json
from six import u

from threading import Timer

def _red(words):
    return u("\033[31m\033[49m%s\033[0m") % words
def _teal(words):
    return u("\033[36m\033[49m%s\033[0m") % words
def _white(words):
    return u("\033[37m\033[49m%s\033[0m") % words
def _blue(words):
    return u("\033[34m\033[49m%s\033[0m") % words

class CidMap:
    def __init__(self, typ, id):
        self.type = typ
        self.id = id

class DeviceIdentity:
    def __init__(self, id, keyId, keySecret):
        self.id = id
        self.keyId = keyId
        self.keySecret = keySecret       

class MqttConnInfo:
    def __init__(self, brokerAddr, clientId, username, password, brokerPort = 1883):
        self.brokerAddr = brokerAddr
        self.brokerPort = brokerPort
        self.clientId = clientId
        self.username = username
        self.password = password

class Session(object):
    class Connection:
        def __init__(self, client):
            self._client = client
        
        def publish(self, topic, data):
            self._client.publish(topic, data)

        def subscribe(self, topic):
            self._client.subscribe(topic)

        def start_loop(self, loopingFn):
            self._client.loop_start()
            loopingFn(self)
            self._client.loop_stop()


    def __init__(self):
        self._timer = None
        self.configPropertyName = None

    def _provisionTimedout(self):
        print(_red("Provisioning timed out! See https://docs.connio.com/docs/provisioning for details."))
        
    def provision(self, mqttConnInfo, cidMap, cfgPropName=None, timeout=10):
        self.timer = Timer(timeout, self._provisionTimedout)
        self.timer.start()

        self.configPropertyName = cfgPropName

        # The callback for when the client receives a CONNACK response from the server.
        def on_connect(client, userdata, flags, rc):
            print(_teal("MQTT Broker returned connection result: " + connack_string(rc)))
            # Subscribing in on_connect() means that if we lose the connection and
            # reconnect then subscriptions will be renewed.            
            client.subscribe("connio/provisions/{}".format(mqttConnInfo.clientId))

        def on_disconnect(client, userdata, rc):            
            client.loop_stop()

        # The callback for when a PUBLISH message is received from the server.
        def on_message(client, userdata, msg):
            self.timer.cancel()           
            client.disconnect()    

            response = json.loads(str(msg.payload, 'utf-8'))

            self.deviceId = response.get('deviceId')
            self.deviceKeyId = response.get('apiKeyId')
            self.deviceKeySecret = response.get('apiSecret')
            self.config = response.get(cfgPropName)

            print(_blue("Device provisioning is complete"))

        def on_subscribe(client, userdata, mid, granted_qos):
            payload = json.dumps({cidMap.type: cidMap.id, 'configProperty': cfgPropName})   
            client.publish("connio/provisions", payload)

        def on_publish(client, userdata, mid):
            pass

        client = mqtt.Client(client_id=mqttConnInfo.clientId, clean_session=True, userdata=None, protocol=MQTTv311)

        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.on_message = on_message
        client.on_subscribe = on_subscribe
        client.on_publish = on_publish

        client.username_pw_set(username=mqttConnInfo.username, password=mqttConnInfo.password)
        client.connect_async(mqttConnInfo.brokerAddr, mqttConnInfo.brokerPort, 60)

        client.loop_forever()
        return DeviceIdentity(self.deviceId, self.deviceKeyId, self.deviceKeySecret)

    def connect(self, mqttConnInfo, onConnected, onMessageReceived, onConfigUpdated = None):        
        def on_connect(client, connection, flags, rc):       
            onConnected(connection)

        def on_disconnect(client, connection, rc):
            print(_red("Connection with the broker is lost: " + connack_string(rc)))

        def on_message(client, connection, msg):
            data = json.loads(str(msg.payload, "utf-8"))
            
            prop = str(msg.topic).split('/')[-1]
            if (self.configPropertyName is not None and prop == self.configPropertyName and onConfigUpdated is not None):
                onConfigUpdated(data)
            else:
                onMessageReceived(str(msg.topic), data)

        def on_subscribe(client, connection, mid, granted_qos):
            pass

        def on_publish(client, connection, mid):
            pass

        client = mqtt.Client(client_id=mqttConnInfo.clientId, clean_session=True, userdata=self, protocol=MQTTv311)
        
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.on_message = on_message
        client.on_subscribe = on_subscribe
        client.on_publish = on_publish

        client.username_pw_set(username=mqttConnInfo.username, password=mqttConnInfo.password)
        client.connect_async(mqttConnInfo.brokerAddr, mqttConnInfo.brokerPort, 30)

        connection =  self.Connection(client)
        client.user_data_set(connection)

        return connection
