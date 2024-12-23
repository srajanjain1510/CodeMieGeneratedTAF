import pytest\nimport requests\nfrom models import Product, ProductLine\n\nBASE_URL = \"http://api.example.com\"\n\n@pytest.fixture\ndef product_payload():\n    return Product(name=\"Product 1\", description=\"Description 1\", price=100.0)\n\n@pytest.fixture\ndef product_line_payload():\n    return ProductLine(name=\"Product Line 1\", description=\"Description 1\")\n\n\ndef test_create_product(product_payload):\n    response = requests.post(f\"{BASE_URL}/products\", json=product_payload.__dict__)\n    assert response.status_code == 201\n\n\ndef test_get_product():\n    product_code = 1\n    response = requests.get(f\"{BASE_URL}/products/{product_code}\")\n    assert response.status_code == 200\n\n\ndef test_update_product(product_payload):\n    product_code = 1\n    response = requests.put(f\"{BASE_URL}/products/{product_code}\", json=product_payload.__dict__)\n    assert response.status_code == 200\n\n\ndef test_delete_product():\n    product_code = 1\n    response = requests.delete(f\"{BASE_URL}/products/{product_code}\")\n    assert response.status_code == 204\n\n\ndef test_list_products():\n    response = requests.get(f\"{BASE_URL}/products\")\n    assert response.status_code == 200\n\n\ndef test_create_product_line(product_line_payload):\n    response = requests.post(f\"{BASE_URL}/product-lines\", json=product_line_payload.__dict__)\n    assert response.status_code == 201\n\n\ndef test_get_product_line():\n    product_line = 1\n    response = requests.get(f\"{BASE_URL}/product-lines/{product_line}\")\n    assert response.status_code == 200\n\n\ndef test_update_product_line(product_line_payload):\n    product_line = 1\n    response = requests.put(f\"{BASE_URL}/product-lines/{product_line}\", json=product_line_payload.__dict__)\n    assert response.status_code == 200\n\n\ndef test_delete_product_line():\n    product_line = 1\n    response = requests.delete(f\"{BASE_URL}/product-lines/{product_line}\")\n    assert response.status_code == 204\n\n\ndef test_list_product_lines():\n    response = requests.get(f\"{BASE_URL}/product-lines\")\n    assert response.status_code == 200\n\n\ndef test_list_products_in_product_line():\n    product_line = 1\n    response = requests.get(f\"{BASE_URL}/product-lines/{product_line}/products\")\n    assert response.status_code == 200\n