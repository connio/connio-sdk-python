import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from connio.mqtt import Session
from connio.mqtt import CidMap
from connio.mqtt import MqttConnInfo
from connio.mqtt import DeviceIdentity

from six import u

import json
import datetime
import os
import time

config = { 'frequency': 20, 'forever': True  }
deviceId = None

def _teal(words):
    return u("\033[36m\033[49m%s\033[0m") % words
def _blue(words):
    return u("\033[34m\033[49m%s\033[0m") % words
 
def onConnected(connection):
    connection.subscribe("connio/data/in/devices/{}/#".format(deviceId))

def onMsgReceived(property, data):
    print(_blue("{} <= {}".format(property, data)))
    
def onConfigUpdated(data):
    global config
    config = data

def readAndWrite(connection):
    while config['forever']:
        data = json.dumps({'dps': [ 
            { 'method': 'setTemperature', 'value': 620 }
        ]})
        #connection.publish("connio/data/out/devices/{}/methods/json".format(deviceId), data)
               
        # payload = json.dumps(reading)        
        # connection.publish("connio/data/out/devices/{}/methods/parseReading".format(deviceId), payload)

        #connection.publish("connio/data/out/devices/{}/properties/state".format(deviceId), "alarm")

        print(_blue("•"))
        time.sleep(config['frequency'])
        

if __name__ == '__main__':

    # Default is our test environment
    BROKER_ADDR = os.environ.get("CONNIO_BROKER_ADDR", "mqtt.connio.cloud")

    # Provisioning credentials
    username = os.environ.get("CONNIO_PROVISION_KEY_ID", "_key_499569128223998049")
    password = os.environ.get("CONNIO_PROVISION_KEY_SECRET", "0af19086c6a1485e890b996776bb58f0")

    # Account wide unique device id, could be sn, mac, imei, esn, or cid
    cid = os.environ.get("CONNIO_DEVICE_MAC", "16:b4:12:7d:5d:da")    
    cidMap = CidMap("mac", cid)

    session = Session()

    # Provision the device
    deviceIdentity = session.provision(MqttConnInfo(BROKER_ADDR, "_???_11111", username, password), cidMap)

    # Connect with device credentials
    mqttConnInfo = MqttConnInfo(BROKER_ADDR, deviceIdentity.id, deviceIdentity.keyId, deviceIdentity.keySecret)
    connection = session.connect(mqttConnInfo, onConnected, onMsgReceived, onConfigUpdated)

    deviceId = deviceIdentity.id

    # Set configuration settings as returned from the platform - if any
    config = session.config  or config

    # Start your data read & write loop
    connection.start_loop(readAndWrite)