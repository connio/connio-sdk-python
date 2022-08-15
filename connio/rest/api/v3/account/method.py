
from connio.base import serialize
from connio.base import values
from connio.base.instance_context import InstanceContext
from connio.base.instance_resource import InstanceResource
from connio.base.list_resource import ListResource
from connio.base.page import Page

class MethodList(ListResource):
    """  """

    def __init__(self, version, account_id, owner_id):
        """
        Initialize the MethodList

        :param Version version: Version that contains the resource
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.method.MethodList
        :rtype: connio.rest.api.v3.account.method.MethodList
        """
        super(MethodList, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'owner_id': owner_id, }
        self._uri = '/accounts/{account_id}/methods?owner={owner_id}'.format(**self._solution)


    def create(self, name, access_type, method_impl=values.unset, friendly_name=values.unset, 
                description=values.unset, tags=values.unset, locked=values.unset):
        """
        Create a new MethodInstance

        :param unicode name: A name uniquely identifying this method within account context
        :param unicode access_type: 
        :param unicode method_impl:
        :param unicode description: A description of this method
        :param unicode tags: Tags associated with this method
        
        :returns: Newly created MethodInstance
        :rtype: connio.rest.api.v3.account.method.MethodInstance
        """
        data = values.of({
            'name': name,
            'ownerId': self._solution['owner_id'],
            'friendlyName': friendly_name,
            'description': description,
            'tags': tags,
            'access': access_type,
            'locked': locked,
            'methodImpl': serialize.methodImplementation(method_impl),
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return MethodInstance(self._version, payload, account_id=self._solution['account_id'], )    

    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams MethodInstance records from the API as a generator stream.
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
        :rtype: list[connio.rest.api.v3.account.method.MethodInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(friendly_name=friendly_name, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])


    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists MethodInstance records from the API as a list.
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
        :rtype: list[connio.rest.api.v3.account.method.MethodInstance]
        """
        return list(self.stream(
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
            
        ))

    def page(self, friendly_name=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of MethodInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: Filter by friendly name
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 200

        :returns: Page of MethodInstance
        :rtype: connio.rest.api.v3.account.method.MethodPage
        """
        params = values.of({
            'ownerId': self._solution['owner_id'],
            'friendlyName': friendly_name,
            'page': page_number,
            'pageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return MethodPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MethodInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MethodInstance
        :rtype: connio.rest.api.v3.account.method.MethodPage
        """
        response = self._version.domain.client.request(
            'GET',
            target_url,
        )

        return MethodPage(self._version, response, self._solution)

    def get(self, id):
        """
        Constructs a MethodContext

        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.method.MethodContext
        :rtype: connio.rest.api.v3.account.method.MethodContext
        """
        return MethodContext(self._version, account_id=self._solution['account_id'], id=id, )

    def __call__(self, owner_id):
        """
        Constructs a MethodContext

        :param owner_id: Owner id

        :returns: connio.rest.api.v3.account.method.MethodContext
        :rtype: connio.rest.api.v3.account.method.MethodContext
        """
        return MethodList(self._version, account_id=self._solution['account_id'], owner_id=owner_id, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.MethodList>'


class MethodPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the MethodPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.method.MethodPage
        :rtype: connio.rest.api.v3.account.method.MethodPage
        """
        super(MethodPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MethodInstance

        :param dict payload: Payload response from the API

        :returns: connio.rest.api.v3.account.method.MethodInstance
        :rtype: connio.rest.api.v3.account.method.MethodInstance
        """
        return MethodInstance(self._version, payload, account_id=self._solution['account_id'], )

    def mk_page_url_path(self):
        """
        :return: 
        """
        return f'{{}}/accounts/{{}}/methods?ownerId={self._solution["owner_id"]}&pageNo={{}}&pageSize={{}}' 

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.MethodPage>'


class MethodContext(InstanceContext):
    """  """

    def __init__(self, version, account_id, id):
        """
        Initialize the MethodContext

        :param Version version: Version that contains the resource
        :param account_id: The account_id
        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.method.MethodContext
        :rtype: connio.rest.api.v3.account.method.MethodContext
        """
        super(MethodContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'id': id, }
        self._uri = '/accounts/{account_id}/methods/{id}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a MethodInstance

        :returns: Fetched MethodInstance
        :rtype: connio.rest.api.v3.account.method.MethodInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return MethodInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )

    def delete(self):
        """
        Delete Method Instance
        """
        return self._version.delete(
            'DELETE',
            self._uri
        )

    def update(self, name=values.unset, friendly_name=values.unset, method_impl=values.unset):
        """
        Update the MethodInstance

        :param unicode name: Given name of the entity
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated MethodInstance
        :rtype: connio.rest.api.v3.account.method.MethodInstance
        """
        data = values.of({
            'name': name,
            'friendlyName': friendly_name,
            'methodImpl': serialize.methodImplementation(method_impl),
        })

        payload = self._version.update(
            'PUT',
            self._uri,
            data=data,
        )

        return MethodInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.MethodContext {}>'.format(context)

    def __eq__(self, other):
        self_context = self.fetch()
        other_context = other.fetch()
        return self_context == other_context

class MethodInstance(InstanceResource):
    """  """

    class MethodImplementation:
        def __init__(self, body, lang='javascript', props=None):
            self.body = body
            self.lang = lang
            self._properties = props

        def __eq__(self, other):
            if not (hasattr(other, "body") and hasattr(other, "lang")):
                return False
            if not (hasattr(self, "body") and hasattr(self, "lang")):
                return False
            return (
                self.body == other.body and
                self.lang == other.lang
                )

    def __init__(self, version, payload, account_id, id=None):
        """
        Initialize the MethodInstance

        :returns: connio.rest.api.v3.account.method.MethodInstance
        :rtype: connio.rest.api.v3.account.method.MethodInstance
        """
        from connio.base import deserialize

        super(MethodInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_id': payload['accountId'],
            'id': payload['id'],
            'owner_id': payload['ownerId'],
            'name': payload['name'],
            'friendly_name': payload['friendlyName'],
            'qualified_name': payload['qualifiedName'],
            'description': payload.get('description'),
            'tags': payload.get('tags'),
            'access_type': payload['access'],
            'method_impl': deserialize.methodImplementation(payload.get('methodImpl')),
            'inherited': payload['inherited'],
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

        :returns: MethodContext for this MethodInstance
        :rtype: connio.rest.api.v3.account.method.MethodContext
        """
        if self._context is None:
            self._context = MethodContext(
                self._version,
                account_id=self._solution['account_id'],
                id=self._solution['id'],
            )
        return self._context

    @property
    def id(self):
        """
        :returns: A string that uniquely identifies this method
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
    def qualified_name(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['qualified_name']

    @property
    def owner_id(self):
        """
        :returns: A string that uniquely identifies this method's owner
        :rtype: unicode
        """
        return self._properties['owner_id']

    @property
    def description(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties.get('description')

    @property
    def tags(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties.get('tags')

    @property
    def inherited(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['inherited']

    @property
    def access_type(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['access_type']

    @property
    def method_impl(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['method_impl']    

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
        Fetch a MethodInstance

        :returns: Fetched MethodInstance
        :rtype: connio.rest.api.v3.account.method.MethodInstance
        """
        return self._proxy.fetch()

    def delete(self):
        return self._proxy.delete()

    def update(self, name=values.unset, friendly_name=values.unset, method_impl=values.unset):
        """
        Update the MethodInstance

        :param unicode name: Name of the resource
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated MethodInstance
        :rtype: connio.rest.api.v3.account.method.MethodInstance
        """
        return self._proxy.update(            
            name=name,
            friendly_name=friendly_name,
            method_impl=method_impl,
        )

    def __getitem__(self, key):
        return self._properties[key]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.MethodInstance {}>'.format(context)

    def __eq__(self, other):
        return(
            self.access_type == other.access_type and
            self.description == other.description and
            self.friendly_name == other.friendly_name and
            self.locked == other.locked and
            self.method_impl == other.method_impl
        )
