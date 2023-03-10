from __future__ import annotations
from requests import get
from .structs import Endpoint


class Client:
    """
    Base class to interact with the api
    """

    def __init__(self, key: str = None) -> None:
        self.api_key = key
        self.__endpoints = []
        self.__loadEndpoints()

    def __loadEndpoints(self) -> None:
        """
        Method to initialize the endpoint cache
        """
        r = get("https://some-random-api.ml/endpoints?format=json", timeout=5)
        data = r.json()

        for categories in data:
            category = data[categories]
            for endpoint in category:
                self.__endpoints.append(Endpoint(endpoint))

    def fetch(self, path: str, query: dict = None) -> dict | bytes:
        """
        Fetch from an endpoint
        """
        endpoint = next((x for x in self.__endpoints if x.path == path), None)
        if endpoint is None:
            raise 'Invalid endpoint provided'
        
        if query is not None and self.api_key is not None:
            query['key'] = self.api_key
        
        self.__validate_request(endpoint, query)
        try:
            res = get('https://some-random-api.ml/' + path, params = query, timeout = 5)
            if res.ok is False:
                raise 'Error when fetching from api. Got status code ' + res.status_code
            ctype = 'application/json'
            if 'content-type' in res.headers:
                ctype = res.headers['content-type']

            if 'application/json' in ctype:
                out = res.json()
                if 'error' in out:
                    raise out['error']
                return out
            elif 'image' in ctype:
                return res.content

            raise 'Invalid content type received from api. Got ' + res
        except:
            raise

    def __validate_request(self, endpoint: Endpoint, query: dict):
        pass

