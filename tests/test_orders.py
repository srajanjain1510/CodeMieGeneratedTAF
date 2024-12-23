import pytest
import json
from models import Order, OrderDetail
from utils.api_client import APIClient

@pytest.fixture
def client():
    # Assuming you have a test client setup
    from myapp import create_app
    app = create_app()
    return app.test_client()

@pytest.fixture
def order_test_data():
    with open('test_data/orders_test_data.json') as f:
        return json.load(f)

def test_create_order(client, order_test_data):
    order_data = order_test_data['create_order']
    order_detail_data = order_data['order_details'][0]
    order_detail = OrderDetail(**order_detail_data)
    order = Order(customer_id=order_data['customer_id'], order_details=[order_detail])
    response = client.post('/orders', json=order.__dict__)
    assert response.status_code == 201
    assert response.json()['customer_id'] == order_data['customer_id']

def test_update_order(client, order_test_data):
    order_data = order_test_data['update_order']
    order_detail_data = order_data['order_details'][0]
    order_detail = OrderDetail(**order_detail_data)
    order = Order(customer_id=order_data['customer_id'], order_details=[order_detail])
    response = client.put(f"/orders/{order_data['order_id']}", json=order.__dict__)
    assert response.status_code == 200
    assert response.json()['customer_id'] == order_data['customer_id']

def test_delete_order(client, order_test_data):
    order_id = order_test_data['delete_order']['order_id']
    response = client.delete(f"/orders/{order_id}")
    assert response.status_code == 204

def test_list_orders(client):
    response = client.get('/orders')
    assert response.status_code == 200
    assert isinstance(response.json(), list)