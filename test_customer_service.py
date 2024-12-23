import pytest\nimport requests\nfrom models import Customer, Order, Payment\n\nBASE_URL = \"http://api.example.com\"\n\n@pytest.fixture\ndef customer_payload():\n    return Customer(name=\"John Doe\", email=\"john.doe@example.com\")\n\n@pytest.fixture\ndef order_payload():\n    return Order(product_id=1, quantity=2)\n\n@pytest.fixture\ndef payment_payload():\n    return Payment(amount=100.0, method=\"Credit Card\")\n\n\ndef test_create_customer(customer_payload):\n    response = requests.post(f\"{BASE_URL}/customers\", json=customer_payload.__dict__)\n    assert response.status_code == 201\n\n\ndef test_get_customer():\n    customer_id = 1\n    response = requests.get(f\"{BASE_URL}/customers/{customer_id}\")\n    assert response.status_code == 200\n\n\ndef test_update_customer(customer_payload):\n    customer_id = 1\n    response = requests.put(f\"{BASE_URL}/customers/{customer_id}\", json=customer_payload.__dict__)\n    assert response.status_code == 200\n\n\ndef test_delete_customer():\n    customer_id = 1\n    response = requests.delete(f\"{BASE_URL}/customers/{customer_id}\")\n    assert response.status_code == 204\n\n\ndef test_create_order_for_customer(order_payload):\n    customer_id = 1\n    response = requests.post(f\"{BASE_URL}/customers/{customer_id}/orders\", json=order_payload.__dict__)\n    assert response.status_code == 201\n\n\ndef test_list_orders_for_customer():\n    customer_id = 1\n    response = requests.get(f\"{BASE_URL}/customers/{customer_id}/orders\")\n    assert response.status_code == 200\n\n\ndef test_record_payment_for_customer(payment_payload):\n    customer_id = 1\n    response = requests.post(f\"{BASE_URL}/customers/{customer_id}/payments\", json=payment_payload.__dict__)\n    assert response.status_code == 201\n\n\ndef test_list_payments_for_customer():\n    customer_id = 1\n    response = requests.get(f\"{BASE_URL}/customers/{customer_id}/payments\")\n    assert response.status_code == 200\n