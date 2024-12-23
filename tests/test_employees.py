import pytest
from models import Employee, Office

@pytest.fixture
def client():
    # Assuming you have a test client setup
    from myapp import create_app
    app = create_app()
    return app.test_client()

def test_create_employee(client):
    employee = Employee(name='John Smith', position='Manager', office_code='1')
    response = client.post('/employees', json=employee.__dict__)
    assert response.status_code == 201
    assert response.json()['name'] == 'John Smith'

def test_get_employee(client):
    response = client.get('/employees/1')
    assert response.status_code == 200

def test_update_employee(client):
    employee = Employee(name='Jane Smith', position='Senior Manager', office_code='1')
    response = client.put('/employees/1', json=employee.__dict__)
    assert response.status_code == 200

def test_delete_employee(client):
    response = client.delete('/employees/1')
    assert response.status_code == 204

def test_list_employees(client):
    response = client.get('/employees')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_subordinates(client):
    response = client.get('/employees/1/subordinates')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_office(client):
    office = Office(code='1', address='123 Main Street')
    response = client.post('/offices', json=office.__dict__)
    assert response.status_code == 201

def test_get_office(client):
    response = client.get('/offices/1')
    assert response.status_code == 200

def test_update_office(client):
    office = Office(code='1', address='456 Elm Street')
    response = client.put('/offices/1', json=office.__dict__)
    assert response.status_code == 200

def test_delete_office(client):
    response = client.delete('/offices/1')
    assert response.status_code == 204

def test_list_offices(client):
    response = client.get('/offices')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_employees_in_office(client):
    response = client.get('/offices/1/employees')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
