import pytest\nimport requests\nfrom models import OrderDetail\n\nBASE_URL = \"http://api.example.com\"\n\n@pytest.fixture\ndef order_detail_payload():\n    return OrderDetail(product_id=1, quantity=2, price=10.0)\n\n\ndef test_get_order():\n    order_id = 1\n    response = requests.get(f\"{BASE_URL}/orders/{order_id}\")\n    assert response.status_code == 200\n\n\ndef test_update_order(order_detail_payload):\n    order_id = 1\n    response = requests.put(f\"{BASE_URL}/orders/{order_id}\", json=order_detail_payload.__dict__)\n    assert response.status_code == 200\n\n\ndef test_delete_order():\n    order_id = 1\n    response = requests.delete(f\"{BASE_URL}/orders/{order_id}\")\n    assert response.status_code == 204\n\n\ndef test_list_orders():\n    response = requests.get(f\"{BASE_URL}/orders\")\n    assert response.status_code == 200\n\n\ndef test_add_line_item_to_order(order_detail_payload):\n    order_id = 1\n    response = requests.post(f\"{BASE_URL}/orders/{order_id}/details\", json=order_detail_payload.__dict__)\n    assert response.status_code == 201\n\n\ndef test_get_line_items_for_order():\n    order_id = 1\n    response = requests.get(f\"{BASE_URL}/orders/{order_id}/details\")\n    assert response.status_code == 200\n\n\ndef test_update_line_item_in_order(order_detail_payload):\n    order_id = 1\n    product_id = 1\n    response = requests.put(f\"{BASE_URL}/orders/{order_id}/details/{product_id}\", json=order_detail_payload.__dict__)\n    assert response.status_code == 200\n\n\ndef test_remove_line_item_from_order():\n    order_id = 1\n    product_id = 1\n    response = requests.delete(f\"{BASE_URL}/orders/{order_id}/details/{product_id}\")\n    assert response.status_code == 204\n