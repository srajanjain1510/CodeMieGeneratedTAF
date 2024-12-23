import requests

def test_create_product(base_url):
    url = f"{base_url}/products"
    payload = {"productCode": "P001", "name": "Product 1"}
    response = requests.post(url, json=payload)
    assert response.status_code == 201

# Add more test cases for other endpoints
