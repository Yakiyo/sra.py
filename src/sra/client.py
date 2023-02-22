import json
from requests import get
from .structs import Endpoint


class Client:
    """
    Base class to interact with the api
    """

    def __init__(self, key: str = None) -> None:
        self.api_key = key
        self._endpoints = []
        self._loadEndpoints()

    def _loadEndpoints(self) -> None:
        """
        Method to initialize the endpoint cache
        """
        r = get("https://some-random-api.ml/endpoints?format=json", timeout=5)
        data = json.loads(r.content)

        for categories in data:
            category = data[categories]
            for endpoint in category:
                self._endpoints.append(Endpoint(endpoint))

    def fetch(self, path: str, query: dict = None) -> dict:
        ep = next((x for x in self._endpoints if x.path == path), None)
        if ep is None:
            raise 'Invalid endpoint provided'
        return ep

