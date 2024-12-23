import pytest
from models import Employee, Office

@pytest.fixture

def base_url():
    return "http://example.com/api"

@pytest.fixture

def employee_data():
    return Employee(name="Jane Doe", position="Manager", office_code="1", reports_to=None)

@pytest.fixture

def office_data():
    return Office(code="1", address="456 Oak Street", city="Metropolis", country="Freedonia")

# Employee Service Tests

def test_create_employee(base_url, employee_data):
    response = requests.post(f"{base_url}/employees", json=employee_data.__dict__)
    assert response.status_code == 201


def test_get_employee(base_url):
    employee_number = 1
    response = requests.get(f"{base_url}/employees/{employee_number}")
    assert response.status_code == 200


def test_update_employee(base_url, employee_data):
    employee_number = 1
    response = requests.put(f"{base_url}/employees/{employee_number}", json=employee_data.__dict__)
    assert response.status_code == 200


def test_delete_employee(base_url):
    employee_number = 1
    response = requests.delete(f"{base_url}/employees/{employee_number}")
    assert response.status_code == 204


def test_list_employees(base_url):
    response = requests.get(f"{base_url}/employees")
    assert response.status_code == 200


def test_list_subordinates(base_url):
    employee_number = 1
    response = requests.get(f"{base_url}/employees/{employee_number}/subordinates")
    assert response.status_code == 200

# Office Service Tests

def test_create_office(base_url, office_data):
    response = requests.post(f"{base_url}/offices", json=office_data.__dict__)
    assert response.status_code == 201


def test_get_office(base_url):
    office_code = 1
    response = requests.get(f"{base_url}/offices/{office_code}")
    assert response.status_code == 200


def test_update_office(base_url, office_data):
    office_code = 1
    response = requests.put(f"{base_url}/offices/{office_code}", json=office_data.__dict__)
    assert response.status_code == 200


def test_delete_office(base_url):
    office_code = 1
    response = requests.delete(f"{base_url}/offices/{office_code}")
    assert response.status_code == 204


def test_list_offices(base_url):
    response = requests.get(f"{base_url}/offices")
    assert response.status_code == 200


def test_list_employees_in_office(base_url):
    office_code = 1
    response = requests.get(f"{base_url}/offices/{office_code}/employees")
    assert response.status_code == 200
