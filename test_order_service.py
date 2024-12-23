import pytest
from models import Order

@pytest.fixture

def base_url():
    return "http://example.com/api"

@pytest.fixture

def order_data():
    return Order(product_id=1, quantity=2)

# Order Service Tests

def test_get_order(base_url):
    order_id = 1
    response = requests.get(f"{base_url}/orders/{order_id}")
    assert response.status_code == 200


def test_update_order(base_url, order_data):
    order_id = 1
    response = requests.put(f"{base_url}/orders/{order_id}", json=order_data.__dict__)
    assert response.status_code == 200


def test_delete_order(base_url):
    order_id = 1
    response = requests.delete(f"{base_url}/orders/{order_id}")
    assert response.status_code == 204


def test_list_orders(base_url):
    response = requests.get(f"{base_url}/orders")
    assert response.status_code == 200


def test_add_line_item_to_order(base_url, order_data):
    order_id = 1
    response = requests.post(f"{base_url}/orders/{order_id}/details", json=order_data.__dict__)
    assert response.status_code == 201


def test_get_line_items_for_order(base_url):
    order_id = 1
    response = requests.get(f"{base_url}/orders/{order_id}/details")
    assert response.status_code == 200


def test_update_line_item_in_order(base_url, order_data):
    order_id = 1
    product_id = 1
    response = requests.put(f"{base_url}/orders/{order_id}/details/{product_id}", json=order_data.__dict__)
    assert response.status_code == 200


def test_remove_line_item_from_order(base_url):
    order_id = 1
    product_id = 1
    response = requests.delete(f"{base_url}/orders/{order_id}/details/{product_id}")
    assert response.status_code == 204
