from dataclasses import dataclass
from typing import List, Optional

# Customer Service Models
@dataclass
class Customer:
    customerId: Optional[int]
    name: str
    email: str
    address: str
    phone: Optional[str] = None

@dataclass
class OrderDetail:
    product_id: int
    quantity: int
    price: float

@dataclass
class Order:
    customer_id: int
    order_details: List[OrderDetail]
    orderDate: str
    status: str

@dataclass
class Payment:
    order_id: int
    amount: float
    method: str

# Product Service Models
@dataclass
class Product:
    productCode: str
    name: str
    price: float
    description: Optional[str] = None

@dataclass
class ProductLine:
    productLine: str
    textDescription: str
    htmlDescription: Optional[str]
    image: Optional[str]
    name: str
    description: Optional[str] = None

# Employee Service Models
@dataclass
class Employee:
    employeeNumber: int
    lastName: str
    firstName: str
    extension: str
    email: str
    officeCode: str
    reportsTo: Optional[int]
    jobTitle: str
    name: str
    position: str

@dataclass
class Office:
    officeCode: str
    city: str
    phone: str
    addressLine1: str
    addressLine2: Optional[str]
    state: Optional[str]
    country: str
    postalCode: str
    territory: str
    code: str
    address: str