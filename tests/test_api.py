from dataclasses import dataclass

@dataclass
class User:
    name: str
    job: str

def test_list_users(api_client):
    response = api_client.get('/users?page=2')
    assert response.status_code == 200
    assert 'data' in response.json()

def test_single_user(api_client):
    response = api_client.get('/users/3')
    assert response.status_code == 200
    assert response.json()['data']['id'] == 3

def test_create_user(api_client):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = api_client.post('/users', json=payload)
    assert response.status_code == 201
    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'leader'

def test_create_user_with_dataclass(api_client):
    user = User(name="neo", job="the one")
    response = api_client.post('/users', json=user.__dict__)
    assert response.status_code == 201
    assert response.json()['name'] == 'neo'
    assert response.json()['job'] == 'the one'