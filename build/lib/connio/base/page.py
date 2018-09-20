import json

from math import ceil
from connio.base.exceptions import ConnioException


class Page(object):
    """
    Represents a page of records in a collection.

    A `Page` lets you iterate over its records and fetch the next and previous
    pages in the collection.
    """
    
    META_KEYS = {
        'total',
        'itemCount',
        'numOfPages',
        'pageNo',
        'page',
        'skip'
    }

    def __init__(self, version, response):
        payload = self.process_response(response)

        self._version = version
        self._payload = payload
        self._solution = {}
        self._records = iter(self.load_page(payload))

    def __iter__(self):
        """
        A `Page` is a valid iterator.
        """
        return self

    def __next__(self):
        return self.next()

    def next(self):
        """
        Returns the next record in the `Page`.
        """
        return self.get_instance(next(self._records))

    @classmethod
    def process_response(self, response):
        """
        Load a JSON response.

        :param Response response: The HTTP response.
        :return dict: The JSON-loaded content.
        """
        if response.status_code != 200:
            raise ConnioException('Unable to fetch page', response)

        return json.loads(response.text)

    def load_page(self, payload):
        """
        Parses the collection of records out of a list payload.

        :param dict payload: The JSON-loaded content.
        :return list: The list of records.
        """
        if 'meta' in payload and 'key' in payload['meta']:
            return payload[payload['meta']['key']]
        else:
            keys = set(payload.keys())
            key = keys - self.META_KEYS
            if len(key) == 1:
                return payload[key.pop()]

        raise ConnioException('Page Records can not be deserialized')

    @property
    def previous_page_url(self):
        """
        :return str: Returns a link to the previous_page_url or None if doesn't exist.
        """
        if 'total' in self._payload and self._payload['total'] == 0:
            return None
        elif 'pageNo' in self._payload and self._payload['pageNo'] == 1:
            return None
        else:
            return self._version.domain.absolute_url(
                self.mk_page_url_path().format(
                    self._version.version, 
                    self._solution['account_id'], 
                    self._payload['pageNo'] - 1, 
                    int(ceil(self._payload['itemCount'] / float(self._payload['numOfPages'])))
                )
            )

    @property
    def next_page_url(self):
        """
        :return str: Returns a link to the next_page_url or None if doesn't exist.
        """
        if 'total' in self._payload and self._payload['total'] == 0:
            return None
        elif 'pageNo' in self._payload and self._payload['pageNo'] + 1 > self._payload['numOfPages']:
            return None
        else:
            id = "_this_"
            if "account_id" in self._solution:
                id = self._solution["account_id"]

            return self._version.domain.absolute_url(
                self.mk_page_url_path().format(
                    self._version.version, 
                    id, 
                    self._payload['pageNo'] + 1, 
                    self._payload['itemCount']
                )
            )

    def get_instance(self, payload):
        """
        :param dict payload: A JSON-loaded representation of an instance record.
        :return: A rich, resource-dependent object.
        """
        raise ConnioException('Page.get_instance() must be implemented in the derived class')

    def mk_page_url_path(self):
        """
        :return: 
        """
        raise ConnioException('Page.mk_page_url_path() must be implemented in the derived class')

    def next_page(self):
        """
        Return the `Page` after this one.
        :return Page: The next page.
        """
        if not self.next_page_url:
            return None

        response = self._version.domain.client.request('GET', self.next_page_url)
        cls = type(self)
        return cls(self._version, response, self._solution)

    def previous_page(self):
        """
        Return the `Page` before this one.
        :return Page: The previous page.
        """
        if not self.previous_page_url:
            return None

        response = self._version.domain.connio.request('GET', self.previous_page_url)
        cls = type(self)
        return cls(self._version, response, self._solution)

    def __repr__(self):
        return '<Page>'
