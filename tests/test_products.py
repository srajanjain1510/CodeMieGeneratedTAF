import pytest
from models import Product, ProductLine
from utils.api_client import APIClient


@pytest.fixture
def client():
    base_url = 'http://localhost:8000'
    return APIClient(base_url)


def test_create_product(client):
    product = Product(name='Product1', description='Description1', price=10.0)
    response = client.post('/products', json=product.__dict__)
    assert response.status_code == 201


def test_update_product(client):
    product = Product(name='Product2', description='Description2', price=20.0)
    response = client.put('/products/1', json=product.__dict__)
    assert response.status_code == 200


def test_delete_product(client):
    response = client.delete('/products/1')
    assert response.status_code == 204


def test_list_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_product_line(client):
    product_line = ProductLine(name='ProductLine1', description='Description1')
    response = client.post('/product-lines', json=product_line.__dict__)
    assert response.status_code == 201


def test_update_product_line(client):
    product_line = ProductLine(name='ProductLine2', description='Description2')
    response = client.put('/product-lines/1', json=product_line.__dict__)
    assert response.status_code == 200


def test_delete_product_line(client):
    response = client.delete('/product-lines/1')
    assert response.status_code == 204


def test_list_product_lines(client):
    response = client.get('/product-lines')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
