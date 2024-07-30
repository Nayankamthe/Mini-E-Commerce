import json
import os
from ecommerce.product import Product
class Cart:
    def __init__(self):
        self.items = {}
        self.products = Product.load_products()

    def add_item(self, product_id, quantity):        

        filtered_product = list(filter(lambda product: product.product_id == product_id, self.products))
        if filtered_product:
            if product_id in self.items:
                self.items[product_id][1] += quantity
            else:
                self.items[product_id] =[filtered_product[0].name, quantity]
        else:
            print("item doesn't found.")
    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def update_item(self, product_id, quantity):
        if product_id in self.items:
            self.items[product_id][1] = quantity
        

    def view_cart(self):
        
        return self.items
    def print_cart(self):
        print(f"{'Product ID':<12}| {'Product Name':<15}| {'Quantity':<8}")
        for product_id, item in self.items.items():
            print(f"{product_id:<12}| {item[0]:<15}| {item[1]:<8}")
        return "Happy Shopping !"    
    

    def clear_cart(self):
        self.items = {}

    @staticmethod
    def load_cart(file_path='data/carts.json'):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return {}

    @staticmethod
    def save_cart(cart, file_path='data/carts.json'):
        with open(file_path, 'w') as file:
            json.dump(cart, file)
