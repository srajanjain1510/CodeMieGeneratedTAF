import pytest
from models import Product, ProductLine

@pytest.fixture

def base_url():
    return "http://example.com/api"

@pytest.fixture

def product_data():
    return Product(name="Product 1", description="Description 1", price=100.0)

@pytest.fixture

def product_line_data():
    return ProductLine(name="Product Line 1", description="Description of Product Line 1")

# Product Service Tests

def test_create_product(base_url, product_data):
    response = requests.post(f"{base_url}/products", json=product_data.__dict__)
    assert response.status_code == 201


def test_get_product(base_url):
    product_code = 1
    response = requests.get(f"{base_url}/products/{product_code}")
    assert response.status_code == 200


def test_update_product(base_url, product_data):
    product_code = 1
    response = requests.put(f"{base_url}/products/{product_code}", json=product_data.__dict__)
    assert response.status_code == 200


def test_delete_product(base_url):
    product_code = 1
    response = requests.delete(f"{base_url}/products/{product_code}")
    assert response.status_code == 204


def test_list_products(base_url):
    response = requests.get(f"{base_url}/products")
    assert response.status_code == 200


def test_create_product_line(base_url, product_line_data):
    response = requests.post(f"{base_url}/product-lines", json=product_line_data.__dict__)
    assert response.status_code == 201


def test_get_product_line(base_url):
    product_line = 1
    response = requests.get(f"{base_url}/product-lines/{product_line}")
    assert response.status_code == 200


def test_update_product_line(base_url, product_line_data):
    product_line = 1
    response = requests.put(f"{base_url}/product-lines/{product_line}", json=product_line_data.__dict__)
    assert response.status_code == 200


def test_delete_product_line(base_url):
    product_line = 1
    response = requests.delete(f"{base_url}/product-lines/{product_line}")
    assert response.status_code == 204


def test_list_product_lines(base_url):
    response = requests.get(f"{base_url}/product-lines")
    assert response.status_code == 200


def test_list_products_in_product_line(base_url):
    product_line = 1
    response = requests.get(f"{base_url}/product-lines/{product_line}/products")
    assert response.status_code == 200
