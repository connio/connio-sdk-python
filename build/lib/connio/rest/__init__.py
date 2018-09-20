
import os
import platform
from connio import __version__
from connio.base.exceptions import ConnioException
from connio.base.obsolete import obsolete_client
from connio.http.http_client import ConnioHttpClient


class Client(object):
    """ A client for accessing the Connio API. """

    def __init__(self, username=None, password=None, host=None, sysadmin=False, region=None,
                 http_client=None, environment=None):
        """
        Initializes the Connio Client

        :param str username: Username to authenticate with
        :param str password: Password to authenticate with
        :param bool sysadmin: Access system with system admin privileges - must provide sys admin credentials
        :param str region: Connio Region to make requests to
        :param HttpClient http_client: HttpClient, defaults to ConnioHttpClient
        :param dict environment: Environment to look for auth details, defaults to os.environ

        :returns: Connio Client
        :rtype: connio.rest.Client
        """
        environment = environment or os.environ

        self.username = username or environment.get('CONNIO_ACCOUNT_KEYID')
        """ :type : str """
        self.password = password or environment.get('CONNIO_ACCOUNT_KEYSECRET')
        """ :type : str """
        self.sys = None
        if sysadmin == True:
            self.sys = '/sys'
        """ :type : bool """
        self.region = region
        """ :type : str """
        self.host = host or 'https://api.connio.cloud'
        """ :type : str """

        if not self.username or not self.password:
            raise ConnioException("Credentials are required to create a ConnioClient")

        self.auth = (self.username, self.password)
        """ :type : tuple(str, str) """
        self.http_client = http_client or ConnioHttpClient()
        """ :type : HttpClient """

        # API 
        self._api = None
       

    def request(self, method, uri, params=None, data=None, headers=None, auth=None,
                timeout=None, allow_redirects=False):
        """
        Makes a request to the Connio API using the configured http client
        Authentication information is automatically added if none is provided

        :param str method: HTTP Method
        :param str uri: Fully qualified url
        :param dict[str, str] params: Query string parameters
        :param dict[str, str] data: POST body data
        :param dict[str, str] headers: HTTP Headers
        :param tuple(str, str) auth: Authentication
        :param int timeout: Timeout in seconds
        :param bool allow_redirects: Should the client follow redirects

        :returns: Response from the Connio API
        :rtype: connio.http.response.Response
        """
        auth = auth or self.auth
        headers = headers or {}

        headers['User-Agent'] = 'connio-python/{} (Python {})'.format(
            __version__,
            platform.python_version(),
        )
        headers['X-Connio-Client'] = 'python-{}'.format(__version__)
        headers['Accept-Charset'] = 'utf-8'

        if method == 'POST' and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        if method == 'PUT' and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        if 'Accept' not in headers:
            headers['Accept'] = 'application/json'

        if self.region:
            head, tail = uri.split('.', 1)

            if not tail.startswith(self.region):
                uri = '.'.join([head, self.region, tail])

        return self.http_client.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects
        )

    @property
    def api(self):
        """
        Access the Api Connio Entity

        :returns: Api Connio Domain
        :rtype: connio.rest.api.Api
        """
        if self._api is None:
            from connio.rest.api import Api
            self._api = Api(self)
        return self._api

    @property
    def account(self):
        """
        :rtype: connio.rest.api.v3.account.account.AccountContext
        """
        return self.api.account

    @property
    def accounts(self):
        """
        :rtype: connio.rest.api.v3.account.account.AccountList
        """
        return self.api.accounts

    @property
    def users(self):
        """
        :rtype: connio.rest.api.v3.user.SysUserList
        """
        return self.api.users