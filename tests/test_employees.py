import json
import pytest
from models import Employee, Office
from utils.api_client import APIClient


@pytest.fixture
def client(api_client):
    # Assuming you have a test client setup
    return api_client


@pytest.fixture
def employee_test_data():
    with open('test_data/employees_test_data.json') as f:
        return json.load(f)


def test_create_employee(client, employee_test_data):
    employee_data = employee_test_data['create_employee']
    employee = Employee(**employee_data)
    response = client.post('/employees', json=employee.__dict__)
    assert response.status_code == 201
    assert response.json()['name'] == employee_data['name']


def test_update_employee(client, employee_test_data):
    employee_data = employee_test_data['update_employee']
    employee = Employee(**employee_data)
    response = client.put('/employees/1', json=employee.__dict__)
    assert response.status_code == 200
    assert response.json()['name'] == employee_data['name']


def test_delete_employee(client):
    response = client.delete('/employees/1')
    assert response.status_code == 204


def test_list_employees(client):
    response = client.get('/employees')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_office(client):
    office = Office(code='1', address='123 Main Street')
    response = client.post('/offices', json=office.__dict__)
    assert response.status_code == 201


def test_update_office(client):
    office = Office(code='2', address='456 Elm Street')
    response = client.put('/offices/1', json=office.__dict__)
    assert response.status_code == 200


def test_delete_office(client):
    response = client.delete('/offices/1')
    assert response.status_code == 204


def test_list_offices(client):
    response = client.get('/offices')
    assert response.status_code == 200
    assert isinstance(response.json(), list)