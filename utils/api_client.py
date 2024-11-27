import requests

class APIClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get(self, endpoint, params=None):
        return requests.get(self.base_url + endpoint, headers=self.headers, params=params)

    def post(self, endpoint, data=None, json=None):
        return requests.post(self.base_url + endpoint, headers=self.headers, data=data, json=json)

    def put(self, endpoint, data=None, json=None):
        return requests.put(self.base_url + endpoint, headers=self.headers, data=data, json=json)

    def delete(self, endpoint):
        return requests.delete(self.base_url + endpoint, headers=self.headers)