import pytest
from models import Customer, Order, Payment

@pytest.fixture
def base_url():
    return "http://example.com/api"

@pytest.fixture
def customer_data():
    return Customer(name="John Doe", email="john.doe@example.com", address="123 Elm Street")

@pytest.fixture
def order_data():
    return Order(product_id=1, quantity=2)

@pytest.fixture
def payment_data():
    return Payment(amount=100.0, method="credit_card")

# Customer Service Tests

def test_create_customer(base_url, customer_data):
    response = requests.post(f"{base_url}/customers", json=customer_data.__dict__)
    assert response.status_code == 201


def test_get_customer(base_url):
    customer_id = 1
    response = requests.get(f"{base_url}/customers/{customer_id}")
    assert response.status_code == 200


def test_update_customer(base_url, customer_data):
    customer_id = 1
    response = requests.put(f"{base_url}/customers/{customer_id}", json=customer_data.__dict__)
    assert response.status_code == 200


def test_delete_customer(base_url):
    customer_id = 1
    response = requests.delete(f"{base_url}/customers/{customer_id}")
    assert response.status_code == 204


def test_list_customers(base_url):
    response = requests.get(f"{base_url}/customers")
    assert response.status_code == 200


def test_create_order_for_customer(base_url, order_data):
    customer_id = 1
    response = requests.post(f"{base_url}/customers/{customer_id}/orders", json=order_data.__dict__)
    assert response.status_code == 201


def test_list_orders_for_customer(base_url):
    customer_id = 1
    response = requests.get(f"{base_url}/customers/{customer_id}/orders")
    assert response.status_code == 200


def test_record_payment_for_customer(base_url, payment_data):
    customer_id = 1
    response = requests.post(f"{base_url}/customers/{customer_id}/payments", json=payment_data.__dict__)
    assert response.status_code == 201


def test_list_payments_for_customer(base_url):
    customer_id = 1
    response = requests.get(f"{base_url}/customers/{customer_id}/payments")
    assert response.status_code == 200
