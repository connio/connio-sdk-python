
from connio.base import deserialize
from connio.base import serialize
from connio.base import values
from connio.base.instance_context import InstanceContext
from connio.base.instance_resource import InstanceResource
from connio.base.list_resource import ListResource
from connio.base.page import Page

class AlertList(ListResource):
    """  """

    def __init__(self, version, account_id, owner_id):
        """
        Initialize the AlertList

        :param Version version: Version that contains the resource
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.alert.AlertList
        :rtype: connio.rest.api.v3.account.alert.AlertList
        """
        super(AlertList, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'owner_id': owner_id, }
        self._uri = '/accounts/{account_id}/alerts?owner={owner_id}'.format(**self._solution)


    def create(self, name, trigger, metric, friendly_name=values.unset, status='enabled',  
                description=values.unset, tags=values.unset, conditions=values.unset, notifications=values.unset, locked=values.unset):
        """
        Create a new AlertInstance

        :param unicode name: A name uniquely identifying this alert within account context
        :param unicode friendly_name: 
        :param unicode status:
        :param unicode description: A description of this alert
        :param unicode tags: Tags associated with this alert
        
        :returns: Newly created AlertInstance
        :rtype: connio.rest.api.v3.account.alert.AlertInstance
        """
        data = values.of({
            'name': name,
            'ownerId': self._solution['owner_id'],
            'friendlyName': friendly_name,
            'description': description,
            'tags': tags,
            'status': status,
            'trigger': trigger,
            'metric': metric,
            'conditions': serialize.conditions(conditions),
            'notifications': serialize.notifications(notifications),
            'locked': locked,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return AlertInstance(self._version, payload, account_id=self._solution['account_id'], )    

    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams AlertInstance records from the API as a generator stream.
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
        :rtype: list[connio.rest.api.v3.account.alert.AlertInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(friendly_name=friendly_name, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists AlertInstance records from the API as a list.
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
        :rtype: list[connio.rest.api.v3.account.alert.AlertInstance]
        """
        return list(self.stream(
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
            
        ))

    def page(self, friendly_name=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of AlertInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: Filter by friendly name
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 200

        :returns: Page of AlertInstance
        :rtype: connio.rest.api.v3.account.alert.AlertPage
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

        return AlertPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AlertInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AlertInstance
        :rtype: connio.rest.api.v3.account.alert.AlertPage
        """
        response = self._version.domain.client.request(
            'GET',
            target_url,
        )

        return AlertPage(self._version, response, self._solution)

    def get(self, id):
        """
        Constructs a AlertContext

        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.alert.AlertContext
        :rtype: connio.rest.api.v3.account.alert.AlertContext
        """
        return AlertContext(self._version, account_id=self._solution['account_id'], id=id, )

    def __call__(self, owner_id):
        """
        Constructs a AlertContext

        :param owner_id: Owner id

        :returns: connio.rest.api.v3.account.alert.AlertContext
        :rtype: connio.rest.api.v3.account.alert.AlertContext
        """
        return AlertList(self._version, account_id=self._solution['account_id'], owner_id=owner_id, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.AlertList>'


class AlertPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the AlertPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.alert.AlertPage
        :rtype: connio.rest.api.v3.account.alert.AlertPage
        """
        super(AlertPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AlertInstance

        :param dict payload: Payload response from the API

        :returns: connio.rest.api.v3.account.alert.AlertInstance
        :rtype: connio.rest.api.v3.account.alert.AlertInstance
        """
        return AlertInstance(self._version, payload, account_id=self._solution['account_id'], )

    def mk_page_url_path(self):
        """
        :return: 
        """
        return '{}/accounts/{}/alerts?ownerId={}&pageNo={}&pageSize={}'    

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.AlertPage>'


class AlertContext(InstanceContext):
    """  """

    def __init__(self, version, account_id, id):
        """
        Initialize the AlertContext

        :param Version version: Version that contains the resource
        :param account_id: The account_id
        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.alert.AlertContext
        :rtype: connio.rest.api.v3.account.alert.AlertContext
        """
        super(AlertContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'id': id, }
        self._uri = '/accounts/{account_id}/alerts/{id}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a AlertInstance

        :returns: Fetched AlertInstance
        :rtype: connio.rest.api.v3.account.alert.AlertInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return AlertInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )

    def update(self, name=values.unset, friendly_name=values.unset, status=values.unset):
        """
        Update the AlertInstance

        :param unicode name: Given name of the entity
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated AlertInstance
        :rtype: connio.rest.api.v3.account.alert.AlertInstance
        """
        data = values.of({
            'name': name,
            'friendlyName': friendly_name,
            'status': status,
        })

        payload = self._version.update(
            'PUT',
            self._uri,
            data=data,
        )

        return AlertInstance(
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
        return '<Connio.Api.V3.AlertContext {}>'.format(context)


class AlertInstance(InstanceResource):
    """  """

    class Condition(object):
        class Expression(object):
            def __init__(self, operation, value=None):
                self.operation=operation
                self.value=value
        class Handler(object):
            def __init__(self, key, notification):
                self.key=key
                self.notification=notification
        def __init__(self, severity, expression, handlers):
            self.severity = severity
            self.expression = expression
            self.handlers = handlers

    class Notification(object):
        def __init__(self, action, name, level=None, message=None, to=None, subject=None, method=None, parameter=None):
            self.action = action
            self.name = name
            self.level = level
            self.to = to
            self.subject = subject
            self.message = message
            self.method = method
            self.parameter = parameter

    def __init__(self, version, payload, account_id, id=None):
        """
        Initialize the AlertInstance

        :returns: connio.rest.api.v3.account.alert.AlertInstance
        :rtype: connio.rest.api.v3.account.alert.AlertInstance
        """
        super(AlertInstance, self).__init__(version)

        # Marshaled Properties
        self._alerts = {
            'account_id': payload['accountId'],
            'id': payload['id'],
            'owner_id': payload['ownerId'],
            'name': payload['name'],
            'friendly_name': payload['friendlyName'],
            'description': payload.get('description'),
            'tags': payload.get('tags'),
            'status': payload.setdefault('status', 'enabled'),
            'metric': payload['metric'],
            'trigger': payload.get('triggerPropId') or payload.get('triggerId'),
            'conditions': deserialize.conditions(payload.get('conditions')),
            'notifications': deserialize.notifications(payload.get('notifications')),
            'locked': payload['locked'],        
            'date_created': deserialize.iso8601_datetime(payload['dateCreated']),
            'date_updated': deserialize.iso8601_datetime(payload['dateModified']),
        }

        # Context
        self._context = None
        self._solution = {'account_id': account_id, 'id': id or self._alerts['id'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: AlertContext for this AlertInstance
        :rtype: connio.rest.api.v3.account.alert.AlertContext
        """
        if self._context is None:
            self._context = AlertContext(
                self._version,
                account_id=self._solution['account_id'],
                id=self._solution['id'],
            )
        return self._context

    @property
    def id(self):
        """
        :returns: A string that uniquely identifies this alert
        :rtype: unicode
        """
        return self._alerts['id']

    @property
    def account_id(self):
        """
        :returns: The unique id that identifies this account
        :rtype: unicode
        """
        return self._alerts['account_id']

    @property
    def name(self):
        """
        :returns: The unique name of this resource
        :rtype: unicode
        """
        return self._alerts['name']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description of this resource
        :rtype: unicode
        """
        return self._alerts['friendly_name']

    @property
    def owner_id(self):
        """
        :returns: A string that uniquely identifies this alert's owner
        :rtype: unicode
        """
        return self._alerts['owner_id']

    @property
    def description(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._alerts['description']

    @property
    def tags(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._alerts['tags']

    @property
    def status(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._alerts['status']

    @property
    def metric(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._alerts['metric']

    @property
    def trigger(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._alerts['trigger']

    @property
    def conditions(self):
        """
        :returns:
        :rtype: 
        """
        return self._alerts['conditions']

    @property
    def notifications(self):
        """
        :returns:
        :rtype: 
        """
        return self._alerts['notifications']

    @property
    def locked(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._alerts['locked']

    @property
    def date_created(self):
        """
        :returns: The date this resource was created
        :rtype: datetime
        """
        return self._alerts['date_created']

    @property
    def date_modified(self):
        """
        :returns: The date this resource was last updated
        :rtype: datetime
        """
        return self._alerts['date_updated']

    def fetch(self):
        """
        Fetch a AlertInstance

        :returns: Fetched AlertInstance
        :rtype: connio.rest.api.v3.account.alert.AlertInstance
        """
        return self._proxy.fetch()

    def update(self, name=values.unset, friendly_name=values.unset, status=values.unset):
        """
        Update the AlertInstance

        :param unicode name: Name of the resource
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated AlertInstance
        :rtype: connio.rest.api.v3.account.alert.AlertInstance
        """
        return self._proxy.update(            
            name=name,
            friendly_name=friendly_name,
            status=status
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.AlertInstance {}>'.format(context)
