import requests


class APIClient:

    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers if headers is not None else {}

    def _full_url(self, endpoint):
        return f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

    def get(self, endpoint, params=None):
        response = requests.get(self._full_url(endpoint), headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None, json=None):
        response = requests.post(self._full_url(endpoint), headers=self.headers, data=data, json=json)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data=None, json=None):
        response = requests.put(self._full_url(endpoint), headers=self.headers, data=data, json=json)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint):
        response = requests.delete(self._full_url(endpoint), headers=self.headers)
        response.raise_for_status()
        return response.json()