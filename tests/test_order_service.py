import requests

def test_get_order(base_url):
    url = f"{base_url}/orders/1"
    response = requests.get(url)
    assert response.status_code == 200

# Add more test cases for other endpoints
