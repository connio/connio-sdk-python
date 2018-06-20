
from connio.base import deserialize
from connio.base import values
from connio.base.instance_context import InstanceContext
from connio.base.instance_resource import InstanceResource
from connio.base.list_resource import ListResource
from connio.base.page import Page

from connio.rest.api.v3.account.apikey import ApiKeyContext

class ApiClientList(ListResource):
    """  """

    def __init__(self, version, account_id):
        """
        Initialize the ApiClientList

        :param Version version: Version that contains the resource
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.apiclient.ApiClientList
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientList
        """
        super(ApiClientList, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id}
        self._uri = '/accounts/{account_id}/apiclients'.format(**self._solution)

    def create(self, context, scope, name=values.unset, friendly_name=values.unset, 
                description=values.unset, tags=values.unset):
        """
        Create a new ApiClientInstance

        :param unicode name: A name uniquely identifying this apiclient within account context
        :param unicode friendly_name: A human readable description of the application
        :param unicode description: A description of this deviceprofile
        :param unicode tags: Tags associated with this deviceprofile

        #TODO Doldur!

        :returns: Newly created ApiClientInstance
        :rtype: connio.rest.api.v3.account.deviceprofile.ApiClientInstance
        """
        data = values.of({
            'name': name,
            'friendlyName': friendly_name,
            'context': context,
            'scope': scope,
            'description': description,
            'tags': tags,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return ApiClientInstance(self._version, payload, account_id=self._solution['account_id'], )    

    def stream(self, friendly_name=values.unset, short_code=values.unset,
               limit=None, page_size=None):
        """
        Streams ApiClientInstance records from the API as a generator stream.
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
        :rtype: list[connio.rest.api.v3.account.apiclient.ApiClientInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(friendly_name=friendly_name, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, friendly_name=values.unset, short_code=values.unset, limit=None,
             page_size=None):
        """
        Lists ApiClientInstance records from the API as a list.
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
        :rtype: list[connio.rest.api.v3.account.apiclient.ApiClientInstance]
        """
        return list(self.stream(
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, friendly_name=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ApiClientInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: Filter by friendly name
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 200

        :returns: Page of ApiClientInstance
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientPage
        """
        params = values.of({
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ApiClientPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ApiClientInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ApiClientInstance
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientPage
        """
        response = self._version.domain.client.request(
            'GET',
            target_url,
        )

        return ApiClientPage(self._version, response, self._solution)

    def get(self, id):
        """
        Constructs a ApiClientContext

        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.apiclient.ApiClientContext
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientContext
        """
        return ApiClientContext(self._version, account_id=self._solution['account_id'], id=id, )

    def __call__(self, id):
        """
        Constructs a ApiClientContext

        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.apiclient.ApiClientContext
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientContext
        """
        return ApiClientContext(self._version, account_id=self._solution['account_id'], id=id, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.ApiClientList>'


class ApiClientPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the ApiClientPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.apiclient.ApiClientPage
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientPage
        """
        super(ApiClientPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ApiClientInstance

        :param dict payload: Payload response from the API

        :returns: connio.rest.api.v3.account.apiclient.ApiClientInstance
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientInstance
        """
        return ApiClientInstance(self._version, payload, account_id=self._solution['account_id'], )

    def mk_page_url_path(self):
        """
        :return: 
        """
        return '{}/accounts/{}/apiclients?pageNo={}&pageSize={}'
    
    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.ApiClientPage>'


class ApiClientContext(InstanceContext):
    """  """

    def __init__(self, version, account_id, id):
        """
        Initialize the ApiClientContext

        :param Version version: Version that contains the resource
        :param account_id: The account_id
        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.apiclient.ApiClientContext
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientContext
        """
        super(ApiClientContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'id': id, }
        self._uri = '/accounts/{account_id}/apiclients/{id}'.format(**self._solution)
        self._apikey = None

    def fetch(self):
        """
        Fetch a ApiClientInstance

        :returns: Fetched ApiClientInstance
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ApiClientInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )

    def update(self, name=values.unset, friendly_name=values.unset, description=values.unset, 
                tags=values.unset):
        """
        Update the ApiClientInstance

        :param unicode name: Given name of the entity
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated ApiClientInstance
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientInstance
        """
        data = values.of({
            'name': name,
            'friendlyName': friendly_name,
            'description': description,
            'tags': tags,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return ApiClientInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )

    def delete(self):
        """
        Deletes the ApiClientInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)    

    @property
    def apikey(self):
        """
        
        :returns: connio.rest.api.v3.account.apiclient.ApiKeyInstance
        :rtype: connio.rest.api.v3.account.apiclient.ApiKeyInstance
        """
        if self._apikey is None:
            self._apikey = ApiKeyContext(
                self._version,
                account_id=self._solution['account_id'],
                owner_type='apiclients',
                owner_id=self._solution['id'],
            ).fetch()
        return self._apikey

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.ApiClientContext {}>'.format(context)


class ApiClientInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_id, id=None):
        """
        Initialize the ApiClientInstance

        :returns: connio.rest.api.v3.account.apiclient.ApiClientInstance
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientInstance
        """
        super(ApiClientInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_id': payload['accountId'],
            'id': payload['id'],
            'name': payload['name'],
            'friendly_name': payload['friendlyName'],
            'description': payload.get('description'),
            'tags': payload.get('tags'),
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

        :returns: DeviceProfileContext for this ApiClientInstance
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientContext
        """
        if self._context is None:
            self._context = ApiClientContext(
                self._version,
                account_id=self._solution['account_id'],
                id=self._solution['id'],
            )
        return self._context

    @property
    def id(self):
        """
        :returns: A string that uniquely identifies this apiclient
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

    def fetch(self):
        """
        Fetch a ApiClientInstance

        :returns: Fetched ApiClientInstance
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset, name=values.unset):
        """
        Update the ApiClientInstance

        :param unicode name: Name of the resource
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated ApiClientInstance
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            name=name,
        )

    def delete(self):
        """
        Deletes the ApiClientInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def apikey(self):
        """
        Access the ApiKey

        :returns: connio.rest.api.v3.account.apiclient.ApiClientInstance.apikey.ApiKeyInstance
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientInstance.apikey.ApiKeyInstance
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
        return '<Connio.Api.V3.ApiClientInstance {}>'.format(context)
