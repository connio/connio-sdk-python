
from connio.base import values
from connio.base.instance_context import InstanceContext
from connio.base.instance_resource import InstanceResource
from connio.base.list_resource import ListResource
from connio.base.page import Page

class UserInfo(object):
    def __init__(self, email, role, name=None):
        self.email = email
        self.role = role
        self.name = name

class AccountList(ListResource):
    """  """

    def __init__(self, version):
        """
        Initialize the AccountList

        :param Version version: Version that contains the resource

        :returns: connio.rest.api.v3.account.AccountList
        :rtype: connio.rest.api.v3.account.AccountList
        """
        super(AccountList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/accounts'.format(**self._solution)

    def create(self, name, friendly_name=values.unset, owner=values.unset, userInfo=values.unset, tags=values.unset, description=values.unset, plan=values.unset):
        """
        Create a new AccountInstance

        :param unicode friendly_name: A human readable description of the account

        :returns: Newly created AccountInstance
        :rtype: connio.rest.api.v3.account.AccountInstance
        """
        from connio.base import serialize

        adminInfo = values.unset
        if userInfo is not values.unset:
            adminInfo = {'email': userInfo.email, 'role': userInfo.role, 'name': userInfo.name}
        
        data = values.of({
            'name': name, 
            'friendlyName': friendly_name, 
            'owner': owner,
            'user': adminInfo,
            'tags': tags,
            'description': description,
            'plan': serialize.plan(plan)
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        if userInfo is not None:
            # System returns a token
            return payload
        else:             
            return AccountInstance(self._version, payload, )

    def stream(self, friendly_name=values.unset, status=values.unset, limit=None,
               page_size=None):
        """
        Streams AccountInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode friendly_name: FriendlyName to filter on
        :param AccountInstance.Status status: Status to filter on
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

        page = self.page(friendly_name=friendly_name, status=status, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, friendly_name=values.unset, status=values.unset, limit=None,
             page_size=None):
        """
        Lists AccountInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode friendly_name: FriendlyName to filter on
        :param AccountInstance.Status status: Status to filter on
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[connio.rest.api.v3.account.AccountInstance]
        """
        return list(self.stream(
            friendly_name=friendly_name,
            status=status,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, friendly_name=values.unset, status=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of AccountInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: FriendlyName to filter on
        :param AccountInstance.Status status: Status to filter on
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AccountInstance
        :rtype: connio.rest.api.v3.account.AccountPage
        """
        params = values.of({
            'friendlyName': friendly_name,
            'status': status,
            'pageNo': page_number,
            'pageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return AccountPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AccountInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AccountInstance
        :rtype: connio.rest.api.v3.account.AccountPage
        """
        response = self._version.domain.connio.request(
            'GET',
            target_url,
        )

        return AccountPage(self._version, response, self._solution)

    def get(self, id='_this_'):
        """
        Constructs a AccountContext

        :param id: Fetch by unique Account Id

        :returns: connio.rest.api.v3.account.AccountContext
        :rtype: connio.rest.api.v3.account.AccountContext
        """
        return AccountContext(self._version, id=id, )

    def __call__(self, id='_this_'):
        """
        Constructs a AccountContext

        :param sid: Fetch by unique Account Id

        :returns: onnio.rest.api.v3.account.AccountContext
        :rtype: connio.rest.api.v3.account.AccountContext
        """
        return AccountContext(self._version, id=id, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.AccountList>'


class AccountPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the AccountPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: connio.rest.api.v3.account.AccountPage
        :rtype: connio.rest.api.v3.account.AccountPage
        """
        super(AccountPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AccountInstance

        :param dict payload: Payload response from the API

        :returns: connio.rest.api.v3.account.AccountInstance
        :rtype: connio.rest.api.v3.account.AccountInstance
        """
        return AccountInstance(self._version, payload, )

    def mk_page_url_path(self):
        """
        :return: 
        """
        return '{}/accounts/{}/accounts?pageNo={}&pageSize={}'

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.AccountPage>'


class AccountContext(InstanceContext):
    """  """

    def __init__(self, version, id):
        """
        Initialize the AccountContext

        :param Version version: Version that contains the resource
        :param sid: Fetch by unique Account Sid

        :returns: connio.rest.api.v3.account.AccountContext
        :rtype: connio.rest.api.v3.account.AccountContext
        """
        super(AccountContext, self).__init__(version)

        # Path Solution
        self._solution = {'id': id }        
        self._uri = '/accounts/{id}'.format(**self._solution)

        # Account Entities
        self._users = None
        self._apiclients = None
        self._deviceprofiles = None
        self._devices = None
        self._appprofiles = None
        self._apps = None
        self._properties = None
        self._methods = None
        self._alerts = None

    def fetch(self):
        """
        Fetch a AccountInstance

        :returns: Fetched AccountInstance
        :rtype: connio.rest.api.v3.account.AccountInstance
        """
        params = values.of({})
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return AccountInstance(self._version, payload, id=self._solution['id'], )

    def update(self, friendly_name=values.unset, status=values.unset):
        """
        Update the AccountInstance

        :param unicode friendly_name: FriendlyName to update
        :param AccountInstance.Status status: Status to update the Account with

        :returns: Updated AccountInstance
        :rtype: connio.rest.api.v3.account.AccountInstance
        """
        data = values.of({'friendlyName': friendly_name, 'status': status, })

        payload = self._version.update(
            'PUT',
            self._uri,
            data=data,
        )

        return AccountInstance(self._version, payload, id=self._solution['id'], )

    def delete(self, remove=False):
        """
        Deletes the AccountInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        if remove:
            self._version.delete('delete', self._uri)
            return self._version.delete('delete', self._uri + '?hard=true')
        else:
            return self._version.delete('delete', self._uri)
            
    @property
    def users(self):
        """
        Access the users

        :returns: connio.rest.api.v3.account.user.UserList
        :rtype: connio.rest.api.v3.account.user.UserList
        """
        from connio.rest.api.v3.account.user import UserList

        if self._users is None:
            self._users = UserList(self._version, account_id=self._solution['id'], )
        return self._users

    @property
    def apiclients(self):
        """
        Access the api clients

        :returns: connio.rest.api.v3.account.apiclient.ApiClientList
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientList
        """
        from connio.rest.api.v3.account.apiclient import ApiClientList

        if self._apiclients is None:
            self._apiclients = ApiClientList(self._version, account_id=self._solution['id'], )
        return self._apiclients    

    @property
    def deviceprofiles(self):
        """
        Access the device profiles

        :returns: connio.rest.api.v3.account.deviceprofile.DeviceProfileList
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileList
        """
        from connio.rest.api.v3.account.deviceprofile import DeviceProfileList

        if self._deviceprofiles is None:
            self._deviceprofiles = DeviceProfileList(self._version, account_id=self._solution['id'], )
        return self._deviceprofiles

    @property
    def devices(self):
        """
        Access the devices

        :returns: connio.rest.api.v3.account.device.DeviceList
        :rtype: connio.rest.api.v3.account.device.DeviceList
        """
        from connio.rest.api.v3.account.device import DeviceList

        if self._devices is None:
            self._devices = DeviceList(self._version, account_id=self._solution['id'], )
        return self._devices

    @property
    def appprofiles(self):
        """
        Access the app profiles

        :returns: connio.rest.api.v3.account.appprofile.AppProfileList
        :rtype: connio.rest.api.v3.account.appprofile.AppProfileList
        """
        from connio.rest.api.v3.account.appprofile import AppProfileList

        if self._appprofiles is None:
            self._appprofiles = AppProfileList(self._version, account_id=self._solution['id'], )
        return self._appprofiles

    @property
    def apps(self):
        """
        Access the apps

        :returns: connio.rest.api.v3.account.app.AppList
        :rtype: connio.rest.api.v3.account.app.AppList
        """
        from connio.rest.api.v3.account.app import AppList

        if self._apps is None:
            self._apps = AppList(self._version, account_id=self._solution['id'], )
        return self._apps

    def properties(self, owner_id, tags=values.unset):
        """
        Access the properties

        :returns: connio.rest.api.v3.account.property.PropertyList
        :rtype: connio.rest.api.v3.account.property.PropertyList
        """
        from connio.rest.api.v3.account.propertyy import PropertyList

        self._properties = PropertyList(self._version, account_id=self._solution['id'], owner_id=owner_id, tags=tags)
        return self._properties

    def methods(self, owner_id):
        """
        Access the methods

        :returns: connio.rest.api.v3.account.method.MethodList
        :rtype: connio.rest.api.v3.account.method.MethodList
        """
        from connio.rest.api.v3.account.method import MethodList

        self._methods = MethodList(self._version, account_id=self._solution['id'], owner_id=owner_id, )
        return self._methods

    def alerts(self, owner_id):
        """
        Access the alerts

        :returns: connio.rest.api.v3.account.alert.AlertList
        :rtype: connio.rest.api.v3.account.alert.AlertList
        """
        from connio.rest.api.v3.account.alert import AlertList

        self._alerts = AlertList(self._version, account_id=self._solution['id'], owner_id=owner_id, )
        return self._alerts
    
    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.AccountContext {}>'.format(context)


class AccountInstance(InstanceResource):
    """  """

    class Status:
        CREATED = "created"
        OPEN = "open"
        SUSPENDED = "suspended"        
        CLOSED = "closed"

    class PlanType:
        TRIAL = "trial"
        PAID_PLAN_A = "paidPlanA"
        PAID_PLAN_B = "paidPlanB"
        PAID_PLAN_C = "paidPlanC"

    class Plan(object):
        def __init__(self, type, expires_at=None):
            self.type = type
            self.expires_at = expires_at

    def __init__(self, version, payload, id=None):
        """
        Initialize the AccountInstance

        :returns: connio.rest.api.v3.account.AccountInstance
        :rtype: connio.rest.api.v3.account.AccountInstance
        """
        from connio.base import deserialize
        
        super(AccountInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'id': payload['id'],
            'name': payload['name'],
            'friendly_name': payload.get('friendlyName'),
            'status': payload['status'],
            'plan': deserialize.plan(payload['plan']),
            'owner_account_id': payload.get('ownerId'),
            'locked': payload['locked'],
            'date_created': deserialize.iso8601_datetime(payload['dateCreated']),
            'date_modified': deserialize.iso8601_datetime(payload.get('dateModified'))
        }

        # Context
        self._context = None
        self._solution = {'id': id or self._properties['id'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: AccountContext for this AccountInstance
        :rtype: connio.rest.api.v3.account.AccountContext
        """
        if self._context is None:
            self._context = AccountContext(self._version, id=self._solution['id'], )
        return self._context

    @property
    def id(self):
        """
        :returns: A character string that uniquely identifies this account.
        :rtype: unicode
        """
        return self._properties['id']    

    @property
    def name(self):
        """
        :returns: Universally unique name of this account
        :rtype: unicode
        """
        return self._properties['name']

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
    def friendly_name(self):
        """
        :returns: A human readable description of this account
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def owner_account_id(self):
        """
        :returns: The unique 34 character id representing the parent of this account
        :rtype: unicode
        """
        return self._properties['owner_account_id']

    @property
    def status(self):
        """
        :returns: The status of this account
        :rtype: AccountInstance.Status
        """
        return self._properties['status']

    @property
    def plan(self):
        """
        :returns: The plan of this account
        :rtype: AccountInstance.Plan
        """
        return self._properties['plan']

    def delete(self, remove=False):
        """
        Deletes the AccountInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(remove)

    def fetch(self):
        """
        Fetch a AccountInstance

        :returns: Fetched AccountInstance
        :rtype: connio.rest.api.v3.account.AccountInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset, status=values.unset):
        """
        Update the AccountInstance

        :param unicode friendly_name: FriendlyName to update
        :param AccountInstance.Status status: Status to update the Account with

        :returns: Updated AccountInstance
        :rtype: connio.rest.api.v3.account.AccountInstance
        """
        return self._proxy.update(friendly_name=friendly_name, status=status, )

    def __getitem__(self, key):
        return self._properties[key]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.AccountInstance {}>'.format(context)
