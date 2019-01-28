import os
import time
import getopt
import operator

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import requests
from requests.auth import HTTPBasicAuth

from connio.rest import Client
from connio.rest.api.v3.account import UserInfo
from connio.rest.api.v3.account import AccountInstance
from connio.base.exceptions import ConnioException
from connio.base.exceptions import ConnioRestException

from six import u
import json

def _teal(words):
    return u("\033[36m\033[49m%s\033[0m") % words
def _blue(words):
    return u("\033[34m\033[49m%s\033[0m") % words

from_host = "https://api3.inv.connio.net"

frmSys = Client(username="user", 
                    password="password",
                    sysadmin=True,
                    host=from_host)

def inspect_system():
    """
    Inspect the given system.
    """

    # List all master accounts
    print(_blue('Discovering master accounts on the source....'))

    masters = dict()
    
    sortedAccountList = sorted(frmSys.accounts.list(), key = operator.itemgetter('date_created'))

    no = 1
    for sysaccount in sortedAccountList:
        if sysaccount.status != 'closed': #and sysaccount.owner_account_id == None:
            master = frmSys.accounts.get(sysaccount.id).fetch()
            if sysaccount.status == 'suspended':
                print(_teal('{}. **Master account: {} [{}], {}'.format(no, master.name, master.id, master.date_created)))
                no += 1
                continue
            else:
                print(_teal('{}. Master account: {} [{}], {}'.format(no, master.name, master.id, master.date_created)))
                no += 1
            
            masters[master.id] = master.name            

            admin_key_id = None
            admin_key_secret = None
        
            # List all system users belong to this master
            sortedUserList = sorted(frmSys.users.list(account=sysaccount.name, status='confirmed'), key = operator.itemgetter('date_created'))
            usrno = 1
            for sysusr in sortedUserList:
                if sysusr.status == 'confirmed' and sysusr.role == 'admin' and sysusr.account_id == master.id and masters.get(sysusr.account_id) is not None:
                    print(_teal('\tAdmin user no {}. user: {} [{}]'.format(usrno, sysusr.email, sysusr.id)))
                    
                    admin_key_id = sysusr.apikey.id
                    admin_key_secret = sysusr.apikey.secret
                
                    usrno += 1
                
            try:
                fromCli = Client(username=admin_key_id, 
                                password=admin_key_secret,
                                host=from_host)

                inspect_account(fromCli)

            except ConnioRestException as ce:
                print(ce)
                continue

            except:
                print('Skipping account: {}'.format(sysaccount.name))
 

def inspect_account(fromCli):    
    sortedDPList = sorted(fromCli.account.deviceprofiles.list(), key = operator.itemgetter('date_created'))
    dpno = 1
    for dpf in sortedDPList:
        print(_teal('\t|-Device profile #{}. {}, {}, {}'.format(dpno, dpf.id, dpf.name, dpf.date_created)))
        dpno += 1

        mtdno = 1
        for mtd in fromCli.account.methods(dpf.id).stream():
            if mtd.inherited == False:
                print(_teal('\t|--Method #{}. {}, {}, {}'.format(mtdno, mtd.id, mtd.name, mtd.date_created)))
                mtdno += 1

    sortedAPList = sorted(fromCli.account.appprofiles.list(), key = operator.itemgetter('date_created'))
    apno = 1
    for apf in sortedAPList:
        print(_teal('\t|-App profile #{}. {}, {}, {}'.format(apno, apf.id, apf.name, apf.date_created)))
        apno +=1

    appno = 1
    for app in fromCli.account.apps.stream():
        print(_teal('\t|-App #{}. {}, {}, {}'.format(appno, app.id, app.name, app.date_created)))
        appno += 1

    devList = fromCli.account.devices.list()
    print(_teal('\t|-Number of devices {}'.format(len(devList))))

    # online = 0
    # offline = 0
    # devno = 1
    # try:
    #     for dev in fromCli.account.devices.stream():
    #         # if (devno % 50 == 0):
    #         #     text = input("prompt")

    #         try:    
    #             url = "{0}/v3/data/devices/{1}/state?header=false&meta=false&properties=connectionstatus&methods=&alerts=".format(from_host, dev.id)
    #             res = requests.get(url, auth=HTTPBasicAuth(fromCli.username, fromCli.password), verify=True)
    #             #print(_teal('\tDevice #{}. {}, {}, {}'.format(devno, dev.id, dev.name, dev.date_created)))
    #             body = json.loads(str(res.content, 'utf-8'))
    #             if res.ok and body['properties'][0].get('value') is not None and body['properties'][0]['value']['mostRecent'] == "online":
    #                 online += 1
    #             else:
    #                 offline += 1
    #             devno += 1

    #             time.sleep(.15)

    #         except:
    #             e = sys.exc_info()[0]
    #             print("******Exception {} at device no {} [{}]".format(e, devno, dev.id))        


    # except ConnioException as ce:
    #     print("****** Connio Exception {} at device no {}".format(ce, devno))
        
    # except:
    #     e = sys.exc_info()[0]
    #     print("******Exception {} at device no {}".format(e, devno))        

    # print(_teal('+++++Online: {} / Offline: {}'.format(online, offline)))

    apino = 1
    for api in fromCli.account.apps.stream():
        print(_teal('\t|-API Client #{}. {}, {}, {}'.format(apino, api.id, api.name, api.date_created)))
        apino += 1
        

def main(argv):
    try:
        inspect_system()
    except ConnioRestException as ce:
        print(ce)
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])