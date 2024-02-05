import mysql.connector
from entity.Customers import Customer
from dao.ServiceProviderImpl import CustomerDAOImpl, ProductDAOImpl, OrderDAOImpl, OrderdetailsDAOImpl
from entity.OrderDetails import OrderDetail
from entity.Orders import Order
from entity.Product import Product
from datetime import datetime


class MainClass:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ABcd300#$',
            database='techshop'
        )
        self.customers_dao = CustomerDAOImpl(self.connection)
        self.products_dao = ProductDAOImpl(self.connection)
        self.orders_dao = OrderDAOImpl(self.connection)
        self.order_detail_dao = OrderdetailsDAOImpl(self.connection)

    @staticmethod
    def display_menu():
        print("\nWelcome to TechShop, an Electronic Gadget Shop")
        print("1. Manage Customers")
        print("2. Manage Products")
        print("3. Manage Orders")
        print("4. Manage Order Details")
        print("5. Manage Inventory")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.manage_customers()
            elif choice == '2':
                self.manage_product()
            elif choice == '3':
                self.manage_orders()
            elif choice == '4':
                self.manage_order_details()
            elif choice == '5':
                self.manage_inventory()
            elif choice == '6':
                print("Program Ends, Bye!")
                break
            else:
                print("Invalid choice. Please enter again.")
                """elif choice == '5':
                    self.manage_inventory()"""

    def manage_customers(self):
        print("\n******************CUSTOMER MENU******************")
        while True:
            print("\nMenu:")
            print("1. Add Customer(C)")
            print("2. Get all the Customer Details(R)")
            print("3. Update the  Customer Information(U)")
            print("4. Delete the Customer(D)")
            print("5. View Specific Customer Details")
            print("6. Calculate Total Orders")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")


            if choice == "1":
                customer_id = input("Enter ID: ")
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone: ")
                address = input("Enter Address: ")
                customer = Customer(customer_id, first_name, last_name, email, phone, address)
                self.customers_dao.add_customer(customer)
                print("Customer added successfully.")

            elif choice == "2":
                customers = self.customers_dao.get_all_customers()
                if customers:
                    for customer in customers:
                        print(customer)
                else:
                    print("Sorry! No customer found")

            elif choice == "3":
                customer_id = int(input("Enter Customer ID: "))
                if self.customers_dao.get_customer_by_id(customer_id):
                    new_email = input("Enter new Email (leave blank to keep unchanged): ").strip() or None
                    new_phone = input("Enter new Phone (leave blank to keep unchanged): ").strip() or None
                    new_address = input("Enter new Address (leave blank to keep unchanged): ").strip() or None
                    self.customers_dao.update_customer_info(customer_id, new_email, new_phone, new_address)
                    print("Customer information updated successfully.")
                else:
                    print("Not found.")

            elif choice == "4":
                customer_id = int(input("Enter Customer ID: "))
                if self.customers_dao.get_customer_by_id(customer_id):
                    self.customers_dao.delete_customer(customer_id)
                    print("Customer deleted successfully.")
                else:
                    print("id not found")

            elif choice == "5":
                customer_id = int(input("Enter Customer ID: "))
                customer = self.customers_dao.get_customer_by_id(customer_id)
                if customer:
                    print(customer.CustomerID, customer.FirstName, customer.LastName, customer.Email, customer.Phone,
                          customer.Address)
                else:
                    print("Customer not found.")

            elif choice == "6":
                customer_id = int(input("Enter Customer ID: "))
                if self.customers_dao.get_customer_by_id(customer_id):
                    total_orders = self.customers_dao.calculate_total_orders(customer_id)
                    print(f"Total orders for customer {customer_id}: {total_orders}")
                else:
                    print("Customer not found.")

            elif choice == "7":
                print("program Ends.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def manage_product(self):
        print("\n******************PRODUCT MENU******************")
        while True:
            print("\nMenu:")
            print("1. Add Product(C)")
            print("2. Get all Product Details(R)")
            print("3. Update Product Information(U)")
            print("4. Delete Product(D)")
            print("5. View Specific Product Details")
            print("6. Is Product In Stock?")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                product_id = input("Enter Product ID; ")
                product_name = input("Enter Product Name: ")
                description = input("Enter the Description: ")
                price = float(input("Enter the Price: "))
                product = Product(product_id, product_name, description, price)
                self.products_dao.add_products(product)
                print("Product added successfully.")

            elif choice == "2":
                products = self.products_dao.get_all_products()
                if products:
                    for product in products:
                        print(product)
                else:
                    print("No Product found")

            elif choice == "3":
                product_id = int(input("Enter Product ID: "))
                if self.products_dao.get_product_by_id(product_id):
                    new_price = input("Enter new Price (leave blank to keep unchanged): ").strip() or None
                    self.products_dao.update_product_info(product_id, new_price)
                    print("Product information updated successfully.")
                else:
                    print("Not found.")

            elif choice == "4":
                product_id = int(input("Enter Product ID: "))
                if self.products_dao.get_product_by_id(product_id):
                    self.products_dao.delete_products(product_id)
                    print("Product deleted successfully.")
                else:
                    print("Product not found")

            elif choice == "5":
                product_id = int(input("Enter Product ID: "))
                product = self.products_dao.get_product_by_id(product_id)
                if product:
                    print(product.ProductID, product.ProductName, product.Description, product.Price)
                else:
                    print("Product not found.")

            elif choice == "6":
                product_id = int(input("Enter Product ID: "))
                if self.products_dao.get_product_by_id(product_id):
                    if self.products_dao.is_product_in_stock(product_id):
                        print("Currently in Stock")
                    else:
                        print("Out of Stock")
                else:
                    print("Product not found.")

            elif choice == "7":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def manage_orders(self):
        print("\n******************ORDER MENU******************")
        while True:
            print("\nMenu:")
            print("1. Create the Order(C)")
            print("2. Display the Orders(R)")
            print("3  Cancel the Order(D)")
            print("4. Get Order Details")
            print("5. Calculate Total Amount")
            print("6. UpdateOrderStatus (Processed/shipped)")
            print("7. Exit")

            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                customer_id = input("Enter Customer id: ")
                order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                order_details = []
                while True:
                    product_id = input("Enter Product ID: ")
                    quantity = int(input("Enter Quantity: "))
                    order_detail = OrderDetail(None, None, product_id, quantity)
                    order_details.append(order_detail)
                    add_more = input("Add more products? (yes/no): ").lower()
                    if add_more != 'yes':
                        break
                order = Order(None, customer_id, order_date, None)
                self.orders_dao.create_orders(order, order_details)
                print("Order added successfully.")

            elif choice == "2":
                orders = self.orders_dao.display_orders()
                if orders:
                    for order in orders:
                        print(order)
                else:
                    print("No Order found")

            elif choice == "3":
                order_id = int(input("Enter Order ID: "))
                if self.orders_dao.GetOrderDetails(order_id):
                    self.orders_dao.CancelOrder(order_id)
                    print("Order cancelled successfully.")
                else:
                    print("Order not found")

            elif choice == "4":
                order_id = int(input("Enter Order ID: "))
                orders = self.orders_dao.GetOrderDetails(order_id)
                if orders:
                    for order in orders:
                        print("Order ID:", order.orderID)
                        print("Customer ID:", order.CustomerID)
                        print("Order Date:", order.orderDate)
                        print("Total Amount:", order.TotalAmount)
                else:
                    print("Order not found for this customer.")

            elif choice == "5":
                print(self.orders_dao.CalculateTotalAmount())
            elif choice == "6":
                order_id = int(input("Enter Order ID: "))
                print(self.orders_dao.UpdateOrderStatus(order_id))

            elif choice == "7":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def manage_order_details(self):
        print("\n******************ORDER DETAILS MENU******************")
        while True:
            print("\nMenu:")
            print("1. Calculate Subtotal")
            print("2. Get Order Detail Info")
            print("3. Update Quantity")
            print("4. Add Discount")
            print("5. Display All OderDetails")
            print("6. Exit")

            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                order_detail_id = int(input("Enter Order Detail ID: "))
                subtotal = self.order_detail_dao.CalculateSubtotal(order_detail_id)
                if subtotal is not None:
                    print("Subtotal:", subtotal)
                else:
                    print("Order detail not found.")

            elif choice == "2":
                order_detail_id = int(input("Enter Order Detail ID: "))
                self.order_detail_dao.GetOrderDetailInfo(order_detail_id)

            elif choice == "3":
                order_detail_id = int(input("Enter Order Detail ID: "))
                new_quantity = int(input("Enter new quantity: "))
                self.order_detail_dao.UpdateQuantity(order_detail_id, new_quantity)

            elif choice == "4":
                order_detail_id = int(input("Enter Order Detail ID: "))
                discount_percentage = float(input("Enter discount percentage: "))
                self.order_detail_dao.AddDiscount(order_detail_id, discount_percentage)

            elif choice == "5":
                orders = self.order_detail_dao.GetAllOrderDetail()
                if orders:
                    for order in orders:
                        print(order)
                else:
                    print("No Order found")

            elif choice == "6":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def manage_inventory(self):
        print("\n******************MANAGE INVENTORY MENU******************")
        while True:
            print("\nMenu:")
            print("1. Get Product")
            print("2. Get QuantityInStock")
            print("3. Remove from Inventory")
            print("4. Update Stock Quantity")
            print("5. Is Product Available")
            print("6. Get Inventory Value")
            print("7.List Low Stock Products")
            print("8. List Out of Stck Products")
            print("9. List all Products")
            print("10. Exit")




if __name__ == '__main__':
    menu = MainClass()
    menu.run()
