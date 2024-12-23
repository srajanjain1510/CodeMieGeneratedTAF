# CodeMieGeneratedTAF
# Project Name

## Overview

This project includes modules for generating test data and performance test data for various entities such as customers, orders, employees, and offices. The data generation is implemented using Python and the `dataclasses` module.

## Test Data Generation

The `DataGenerator` class in `data_generator.py` is responsible for generating test data for different entities. The class provides methods to load JSON data, generate random data, and insert the generated data into the database.

### Example Usage

```python
import json
from data_generator import DataGenerator

# Initialize the database connection
db = YourDatabaseConnection()

# Create an instance of DataGenerator
data_gen = DataGenerator(db)

# Generate offices
offices = data_gen.generate_offices()

# Load employee test data from JSON file
employee_data = data_gen.load_json('test_data/employees_test_data.json')

# Generate employees and insert into the database
data_gen.generate_employees(offices, employee_data)

# Load product line test data from JSON file
product_line_data = data_gen.load_json('test_data/products_test_data.json')

# Generate product lines and insert into the database
product_lines = data_gen.generate_product_lines(product_line_data)

# Generate products and insert into the database
data_gen.generate_products(product_lines, product_line_data)

# Load customer test data from JSON file
customer_data = data_gen.load_json('test_data/customers_test_data.json')

# Generate customers and insert into the database
data_gen.generate_customers(customer_data)


## Performance Test Data Generation

from performance_data_generator import PerformanceDataGenerator

# Initialize the database connection
db = YourDatabaseConnection()

# Create an instance of PerformanceDataGenerator
data_gen = PerformanceDataGenerator(db)

# Generate offices
offices = data_gen.generate_offices()

# Configuration for generating employees
config = {
    'employees_with_manager': 0.8  # 80% of employees will have a manager
}

# Generate employees and insert into the database
data_gen.generate_employees(offices, config)

# Generate customers (assuming you have a method for this)
customers = data_gen.generate_customers()

# Generate products (assuming you have a method for this)
products = data_gen.generate_products()

# Configuration for generating orders
config = {
    'orders_with_payments': 0.9,  # 90% of orders will have payments
    'orders_with_multiple_payments': 0.2  # 20% of orders will have multiple payments
}

# Generate orders and insert into the database
data_gen.generate_orders(customers, products, config)

