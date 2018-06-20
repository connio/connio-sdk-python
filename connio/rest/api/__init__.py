
from connio.base.domain import Domain
from connio.rest.api.v3 import V3

class Api(Domain):

    def __init__(self, client):
        """
        Initialize the Api Domain

        :returns: Domain for Api
        :rtype: connio.rest.api.Api
        """ 
        super(Api, self).__init__(client)

        self.base_url = client.host
        self.sys = client.sys

        # Versions
        self._v3 = None

    @property
    def v3(self):
        """
        :returns: Version v3 of accounts
        :rtype: connio.rest.accounts.v3.V3
        """
        if self._v3 is None:
            self._v3 = V3(self)
        return self._v3

    @property
    def account(self):
        """
        :returns: Account provided as the authenticating account
        :rtype: connio.rest.api.v3.account.AccountContext
        """
        return self.v3.account

    @property
    def accounts(self):
        """
        :rtype: connio.rest.api.v3.account.AccountList
        """
        return self.v3.accounts

    @property
    def users(self):
        """
        :rtype: connio.rest.api.v3.sysuser.SysUserList
        """
        return self.v3.system_users

    @property
    def helpers(self):
        """
        :rtype: connio.rest.api.v3
        """
        return self.v3.helpers

