import pytest
from models.customer import Customer

@pytest.fixture
def client():
    from requests import Session
    return Session()

def test_create_customer(client):
    customer = Customer(name='John Doe', address='123 Elm Street', email='john.doe@example.com')
    response = client.post('http://localhost:8000/customers', json=customer.__dict__)
    assert response.status_code == 201
    assert response.json()['name'] == 'John Doe'

def test_get_customer(client):
    response = client.get('http://localhost:8000/customers/1')
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_update_customer(client):
    customer = Customer(name='Jane Doe', address='456 Oak Street', email='jane.doe@example.com')
    response = client.put('http://localhost:8000/customers/1', json=customer.__dict__)
    assert response.status_code == 200
    assert response.json()['name'] == 'Jane Doe'

def test_delete_customer(client):
    response = client.delete('http://localhost:8000/customers/1')
    assert response.status_code == 204
