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

    def generate_offices(self, count=5) -> List[Office]:
        offices = [Office(id=i, location=f"Office-{i}") for i in range(1, count + 1)]
        self.db.insert_offices(offices)
        return offices

    def generate_employees(self, offices: List[Office], count_per_office=100) -> List[Employee]:
        employees = [
            Employee(id=i, name=f"Employee-{i}", office_id=office.id)
            for office in offices
            for i in range(office.id * 100, office.id * 100 + count_per_office)
        ]
        self.db.insert_employees(employees)
        return employees

    def generate_product_lines(self, count=50) -> List[ProductLine]:
        product_lines = [ProductLine(id=i, name=f"ProductLine-{i}") for i in range(1, count + 1)]
        self.db.insert_product_lines(product_lines)
        return product_lines

    def generate_products(self, product_lines: List[ProductLine], count_per_line=500) -> List[Product]:
        products = [
            Product(id=i, name=f"Product-{i}", product_line_id=product_line.id)
            for product_line in product_lines
            for i in range(product_line.id * 500, product_line.id * 500 + count_per_line)
        ]
        self.db.insert_products(products)
        return products

    def generate_customers(self, count=10000) -> List[Customer]:
        customers = [Customer(id=i, name=f"Customer-{i}") for i in range(1, count + 1)]
        self.db.insert_customers(customers)
        return customers

    def load_test_data_from_json(self, json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        return data

