
from connio.base import values
from connio.base.instance_context import InstanceContext
from connio.base.instance_resource import InstanceResource
from connio.base.list_resource import ListResource
from connio.base.page import Page

class ApiKeyContext(InstanceContext):
    """  """

    def __init__(self, version, account_id, owner_type, owner_id):
        """
        Initialize the ApiKeyContext

        :param Version version: Version that contains the resource
        :param account_id: The account_id
        
        :returns: connio.rest.api.v3.account.apikey.ApiKeyContext
        :rtype: connio.rest.api.v3.account.apikey.ApiKeyContext
        """
        super(ApiKeyContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_id': account_id, 'owner_type': owner_type,  'owner_id': owner_id, }
        self._uri = '/accounts/{account_id}/{owner_type}/{owner_id}/apikey'.format(**self._solution)
            
    def fetch(self):
        """
        Fetch a ApiKeyInstance

        :returns: Fetched ApiKeyInstance
        :rtype: connio.rest.api.v3.account.apikey.ApiKeyInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ApiKeyInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            owner_type=self._solution['owner_type'],
            owner_id=self._solution['owner_id'],
        )

    def update(self, context=values.unset, scope=values.unset, rate_limit=values.unset):
        """
        Update the ApiKeyInstance

        :param unicode context: 
        :param unicode scope: 

        :returns: Updated ApiKeyInstance
        :rtype: connio.rest.api.v3.account.apikey.ApiKeyInstance
        """
        data = values.of({
            'context': context,
            'scope': scope,
            'rateLimit': rate_limit,
        })

        payload = self._version.update(
            'PUT',
            self._uri,
            data=data,
        )

        return ApiKeyInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            owner_type=self._solution['owner_type'],
            owner_id=self._solution['owner_id'],
        )

    def regen(self):
        """
        Regenerate the key credentials

        :returns: Updated ApiKeyInstance
        :rtype: connio.rest.api.v3.account.apikey.ApiKeyInstance
        """
        payload = self._version.update(
            'POST',
            self._uri,
        )

        return ApiKeyInstance(
            self._version,
            payload,
            account_id=self._solution['account_id'],
            owner_type=self._solution['owner_type'],
            owner_id=self._solution['owner_id'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.ApiKeyContext {}>'.format(context)


class ApiKeyInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_id, owner_type, owner_id):
        """
        Initialize the ApiKeyInstance

        :returns: connio.rest.api.v3.account.apikey.ApiKeyInstance
        :rtype: connio.rest.api.v3.account.apikey.ApiKeyInstance
        """
        from connio.base import deserialize

        super(ApiKeyInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_id': payload['accountId'],
            'id': payload['id'],
            'secret': payload['secret'],
            'owner_id': payload['ownerId'],
            'context': payload['context'],
            'scope': payload['scope'],
            'rate_limit': payload['rateLimit'],
            'date_created': deserialize.iso8601_datetime(payload['dateCreated']),
            'date_updated': deserialize.iso8601_datetime(payload['dateModified']),
        }

        # Context
        self._context = None
        self._solution = {'account_id': account_id, 'owner_type': owner_type, 
                            'owner_id': owner_id or self._properties['owner_id'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: DeviceProfileContext for this ApiKeyInstance
        :rtype: connio.rest.api.v3.account.apikey.ApiKeyContext
        """
        if self._context is None:
            self._context = ApiKeyContext(
                self._version,
                account_id=self._solution['account_id'],
                owner_type=self._solution['owner_type'],
                owner_id=self._solution['owner_id'],
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
        :returns: A string that uniquely identifies this apikey
        :rtype: unicode
        """
        return self._properties['id']

    @property
    def secret(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['secret']

    @property
    def owner_id(self):
        """
        :returns: A string that uniquely identifies this apikey's owner
        :rtype: unicode
        """
        return self._properties['owner_id']

    @property
    def context(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['context']

    @property
    def scope(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['scope']

    @property
    def rate_limit(self):
        """
        :returns:
        :rtype: unicode
        """
        return self._properties['rate_limit']

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
        Fetch a ApiKeyInstance

        :returns: Fetched ApiKeyInstance
        :rtype: connio.rest.api.v3.account.apikey.ApiKeyInstance
        """
        return self._proxy.fetch()

    def update(self, context=values.unset, scope=values.unset, rate_limit=values.unset):
        """
        Update the ApiKeyInstance

        :param unicode context:
        :param unicode scope:
        :param unicode rate_limit:

        :returns: Updated ApiKeyInstance
        :rtype: connio.rest.api.v3.account.apikey.ApiKeyInstance
        """
        return self._proxy.update(
            context=context,
            scope=scope,
            rate_limit=rate_limit,
        )

    def regen(self):
        """
        Regenerate the key credentials

        :returns: Updated ApiKeyInstance
        :rtype: connio.rest.api.v3.account.apikey.ApiKeyInstance
        """
        return self._proxy.regen()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Connio.Api.V3.ApiKeyInstance {}>'.format(context)
