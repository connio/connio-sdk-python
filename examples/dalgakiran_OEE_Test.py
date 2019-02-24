import requests
import datetime

device_username = "_key_565008250185037961"
device_password = "acf1bc536ffb44f0b0500a19383f48e7"

for x in range(15):
    time = datetime.datetime(2019,2,16,13,10+x).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    payload = {
    'value': {
        "value": [0,x],
        "time": time
        }
    }
    r = requests.post('https://api.connio.cloud:443/v3/data/devices/_this_/methods/setCompressorStateWithTime', auth=(device_username, device_password),json= payload)
    print(r.text)
