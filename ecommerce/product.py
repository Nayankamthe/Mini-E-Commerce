import json
import os

class Product:
    def __init__(self, product_id, name, description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity
        }
    
        


    @classmethod
    def from_dict(cls, data):
        return cls(data['product_id'], data['name'], data['description'], data['price'], data['quantity'])

    @staticmethod
    def load_products(file_path='data/products.json'):
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    return [Product.from_dict(product) for product in json.load(file)]
            except json.JSONDecodeError as e:
                print(f"Error: The file ast {file_path} is empty or contains invalid JSON")
                return []
        else:
            print(f"Error: The file at {file_path} does not exist.")
            return []

    @staticmethod
    def save_products(products, file_path='data/products.json'):
        with open(file_path, 'w') as file:
            json.dump([product.to_dict() for product in products], file)
