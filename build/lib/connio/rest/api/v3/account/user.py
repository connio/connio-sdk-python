
from connio.base import deserialize
from connio.base import values
from connio.base.instance_context import InstanceContext
from connio.base.instance_resource import InstanceResource
from connio.base.list_resource import ListResource
from connio.base.page import Page

from connio.rest.api.v3.account.apikey import ApiKeyContext

class UserList(ListResource):
    """  """

    def __init__(self, version, account_id):
        """
        Initialize the UserList

        :param Version version: Version that contains the resource
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.user.UserList
        :rtype: connio.rest.api.v3.account.user.UserList
        """
        super(UserList, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, }
        self._uri = '/accounts/{account_id}/users'.format(**self._solution)

    def create(self, email, role, name=values.unset):
        """
        Create a new UserInstance

        :param unicode email: 
        :param unicode role: 
        :param unicode name: 

        :returns: Newly created UserInstance
        :rtype: connio.rest.api.v3.account.user.UserInstance
        """
        data = values.of({
            'name': name,
            'email': email,
            'role': role
        })

        token = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return token

    def stream(self, friendly_name=values.unset, short_code=values.unset,
               limit=None, page_size=None):
        """
        Streams UserInstance records from the API as a generator stream.
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
        :rtype: list[connio.rest.api.v3.account.user.UserInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(friendly_name=friendly_name, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, friendly_name=values.unset, short_code=values.unset, limit=None,
             page_size=None):
        """
        Lists UserInstance records from the API as a list.
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
        :rtype: list[connio.rest.api.v3.account.user.UserInstance]
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
        Retrieve a single page of UserInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: Filter by friendly name
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 200

        :returns: Page of UserInstance
        :rtype: connio.rest.api.v3.account.user.UserPage
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

        return UserPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UserInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserInstance
        :rtype: connio.rest.api.v3.account.user.UserPage
        """
        response = self._version.domain.client.request(
            'GET',
            target_url,
        )

        return UserPage(self._version, response, self._solution)

    def get(self, id):
        """
        Constructs a UserContext

        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.user.UserContext
        :rtype: connio.rest.api.v3.account.user.UserContext
        """
        return UserContext(self._version, account_id=self._solution['account_id'], id=id, )

    def __call__(self, id):
        """
        Constructs a UserContext

        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.user.UserContext
        :rtype: connio.rest.api.v3.account.user.UserContext
        """
        return UserContext(self._version, account_id=self._solution['account_id'], id=id, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.UserList>'


class UserPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the UserPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.user.UserPage
        :rtype: connio.rest.api.v3.account.user.UserPage
        """
        super(UserPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserInstance

        :param dict payload: Payload response from the API

        :returns: connio.rest.api.v3.account.user.UserInstance
        :rtype: connio.rest.api.v3.account.user.UserInstance
        """
        return UserInstance(self._version, payload, account_id=self._solution['account_id'], )

    def mk_page_url_path(self):
        """
        :return: 
        """
        return '{}/accounts/{}/users?pageNo={}&pageSize={}'

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.UserPage>'


class UserContext(InstanceContext):
    """  """

    def __init__(self, version, account_id, id):
        """
        Initialize the UserContext

        :param Version version: Version that contains the resource
        :param account_id: The account_id
        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.user.UserContext
        :rtype: connio.rest.api.v3.account.user.UserContext
        """
        super(UserContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'id': id, }
        self._uri = '/accounts/{account_id}/users/{id}'.format(**self._solution)
        self._apikey = None

    def fetch(self):
        """
        Fetch a UserInstance

        :returns: Fetched UserInstance
        :rtype: connio.rest.api.v3.account.user.UserInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return UserInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )

    def update(self, name=values.unset, password=values.unset):
        """
        Update the UserInstance

        :param unicode name: Given name of the entity
        :param unicode password:

        :returns: Updated UserInstance
        :rtype: connio.rest.api.v3.account.user.UserInstance
        """
        data = values.of({
            'name': name,
            'password': password,
        })

        payload = self._version.update(
            'PUT',
            self._uri,
            data=data,
        )

        return UserInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )

    def delete(self):
        """
        Deletes the UserInstance

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
                owner_type='users',
                owner_id=self._solution['id'],
            )
        return self._apikey.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.UserContext {}>'.format(context)


class UserInstance(InstanceResource):
    """  """

    class Role(object):
        ADMIN = "admin"
        USER = "user"
        POWER = "power"
        GUEST = "guest"
        CUSTOM = "custom"

    class Status(object):
        CONFIRMED = "confirmed"
        INVITED = "invited"

    def __init__(self, version, payload, account_id, id=None):
        """
        Initialize the UserInstance

        :returns: connio.rest.api.v3.account.user.UserInstance
        :rtype: connio.rest.api.v3.account.user.UserInstance
        """
        super(UserInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_id': payload['accountId'],
            'id': payload['id'],
            'name': payload.get('name'),
            'email': payload['email'],
            'status': payload['status'],
            'role': payload['role'],
            'description': payload.get('description'),
            'tags': payload.get('tags'),
            'locale': payload.get('locale'),
            'timezone': payload.get('timezone'),
            'prefs': payload.get('prefs'),
            'avatarUrl': payload.get('avatarUrl'),
            'date_created': deserialize.iso8601_datetime(payload['dateCreated']),
            'date_updated': deserialize.iso8601_datetime(payload.get('dateModified')),
        }

        # Context
        self._context = None
        self._solution = {'account_id': account_id, 'id': id or self._properties['id'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: DeviceProfileContext for this UserInstance
        :rtype: connio.rest.api.v3.account.user.UserContext
        """
        if self._context is None:
            self._context = UserContext(
                self._version,
                account_id=self._solution['account_id'],
                id=self._solution['id'],
            )
        return self._context

    @property
    def account_id(self):
        """
        :returns: The unique id that identifies this account
        :rtype: unicode
        """
        return self._properties['account_id']

    @property
    def id(self):
        """
        :returns: A string that uniquely identifies this user
        :rtype: unicode
        """
        return self._properties['id']

    @property
    def email(self):
        """
        :returns: User's email
        :rtype: unicode
        """
        return self._properties['email']

    @property
    def name(self):
        """
        :returns: 
        :rtype: unicode
        """
        return self._properties['name']

    @property
    def role(self):
        """
        :returns: 
        :rtype: unicode
        """
        return self._properties['role']

    @property
    def status(self):
        """
        :returns: 
        :rtype: unicode
        """
        return self._properties['status']

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
    def locale(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['locale']

    @property
    def timezone(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['timezone']

    @property
    def prefs(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['prefs']

    @property
    def avatarUrl(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['avatarUrl']

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
        Fetch a UserInstance

        :returns: Fetched UserInstance
        :rtype: connio.rest.api.v3.account.user.UserInstance
        """
        return self._proxy.fetch()

    def update(self, name=values.unset, password=values.unset):
        """
        Update the UserInstance

        :param unicode name: Name of the resource
        :param unicode password:

        :returns: Updated UserInstance
        :rtype: connio.rest.api.v3.account.user.UserInstance
        """
        return self._proxy.update(
            name=name,
            password=password
        )

    def delete(self):
        """
        Deletes the UserInstance

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
        return '<Connio.Api.V3.UserInstance {}>'.format(context)
