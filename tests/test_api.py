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