import pytest
from models import Order, OrderDetail

@pytest.fixture
def client():
    # Assuming you have a test client setup
    from myapp import create_app
    app = create_app()
    return app.test_client()


def test_create_order(client):
    order_detail = OrderDetail(product_id=1, quantity=2, price=9.99)
    order = Order(customer_id=1, order_details=[order_detail])
    response = client.post('/orders', json=order.__dict__)
    assert response.status_code == 201


def test_update_order(client):
    order_detail = OrderDetail(product_id=1, quantity=3, price=8.99)
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
