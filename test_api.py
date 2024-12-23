import pytest
from models import Customer, Order, Payment, OrderDetail, Product, ProductLine, Employee, Office

# Define the base URL for the API
BASE_URL = "http://localhost:5000/api"

# Customer Service Tests

def test_create_customer():
    customer = Customer(name="John Doe", address="123 Elm Street", phone="555-1234", email="john.doe@example.com")
    response = requests.post(f"{BASE_URL}/customers", json=customer.__dict__)
    assert response.status_code == 201


def test_get_customer():
    customer_id = 1
    response = requests.get(f"{BASE_URL}/customers/{customer_id}")
    assert response.status_code == 200


def test_update_customer():
    customer_id = 1
    updated_customer = Customer(name="Jane Doe", address="123 Elm Street", phone="555-5678", email="jane.doe@example.com")
    response = requests.put(f"{BASE_URL}/customers/{customer_id}", json=updated_customer.__dict__)
    assert response.status_code == 200


def test_delete_customer():
    customer_id = 1
    response = requests.delete(f"{BASE_URL}/customers/{customer_id}")
    assert response.status_code == 204

# Order Service Tests

def test_create_order():
    order = Order(product_id=1, quantity=2, price=19.99)
    response = requests.post(f"{BASE_URL}/customers/1/orders", json=order.__dict__)
    assert response.status_code == 201


def test_get_order():
    order_id = 1
    response = requests.get(f"{BASE_URL}/orders/{order_id}")
    assert response.status_code == 200


def test_update_order():
    order_id = 1
    updated_order = Order(product_id=1, quantity=3, price=29.99)
    response = requests.put(f"{BASE_URL}/orders/{order_id}", json=updated_order.__dict__)
    assert response.status_code == 200


def test_delete_order():
    order_id = 1
    response = requests.delete(f"{BASE_URL}/orders/{order_id}")
    assert response.status_code == 204

# Product Service Tests

def test_create_product():
    product = Product(name="Widget", description="A useful widget", price=9.99, product_line="Gadgets")
    response = requests.post(f"{BASE_URL}/products", json=product.__dict__)
    assert response.status_code == 201


def test_get_product():
    product_code = 1
    response = requests.get(f"{BASE_URL}/products/{product_code}")
    assert response.status_code == 200


def test_update_product():
    product_code = 1
    updated_product = Product(name="Super Widget", description="An even more useful widget", price=14.99, product_line="Gadgets")
    response = requests.put(f"{BASE_URL}/products/{product_code}", json=updated_product.__dict__)
    assert response.status_code == 200


def test_delete_product():
    product_code = 1
    response = requests.delete(f"{BASE_URL}/products/{product_code}")
    assert response.status_code == 204

# Employee Service Tests

def test_create_employee():
    employee = Employee(name="Alice", position="Manager", office_code="NYC001")
    response = requests.post(f"{BASE_URL}/employees", json=employee.__dict__)
    assert response.status_code == 201


def test_get_employee():
    employee_number = 1
    response = requests.get(f"{BASE_URL}/employees/{employee_number}")
    assert response.status_code == 200


def test_update_employee():
    employee_number = 1
    updated_employee = Employee(name="Alice Smith", position="Senior Manager", office_code="NYC001")
    response = requests.put(f"{BASE_URL}/employees/{employee_number}", json=updated_employee.__dict__)
    assert response.status_code == 200


def test_delete_employee():
    employee_number = 1
    response = requests.delete(f"{BASE_URL}/employees/{employee_number}")
    assert response.status_code == 204
