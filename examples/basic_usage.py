import os
import time

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from connio.rest import Client

ACCOUNT_KEYID = os.environ.get('CONNIO_ACCOUNT_KEYID')
ACCOUNT_KEYSECRET = os.environ.get('CONNIO_ACCOUNT_KEYSECRET')

def example():
    """
    Some example usage of different connio resources.
    """

    client = Client(username="_key_379761022028664872", 
                    password="74adb3d7737f458eaa15880ee464b3e0")

    # client = Client(username="_key_380424795492783152", 
    #                 password="dee3dac1a9b54078b0a4d4796ba9e210",
    #                 host="http://localhost:8081")

    master = client.accounts.get().fetch()
    #master2 = client.account.fetch()
    
    #.get().fetch()
    print('Master account: ' + master.name)
    #print('Master  2 account: ' + master2.name)

    # for i in range(1, 51):
    #     newSub = client.accounts.create(name='SubAcccc.' + str(i))
    #     print('New subaccount name: ' + newSub.name + ', id: ' + newSub.id)
          # time.sleep(.250)

    # for i in range(5001, 10001):
    #     device = client.account.devices.create(name='DeviceT.{}'.format(i), profile='connecteddevice')
    #     print('New device: {}, {}'.format(device.id, device.name))
        
    no = 1
    for acc in client.accounts.stream(status='open', limit=25, page_size=5):
        print(str(no) + '. ' + acc.name + ' - ' + acc.status + ' @ ' + acc.date_created)
        no = no + 1

    no = 1
    for usr in client.account.users.stream():
        print('No {}. User: {}, {}, {}, {}'.format(no, usr.id, usr.name, usr.email, usr.date_created))
        no += 1

    # no = 1
    # for apicli in client.account.apiclients.stream():
    #     client.account.apiclients.create(name="SSSSSS" + apicli.name,
    #                                     friendly_name=apicli.friendly_name,
    #                                     description=apicli.description,
    #                                     tags=apicli.tags,
    #                                     context=apicli.apikey.context,
    #                                     scope=apicli.apikey.scope,
    #                                     )

    # client.account.apiclients.create(name="TestApiClient",
    #                                 friendly_name="Test Api Client",
    #                                 description="My Test",
    #                                 tags=['test'],
    #                                 context={'type': "account", 'ids': [master.id]},
    #                                 scope=['device:read'],
    #                                 )
                                         
    # for apicli in client.account.apiclients.stream():
    #     apicli.delete()

    no = 1
    for apicli in client.account.apiclients.stream():
        print('No {}. API Client: {}, {}, {}, {}, {} req/min'.format(no, apicli.id, apicli.name, apicli.date_created, apicli.apikey.id, apicli.apikey.rate_limit))
        no += 1

    # dp = client.account.deviceprofiles.create(name='Compressor3', base_profile='ConnectedDevice')
    # dp = client.account.deviceprofiles.get('compressor3').fetch()
    # prop = client.account.properties(dp.id).create(name='temperature6', data_type='number', access_type='protected', publish_type='always')

    # original = client.account.deviceprofiles.get('compressor3').fetch()
    # target = client.account.deviceprofiles.create(name='Compressor_Clone6', 
    #                                               friendly_name=original.friendly_name,
    #                                               base_profile=original.base_profile_id,
    #                                               description=original.description,
    #                                               tags=original.tags,
    #                                               device_class=original.device_class,
    #                                               product_name=original.product_name,
    #                                               vendor_name=original.vendor_name
    #                                             )

    # time.sleep(3)

    # for prp in client.account.properties(original.id).stream():
    #     if prp.owner_id == original.id:            
    #         client.account.properties(target.id).create(name=prp.name,
    #                                                     friendly_name=prp.friendly_name,
    #                                                     description=prp.description,
    #                                                     tags=prp.tags,
    #                                                     data_type=prp.data_type, 
    #                                                     access_type=prp.access_type, 
    #                                                     publish_type=prp.publish_type,
    #                                                     # retention=prp.retention
    #                                                 )
        


    # time.sleep(1)

    # no = 1
    # for dpf in client.account.deviceprofiles.stream():
    #     print('Device profile {}. Device Profile: {}, {}, {}'.format(no, dpf.id, dpf.name, dpf.date_created))
    #     pno = 1
    #     props = client.account.properties(dpf.id)
    #     for prp in props.stream():
    #         print('Prop #{}. Property of {}: {}, {}, {}, {}, {}'.format(pno, dpf.id, prp.id, prp.name, prp.inherited, prp.access_type, prp.date_created))
    #         pno += 1
    #     no += 1

    # no = 1
    # for dev in client.account.devices.stream(page_size=150,limit=5):
    #     print('No {}. Device: {}, {}, {}'.format(no, dev.id, dev.name, dev.date_created))
    #     no += 1

    # no = 1
    # for apf in client.account.appprofiles.stream():
    #     print('No {}. App Profile: {}, {}, {}'.format(no, apf.id, apf.name, apf.date_created))
    #     no += 1

    # no = 1
    # for app in client.account.apps.stream():
    #     print('No {}. App: {}, {}, {}'.format(no, app.id, app.name, app.date_created))
    #     no += 1

    # subaccounts = client.accounts.stream(limit=100, page_size=3)
    # for a in subaccounts:        
    #     print(a.name + ' - ' + a.status)

        # a.delete()
        # subaccount = client.accounts.get(a.id)
        # subaccount.delete()

    # accounts = client.subaccounts.page(page_number=3, page_size=1)

    # for a in accounts:
    #     print(a.name)

    # g = accounts.pop()

    #p = l.get_page


    # myaccount = client.api.v3.account
    
    # myaccount.update('Test Account')
    
    # accountInfo = myaccount.fetch()
    
    # print('Account id: ' + accountInfo.id + ', ' + accountInfo.friendly_name + ', ' + accountInfo.date_created)


    # # Get all messages
    # all_messages = client.messages.list()
    # print('There are {} messages in your account.'.format(len(all_messages)))

    # # Get only last 10 messages...
    # some_messages = client.messages.list(limit=10)
    # print('Here are the last 10 messages in your account:')
    # for m in some_messages:
    #     print(m)

    # # Get messages in smaller pages...
    # all_messages = client.messages.list(page_size=10)
    # print('There are {} messages in your account.'.format(len(all_messages)))

    # print('Sending a message...')
    # new_message = client.messages.create(to='XXXX', from_='YYYY', body='Twilio rocks!')

    # print('Making a call...')
    # new_call = client.calls.create(to='XXXX', from_='YYYY', method='GET')

    # print('Serving TwiML')
    # twiml_response = VoiceResponse()
    # twiml_response.say('Hello!')
    # twiml_response.hangup()
    # twiml_xml = twiml_response.to_xml()
    # print('Generated twiml: {}'.format(twiml_xml))


if __name__ == '__main__':
    example()
