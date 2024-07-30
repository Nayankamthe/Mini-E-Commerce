from ecommerce.product import Product
from ecommerce.cart import Cart
from ecommerce.order import Order
from datetime import datetime

class ECommerceSystem:
    def __init__(self):
        self.products = Product.load_products()
        self.carts = {}
        self.orders = Order.load_orders()
        self.current_cart = Cart()

    def add_product(self, name, description, price, quantity):
        product_id = len(self.products) + 1
        new_product = Product(product_id, name, description, price, quantity)
        self.products.append(new_product)
        Product.save_products(self.products)

    def update_product(self, product_id, name=None, description=None, price=None, quantity=None):
        for product in self.products:
            if product.product_id == product_id:
                if name:
                    product.name = name
                if description:
                    product.description = description
                if price:
                    product.price = price
                if quantity:
                    product.quantity = quantity
                Product.save_products(self.products)
                break

    def delete_product(self, product_id):
        self.products = [product for product in self.products if product.product_id != product_id]
        Product.save_products(self.products)

    def view_products(self):
        print(f"{'Product ID':<12}| {'Product Name':<15}| {'Description':<15}| {'Price':<8}| {'Quantity':<8}")
        for product in self.products:
            print(f"{product.product_id:<12}| {product.name:<15}| {product.description:<15}| {product.price:<8}| {product.quantity:<8}")
        
        return 



        # return [product.to_dict() for product in self.products]

    def add_to_cart(self, product_id, quantity):
        self.current_cart.add_item(product_id, quantity)
        Cart.save_cart(self.current_cart.view_cart())

    def view_cart(self):
        return self.current_cart.print_cart()

    def update_cart(self, product_id, quantity):
        self.current_cart.update_item(product_id, quantity)
        Cart.save_cart(self.current_cart.view_cart())

    def remove_from_cart(self, product_id):
        self.current_cart.remove_item(product_id)
        Cart.save_cart(self.current_cart.view_cart())

    def place_order(self, customer_details):
        order_id = len(self.orders) + 1
        items = self.current_cart.view_cart()
        total_amount = sum(product.price * data[1] for product_id, data in items.items() for product in self.products if product.product_id == product_id)
        order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_order = Order(order_id, customer_details, items, total_amount, order_date)
        self.orders.append(new_order)
        Order.save_orders(self.orders)
        self.current_cart.clear_cart()
        Cart.save_cart(self.current_cart.view_cart())

    def generate_sales_report(self):
        print(f"Total Revenue: {sum(order.total_amount for order in self.orders)}")
        # report = {
        #     "orders": [order.to_dict() for order in self.orders]
        # }
        print("ORDERS:")
        print(f"{'Order ID':<12}| {'Customer Details':<16}| {'Product Details':<15}| {'Quantity':<8}| {'Total Amount':<15}| {'Order Date':<20}")
        for order in self.orders:
            data = order.items.values()
            for product,Quantity in data:

                print(f"{order.order_id:<12}| {order.customer_details:<16}| {product:<15}| {Quantity:<8}| {order.total_amount:<15}| {order.order_date:<20}")
                      
        return ""
