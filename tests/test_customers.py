import json
import pytest
from models import Customer

@pytest.fixture
def client(api_client):
    # Assuming you have a test client setup
    return api_client

@pytest.fixture
def customer_test_data():
    with open('test_data/customers_test_data.json') as f:
        return json.load(f)

def test_create_customer(client, customer_test_data):
    customer_data = customer_test_data['create_customer']
    customer = Customer(**customer_data)
    response = client.post('/customers', json=customer.__dict__)
    assert response.status_code == 201
    assert response.json()['name'] == customer_data['name']

def test_update_customer(client, customer_test_data):
    customer_data = customer_test_data['update_customer']
    customer = Customer(**customer_data)
    response = client.put('/customers/1', json=customer.__dict__)
    assert response.status_code == 200
    assert response.json()['name'] == customer_data['name']

def test_delete_customer(client):
    response = client.delete('/customers/1')
    assert response.status_code == 204

def test_list_customers(client):
    response = client.get('/customers')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_customer(client):
    response = client.get('/customers/1')
    assert response.status_code == 200
    assert response.json()['id'] == 1