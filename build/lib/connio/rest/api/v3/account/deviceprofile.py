
from connio.base import deserialize
from connio.base import values
from connio.base.instance_context import InstanceContext
from connio.base.instance_resource import InstanceResource
from connio.base.list_resource import ListResource
from connio.base.page import Page


class DeviceProfileList(ListResource):
    """  """

    def __init__(self, version, account_id):
        """
        Initialize the DeviceProfileList

        :param Version version: Version that contains the resource
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.deviceprofile.DeviceProfileList
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileList
        """
        super(DeviceProfileList, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, }
        self._uri = '/accounts/{account_id}/deviceprofiles'.format(**self._solution)

    def create(self, name, base_profile=values.unset, friendly_name=values.unset, description=values.unset,
                tags=values.unset, device_class=values.unset, vendor_name=values.unset, product_name=values.unset, image_url=values.unset, 
                locked=values.unset):
        """
        Create a new DeviceProfileInstance

        :param unicode name: A name uniquely identifying this deviceprofile within account context
        :param unicode friendly_name: A human readable description of the application
        :param unicode description: A description of this deviceprofile
        :param unicode tags: Tags associated with this deviceprofile
        
        :returns: Newly created DeviceProfileInstance
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileInstance
        """

        # if tags is not None:
        #     tags = tags[:32]
        
        data = values.of({
            'name': name,
            'friendlyName': friendly_name,
            'baseProfile': base_profile,
            'description': description,
            'tags': tags,
            'deviceClass': device_class,
            'vendorName': vendor_name,
            'productName': product_name,  
            'imageUrl': image_url,
            'locked': locked,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return DeviceProfileInstance(self._version, payload, account_id=self._solution['account_id'], )

    def stream(self, friendly_name=values.unset, short_code=values.unset,
               limit=None, page_size=None):
        """
        Streams DeviceProfileInstance records from the API as a generator stream.
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
        :rtype: list[connio.rest.api.v3.account.deviceprofile.DeviceProfileInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(friendly_name=friendly_name, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, friendly_name=values.unset, short_code=values.unset, limit=None,
             page_size=None):
        """
        Lists DeviceProfileInstance records from the API as a list.
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
        :rtype: list[connio.rest.api.v3.account.deviceprofile.DeviceProfileInstance]
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
        Retrieve a single page of DeviceProfileInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: Filter by friendly name
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 200

        :returns: Page of DeviceProfileInstance
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfilePage
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

        return DeviceProfilePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DeviceProfileInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DeviceProfileInstance
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfilePage
        """
        response = self._version.domain.client.request(
            'GET',
            target_url,
        )

        return DeviceProfilePage(self._version, response, self._solution)

    def get(self, id):
        """
        Constructs a DeviceProfileContext

        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.deviceprofile.DeviceProfileContext
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileContext
        """
        return DeviceProfileContext(self._version, account_id=self._solution['account_id'], id=id, )

    def __call__(self, id):
        """
        Constructs a DeviceProfileContext

        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.deviceprofile.DeviceProfileContext
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileContext
        """
        return DeviceProfileContext(self._version, account_id=self._solution['account_id'], id=id, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.DeviceProfileList>'


class DeviceProfilePage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the DeviceProfilePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.deviceprofile.DeviceProfilePage
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfilePage
        """
        super(DeviceProfilePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DeviceProfileInstance

        :param dict payload: Payload response from the API

        :returns: connio.rest.api.v3.account.deviceprofile.DeviceProfileInstance
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileInstance
        """
        return DeviceProfileInstance(self._version, payload, account_id=self._solution['account_id'], )

    def mk_page_url_path(self):
        """
        :return: 
        """
        return '{}/accounts/{}/deviceprofiles?pageNo={}&pageSize={}'
        
    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.DeviceProfilePage>'


class DeviceProfileContext(InstanceContext):
    """  """

    def __init__(self, version, account_id, id):
        """
        Initialize the DeviceProfileContext

        :param Version version: Version that contains the resource
        :param account_id: The account_id
        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.deviceprofile.DeviceProfileContext
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileContext
        """
        super(DeviceProfileContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'id': id, }
        self._uri = '/accounts/{account_id}/deviceprofiles/{id}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a DeviceProfileInstance

        :returns: Fetched DeviceProfileInstance
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return DeviceProfileInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )

    def update(self, name=values.unset, friendly_name=values.unset, description=values.unset,
                tags=values.unset, device_class=values.unset, vendor_name=values.unset, product_name=values.unset, image_url=values.unset):
        """
        Update the DeviceProfileInstance

        :param unicode name: Given name of the entity
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated DeviceProfileInstance
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileInstance
        """
        data = values.of({
            'name': name,
            'friendlyName': friendly_name,
            'description': description,
            'tags': tags,
            'deviceClass': device_class,
            'vendorName': vendor_name,
            'productName': product_name,
            'imageUrl': image_url,
        })

        payload = self._version.update(
            'PUT',
            self._uri,
            data=data,
        )

        return DeviceProfileInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )

    def delete(self):
        """
        Deletes the DeviceProfileContext

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.DeviceProfileContext {}>'.format(context)


class DeviceProfileInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_id, id=None):
        """
        Initialize the DeviceProfileInstance

        :returns: connio.rest.api.v3.account.deviceprofile.DeviceProfileInstance
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileInstance
        """
        super(DeviceProfileInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_id': payload['accountId'],
            'id': payload['id'],
            'name': payload['name'],
            'friendly_name': payload['friendlyName'],
            'base_profile_id': payload.get('baseProfileId'),
            'description': payload.get('description'),
            'tags': payload.get('tags'),
            'device_class': payload.get('deviceClass'),
            'vendor_name': payload.get('vendorName'),
            'product_name': payload.get('productName'),
            'image_url': payload.get('imageUrl'),
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

        :returns: DeviceProfileContext for this DeviceProfileInstance
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileContext
        """
        if self._context is None:
            self._context = DeviceProfileContext(
                self._version,
                account_id=self._solution['account_id'],
                id=self._solution['id'],
            )
        return self._context

    @property
    def id(self):
        """
        :returns: A string that uniquely identifies this deviceprofile
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
    def base_profile_id(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['base_profile_id']

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
    def device_class(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['device_class']

    @property
    def product_name(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['product_name']

    @property
    def vendor_name(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['vendor_name']

    @property
    def image_url(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['image_url']

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
        Fetch a DeviceProfileInstance

        :returns: Fetched DeviceProfileInstance
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset, name=values.unset):
        """
        Update the DeviceProfileInstance

        :param unicode name: Name of the resource
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated DeviceProfileInstance
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            name=name,
        )

    def delete(self):
        """
        Deletes the DeviceProfileInstance

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
        return '<Connio.Api.V3.DeviceProfileInstance {}>'.format(context)
