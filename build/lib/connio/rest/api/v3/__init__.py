
from connio.base.version import Version
from connio.rest.api.v3.account import AccountContext
from connio.rest.api.v3.account import AccountList
from connio.rest.api.v3.sysuser import SysUserList
from connio.rest.api.v3.helpers import HelperContext


class V3(Version):

    def __init__(self, domain):
        """
        Initialize the V3 version of Api

        :returns: V3 version of Api
        :rtype: connio.rest.api.v3.V3
        """
        super(V3, self).__init__(domain)
        self.sysAdminPath = domain.sys
        self.version = 'v3' + (self.sysAdminPath or '')
        self._account = None
        self._accounts = None
        self._sysusers = None
        self._helpers = None

    @property
    def accounts(self):
        """
        :rtype: connio.rest.api.v3.account.AccountList
        """
        if self._accounts is None:
            self._accounts = AccountList(self)
        return self._accounts

    @property
    def account(self):
        """
        :returns: Account provided as the authenticating account
        :rtype: AccountContext
        """
        if self._account is None:
            self._account = AccountContext(self, '_this_')
        return self._account

    @property
    def system_users(self):
        """
        :rtype: connio.rest.api.v3.sysuser.SysUserList
        """
        if self._sysusers is None and self.sysAdminPath is not None:
            self._sysusers = SysUserList(self)
        return self._sysusers

    @property
    def helpers(self):
        """
        
        """
        if self.sysAdminPath is not None:
            self._helpers = HelperContext(self)
        return self._helpers

    # We don't want to override the primary account
    # @account.setter
    # def account(self, value):
    #     """
    #     Setter to override the primary account

    #     :param AccountContext|AccountInstance value: account to use as primary account
    #     """
    #     self._account = value

    @property
    def users(self):
        """
        :rtype: connio.rest.api.v3.account.user.UserList
        """
        return self.account.users

    @property
    def apiclients(self):
        """
        :rtype: connio.rest.api.v3.account.apiclient.ApiClientList
        """
        return self.account.apiclients  

    @property
    def deviceprofiles(self):
        """
        :rtype: connio.rest.api.v3.account.deviceprofile.DeviceProfileList
        """
        return self.account.deviceprofiles

    @property
    def devices(self):
        """
        :rtype: connio.rest.api.v3.account.device.DeviceList
        """
        return self.account.devices  

    @property
    def appprofiles(self):
        """
        :rtype: connio.rest.api.v3.account.appprofile.AppProfileList
        """
        return self.account.appprofiles

    @property
    def apps(self):
        """
        :rtype: connio.rest.api.v3.account.app.AppList
        """
        return self.account.apps 

    @property
    def properties(self, owner_id):
        """
        :rtype: connio.rest.api.v3.account.property.PropertyList
        """
        return self.account.properties(owner_id)  

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Connio.Api.V3>'
