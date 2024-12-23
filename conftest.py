import pytest
from data_flusher import DataFlusher
from data_generator import DataGenerator
from your_database_module import YourDatabaseConnection

@pytest.fixture(scope='session', autouse=True)
def setup_test_environment():
    base_url = 'http://localhost:5000'  # Replace with your actual base URL
    flusher = DataFlusher(base_url)

    db = YourDatabaseConnection()
    data_gen = DataGenerator(db)
    offices = data_gen.generate_offices()
    data_gen.generate_employees(offices)
    product_lines = data_gen.generate_product_lines()
    data_gen.generate_products(product_lines)
    data_gen.generate_customers()
    
    yield
    flusher.flush_all_data()