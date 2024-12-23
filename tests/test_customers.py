import pytest
from models import Customer, OrderDetail, Order, Payment

@pytest.fixture
def client():
    # Assuming you have a test client setup
    from myapp import create_app
    app = create_app()
    return app.test_client()

def test_create_customer(client):
    customer = Customer(name='John Doe', address='123 Elm Street', email='john.doe@example.com')
    response = client.post('/customers', json=customer.__dict__)
    assert response.status_code == 201
    assert response.json()['name'] == 'John Doe'

def test_get_customer(client):
    response = client.get('/customers/1')
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_update_customer(client):
    customer = Customer(name='Jane Doe', address='456 Oak Street', email='jane.doe@example.com')
    response = client.put('/customers/1', json=customer.__dict__)
    assert response.status_code == 200
    assert response.json()['name'] == 'Jane Doe'

def test_delete_customer(client):
    response = client.delete('/customers/1')
    assert response.status_code == 204

def test_list_customers(client):
    response = client.get('/customers')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_order(client):
    order_detail = OrderDetail(product_id=1, quantity=2, price=9.99)
    order = Order(customer_id=1, order_details=[order_detail])
    response = client.post('/customers/1/orders', json=order.__dict__)
    assert response.status_code == 201

def test_create_payment(client):
    payment = Payment(order_id=1, amount=19.98)
    response = client.post('/customers/1/payments', json=payment.__dict__)
    assert response.status_code == 201
    assert response.json()['amount'] == 19.98