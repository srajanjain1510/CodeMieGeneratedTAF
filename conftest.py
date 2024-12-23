import pytest
import json
from data_flusher import DataFlusher
from data_generator import DataGenerator
from your_database_module import YourDatabaseConnection

@pytest.fixture(scope='session', autouse=True)
def setup_test_environment():
    base_url = 'http://localhost:5000'  # Replace with your actual base URL
    flusher = DataFlusher(base_url)

    db = YourDatabaseConnection()
    data_gen = DataGenerator(db)
    
    with open('test_data/offices.json') as f:
        offices_data = json.load(f)
    offices = data_gen.load_offices(offices_data)
    
    with open('test_data/employees.json') as f:
        employees_data = json.load(f)
    data_gen.load_employees(employees_data)
    
    with open('test_data/product_lines.json') as f:
        product_lines_data = json.load(f)
    product_lines = data_gen.load_product_lines(product_lines_data)
    
    with open('test_data/products.json') as f:
        products_data = json.load(f)
    data_gen.load_products(products_data)
    
    with open('test_data/customers.json') as f:
        customers_data = json.load(f)
    data_gen.load_customers(customers_data)
    
    yield
    flusher.flush_all_data()