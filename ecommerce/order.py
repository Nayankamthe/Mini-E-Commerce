import json
import os
from datetime import datetime

class Order:
    def __init__(self, order_id, customer_details, items, total_amount, order_date):
        self.order_id = order_id
        self.customer_details = customer_details
        self.items = items
        self.total_amount = total_amount
        self.order_date = order_date

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_details": self.customer_details,
            "items": self.items,
            "total_amount": self.total_amount,
            "order_date": self.order_date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['order_id'], data['customer_details'], data['items'], data['total_amount'], data['order_date'])

    @staticmethod
    def load_orders(file_path='data/orders.json'):
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    return [Order.from_dict(order) for order in json.load(file)]
            except json.JSONDecodeError as e:
                print(f"Error: The file ast {file_path} is empty or contains invalid JSON")
                return []
        else:
            print(f"Error: The file at {file_path} does not exist.")
            return []

    @staticmethod
    def save_orders(orders, file_path='data/orders.json'):
        with open(file_path, 'w') as file:
            json.dump([order.to_dict() for order in orders], file)
