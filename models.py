from dataclasses import dataclass, field
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
    product_id: int
    quantity: int

@dataclass
class OrderDetail:
    orderId: int
    productId: int
    quantity: int
    price: float

@dataclass
class Payment:
    amount: float
    method: str

@dataclass
class Product:
    productCode: str
    name: str
    description: str
    price: float

@dataclass
class ProductLine:
    productLine: str
    name: str
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
    name: str
    position: str
    office_code: str
    reports_to: Optional[int] = None

@dataclass
class Office:
    officeCode: str
    code: str
    city: str
    phone: str
    addressLine1: str
    addressLine2: Optional[str]
    state: Optional[str]
    country: str
    postalCode: str
    territory: str
    address: str

# New dataclass models for request payloads

@dataclass
class CreateCustomerRequest:
    name: str
    email: str
    address: str

@dataclass
class CreateOrderRequest:
    customerId: int
    orderDate: str
    status: str
    product_id: int
    quantity: int

@dataclass
class CreateOrderDetailRequest:
    orderId: int
    productId: int
    quantity: int
    price: float

@dataclass
class CreatePaymentRequest:
    amount: float
    method: str

@dataclass
class CreateProductRequest:
    productCode: str
    name: str
    description: str
    price: float

@dataclass
class CreateProductLineRequest:
    productLine: str
    name: str
    textDescription: str
    htmlDescription: Optional[str] = None
    image: Optional[str] = None

@dataclass
class CreateEmployeeRequest:
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
class CreateOfficeRequest:
    code: str
    city: str
    phone: str
    addressLine1: str
    addressLine2: Optional[str] = None
    state: Optional[str] = None
    country: str
    postalCode: str
    territory: str