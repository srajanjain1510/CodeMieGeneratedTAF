import requests

def test_create_customer(base_url):
    url = f"{base_url}/customers"
    payload = {"name": "John Doe", "email": "john.doe@example.com"}
    response = requests.post(url, json=payload)
    assert response.status_code == 201

# Add more test cases for other endpoints
