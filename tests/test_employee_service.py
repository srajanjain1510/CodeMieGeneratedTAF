import requests

def test_create_employee(base_url):
    url = f"{base_url}/employees"
    payload = {"employeeNumber": "E001", "name": "Employee 1"}
    response = requests.post(url, json=payload)
    assert response.status_code == 201

# Add more test cases for other endpoints
