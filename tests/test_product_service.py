import requests

def test_create_product(base_url):
    url = f"{base_url}/products"
    payload = {"name": "Example Product", "price": 10.0}
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Example Product"


def test_get_product(base_url):
    product_code = 1  # Example product code, replace with actual code
    url = f"{base_url}/products/{product_code}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["code"] == product_code


def test_update_product(base_url):
    product_code = 1  # Example product code, replace with actual code
    url = f"{base_url}/products/{product_code}"
    payload = {"name": "Updated Product", "price": 12.0}
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Product"


def test_delete_product(base_url):
    product_code = 1  # Example product code, replace with actual code
    url = f"{base_url}/products/{product_code}"
    response = requests.delete(url)
    assert response.status_code == 204


def test_list_products(base_url):
    url = f"{base_url}/products"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_product_line(base_url):
    url = f"{base_url}/product-lines"
    payload = {"name": "Example Product Line"}
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Example Product Line"


def test_get_product_line(base_url):
    product_line = 1  # Example product line, replace with actual line
    url = f"{base_url}/product-lines/{product_line}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["line"] == product_line


def test_update_product_line(base_url):
    product_line = 1  # Example product line, replace with actual line
    url = f"{base_url}/product-lines/{product_line}"
    payload = {"name": "Updated Product Line"}
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Product Line"


def test_delete_product_line(base_url):
    product_line = 1  # Example product line, replace with actual line
    url = f"{base_url}/product-lines/{product_line}"
    response = requests.delete(url)
    assert response.status_code == 204


def test_list_product_lines(base_url):
    url = f"{base_url}/product-lines"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_list_products_in_product_line(base_url):
    product_line = 1  # Example product line, replace with actual line
    url = f"{base_url}/product-lines/{product_line}/products"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)