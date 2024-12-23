import json
import random
from dataclasses import dataclass
from typing import List

@dataclass
class Office:
    id: int
    location: str

@dataclass
class Employee:
    id: int
    name: str
    office_id: int

@dataclass
class ProductLine:
    id: int
    name: str

@dataclass
class Product:
    id: int
    name: str
    product_line_id: int

@dataclass
class Customer:
    id: int
    name: str

class DataGenerator:
    def __init__(self, db):
        self.db = db

    def load_json(self, file_path):
        with open(file_path) as f:
            return json.load(f)

    def generate_random_data(self, data, count):
        return [random.choice(data) for _ in range(count)]

    def generate_offices(self, count=5) -> List[Office]:
        offices = [Office(id=i, location=f"Office-{i}") for i in range(1, count + 1)]
        self.db.insert_offices(offices)
        return offices

    def generate_employees(self, offices: List[Office], data, count_per_office=100) -> List[Employee]:
        employees = []
        for office in offices:
            office_employees = self.generate_random_data(data, count_per_office)
            for i, emp_data in enumerate(office_employees):
                emp = Employee(id=office.id * 100 + i, name=emp_data['name'], office_id=office.id)
                employees.append(emp)
        self.db.insert_employees(employees)
        return employees

    def generate_product_lines(self, data, count=50) -> List[ProductLine]:
        product_lines = [ProductLine(id=i, name=data[i % len(data)]['name']) for i in range(1, count + 1)]
        self.db.insert_product_lines(product_lines)
        return product_lines

    def generate_products(self, product_lines: List[ProductLine], data, count_per_line=500) -> List[Product]:
        products = []
        for product_line in product_lines:
            line_products = self.generate_random_data(data, count_per_line)
            for i, prod_data in enumerate(line_products):
                prod = Product(id=product_line.id * 500 + i, name=prod_data['name'], product_line_id=product_line.id)
                products.append(prod)
        self.db.insert_products(products)
        return products

    def generate_customers(self, data, count=10000) -> List[Customer]:
        customers = [Customer(id=i, name=data[i % len(data)]['name']) for i in range(1, count + 1)]
        self.db.insert_customers(customers)
        return customers

# Example usage:
# db = YourDatabaseConnection()
# data_gen = DataGenerator(db)
# offices = data_gen.generate_offices()
# employee_data = data_gen.load_json('test_data/employees_test_data.json')
# data_gen.generate_employees(offices, employee_data)
# product_line_data = data_gen.load_json('test_data/products_test_data.json')
# product_lines = data_gen.generate_product_lines(product_line_data)
# data_gen.generate_products(product_lines, product_line_data)
# customer_data = data_gen.load_json('test_data/customers_test_data.json')
# data_gen.generate_customers(customer_data)
# data_gen.generate_employees(offices)
# product_lines = data_gen.generate_product_lines()
# data_gen.generate_products(product_lines)
# data_gen.generate_customers()