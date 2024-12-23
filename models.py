from dataclasses import dataclass
from typing import List

@dataclass
class Customer:
    name: str
    address: str
    email: str

@dataclass
class OrderDetail:
    product_id: int
    quantity: int
    price: float

@dataclass
class Order:
    customer_id: int
    order_details: List[OrderDetail]

@dataclass
class Payment:
    order_id: int
    amount: float

@dataclass
class Product:
    name: str
    description: str
    price: float

@dataclass
class ProductLine:
    name: str
    description: str

@dataclass
class Employee:
    name: str
    position: str
    office_code: str

@dataclass
class Office:
    code: str
    address: str