
def test_sample_endpoint(api_client, config):
    endpoint = config['endpoints']['sample_endpoint']
    response = api_client.get(endpoint)
    assert response.status_code == 200

import requests

class TestAPI:
    def test_example(self):
        response = requests.get('http://localhost:5000/example')
        assert response.status_code == 200
def test_list_users(api_client):
    response = api_client.get('/users?page=2')
    assert response.status_code == 200
    assert 'data' in response.json()

def test_single_user(api_client):
    response = api_client.get('/users/2')
    assert response.status_code == 200
    assert response.json()['data']['id'] == 2

def test_create_user(api_client):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = api_client.post('/users', json=payload)
    assert response.status_code == 201
    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'leader'
