
import json
import datetime
import os, sys, inspect
import time
from six import u

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from connio.mqtt import Session
from connio.mqtt import CidMap
from connio.mqtt import MqttConnInfo
from connio.mqtt import DeviceIdentity

def _teal(words):
    return u("\033[36m\033[49m%s\033[0m") % words
def _blue(words):
    return u("\033[34m\033[49m%s\033[0m") % words
 
def onConnected(connection):
    print(_teal("Successfully connected to Connio"))
#     connection.subscribe("connio/data/in/devices/_dev_539414515237677974/properties/yeniisemrigirildi")
#     connection.subscribe("connio/data/in/devices/_dev_539414515237677974/properties/#")
    connection.subscribe("ttamp/#")
#     connection.subscribe("podgroup/apps/carrierwatchdog/devices/#")
#     connection.subscribe("podgroup/devices/modbus2/#")


def onMsgReceived(topic, data):
    property = topic.split('/')[-1]
    device = topic.split('/')[-3]
    print(_blue("Device: {}:{} <= {}".format(device, property, data)))
    
def listen(connection):
    while True:
        print(_blue("•"))
        time.sleep(60)
        

if __name__ == '__main__':

    # Default is our test environment
    # BROKER_ADDR = os.environ.get("CONNIO_BROKER_ADDR", "mqtt.connio.cloud")
    BROKER_ADDR = os.environ.get("CONNIO_BROKER_ADDR", "mqtt.skywaveiot.com")

    # Provisioning credentials
#     apicliId = os.environ.get("CONNIO_APICLIENT_ID", "_dev_539414515237677974")
#     apicliKeyId = os.environ.get("CONNIO_APICLIENT_KEY_ID", "_key_539414515590026134")
#     apicliKeySecret = os.environ.get("CONNIO_APICLIENT_KEY_SECRET", "70003500a4a740ae9399d2769d117035")

    apicliId = os.environ.get("CONNIO_APICLIENT_ID", "_bridge_werwrew")
    apicliKeyId = os.environ.get("CONNIO_APICLIENT_KEY_ID", "burrard")
    apicliKeySecret = os.environ.get("CONNIO_APICLIENT_KEY_SECRET", "burrard")


    session = Session()

    # Connect with device credentials
    mqttConnInfo = MqttConnInfo(BROKER_ADDR, apicliId, apicliKeyId, apicliKeySecret)
    connection = session.connect(mqttConnInfo, onConnected, onMsgReceived)

    # Start your data read & write loop
    connection.start_loop(listen)
