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
class Order:
    orderId: Optional[int]
    customerId: int
    orderDate: str
    status: str
    product_id: int
    quantity: int

@dataclass
class Payment:
    amount: float
    method: str

# Order Service Models
@dataclass
class OrderDetail:
    orderId: int
    productId: int
    quantity: int
    price: float

# Product Service Models
@dataclass
class Product:
    productCode: str
    name: str
    description: Optional[str] = None
    price: float

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
    first_name: str
    last_name: str

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