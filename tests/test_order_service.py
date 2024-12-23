import requests

def test_get_order(base_url):
    order_id = 1  # Example order ID, replace with actual ID
    url = f"{base_url}/orders/{order_id}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["id"] == order_id

def test_update_order(base_url):
    order_id = 1  # Example order ID, replace with actual ID
    url = f"{base_url}/orders/{order_id}"
    payload = {"status": "Shipped"}
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "Shipped"

def test_delete_order(base_url):
    order_id = 1  # Example order ID, replace with actual ID
    url = f"{base_url}/orders/{order_id}"
    response = requests.delete(url)
    assert response.status_code == 204

def test_list_orders(base_url):
    url = f"{base_url}/orders"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_line_item_to_order(base_url):
    order_id = 1  # Example order ID, replace with actual ID
    url = f"{base_url}/orders/{order_id}/details"
    payload = {"product": "Example Product", "quantity": 1}
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["product"] == "Example Product"

def test_get_line_items_for_order(base_url):
    order_id = 1  # Example order ID, replace with actual ID
    url = f"{base_url}/orders/{order_id}/details"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_line_item_in_order(base_url):
    order_id = 1  # Example order ID, replace with actual ID
    product_id = 1  # Example product ID, replace with actual ID
    url = f"{base_url}/orders/{order_id}/details/{product_id}"
    payload = {"quantity": 2}
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    assert response.json()["quantity"] == 2

def test_remove_line_item_from_order(base_url):
    order_id = 1  # Example order ID, replace with actual ID
    product_id = 1  # Example product ID, replace with actual ID
    url = f"{base_url}/orders/{order_id}/details/{product_id}"
    response = requests.delete(url)
    assert response.status_code == 204