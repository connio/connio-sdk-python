
from connio.base import deserialize
from connio.base import values
from connio.base.instance_context import InstanceContext
from connio.base.instance_resource import InstanceResource
from connio.base.list_resource import ListResource
from connio.base.page import Page
from connio.rest.api.v3.account.dataconnector import DataConnectorList


class AppList(ListResource):
    """  """

    def __init__(self, version, account_id):
        """
        Initialize the AppList

        :param Version version: Version that contains the resource
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.app.AppList
        :rtype: connio.rest.api.v3.account.app.AppList
        """
        super(AppList, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, }
        self._uri = '/accounts/{account_id}/apps'.format(**self._solution)

    def create(self, name, profile, friendly_name=values.unset, 
                description=values.unset, tags=values.unset, status=values.unset):
        """
        Create a new AppInstance

        :param unicode name: A name uniquely identifying this app within account context

        :param unicode friendly_name: A human readable description of the application
        :param unicode description: A description of this app
        :param unicode tags: Tags associated with this app
        
        :returns: Newly created AppInstance
        :rtype: connio.rest.api.v3.account.device.AppInstance
        """

        data = values.of({
            'name': name,
            'profile': profile,
            'friendlyName': friendly_name,
            'description': description,
            'tags': tags,
            'status': status,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return AppInstance(self._version, payload, account_id=self._solution['account_id'], )    

    def stream(self, friendly_name=values.unset, profile_id=values.unset, short_code=values.unset,
               limit=None, page_size=None):
        """
        Streams AppInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode friendly_name: Filter by friendly name
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 200 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 200)

        :returns: Generator that will yield up to limit results
        :rtype: list[connio.rest.api.v3.account.app.AppInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(profile_id=profile_id,
                         friendly_name=friendly_name, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, friendly_name=values.unset, short_code=values.unset, limit=None,
             page_size=None, profile_id=None):
        """
        Lists AppInstance records from the API as a list.
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
        :rtype: list[connio.rest.api.v3.account.app.AppInstance]
        """
        return list(self.stream(
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
            profile_id=profile_id
        ))

    def page(self, friendly_name=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset, profile_id=values.unset):
        """
        Retrieve a single page of AppInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: Filter by friendly name
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 200

        :returns: Page of AppInstance
        :rtype: connio.rest.api.v3.account.app.AppPage
        """
        params = values.of({
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
            'is_a': profile_id
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return AppPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AppInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AppInstance
        :rtype: connio.rest.api.v3.account.app.AppPage
        """
        response = self._version.domain.client.request(
            'GET',
            target_url,
        )

        return AppPage(self._version, response, self._solution)

    def get(self, id):
        """
        Constructs a AppContext

        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.app.AppContext
        :rtype: connio.rest.api.v3.account.app.AppContext
        """
        return AppContext(self._version, account_id=self._solution['account_id'], id=id, )

    def __call__(self, id):
        """
        Constructs a AppContext

        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.app.AppContext
        :rtype: connio.rest.api.v3.account.app.AppContext
        """
        return AppContext(self._version, account_id=self._solution['account_id'], id=id, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.AppList>'


class AppPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the AppPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.app.AppPage
        :rtype: connio.rest.api.v3.account.app.AppPage
        """
        super(AppPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AppInstance

        :param dict payload: Payload response from the API

        :returns: connio.rest.api.v3.account.app.AppInstance
        :rtype: connio.rest.api.v3.account.app.AppInstance
        """
        return AppInstance(self._version, payload, account_id=self._solution['account_id'], )

    def mk_page_url_path(self):
        """
        :return: 
        """
        return '{}/accounts/{}/apps?pageNo={}&pageSize={}'

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.AppPage>'


class AppContext(InstanceContext):
    """  """

    def __init__(self, version, account_id, id):
        """
        Initialize the AppContext

        :param Version version: Version that contains the resource
        :param account_id: The account_id
        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.app.AppContext
        :rtype: connio.rest.api.v3.account.app.AppContext
        """
        super(AppContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'id': id, }
        self._uri = '/accounts/{account_id}/apps/{id}'.format(**self._solution)
        self._data_connectors = None

    def fetch(self):
        """
        Fetch a AppInstance

        :returns: Fetched AppInstance
        :rtype: connio.rest.api.v3.account.app.AppInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return AppInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )

    def state(self):
        """
        Return device state as dict
        """
        app_id = self._solution['id']
        return self._version.fetch('get', f'data/apps/{app_id}')

    def insert_property_value(self, payload, auth_key=None):
        app_id = self._solution['id']
        if auth_key is None:
            return self._version.fetch('post', f'data/apps/{app_id}', data=payload)
        return self._version.fetch('post', f'data/apps/{app_id}', data=payload, auth=auth_key)
        
    def call_method(self, payload, method_name):
        app_id = self._solution['id']
        return self._version.fetch('post', f'data/apps/{app_id}/methods/{method_name}', data=payload)

    def update(self, name=values.unset, friendly_name=values.unset,
                description=values.unset, tags=values.unset, status=values.unset):
        """
        Update the AppInstance

        :param unicode name: Given name of the entity
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated AppInstance
        :rtype: connio.rest.api.v3.account.app.AppInstance
        """
        data = values.of({
            'name': name,
            'friendlyName': friendly_name,
            'description': description,
            'tags': tags,
            'status': status,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return AppInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )

    def delete(self):
        """
        Deletes the AppInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri) 

    @property
    def data_connectors(self):
        """
        
        :returns: connio.rest.api.v3.account.connector.ConnectorList
        :rtype: connio.rest.api.v3.account.connector.ConnectorList
        """
        if self._data_connectors is None:
            self._data_connectors = DataConnectorList(
                self._version,
                account_id=self._solution['account_id'],
                owner_id=self._solution['id']
            )
        return self._data_connectors

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.AppContext {}>'.format(context)


class AppInstance(InstanceResource):
    """  """

    class Status(object):
        ENABLED = "enabled"
        DISABLED = "disabed"
        DEBUG = "debug"

    def __init__(self, version, payload, account_id, id=None):
        """
        Initialize the AppInstance

        :returns: connio.rest.api.v3.account.app.AppInstance
        :rtype: connio.rest.api.v3.account.app.AppInstance
        """
        super(AppInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_id': payload['accountId'],
            'id': payload['id'],
            'name': payload['name'],
            'friendly_name': payload['friendlyName'],
            'profile_id': payload['profileId'],
            'description': payload.get('description'),
            'tags': payload.get('tags'),
            'status': payload.get('status') or 'enabled',
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

        :returns: DeviceProfileContext for this AppInstance
        :rtype: connio.rest.api.v3.account.app.AppContext
        """
        if self._context is None:
            self._context = AppContext(
                self._version,
                account_id=self._solution['account_id'],
                id=self._solution['id'],
            )
        return self._context

    def insert_property_value(self, payload, auth_key=None):
        return self._proxy.insert_property_value(payload, auth_key)

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

    @property
    def id(self):
        """
        :returns: A string that uniquely identifies this app
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
        :returns: 
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
    def status(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['status']

    @property
    def data_connectors(self):
        """
        Access the Data Connectors

        :returns: connio.rest.api.v3.account.connector.ConnectorList
        :rtype: connio.rest.api.v3.account.connector.ConnectorList
        """
        return self._proxy.data_connectors
    
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

    def fetch(self):
        """
        Fetch a AppInstance

        :returns: Fetched AppInstance
        :rtype: connio.rest.api.v3.account.app.AppInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset, name=values.unset):
        """
        Update the AppInstance

        :param unicode name: Name of the resource
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated AppInstance
        :rtype: connio.rest.api.v3.account.app.AppInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            name=name,
        )

    def delete(self):
        """
        Deletes the AppInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __getitem__(self, key):
        return self._properties[key]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.AppInstance {}>'.format(context)
