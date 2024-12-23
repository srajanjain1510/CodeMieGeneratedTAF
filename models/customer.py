from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    address: str
    email: str

@dataclass
class Order:
    product_id: int
    quantity: int
    price: float

@dataclass
class Payment:
    order_id: int
    amount: float
