import pytest
from models import OrderDetail, Order

@pytest.fixture
def client():
    # Assuming you have a test client setup
    from myapp import create_app
    app = create_app()
    return app.test_client()

def test_get_order(client):
    response = client.get('/orders/1')
    assert response.status_code == 200

def test_update_order(client):
    order_detail = OrderDetail(product_id=1, quantity=3, price=10.99)
    order = Order(customer_id=1, order_details=[order_detail])
    response = client.put('/orders/1', json=order.__dict__)
    assert response.status_code == 200

def test_delete_order(client):
    response = client.delete('/orders/1')
    assert response.status_code == 204

def test_list_orders(client):
    response = client.get('/orders')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_order_detail(client):
    order_detail = OrderDetail(product_id=1, quantity=2, price=9.99)
    response = client.post('/orders/1/details', json=order_detail.__dict__)
    assert response.status_code == 201

def test_update_order_detail(client):
    order_detail = OrderDetail(product_id=1, quantity=3, price=10.99)
    response = client.put('/orders/1/details/1', json=order_detail.__dict__)
    assert response.status_code == 200

def test_delete_order_detail(client):
    response = client.delete('/orders/1/details/1')
    assert response.status_code == 204

def test_list_order_details(client):
    response = client.get('/orders/1/details')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
