from ecommerce.ecommerce_system import ECommerceSystem

def main():
    system = ECommerceSystem()
    while True:
        print("\n1. Admin - Add Product")
        print("2. Admin - Update Product")
        print("3. Admin - Delete Product")
        print("4. Customer - View Products")
        print("5. Customer - Add to Cart")
        print("6. Customer - View Cart")
        print("7. Customer - Update Cart")
        print("8. Customer - Remove from Cart")
        print("9. Customer - Place Order")
        print("10. Admin - Generate Sales Report")
        print("11. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Product name: ")
            description = input("Product description: ")
            price = float(input("Product price: "))
            quantity = int(input("Product quantity: "))
            system.add_product(name, description, price, quantity)
        elif choice == '2':
            product_id = int(input("Product ID to update: "))
            name = input("New name (leave blank to keep current): ")
            description = input("New description (leave blank to keep current): ")
            price = input("New price (leave blank to keep current): ")
            quantity = input("New quantity (leave blank to keep current): ")
            system.update_product(product_id, name or None, description or None, float(price) if price else None, int(quantity) if quantity else None)
        elif choice == '3':
            product_id = int(input("Product ID to delete: "))
            system.delete_product(product_id)
        elif choice == '4':
            products = system.view_products()
        elif choice == '5':
            product_id = int(input("Product ID to add to cart: "))
            quantity = int(input("Quantity: "))
            system.add_to_cart(product_id, quantity)
        elif choice == '6':
            cart = system.view_cart()
            print(cart)
        elif choice == '7':
            product_id = int(input("Product ID to update in cart: "))
            quantity = int(input("New quantity: "))
            system.update_cart(product_id, quantity)
        elif choice == '8':
            product_id = int(input("Product ID to remove from cart: "))
            system.remove_from_cart(product_id)
        elif choice == '9':
            customer_details = input("Enter customer details: ")
            system.place_order(customer_details)
        elif choice == '10':
            report = system.generate_sales_report()
            print(report)
        elif choice == '11':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()