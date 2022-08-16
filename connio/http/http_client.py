from requests import Request, Session, hooks

from connio.http import HttpClient
from connio.http.response import Response
from connio.http.request import Request as ConnioRequest
import logging
from connio.compat import urlencode

_logger = logging.getLogger('connio.http_client')


class ConnioHttpClient(HttpClient):
    """
    General purpose HTTP Client for interacting with the Connio API
    """
    def __init__(self, pool_connections=True, request_hooks=None):
        self.session = Session() if pool_connections else None
        self.last_request = None
        self.last_response = None
        self.request_hooks = request_hooks or hooks.default_hooks()

    def request(self, method, url, params=None, data=None, headers=None, auth=None, timeout=None,
                allow_redirects=False):
        """
        Make an HTTP Request with parameters provided.

        :param str method: The HTTP method to use
        :param str url: The URL to request
        :param dict params: Query parameters to append to the URL
        :param dict data: Parameters to go in the body of the HTTP request
        :param dict headers: HTTP Headers to send with the request
        :param tuple auth: Basic Auth arguments
        :param float timeout: Socket/Read timeout for the request
        :param boolean allow_redirects: Whether or not to allow redirects
        See the requests documentation for explanation of all these parameters

        :return: An http response
        :rtype: A :class:`Response <connio.rest.http.response.Response>` object
        """

        kwargs = {
            'method': method.upper(),
            'url': url,
            'params': params,
            'json': data,
            'headers': headers,
            'auth': auth,
            'hooks': self.request_hooks
        }

        if params:
            _logger.debug('{method} Request: {url}?{query}'.format(query=urlencode(params), **kwargs))
            _logger.debug('PARAMS: {params}'.format(**kwargs))
        else:
            _logger.debug('{method} Request: {url}'.format(**kwargs))
        if data:
            _logger.debug('PAYLOAD: {json}'.format(**kwargs))

        self.last_response = None
        session = self.session or Session()
        request = Request(**kwargs)
        self.last_request = ConnioRequest(**kwargs)

        prepped_request = session.prepare_request(request)
        response = session.send(
            prepped_request,
            allow_redirects=allow_redirects,
            timeout=timeout,
        )
        
        _logger.debug(u'{method} Response: {status} {text}'.format(
            method=method, status=response.status_code, text=response.text))

        self.last_response = Response(int(response.status_code), response.text)

        return self.last_response
