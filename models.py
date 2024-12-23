from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Customer:
    customerId: Optional[int]
    name: str
    email: str
    address: str

@dataclass
class Order:
    orderId: Optional[int]
    customerId: int
    orderDate: str
    status: str

@dataclass
class OrderDetail:
    orderId: int
    productId: int
    quantity: int
    price: float

@dataclass
class Product:
    productCode: str
    name: str
    description: str
    price: float

@dataclass
class ProductLine:
    productLine: str
    textDescription: str
    htmlDescription: Optional[str]
    image: Optional[str]

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

@dataclass
class CustomerRequest:
    name: str
    email: str
    address: str

@dataclass
class OrderRequest:
    customerId: int
    orderDate: str
    status: str

@dataclass
class OrderDetailRequest:
    productId: int
    quantity: int
    price: float

@dataclass
class ProductRequest:
    name: str
    description: str
    price: float

@dataclass
class ProductLineRequest:
    productLine: str
    textDescription: str
    htmlDescription: Optional[str]
    image: Optional[str]

@dataclass
class EmployeeRequest:
    lastName: str
    firstName: str
    extension: str
    email: str
    officeCode: str
    reportsTo: Optional[int]
    jobTitle: str

@dataclass
class OfficeRequest:
    city: str
    phone: str
    addressLine1: str
    addressLine2: Optional[str]
    state: Optional[str]
    country: str
    postalCode: str
    territory: str