import random
from dataclasses import dataclass
from typing import List

@dataclass
class Customer:
    id: int
    name: str

@dataclass
class OrderDetail:
    product_id: int
    quantity: int
    price: float

@dataclass
class Order:
    id: int
    customer_id: int
    order_details: List[OrderDetail]

@dataclass
class Payment:
    order_id: int
    amount: float

@dataclass
class Employee:
    id: int
    name: str
    office_id: int
    manager_id: int

@dataclass
class Office:
    id: int
    location: str

class PerformanceDataGenerator:
    def __init__(self, db):
        self.db = db

    def generate_orders(self, customers: List[Customer], products: List[OrderDetail], config: dict):
        orders = []
        payments = []
        order_id = 1
        for customer in customers:
            for _ in range(10):  # 10 orders per customer
                order_details = random.sample(products, k=random.randint(1, 5))
                order = Order(id=order_id, customer_id=customer.id, order_details=order_details)
                orders.append(order)
                
                if random.random() < config['orders_with_payments']:
                    payment = Payment(order_id=order_id, amount=sum(od.price * od.quantity for od in order_details))
                    payments.append(payment)
                
                if random.random() < config['orders_with_multiple_payments']:
                    for _ in range(random.randint(2, 5)):
                        payment = Payment(order_id=order_id, amount=random.uniform(10, 100))
                        payments.append(payment)
                
                order_id += 1
        
        self.db.insert_orders(orders)
        self.db.insert_payments(payments)

    def generate_employees(self, offices: List[Office], config: dict):
        employees = []
        employee_id = 1
        for office in offices:
            for _ in range(random.randint(50, 100)):  # Random number of employees per office
                manager_id = None
                if random.random() < config['employees_with_manager']:
                    manager_id = random.randint(1, employee_id - 1) if employees else None
                employee = Employee(id=employee_id, name=f"Employee-{employee_id}", office_id=office.id, manager_id=manager_id)
                employees.append(employee)
                employee_id += 1
        
        self.db.insert_employees(employees)

    def generate_offices(self, count=5):
        offices = [Office(id=i, location=f"Office-{i}") for i in range(1, count + 1)]
        self.db.insert_offices(offices)
        return offices

# Example usage:
# db = YourDatabaseConnection()
# data_gen = PerformanceDataGenerator(db)
# offices = data_gen.generate_offices()
# data_gen.generate_employees(offices, config)
# customers = data_gen.generate_customers()
# products = data_gen.generate_products(product_lines)
# data_gen.generate_orders(customers, products, config)