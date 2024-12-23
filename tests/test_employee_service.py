import requests


def test_create_employee(base_url):
    url = f"{base_url}/employees"
    payload = {"name": "John Smith", "position": "Manager"}
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "John Smith"


def test_get_employee(base_url):
    employee_number = 1  # Example employee number, replace with actual number
    url = f"{base_url}/employees/{employee_number}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["number"] == employee_number


def test_update_employee(base_url):
    employee_number = 1  # Example employee number, replace with actual number
    url = f"{base_url}/employees/{employee_number}"
    payload = {"name": "Jane Smith", "position": "Director"}
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Smith"


def test_delete_employee(base_url):
    employee_number = 1  # Example employee number, replace with actual number
    url = f"{base_url}/employees/{employee_number}"
    response = requests.delete(url)
    assert response.status_code == 204


def test_list_employees(base_url):
    url = f"{base_url}/employees"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_list_subordinates(base_url):
    employee_number = 1  # Example employee number, replace with actual number
    url = f"{base_url}/employees/{employee_number}/subordinates"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_office(base_url):
    url = f"{base_url}/offices"
    payload = {"location": "New York"}
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["location"] == "New York"


def test_get_office(base_url):
    office_code = 1  # Example office code, replace with actual code
    url = f"{base_url}/offices/{office_code}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["code"] == office_code


def test_update_office(base_url):
    office_code = 1  # Example office code, replace with actual code
    url = f"{base_url}/offices/{office_code}"
    payload = {"location": "Los Angeles"}
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    assert response.json()["location"] == "Los Angeles"


def test_delete_office(base_url):
    office_code = 1  # Example office code, replace with actual code
    url = f"{base_url}/offices/{office_code}"
    response = requests.delete(url)
    assert response.status_code == 204


def test_list_offices(base_url):
    url = f"{base_url}/offices"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_list_employees_in_office(base_url):
    office_code = 1  # Example office code, replace with actual code
    url = f"{base_url}/offices/{office_code}/employees"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)