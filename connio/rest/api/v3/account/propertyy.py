
from connio.base import values
from connio.base.instance_context import InstanceContext
from connio.base.instance_resource import InstanceResource
from connio.base.list_resource import ListResource
from connio.base.page import Page

class PropertyList(ListResource):
    """  """

    def __init__(self, version, account_id, owner_id, tags=values.unset):
        """
        Initialize the PropertyList

        :param Version version: Version that contains the resource
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.property.PropertyList
        :rtype: connio.rest.api.v3.account.property.PropertyList
        """
        super(PropertyList, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'owner_id': owner_id, 'tags': tags}
        uri = f'/accounts/{account_id}/properties?owner={owner_id}'

        if(tags is not values.unset):
            uri += '&tags='

            for tag in tags:
                uri += f'{tag},'

            uri = uri[:-1]

        self._uri = uri

    def create(self, name, data_type, access_type, publish_type, friendly_name=values.unset, description=values.unset,
                tags=values.unset, measurement=values.unset, retention=values.unset, boundaries=values.unset, locked=values.unset):
        """
        Create a new PropertyInstance

        :param unicode name: A name uniquely identifying this property within account context
        :param unicode owner_id: Property owner's id
        :param unicode type: Property data type
        :param unicode friendly_name: A human readable description of the application
        :param unicode description: A description of this property
        :param unicode tags: Tags associated with this property
        
        :returns: Newly created PropertyInstance
        :rtype: connio.rest.api.v3.account.property.PropertyInstance
        """
        from connio.base import serialize

        data = values.of({
            'name': name,
            'ownerId': self._solution['owner_id'],
            'friendlyName': friendly_name,
            'description': description,
            'tags': tags,
            'type': data_type,
            'access': access_type,
            'publish': publish_type,
            'measurement': serialize.measurement(measurement),
            'boundaries': serialize.boundaries(boundaries),        
            'retention': serialize.retention(retention),
            'locked': locked,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return PropertyInstance(self._version, payload, account_id=self._solution['account_id'], )    

    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams PropertyInstance records from the API as a generator stream.
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
        :rtype: list[connio.rest.api.v3.account.property.PropertyInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(friendly_name=friendly_name, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists PropertyInstance records from the API as a list.
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
        :rtype: list[connio.rest.api.v3.account.property.PropertyInstance]
        """
        return list(self.stream(
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
            
        ))

    def page(self, friendly_name=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of PropertyInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: Filter by friendly name
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 200

        :returns: Page of PropertyInstance
        :rtype: connio.rest.api.v3.account.property.PropertyPage
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

        return PropertyPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of PropertyInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PropertyInstance
        :rtype: connio.rest.api.v3.account.property.PropertyPage
        """
        response = self._version.domain.client.request(
            'GET',
            target_url,
        )

        return PropertyPage(self._version, response, self._solution)

    def get(self, id):
        """
        Constructs a PropertyContext

        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.property.PropertyContext
        :rtype: connio.rest.api.v3.account.property.PropertyContext
        """
        return PropertyContext(self._version, account_id=self._solution['account_id'], id=id, )

    def __call__(self, owner_id):
        """
        Constructs a PropertyContext

        :param owner_id: Owner id

        :returns: connio.rest.api.v3.account.property.PropertyContext
        :rtype: connio.rest.api.v3.account.property.PropertyContext
        """
        return PropertyList(self._version, account_id=self._solution['account_id'], owner_id=owner_id, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.PropertyList>'


class PropertyPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the PropertyPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_id: The unique id that identifies this account

        :returns: connio.rest.api.v3.account.property.PropertyPage
        :rtype: connio.rest.api.v3.account.property.PropertyPage
        """
        super(PropertyPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of PropertyInstance

        :param dict payload: Payload response from the API

        :returns: connio.rest.api.v3.account.property.PropertyInstance
        :rtype: connio.rest.api.v3.account.property.PropertyInstance
        """
        return PropertyInstance(self._version, payload, account_id=self._solution['account_id'], )

    def mk_page_url_path(self):
        """
        :return: 
        """
        return f'{{}}/accounts/{{}}/properties?ownerId={self._solution["owner_id"]}&pageNo={{}}&pageSize={{}}'

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.PropertyPage>'


class PropertyContext(InstanceContext):
    """  """

    def __init__(self, version, account_id, id):
        """
        Initialize the PropertyContext

        :param Version version: Version that contains the resource
        :param account_id: The account_id
        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.property.PropertyContext
        :rtype: connio.rest.api.v3.account.property.PropertyContext
        """
        super(PropertyContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'id': id, }
        self._uri = '/accounts/{account_id}/properties/{id}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a PropertyInstance

        :returns: Fetched PropertyInstance
        :rtype: connio.rest.api.v3.account.property.PropertyInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return PropertyInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            id=self._solution['id'],
        )
    def delete(self):
        """
        Delete the Property Instance
        """

        self._version.delete(
            'DELETE',
            self._uri
        )

    def update(self, name=values.unset, friendly_name=values.unset, measurement=values.unset, tags=values.unset):
        """
        Update the PropertyInstance

        :param unicode name: Given name of the entity
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated PropertyInstance
        :rtype: connio.rest.api.v3.account.property.PropertyInstance
        """
        from connio.base import serialize

        data = values.of({
            'name': name,
            'friendlyName': friendly_name,
            'measurement': serialize.measurement(measurement),
            'tags': tags
        })

        payload = self._version.update(
            'PUT',
            self._uri,
            data=data,
        )

        return PropertyInstance(
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
        return '<Connio.Api.V3.PropertyContext {}>'.format(context)

class PropertyInstance(InstanceResource):
    """  """

    class MeasurementUnit(object):
        def __init__(self, label, symbol):
            self.label = label
            self.symbol = symbol

        def __eq__(self, other):
            if type(self) is not type(other):
                return False
            return self.label == other.label and self.symbol == other.symbol

    class Measurement(object):
        def __init__(self, type, unit, props):
            self._properties = props
            self.type = type
            self.unit = unit

        def __eq__(self, other):
            if type(self) is not type(other):
                return False
            return self.type == other.type and self.unit == other.unit

    class Boundaries(object):
        class Geofence:
            def __init__(self, lat=None, lon=None, radius=None, inside=None):
                self.lat = lat
                self.lon = lon
                self.radius = radius
                self.inside = inside

        def __init__(self, size=values.unset, min=values.unset, max=values.unset, set=values.unset, geofence=values.unset, props=values.unset):
            self.size = size
            self.min = min
            self.max = max
            self.set = set
            self._properties = props

            if geofence is not values.unset:
                self.lat = geofence.lat
                self.lon = geofence.lon
                self.radius = geofence.radius
                self.inside = geofence.inside
            else:
                self.lat = values.unset
                self.lon = values.unset
                self.radius = values.unset
                self.inside = values.unset

        def __eq__(self, other):
            if type(self) is not type(other):
                return False
            return (
                self.size == other.size and
                self.min == other.min and
                self.max == other.max and
                self.set == other.set and
                self.lat == other.lat and
                self.lon == other.lon and
                self.radius == other.radius and
                self.inside == other.inside
            )

    class Context(object):
        def __init__(self, type=values.unset):
            self.type = type

        def __eq__(self, other):
            return self.type == other.type

    class Condition(object):
        class ConditionType:
            ALWAYS = "always"
            CHANGED = "changed"
            CHANGED_BY_X = "changedx"

        def __init__(self, when=values.unset, value=values.unset, props=values.unset):
            self.when = when
            self.value = value
            self._properties = props
        def __eq__(self, other):
            if type(self) is not type(other):
                return False
            return (
                self.when == other.when and
                self.value == other.value
            )
    class Retention(object):
        class RetentionType:
            MOSTRECENT = "mostrecent"
            HISTORICAL = "historical"

        def __init__(self, type=values.unset, context=values.unset, lifetime=values.unset, capacity=values.unset, condition=values.unset, props=values.unset):
            self.type = type
            self.context = context
            self.lifetime = lifetime
            self.capacity = capacity
            self.condition = condition
            self._properties = props

        def __eq__(self, other):
            if type(self) is not type(other):
                return False
            return (
                self.capacity == other.capacity and
                self.type == other.type and
                self.context == other.context and
                self.lifetime == other.lifetime and
                self.condition == other.condition

                )

    def __init__(self, version, payload, account_id, id=None):
        """
        Initialize the PropertyInstance

        :returns: connio.rest.api.v3.account.property.PropertyInstance
        :rtype: connio.rest.api.v3.account.property.PropertyInstance
        """
        from connio.base import deserialize
        super(PropertyInstance, self).__init__(version)
        # Marshaled Properties
        self._properties = values.of({
            'account_id': payload['accountId'],
            'id': payload['id'],
            'owner_id': payload['ownerId'],
            'name': payload['name'],
            'friendly_name': payload['friendlyName'],
            'qualified_name': payload['qualifiedName'],
            'description': payload.get('description'),
            'tags': payload.get('tags'),
            'data_type': payload['type'],
            'access_type': payload['access'],
            'publish_type': payload['publish'],
            'retention': deserialize.retention(payload.get('retention')),
            'measurement': deserialize.measurement(payload.get('measurement')),
            'boundaries': deserialize.boundaries(payload.get('boundaries')),
            'inherited': payload['inherited'],
            'locked': payload['locked'],        
            'date_created': deserialize.iso8601_datetime(payload['dateCreated']),
            'date_updated': deserialize.iso8601_datetime(payload['dateModified']),
        })

        # Context
        self._context = None
        self._solution = {'account_id': account_id, 'id': id or self._properties['id'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: PropertyContext for this PropertyInstance
        :rtype: connio.rest.api.v3.account.property.PropertyContext
        """
        if self._context is None:
            self._context = PropertyContext(
                self._version,
                account_id=self._solution['account_id'],
                id=self._solution['id'],
            )
        return self._context

    @property
    def id(self):
        """
        :returns: A string that uniquely identifies this property
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
        :returns: A string that uniquely identifies this property's owner
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
    def data_type(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['data_type']

    @property
    def access_type(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['access_type']

    @property
    def publish_type(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['publish_type']

    @property
    def retention(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties.get('retention')

    @property
    def boundaries(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties.get('boundaries')

    @property
    def measurement(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties.get('measurement')

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
        Fetch a PropertyInstance

        :returns: Fetched PropertyInstance
        :rtype: connio.rest.api.v3.account.property.PropertyInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Delete property instance
        """

        return self._proxy.delete()

    def update(self, friendly_name=values.unset, name=values.unset, measurement=values.unset, tags=values.unset):
        """
        Update the PropertyInstance

        :param unicode name: Name of the resource
        :param unicode friendly_name: A human readable description of this resource

        :returns: Updated PropertyInstance
        :rtype: connio.rest.api.v3.account.property.PropertyInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            name=name,
            measurement=measurement,
            tags=tags
        )

    def __getitem__(self, key):
        return self._properties[key]

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        return (
            self.data_type == other.data_type and
            self.name == other.name and
            self.friendly_name == other.friendly_name and
            self.description == other.description and
            self.tags == other.tags and
            self.data_type == other.data_type and
            self.access_type == other.access_type and
            self.publish_type == other.publish_type and
            self.retention == other.retention and
            self.boundaries == other.boundaries and
            self.measurement == other.measurement and
            self.locked == other.locked and
            self.inherited == other.inherited
            )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.PropertyInstance {}>'.format(context)
