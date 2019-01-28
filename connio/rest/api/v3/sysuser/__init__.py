
from connio.base import deserialize
from connio.base import values
from connio.base.instance_context import InstanceContext
from connio.base.instance_resource import InstanceResource
from connio.base.list_resource import ListResource
from connio.base.page import Page

from connio.rest.api.v3.account.apikey import ApiKeyContext

class SysUserList(ListResource):
    """  """

    def __init__(self, version):
        """
        Initialize the SysUserList

        :param Version version: Version that contains the resource

        :returns: connio.rest.api.v3.sysuser.SysUserList
        :rtype: connio.rest.api.v3.sysuser.SysUserList
        """
        super(SysUserList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/users'.format(**self._solution)

    def create(self, email, name=values.unset):
        """
        Create a new SysUserInstance

        :param unicode name: Name of this user

        :returns: Newly created SysUserInstance
        :rtype: connio.rest.api.v3.sysuser.SysUserInstance
        """
        data = values.of({'name': name, 'email': email, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return SysUserInstance(self._version, payload, )

    def stream(self, account=values.unset, name=values.unset, status=values.unset, limit=None,
               page_size=None):
        """
        Streams SysUserInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode name: User name to filter on
        :param SysUserInstance.Status status: Status to filter on
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[connio.rest.api.v3.account.AccountInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(account=account, name=name, status=status, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, account=values.unset, name=values.unset, status=values.unset, limit=None,
             page_size=None):
        """
        Lists SysUserInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode account: User account to filter on
        :param unicode name: User name to filter on
        :param SysUserInstance.Status status: Status to filter on
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[connio.rest.api.v3.sysuser.SysUserInstance]
        """
        return list(self.stream(
            account=account,
            name=name,
            status=status,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, account=values.unset, name=values.unset, status=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SysUserInstance records from the API.
        Request is executed immediately

        :param unicode account: User account to filter on
        :param unicode name: User name to filter on
        :param SysUserInstance.Status status: Status to filter on
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SysUserInstance
        :rtype: connio.rest.api.v3.sysuser.SysUserPage
        """
        params = values.of({
            'account': account,
            'name': name,
            'status': status,
            'pageNo': page_number,
            'pageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return SysUserPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SysUserInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AccountInstance
        :rtype: connio.rest.api.v3.sysuser.SysUserPage
        """
        response = self._version.domain.connio.request(
            'GET',
            target_url,
        )

        return SysUserPage(self._version, response, self._solution)

    def get(self, id, account_id=None):
        """
        Constructs a SysUserContext

        :param id: Fetch by unique User Id

        :returns: connio.rest.api.v3.sysuser.SysUserContext
        :rtype: connio.rest.api.v3.sysuser.SysUserContext
        """
        return SysUserContext(self._version, id=id, account_id=account_id)

    def __call__(self, id, account_id=None):
        """
        Constructs a SysUserContext

        :param sid: Fetch by unique User Id

        :returns: onnio.rest.api.v3.sysuser.SysUserContext
        :rtype: connio.rest.api.v3.sysuser.SysUserContext
        """
        return SysUserContext(self._version, id=id, account_id=account_id)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.SysUserList>'


class SysUserPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the SysUserPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: connio.rest.api.v3.sysuser.SysUserPage
        :rtype: connio.rest.api.v3.sysuser.SysUserPage
        """
        super(SysUserPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SysUserInstance

        :param dict payload: Payload response from the API

        :returns: connio.rest.api.v3.sysuser.SysUserInstance
        :rtype: connio.rest.api.v3.sysuser.SysUserInstance
        """
        return SysUserInstance(self._version, payload, )

    def mk_page_url_path(self):
        """
        :return: 
        """
        return '{}/users?ignore={}&pageNo={}&pageSize={}'

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.SysUserPage>'


class SysUserContext(InstanceContext):
    """  """

    def __init__(self, version, account_id, id):
        """
        Initialize the SysUserContext

        :param Version version: Version that contains the resource
        :param sid: Fetch by unique User id

        :returns: connio.rest.api.v3.sysuser.SysUserContext
        :rtype: connio.rest.api.v3.sysuser.SysUserContext
        """
        super(SysUserContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'id': id }        
        self._uri = '/users/{id}'.format(**self._solution)
        self._apikey = None

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

    def fetch(self):
        """
        Fetch a SysUserInstance

        :returns: Fetched SysUserInstance
        :rtype: connio.rest.api.v3.sysuser.SysUserInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return SysUserInstance(self._version, payload, id=self._solution['id'], )

    def update(self, name=values.unset, status=values.unset):
        """
        Update the SysUserInstance

        :param unicode name: User name to update
        :param SysUserInstance.Status status: Status to update the User with

        :returns: Updated SysUserInstance
        :rtype: connio.rest.api.v3.sysuser.SysUserInstance
        """
        data = values.of({'name': name, 'status': status, })

        payload = self._version.update(
            'PUT',
            self._uri,
            data=data,
        )

        return SysUserInstance(self._version, payload, id=self._solution['id'], )

    def delete(self):
        """
        Deletes the SysUserInstance

        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

class SysUserInstance(InstanceResource):
    """  """

    class Status(object):
        CONFIRMED = "confirmed"
        INVITED = "invited"
        SUSPENDED = "suspended"        

    def __init__(self, version, payload, id=None):
        """
        Initialize the SysUserInstance

        :returns: connio.rest.api.v3.sysuser.SysUserInstance
        :rtype: connio.rest.api.v3.sysuser.SysUserInstance
        """
        super(SysUserInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'id': payload['id'],
            'account_id': payload['accountId'],
            'email': payload['email'],
            'name': payload.get('name') or payload.get('fullName'),
            'status': payload['status'],
            'role': payload['role'],
            'locked': payload.get('locked'),
            'date_created': deserialize.iso8601_datetime(payload['dateCreated']),
            'date_modified': deserialize.iso8601_datetime(payload.get('dateModified'))
        }

        # Context
        self._context = None
        self._solution = {'id': id or self._properties['id'], 'account_id': self._properties['account_id']}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SysUserContext for this SysUserInstance
        :rtype: connio.rest.api.v3.sysuser.SysUserContext
        """
        if self._context is None:
            self._context = SysUserContext(self._version, id=self._solution['id'], account_id=self._solution['account_id'],)
        return self._context

    @property
    def id(self):
        """
        :returns: A character string that uniquely identifies this user.
        :rtype: unicode
        """
        return self._properties['id']
    
    @property
    def account_id(self):
        """
        :returns: Account id of this user.
        :rtype: unicode
        """
        return self._properties['account_id']    

    @property
    def email(self):
        """
        :returns: Universally unique user email address.
        :rtype: unicode
        """
        return self._properties['email']

    @property
    def name(self):
        """
        :returns: User name
        :rtype: unicode
        """
        return self._properties['name']

    @property
    def role(self):
        """
        :returns: User role
        :rtype: unicode
        """
        return self._properties['role']

    @property
    def status(self):
        """
        :returns: The status of this account
        :rtype: AccountInstance.Status
        """
        return self._properties['status']

    @property
    def date_created(self):
        """
        :returns: The date this account was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_modified(self):
        """
        :returns: The date this account was last updated
        :rtype: datetime
        """
        return self._properties['date_modified']

    @property
    def apikey(self):
        """
        Access the ApiKey

        :returns: connio.rest.api.v3.account.apikey.ApiKeyInstance
        :rtype: connio.rest.api.v3.account.apikey.ApiKeyInstance
        """
        return self._proxy.apikey

    def delete(self):
        """
        Deletes the SysUserInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch a SysUserInstance

        :returns: Fetched SysUserInstance
        :rtype: connio.rest.api.v3.sysuser.SysUserInstance
        """
        return self._proxy.fetch()

    def update(self, name=values.unset, status=values.unset):
        """
        Update the AccountInstance

        :param unicode name: User name to update
        :param SysUserInstance.Status status: Status to update the Account with

        :returns: Updated AccountInstance
        :rtype: connio.rest.api.v3.sysuser.SysUserInstance
        """
        return self._proxy.update(name=name, status=status, )

    def __getitem__(self, key):
        return self._properties[key]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.SysUserInstance {}>'.format(context)
