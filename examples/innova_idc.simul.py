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
import random

writeSettings = { 'frequency': 20, 'forever': True  }
deviceId = None
config = ''

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
    while writeSettings.get('forever', True):
        # now = datetime.datetime.utcnow().replace(microsecond=0).replace(tzinfo=datetime.timezone.utc).isoformat()

        data = json.dumps({'dps': [ 
            # { 'method': 'setSerialNumber', 'value': [ 68, 69, 78, 69, 77, 69, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] },
            # { 'method': 'setLogikaModel', 'value': [ 2, 161 ] },
            # { 'method': 'setLogikaFwVersion', 'value': [ 3, 1 ] },
            # { 'method': 'setAlarms', 'value': [0,0,0,2,0,0,0,0] },
            # { 'method': 'setNonAckAlarms', 'value': [0,0,0,2,0,0,0,0] },
            # { 'method': 'setScrewTemperature', 'value': [1, 4] },
            # { 'method': 'setWorkingPressure', 'value': [ 0, 21 ] },
            # # { 'method': 'setAuxiliaryPressure', 'value': 68.1 },            
            # { 'method': 'setTotalLoadHours', 'value': [15, 34] },
            # { 'method': 'setTotalHours', 'value': [34, 56] },
            # { 'method': 'setCompressorState', 'value': [ 0, 13 ] },
            # { 'method': 'setControllerState', 'value': [ 0, 5 ] },
            # { 'method': 'setCompressorState', 'value': [ 0, 11 ] }
        ]})
        # connection.publish("connio/data/out/devices/{}/methods/json".format(deviceId), data)
               
        # payload = json.dumps(reading)        
        # connection.publish("connio/data/out/devices/{}/methods/parseReading".format(deviceId), payload)

        #connection.publish("connio/data/out/devices/{}/properties/cfgReleaseNo".format(deviceId), "23.233")

        print(_blue("•"))
        time.sleep(writeSettings.get('frequency', 5))
        

if __name__ == '__main__':

    # Default is our test environment
    BROKER_ADDR = os.environ.get("CONNIO_BROKER_ADDR", "mqtt.skywaveiot.com")

    # Provisioning credentials
    username = os.environ.get("CONNIO_PROVISION_KEY_ID", "_key_535199912233292681")
    password = os.environ.get("CONNIO_PROVISION_KEY_SECRET", "3f5aa9fe100d4e2282acbae9492ab78b")

    cid = os.environ.get("CONNIO_DEVICE_SN", "C001-001")
    cidMap = CidMap("sn", cid)

    session = Session()

    # broker_port = 30001
    broker_port = 1883

    # Provision the device
    deviceIdentity = session.provision(MqttConnInfo(BROKER_ADDR, "_???_" + str(random.randint(11111111,99999999)), username, password, broker_port), cidMap, "modbus_settings")
    
    # Connect with device credentials
    mqttConnInfo = MqttConnInfo(BROKER_ADDR, deviceIdentity.id, deviceIdentity.keyId, deviceIdentity.keySecret)
    connection = session.connect(mqttConnInfo, onConnected, onMsgReceived, onConfigUpdated)

    deviceId = deviceIdentity.id

    # Set configuration settings as returned from the platform - if any
    config = session.config  or config

    # Start your data read & write loop
    connection.start_loop(readAndWrite)

    #40.36666 49.83518
    #869867035753377