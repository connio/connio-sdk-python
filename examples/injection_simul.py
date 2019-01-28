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
        # now = datetime.datetime.utcnow().replace(microsecond=0).replace(tzinfo=datetime.timezone.utc).isoformat()

        # data = json.dumps({'dps': [ 
        #     { 'method': 'setScrewTemperature', 'value': 620 },
        #     { 'method': 'setWorkingPressure', 'value': 78.3 },
        #     { 'method': 'setAuxiliaryPressure', 'value': 68.1 },
        #     { 'method': 'setAlarms', 'value': [0,0,0,0] },
        #     { 'method': 'setNonAckAlarms', 'value': [0,0,0,0] },
        #     { 'method': 'setLoadHours', 'value': [15,34] },
        #     { 'method': 'setTotalHours', 'value': [34,56] },
        #     { 'method': 'setCompressorState', 'value': 11 },
        #     { 'method': 'setControllerState', 'value': 5 },
        # ]})
        # connection.publish("connio/data/out/devices/{}/methods/json".format(deviceId), data)
               
        # # payload = json.dumps(reading)        
        # # connection.publish("connio/data/out/devices/{}/methods/parseReading".format(deviceId), payload)

        # connection.publish("connio/data/out/devices/{}/properties/cfgReleaseNo".format(deviceId), "23.233")

        print(_blue("•"))
        time.sleep(config['frequency'])
        

if __name__ == '__main__':

    # Default is our test environment
    BROKER_ADDR = os.environ.get("CONNIO_BROKER_ADDR", "mqtt.connio.cloud")

    # Provisioning credentials
    username = os.environ.get("CONNIO_PROVISION_KEY_ID", "_key_508527076699268740")
    password = os.environ.get("CONNIO_PROVISION_KEY_SECRET", "6c8b33008f7b465084c926b221487e6c")

    # Account wide unique device id, could be sn, mac, imei, esn, or cid
    cid = os.environ.get("CONNIO_DEVICE_CID", "1450-1")    
    cidMap = CidMap("sn", cid)

    session = Session()

    # Provision the device
    deviceIdentity = session.provision(MqttConnInfo(BROKER_ADDR, "_???_01234567891234567890", username, password), cidMap)

    # Connect with device credentials
    mqttConnInfo = MqttConnInfo(BROKER_ADDR, deviceIdentity.id, deviceIdentity.keyId, deviceIdentity.keySecret)
    connection = session.connect(mqttConnInfo, onConnected, onMsgReceived, onConfigUpdated)

    deviceId = deviceIdentity.id

    # Set configuration settings as returned from the platform - if any
    config = session.config  or config

    # Start your data read & write loop
    connection.start_loop(readAndWrite)