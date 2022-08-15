# pip install conniosdk
from connio.rest import Client
from connio.rest.api.v3.account import device

HOST = "http://167.99.129.128:8081"
USERNAME = "_key_1391176590598140988"
PASSWORD = "c7bad986f0ea4a4099b7fdc3bf506b5b"

def example():
    client = Client(username=USERNAME,
                        password=PASSWORD, host=HOST)

    ## Get devices or apps as stream
    devices = client.account.devices.stream()
    apps = client.account.apps.stream()

    ## Get devices or apps as list
    devicesList = client.account.devices.list()
    appsList = client.account.apps.list()

    ## Get all names from stream
    deviceNames = list(device.name for device in devices) # ["device1", "device2"]
    appNames = list(app.name for app in apps)

    ## Get single device by id and get its state
    deviceById = client.account.devices("_dev_1127454099228059958")
    appById    = client.account.apps("_app_1275818358594712326")

    ## Get single device by name
    deviceByName = client.account.devices("FORMULA")
    appByName    = client.account.apps("Downtime")

    ## Reach device state
    state = deviceByName.state() # {"active": "---", "StationCode": 15}
    appState = appById.state()

    ## get current property value from state 
    property = state.get("active") # "---"
    appProperty =state.get("active")

    ## Query Historical property values
    queryResult = deviceByName.read_property_historical("active",{ })# Query object: https://docs.connio.com/reference/querying-historical-data
    appQueryResult = appByName.read_property_historical("active",{ })
    # Example Output: {'sampleSize': 3, 'results': [{'ref': {'id': '_prp_1109250878923636601', 'qname': 'device$active', 'objectId': '_dev_1127454099228059958'}, 'values': [{'t': '2021-10-30T17:22:25.092Z', 'v': '---'}, {'t': '2021-11-01T14:17:20.2Z', 'v': '---'}, {'t': '2021-11-01T15:33:21.761Z', 'v': '---'}], 'groupBy': [{'GroupByType': {'type': 'text'}}], 'attributes': {'protocol': ['imsg', 'rest'], 'source': ['object']}}]}

    ## Get latest datapoint with time
    current = deviceById.read_property_historical("active", {"limit": 1, "order": "desc"}) # {'sampleSize': 1, 'results': [{'ref': {'id': '_prp_1109250878923636601', 'qname': 'device$active', 'objectId': '_dev_1127454099228059958'}, 'values': [{'t': '2021-11-01T15:33:21.761Z', 'v': '---'}], 'groupBy': [{'GroupByType': {'type': 'text'}}], 'attributes': {'protocol': ['imsg', 'rest'], 'source': ['object']}}]}
    appCurrent = appByName.read_property_historical("DownTimeCauses", {"limit": 1, "order": "desc"})

    ## Change device name and friendly name
    deviceById.update(name="FORMULA", friendly_name="FORMULA")
    appById.update(name="Downtime", friendly_name="Downtime")

    ## Insert value to property
    deviceById.insert_property_value({ 
        "StationCode": 15
    }) # Returns amount of accepted and rejected datapoints: {'accepted': 1, 'rejected': 0}
    #appById.insert_property_value({ 
    #    "StationCode": 15
    #})


    ## Get device info
    deviceInstance = deviceById.fetch()
    deviceInstance.apikey        # apikey
    deviceInstance.account_id    # account id
    deviceInstance.apps          # apps
    deviceInstance.custom_ids    # custom ids
    deviceInstance.description   # description
    deviceInstance.id            # id
    deviceInstance.date_created  # date created
    deviceInstance.date_modified # date modified
    deviceInstance.locked        # locked
    deviceInstance.location      # location
    deviceInstance.tags          # tags
    deviceInstance.status        # status

    ## Get app info
    appInstance = appById.fetch()
    appInstance.account_id    # account id
    appInstance.description   # description
    appInstance.id            # id
    appInstance.date_created  # date created
    appInstance.date_modified # date modified
    appInstance.tags          # tags
    appInstance.status        # status

    # Get sub accounts

    ## One by one:
    subaccountsStream = client.accounts.stream()
    
    ## Get all
    subaccounts = list(subaccountsStream)

    subaccountsStream = client.accounts.stream()
    subaccount = next(subaccountsStream)

    ### Get subaccount device
    subAccountDevices = subaccount.devices("_dev_1127454099228059958") # All above methods can be used with subaccount instance

    # Get master account details
    master = client.accounts.get().fetch()    
    print('Master account: ' + master.name)

    # Create sub accounts
    for i in range(1, 11):
        newSub = client.accounts.create(name='SubAcc.' + str(i))
        print('New subaccount name: ' + newSub.name + ', id: ' + newSub.id)

    # List users
    no = 1
    for usr in client.account.users.stream():
        print('No {}. User: {}, {}, {}, {}'.format(no, usr.id, usr.name, usr.email, usr.date_created))
        no += 1

    # Create an app
    client.account.apps.create(name='SampleApp',
                                profile='Sample',
                                friendly_name='My first app',
                                description='The first sample app',
                                tags=['test']
                                )

    # Create a provisioning key
    client.account.apiclients.create(name='ProvisioningClient',
                                    friendly_name='Provisioning Key',
                                    description='An API Client for device provisioning',
                                    tags=['provisioning'],
                                    context={'type': "account", 'ids': [master.id]},
                                    scope=['device:read'],
                                    )
                                            
    # Create new device profile
    compressor = client.account.deviceprofiles.create(name='Compressor', 
                                                    friendly_name='Compressor Machine',
                                                    base_profile='ConnectedDevice',
                                                    description='Industrial compressor',
                                                    tags=['test'],
                                                    device_class='compressor',
                                                    product_name='Logika101',
                                                    vendor_name='Dalgakiran'
                                                )

    # Add property to the device profile
    client.account.properties(compressor.id).create(name='temperature',
                                            friendly_name='Temperature',
                                            description='Temperature Sensor',
                                            tags=['temp'],
                                            data_type='number', 
                                            access_type='protected', 
                                            publish_type='always',
                                            # retention=prp.retention
                                        )

    client.account.properties(compressor.id).create(name='humidity',
                                            friendly_name='Humidity',
                                            description='Humidity Sensor',
                                            tags=['humidity'],
                                            data_type='number', 
                                            access_type='protected', 
                                            publish_type='always',
                                            # retention=prp.retention
                                        )

    client.account.properties(compressor.id).create(name='pressure',
                                            friendly_name='Pressure',
                                            description='Pressure Sensor',
                                            tags=['pressure'],
                                            data_type='number', 
                                            access_type='protected', 
                                            publish_type='always',
                                            # retention=prp.retention
                                        )

    # Create devices generated from this device profile
    for i in range(1, 10):
        device = client.account.devices.create(name='Device.{}'.format(i), 
                                                profile='compressor',
                                                )
        print('New device: {}, {}'.format(device.id, device.name))

if __name__ == '__main__':
    example()