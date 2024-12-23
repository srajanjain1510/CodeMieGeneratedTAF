import requests

class DataFlusher:
    def __init__(self, base_url):
        self.base_url = base_url

    def delete_all_customers(self):
        response = requests.get(f'{self.base_url}/customers')
        customers = response.json()
        for customer in customers:
            requests.delete(f'{self.base_url}/customers/{customer["id"]}')

    def delete_all_orders(self):
        response = requests.get(f'{self.base_url}/orders')
        orders = response.json()
        for order in orders:
            requests.delete(f'{self.base_url}/orders/{order["id"]}')

    def delete_all_products(self):
        response = requests.get(f'{self.base_url}/products')
        products = response.json()
        for product in products:
            requests.delete(f'{self.base_url}/products/{product["code"]}')

    def delete_all_employees(self):
        response = requests.get(f'{self.base_url}/employees')
        employees = response.json()
        for employee in employees:
            requests.delete(f'{self.base_url}/employees/{employee["employeeNumber"]}')
            
    def delete_all_offices(self):
        response = requests.get(f'{self.base_url}/offices')
        offices = response.json()
        for office in offices:
            requests.delete(f'{self.base_url}/offices/{office["officeCode"]}')

    def flush_all_data(self):
        self.delete_all_customers()
        self.delete_all_orders()
        self.delete_all_products()
        self.delete_all_employees()
        self.delete_all_offices()
