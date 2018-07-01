
import json

from connio.base import deserialize
from connio.base import values
from connio.base.instance_context import InstanceContext
from connio.base.instance_resource import InstanceResource
from connio.base.list_resource import ListResource
from connio.base.page import Page

class DataConnectorList(ListResource):
    """  """

    def __init__(self, version, account_id, owner_id):
        """
        Initialize the DataConnectorList

        :param Version version: Version that contains the resource
        :param account_id: The unique id that identifies this account
        :param owner_id: The unique id that identifies the owner app of this data connector

        :returns: connio.rest.api.v3.account.dataconnector.DataConnectorList
        :rtype: connio.rest.api.v3.account.dataconnector.DataConnectorList
        """
        super(DataConnectorList, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'owner_id': owner_id, }
        self._uri = '/accounts/{account_id}/apps/{owner_id}/dataconnectors'.format(**self._solution)

    def create(self, id, type, config, disabled=values.unset):
        """
        Create a new DataConnectorInstance

        :param unicode id: Unique identifier assinged to this data connector
        :param unicode type: 
        :param unicode config:
        
        :returns: Newly created DataConnectorInstance
        :rtype: connio.rest.api.v3.account.dataconnector.DataConnectorInstance
        """
        
        data = None
        if type == DataConnectorInstance.ConnectorType.COUCHDB:
            data = values.of({
                'id': id,
                'type': type,
                'disabled': disabled,
                'server': config['server'],
                'databaseName': config['database_name'],
                'port': config['port'],
                'ssl': config['ssl'],
                'credentials': config['credentials']
            })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return DataConnectorInstance(self._version, payload, account_id=self._solution['account_id'], owner_id=self._solution['owner_id'], )

    def list(self):
        """
        """
        response = self._version.page(
            'GET',
            self._uri,
        )

        connectors = list()
        for connector in json.loads(response.content):
            connectors.append(
                DataConnectorInstance(self._version, connector, account_id=self._solution['account_id'], owner_id=self._solution['owner_id'], )
            )

        return connectors

    def get(self, id):
        """
        Constructs a DataConnectorContext

        :param id: Fetch by unique connector id

        :returns: connio.rest.api.v3.account.dataconnector.DataConnectorContext
        :rtype: connio.rest.api.v3.account.dataconnector.DataConnectorContext
        """
        return DataConnectorContext(self._version, account_id=self._solution['account_id'], owner_id=self._solution['owner_id'], id=id, )

    def __call__(self, owner_id):
        """
        Constructs a DataConnectorContext

        :param owner_id: Owner id

        :returns: connio.rest.api.v3.account.dataconnector.DataConnectorContext
        :rtype: connio.rest.api.v3.account.dataconnector.DataConnectorContext
        """
        return DataConnectorList(self._version, account_id=self._solution['account_id'], owner_id=owner_id, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3.DataConnectorList>'


class DataConnectorContext(InstanceContext):
    """  """

    def __init__(self, version, account_id, owner_id, id):
        """
        Initialize the DataConnectorContext

        :param Version version: Version that contains the resource
        :param account_id: The account_id
        :param owner_id: The owner_id
        :param id: Fetch by unique entity id

        :returns: connio.rest.api.v3.account.dataconnector.DataConnectorContext
        :rtype: connio.rest.api.v3.account.dataconnector.DataConnectorContext
        """
        super(DataConnectorContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'owner_id': owner_id, 'id': id, }
        self._uri = '/accounts/{account_id}/apps/{owner_id}/dataconnectors/{id}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a DataConnectorInstance

        :returns: Fetched DataConnectorInstance
        :rtype: connio.rest.api.v3.account.dataconnector.DataConnectorInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return DataConnectorInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            owner_id=self._solution['owner_id'],
            id=self._solution['id'],
        )

    def update(self, id, type, disabled=values.unset, config=values.unset):
        """
        Update the DataConnectorInstance

        :param unicode config: 

        :returns: Updated DataConnectorInstance
        :rtype: connio.rest.api.v3.account.dataconnector.DataConnectorInstance
        """

        data = None
        if type == DataConnectorInstance.ConnectorType.COUCHDB:
            data = values.of({
                'id': id,
                'type': type,
                'disabled': disabled,
                'server': config['server'],
                'database_name': config['databaseName'],
                'port': config['port'],
                'ssl': config['ssl'],
                'credentials': config['credentials']
            })
        
        payload = self._version.update(
            'PUT',
            self._uri,
            data=data,
        )

        return DataConnectorInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            owner_id=self._solution['owner_id'],
            id=self._solution['id'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.DataConnectorContext {}>'.format(context)


class DataConnectorInstance(InstanceResource):
    """  """

    class ConnectorType(object):
        COUCHDB = "couchDB"

    def __init__(self, version, payload, account_id, owner_id, id=None):
        """
        Initialize the DataConnectorInstance

        :returns: connio.rest.api.v3.account.dataconnector.DataConnectorInstance
        :rtype: connio.rest.api.v3.account.dataconnector.DataConnectorInstance
        """
        super(DataConnectorInstance, self).__init__(version)

        config = {}
        if payload.get('type') == DataConnectorInstance.ConnectorType.COUCHDB:
            # Marshaled Properties
            config = {
                'server': payload['server'],
                'database_name': payload['databaseName'],
                'port': payload['port'],
                'ssl': payload['ssl'],
                'credentials': payload['credentials']
            }

        self._properties = {
            'id': payload['id'],
            'type': payload['type'],
            'disabled': payload['disabled'],
            'config': config
        }

        # Context
        self._context = None
        self._solution = {'account_id': account_id, 'owner_id': owner_id, 'id': id or self._properties['id'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: DataConnectorContext for this DataConnectorInstance
        :rtype: connio.rest.api.v3.account.dataconnector.DataConnectorContext
        """
        if self._context is None:
            self._context = DataConnectorContext(
                self._version,
                account_id=self._solution['account_id'],
                owner_id=self._solution['owner_id'],
                id=self._solution['id'],
            )
        return self._context

    @property
    def id(self):
        """
        :returns: A string that uniquely identifies this data connector
        :rtype: unicode
        """
        return self._properties['id']

    @property
    def type(self):
        """
        :returns: Type of the data connector
        :rtype: unicode
        """
        return self._properties['type']

    @property
    def disabled(self):
        """
        :returns: Status of the data connector
        :rtype: unicode
        """
        return self._properties['disabled']

    @property
    def config(self):
        """
        :returns: 
        :rtype: unicode
        """
        return self._properties['config']

    def fetch(self):
        """
        Fetch a DataConnectorInstance

        :returns: Fetched DataConnectorInstance
        :rtype: connio.rest.api.v3.account.dataconnector.DataConnectorInstance
        """
        return self._proxy.fetch()

    def update(self, id=values.unset, config=values.unset):
        """
        Update the DataConnectorInstance

        :param unicode id: Id of the resource
        :param unicode config:

        :returns: Updated DataConnectorInstance
        :rtype: connio.rest.api.v3.account.dataconnector.DataConnectorInstance
        """
        return self._proxy.update(            
            id=id,
            type=type,
            config=config
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
        return '<Connio.Api.V3.DataConnectorInstance {}>'.format(context)
