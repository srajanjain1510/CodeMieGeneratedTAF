import requests


def test_create_customer(base_url):
    url = f"{base_url}/customers"
    payload = {"name": "John Doe", "email": "john.doe@example.com"}
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"


def test_get_customer(base_url):
    customer_id = 1  # Example customer ID, replace with actual ID
    url = f"{base_url}/customers/{customer_id}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["id"] == customer_id


def test_update_customer(base_url):
    customer_id = 1  # Example customer ID, replace with actual ID
    url = f"{base_url}/customers/{customer_id}"
    payload = {"name": "Jane Doe", "email": "jane.doe@example.com"}
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"


def test_delete_customer(base_url):
    customer_id = 1  # Example customer ID, replace with actual ID
    url = f"{base_url}/customers/{customer_id}"
    response = requests.delete(url)
    assert response.status_code == 204


def test_list_customers(base_url):
    url = f"{base_url}/customers"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_order_for_customer(base_url):
    customer_id = 1  # Example customer ID, replace with actual ID
    url = f"{base_url}/customers/{customer_id}/orders"
    payload = {"product": "Example Product", "quantity": 1}
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["product"] == "Example Product"


def test_list_orders_for_customer(base_url):
    customer_id = 1  # Example customer ID, replace with actual ID
    url = f"{base_url}/customers/{customer_id}/orders"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_record_payment_for_customer(base_url):
    customer_id = 1  # Example customer ID, replace with actual ID
    url = f"{base_url}/customers/{customer_id}/payments"
    payload = {"amount": 100.0, "method": "Credit Card"}
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["amount"] == 100.0


def test_list_payments_for_customer(base_url):
    customer_id = 1  # Example customer ID, replace with actual ID
    url = f"{base_url}/customers/{customer_id}/payments"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)