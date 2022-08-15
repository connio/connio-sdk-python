
from connio.base import serialize
from connio.base import values
from connio.base.instance_context import InstanceContext
from connio.base.instance_resource import InstanceResource
from connio.base.list_resource import ListResource
from connio.base.page import Page

from connio.rest.api.v3.account.apikey import ApiKeyContext

HTTP_POST = "POST"
HTTP_GET = "GET"
HTTP_PUT = "PUT"

class DeviceList(ListResource):
    """  """

    def __init__(self, version, account_id):
        """
        Initialize the DeviceList

        :param Version version: Version that contains the resource
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.device.DeviceList
        :rtype: connio.rest.api.v3.account.device.DeviceList
        """
        super(DeviceList, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, }
        self._uri = '/accounts/{account_id}/devices'.format(**self._solution)

    def create(self, name, profile, apps=values.unset, friendly_name=values.unset,
                description=values.unset, tags=values.unset, status=values.unset, location=values.unset,
                custom_ids=values.unset, period=values.unset, annotate_with_location=values.unset, annotate_with_meta=values.unset):
        """
        Create a new DeviceInstance

        :param unicode name: A name uniquely identifying this device within account context

        :param unicode friendly_name: A human readable description of the device
        :param unicode description: A description of this device
        :param unicode tags: Tags associated with this device
        
        :returns: Newly created DeviceInstance
        :rtype: connio.rest.api.v3.account.device.DeviceInstance
        """
        data = values.of({
            'name': name,
            'profile': profile,
            'apps': apps,
            'friendlyName': friendly_name,
            'description': description,
            'tags': tags,
            'location': serialize.location(location),
            'customIds': custom_ids,
            'status': status,
            'period': period,
            'annotateWithLoc': annotate_with_location,
            'annotateWithMeta': annotate_with_meta,
        })

        payload = self._version.create(
            HTTP_POST,
            self._uri,
            data=data,
        )

        return DeviceInstance(self._version, payload, account_id=self._solution['account_id'], )

    def create_bulk(self, devices):
        """
        Create multiple devices

        """        
        payload = self._version.create(
            HTTP_POST,
            self._uri + '/bulk',
            data=devices,
        )

        return payload

    def stream(self, profile_id=values.unset, friendly_name=values.unset, short_code=values.unset,
               limit=None, page_size=None):
        """
        Streams DeviceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        :param unicode profile_id: Filter by profile name 
        :param unicode friendly_name: Filter by friendly name
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 200 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 200)

        :returns: Generator that will yield up to limit results
        :rtype: list[connio.rest.api.v3.account.device.DeviceInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(profile_id=profile_id, friendly_name=friendly_name, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, friendly_name=values.unset, short_code=values.unset, limit=None,
             page_size=None, profile_id=None):
        """
        Lists DeviceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode friendly_name: Filter by friendly name
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 200 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 200)

        :returns: Generator that will yield up to limit results
        :rtype: list[connio.rest.api.v3.account.device.DeviceInstance]
        """
        return list(self.stream(
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
            profile_id=profile_id
        ))

    def page(self, friendly_name=values.unset, profile_id=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of DeviceInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: Filter by friendly name
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 200

        :returns: Page of DeviceInstance
        :rtype: connio.rest.api.v3.account.device.DevicePage
        """
        params = values.of({
            'friendlyName': friendly_name,
            'pageNo': page_number,
            'pageSize': page_size,
            'is_a': profile_id
        })

        response = self._version.page(
            HTTP_GET,
            self._uri,
            params=params,
        )

        return DevicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DeviceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DeviceInstance
        :rtype: connio.rest.api.v3.account.device.DevicePage
        """
        response = self._version.domain.client.request(
            HTTP_GET,
            target_url,
        )

        return DevicePage(self._version, response, self._solution)

    def get(self, id):
        """
        Constructs a DeviceContext

        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.device.DeviceContext
        :rtype: connio.rest.api.v3.account.device.DeviceContext
        """
        return DeviceContext(self._version, account_id=self._solution['account_id'], id=id, )

    def __call__(self, id):
        """
        Constructs a DeviceContext

        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.device.DeviceContext
        :rtype: connio.rest.api.v3.account.device.DeviceContext
        """
        return DeviceContext(self._version, account_id=self._solution['account_id'], id=id, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.DeviceList>'


class DevicePage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the DevicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.device.DevicePage
        :rtype: connio.rest.api.v3.account.device.DevicePage
        """
        super(DevicePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DeviceInstance

        :param dict payload: Payload response from the API

        :returns: connio.rest.api.v3.account.device.DeviceInstance
        :rtype: connio.rest.api.v3.account.device.DeviceInstance
        """
        return DeviceInstance(self._version, payload, account_id=self._solution['account_id'], )

    def mk_page_url_path(self):
        """
        :return: 
        """
        return '{}/accounts/{}/devices?pageNo={}&pageSize={}'    

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.DevicePage>'


class DeviceContext(InstanceContext):
    ID_KEY = "id"

    """  """

    def __init__(self, version, account_id, id):
        """
        Initialize the DeviceContext

        :param Version version: Version that contains the resource
        :param account_id: The account_id
        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.device.DeviceContext
        :rtype: connio.rest.api.v3.account.device.DeviceContext
        """
        super(DeviceContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'id': id, }
        self._uri = '/accounts/{account_id}/devices/{id}'.format(**self._solution)
        self._apikey = None

    def fetch(self):
        """
        Fetch a DeviceInstance

        :returns: Fetched DeviceInstance
        :rtype: connio.rest.api.v3.account.device.DeviceInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            HTTP_GET,
            self._uri,
            params=params,
        )

        return DeviceInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )

    def update(self, name=values.unset, friendly_name=values.unset, apps=values.unset,
                description=values.unset, tags=values.unset, period=values.unset, location=values.unset,
                custom_ids=values.unset, status=values.unset, annotate_with_location=values.unset, annotate_with_meta=values.unset):
        """
        Update the DeviceInstance

        :param unicode name: Given name of the entity
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated DeviceInstance
        :rtype: connio.rest.api.v3.account.device.DeviceInstance
        """
        data = values.of({
            'name': name,
            'friendlyName': friendly_name,
            'apps': apps,
            'description': description,
            'tags': tags,
            'location': serialize.location(location),
            'custom_ids': custom_ids,
            'status': status,
            'period': period,
            'annotateWithLoc': annotate_with_location,
            'annotateWithMeta': annotate_with_meta,
        })

        payload = self._version.update(
            HTTP_PUT,
            self._uri,
            data=data,
        )

        return DeviceInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )

    def delete(self):
        """
        Deletes the DeviceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)   

    @property
    def apikey(self):
        """
        :returns: connio.rest.api.v3.account.apikey.ApiKeyInstance
        :rtype: connio.rest.api.v3.account.apikey.ApiKeyInstance
        """
        if self._apikey is None:
            self._apikey = ApiKeyContext(
                self._version,
                account_id=self._solution['account_id'],
                owner_type='devices',
                owner_id=self._solution['id'],
            )
        return self._apikey.fetch()

    def insert_property_value(self, payload, use_device_key=False):
        device_id = self._solution['id']
        if(not use_device_key):
            return self._version.fetch(HTTP_POST, f'data/devices/{device_id}', data=payload)

        return self._version.fetch(HTTP_POST, f'data/devices/{device_id}', data=payload, auth=(self.apikey.id, self.apikey.secret))

    def call_method(self, payload, method_name):
        device_id = self._solution[self.ID_KEY]
        return self._version.fetch(HTTP_POST, f'data/devices/{device_id}/methods/{method_name}', data=payload)

        return self._version.fetch('post', f'data/devices/{device_id}', data=payload)

    def read_property_historical(self, property_name, query):
        device_id = self._solution['id']
        return self._version.fetch('post', f'data/devices/{device_id}/properties/{property_name}/query', data=query)

    def read_events(self, page_size, page_no, admin_auth):
        device_id = self._solution['id']
        return self._version.fetch('get', f'sys/data/devices/{device_id}?pageSize={page_size}&pageNo={page_no}', auth=admin_auth)

    def state(self):
        """
        Return device state as dict
        """
        device_id = self._solution[self.ID_KEY]
        return self._version.fetch(HTTP_GET, f'data/devices/{device_id}')

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.DeviceContext {}>'.format(context)



class DeviceInstance(InstanceResource):
    """  """

    class Status(object):
        ENABLED = "enabled"
        DISABLED = "disabed"
        DEBUG = "debug"

    class GeoCoord:
        def __init__(self, lat, lon, alt=None):
            self.lat = lat
            self.lon = lon
            self.alt = alt
        
    class Location:
        def __init__(self, zone, geo, props=values.unset):
            self._properties = props
            self.zone = zone
            self.geo = geo

    def __init__(self, version, payload, account_id, id=None):
        """
        Initialize the DeviceInstance

        :returns: connio.rest.api.v3.account.device.DeviceInstance
        :rtype: connio.rest.api.v3.account.device.DeviceInstance
        """
        from connio.base import deserialize

        super(DeviceInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_id': payload['accountId'],
            'id': payload['id'],
            'name': payload['name'],
            'friendly_name': payload['friendlyName'],
            'profile_id': payload['profileId'],
            'apps': payload['apps'],
            'description': payload.get('description'),
            'tags': payload.get('tags'),
            'location': deserialize.location(payload.get('location')),
            'custom_ids': payload.get('customIds'),
            'status': payload['status'],
            'period': payload['period'],
            'annotate_with_location': payload['annotateWithLoc'],
            'annotate_with_meta': payload['annotateWithMeta'],
            'locked': payload['locked'],
            'date_created': deserialize.iso8601_datetime(payload['dateCreated']),
            'date_updated': deserialize.iso8601_datetime(payload['dateModified']),
        }

        # Context
        self._context = None
        self._solution = {'account_id': account_id, 'id': id or self._properties['id'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: DeviceProfileContext for this DeviceInstance
        :rtype: connio.rest.api.v3.account.device.DeviceContext
        """
        if self._context is None:
            self._context = DeviceContext(
                self._version,
                account_id=self._solution['account_id'],
                id=self._solution['id'],
            )
        return self._context

    @property
    def id(self):
        """
        :returns: A string that uniquely identifies this device
        :rtype: unicode
        """
        return self._properties['id']

    @property
    def account_id(self):
        """
        :returns: The unique id that identifies this account
        :rtype: unicode
        """
        return self._properties['account_id']

    @property
    def name(self):
        """
        :returns: The unique name of this resource
        :rtype: unicode
        """
        return self._properties['name']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description of this resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def profile_id(self):
        """
        :returns: Device profile id
        :rtype: unicode
        """
        return self._properties['profile_id']

    @property
    def apps(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['apps']

    @property
    def description(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['description']

    @property
    def tags(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['tags']

    @property
    def location(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['location']

    @property
    def custom_ids(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['custom_ids']

    @property
    def status(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['status']

    @property
    def period(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['period']

    @property
    def annotate_with_location(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['annotate_with_location']

    @property
    def annotate_with_meta(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['annotate_with_meta']

    @property
    def locked(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['locked']

    @property
    def date_created(self):
        """
        :returns: The date this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_modified(self):
        """
        :returns: The date this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def state(self):
        """
        :returns: A string that uniquely identifies this device
        :rtype: unicode
        """
        return self._proxy.state()

    def call_method(self, payload, method_name):
        """
        :returns: Whatever method returns
        :rtype: unicode
        """
        return self._proxy.call_method(payload, method_name)

    def fetch(self):
        """
        Fetch a DeviceInstance

        :returns: Fetched DeviceInstance
        :rtype: connio.rest.api.v3.account.device.DeviceInstance
        """
        return self._proxy.fetch()

    def insert_property_value(self, payload, use_device_key=False):
        return self._proxy.insert_property_value(payload, use_device_key)

    def read_property_historical(self, property_name, query):
        return self._proxy.read_property_historical(property_name, query)

    def read_events(self, page_size, page_no, admin_auth):
        return self._proxy.read_events(page_size, page_no, admin_auth)

    def update(self, 
                name=values.unset, 
                friendly_name=values.unset,
                apps=values.unset, 
                description=values.unset, 
                tags=values.unset, 
                period=values.unset, 
                location=values.unset,
                custom_ids=values.unset, 
                status=values.unset, 
                annotate_with_location=values.unset, 
                annotate_with_meta=values.unset):
        """
        Update the DeviceInstance

        :param unicode name: Name of the resource
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated DeviceInstance
        :rtype: connio.rest.api.v3.account.device.DeviceInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            name=name,
            apps=apps,
            description=description,
            tags=tags,
            status=status,
            period=period,
            location=location,
            custom_ids=custom_ids,
            annotate_with_location=annotate_with_location,
            annotate_with_meta=annotate_with_meta
        )

    def delete(self):
        """
        Deletes the DeviceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def apikey(self):
        """
        Access the ApiKey

        :returns: connio.rest.api.v3.account.apikey.ApiKeyInstance
        :rtype: connio.rest.api.v3.account.apikey.ApiKeyInstance
        """
        return self._proxy.apikey

    def __getitem__(self, key):
        return self._properties[key]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.DeviceInstance {}>'.format(context)
