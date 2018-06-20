
from connio.base import deserialize
from connio.base import values
from connio.base.instance_context import InstanceContext
from connio.rest.api.v3.account.user import UserInstance

class HelperContext(InstanceContext):
    """  """

    def __init__(self, version):
        """
        """
        super(HelperContext, self).__init__(version)

        # Path Solution
        self._solution = {}        
        self._uri = ''

    def activate(self, token):
        """       
        """
        params = values.of({
            'token': token
        })

        payload = self._version.fetch(
            'GET',
            self._uri + '/activate',
            params=params,
        )
        return UserInstance(self._version, payload, payload['accountId'])