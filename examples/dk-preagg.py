import requests
from requests.auth import HTTPBasicAuth

import operator
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from connio.rest import Client
from connio.base.exceptions import ConnioRestException

from six import u
import json
from threading import Timer

def _teal(words):
    return u("\033[36m\033[49m%s\033[0m") % words
def _blue(words):
    return u("\033[34m\033[49m%s\033[0m") % words

HOST = "https://api.connio.cloud"

apikeyID = ''
secret = ''

def preaggregate():
    try:
        client = Client(username=apikeyID, 
                        password=secret)

        sortedDevList = sorted(client.account.devices.list(), key = operator.itemgetter('date_created'))
        for dev in sortedDevList:
            print(_blue('Preaggregating device {}'.format(dev.name)))
            url = "{0}/v3/data/devices/{1}/methods/preaggregate".format(HOST, dev.name)

            payload = {  'value': '' }
            res = requests.post(url, auth=HTTPBasicAuth(client.username, client.password), json=payload, verify=True)

            # For successful API call, response code will be 200 (OK)
            # if(not res.ok):
            #     res.raise_for_status()

    except ConnioRestException as ce:
        print(ce)

    print(_teal('Preaggregation session is complete'))

#
#
#
def timeout():
    print("Preaggregating")
    preaggregate()

if __name__ == '__main__':
    print(_teal('Preaggregation started...'))

    # Default Dalgakiran
    apikeyID = os.environ.get('CONNIO_PREAGGREGATE_ACCOUNT_KEYID', '_key_500600814475760930')
    secret = os.environ.get('CONNIO_PREAGGREGATE_ACCOUNT_KEYSECRET', '0b51ab06dc554165bda3db495eb00737')

    preaggregate()

    # duration is in seconds
    mytimer = Timer(3600, timeout)
    mytimer.start()