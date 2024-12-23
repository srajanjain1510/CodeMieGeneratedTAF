import pytest
from models import Product, ProductLine

@pytest.fixture
def client():
    # Assuming you have a test client setup
    from myapp import create_app
    app = create_app()
    return app.test_client()

def test_create_product(client):
    product = Product(name='Widget', description='A useful widget', price=19.99)
    response = client.post('/products', json=product.__dict__)
    assert response.status_code == 201
    assert response.json()['name'] == 'Widget'

def test_get_product(client):
    response = client.get('/products/1')
    assert response.status_code == 200

def test_update_product(client):
    product = Product(name='Gadget', description='An updated gadget', price=29.99)
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
    product_line = ProductLine(name='Gizmos', description='A line of gizmos')
    response = client.post('/product-lines', json=product_line.__dict__)
    assert response.status_code == 201

def test_get_product_line(client):
    response = client.get('/product-lines/1')
    assert response.status_code == 200

def test_update_product_line(client):
    product_line = ProductLine(name='Updated Gizmos', description='An updated line of gizmos')
    response = client.put('/product-lines/1', json=product_line.__dict__)
    assert response.status_code == 200

def test_delete_product_line(client):
    response = client.delete('/product-lines/1')
    assert response.status_code == 204

def test_list_product_lines(client):
    response = client.get('/product-lines')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_products_in_product_line(client):
    response = client.get('/product-lines/1/products')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
