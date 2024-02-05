import mysql.connector
from dao.ServiceProvider import CustomerDAO, ProductDAO, OrderDAO, OrderdetailsDAO, InventoryDAO
from entity.Customers import Customer
from entity.Orders import Order
from entity.Product import Product
from exception.ExceptionHandling import DAOException
from datetime import datetime


class CustomerDAOImpl(CustomerDAO):
    def __init__(self, connection):
        self.connection = connection

    def calculate_total_orders(self, customer_id):
        try:
            cursor = self.connection.cursor()
            sql = "select count(*) from Orders where CustomerID = %s"
            cursor.execute(sql, (customer_id,))
            result = cursor.fetchone()
            total_orders = result[0]
            cursor.close()
            return total_orders
        except mysql.connector.Error as e:
            print(f"Error calculating total orders: {e}")
            raise DAOException("Error in calculating total orders")

    def add_customer(self, customer):
        try:
            cursor = self.connection.cursor()
            sql = ("insert into Customers ( CustomerID,FirstName, LastName, Email, Phone, Address) "
                   "VALUES (%s, %s, %s, %s, %s, %s)")
            val = (customer.CustomerID,customer.FirstName, customer.LastName, customer.Email, customer.Phone,
                   customer.Address)
            cursor.execute(sql, val)
            self.connection.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error in creating customer: {e}")
            raise DAOException("Error creating customer")

    def get_customer_by_id(self, customer_id):
        try:
            cursor = self.connection.cursor()
            sql = "select * from Customers where CustomerID = %s"
            cursor.execute(sql, (customer_id,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                customer1 = Customer(result[0], result[1], result[2], result[3], result[4], result[5])
                return customer1
            else:
                return None
        except mysql.connector.Error as e:
            print(f"Error in fetching customer: {e}")
            raise DAOException("Error fetching customer")

    def update_customer_info(self, customer_id, email=None, phone=None, address=None):
        try:
            cursor = self.connection.cursor()
            sql = "UPDATE Customers SET"
            val = []

            if email is not None:
                sql += " Email=%s,"
                val.append(email)

            if phone is not None:
                sql += " Phone=%s,"
                val.append(phone)

            if address is not None:
                sql += " Address=%s,"
                val.append(address)

            # Remove the trailing comma from the SQL query
            if len(val) > 0:
                sql = sql.rstrip(',')
                sql += " WHERE CustomerID=%s"
                val.append(customer_id)

                cursor.execute(sql, val)
                self.connection.commit()
                cursor.close()
                return True
            else:
                print("No parameters provided for update")
                return False
        except mysql.connector.Error as e:
            print(f"Error updating customer: {e}")
            raise DAOException("Error updating customer")

    def get_all_customers(self):
        try:
            cursor = self.connection.cursor()
            sql = "select * from Customers"
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except mysql.connector.Error as e:
            print(f"Error in fetching all customers: {e}")
            raise DAOException("Error fetching all customers")

    def delete_customer(self, customer_id):
        try:
            cursor = self.connection.cursor()
            sql = "DELETE FROM Customers WHERE CustomerID=%s"
            cursor.execute(sql, (customer_id,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print(f"Error deleting customer: {e}")
            raise DAOException("Error deleting customer")


class ProductDAOImpl(ProductDAO):
    def __init__(self, connection):
        self.connection = connection

    def add_products(self, product):
        try:
            cursor = self.connection.cursor()
            sql = "INSERT INTO Products (ProductID,ProductName, Description, Price) VALUES (%s, %s, %s, %s)"
            val = (product.ProductID,product.ProductName, product.Description, product.Price)
            cursor.execute(sql, val)
            self.connection.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error creating customer: {e}")
            raise DAOException("Error creating customer")

    def get_product_by_id(self, product_id):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT * FROM Products WHERE ProductID = %s"
            cursor.execute(sql, (product_id,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                product1 = Product(result[0], result[1], result[2], result[3])
                return product1
            else:
                return None
        except mysql.connector.Error as e:
            print(f"Error fetching customer: {e}")
            raise DAOException("Error fetching customer")

    def update_product_info(self, product_id, new_price=None):
        try:
            cursor = self.connection.cursor()
            sql = "UPDATE Products SET"
            val = []

            if new_price is not None:
                sql += " Price=%s,"
                val.append(new_price)

            if len(val) > 0:
                sql = sql.rstrip(',')
                sql += " WHERE ProductID=%s"
                val.append(product_id)

                cursor.execute(sql, val)
                self.connection.commit()
                cursor.close()
                return True
            else:
                print("No parameters provided for update")
                return False
        except mysql.connector.Error as e:
            print(f"Error updating customer: {e}")
            raise DAOException("Error updating customer")

    def is_product_in_stock(self, product_id):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT QuantityInStock FROM Inventory WHERE ProductID = %s"
            cursor.execute(sql, (product_id,))
            total_orders = cursor.fetchone()
            cursor.close()
            if total_orders is not None:
                return True
            else:
                return False
        except mysql.connector.Error as e:
            print(f"Error calculating total orders: {e}")
            raise DAOException("Error calculating total orders")

    def get_all_products(self):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT * FROM Products"
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except mysql.connector.Error as e:
            print(f"Error fetching all customers: {e}")
            raise DAOException("Error fetching all customers")

    def delete_products(self, product_id):
        try:
            cursor = self.connection.cursor()
            sql = "DELETE FROM Products WHERE ProductID = %s"
            cursor.execute(sql, (product_id,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print(f"Error deleting product: {e}")
            raise DAOException("Error deleting product")


class OrderDAOImpl(OrderDAO):
    def __init__(self, connection):
        self.connection = connection

    def create_orders(self, order, order_details):
        try:
            cursor = self.connection.cursor()
            total_amount = 0
            for order_detail in order_details:
                sql_get_price = "SELECT Price FROM Products WHERE ProductID = %s"
                cursor.execute(sql_get_price, (order_detail.ProductID,))
                price = cursor.fetchone()[0]
                total_amount += order_detail.Quantity * price
            sql_insert_order = "INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES (%s, %s, %s)"
            order_data = (order.CustomerID, order.orderDate, total_amount)
            cursor.execute(sql_insert_order, order_data)
            order_id = cursor.lastrowid
            for order_detail in order_details:
                sql_insert_order_detail = "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (%s, %s, %s)"
                order_detail_data = (order_id, order_detail.ProductID, order_detail.Quantity)
                cursor.execute(sql_insert_order_detail, order_detail_data)
            self.connection.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error creating customer: {e}")
            raise DAOException("Error adding order")

    def display_orders(self):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT * FROM Orders"
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except mysql.connector.Error as e:
            print(f"Error fetching all customers: {e}")
            raise DAOException("Error fetching all customers")

    def CancelOrder(self, order_id):
        try:
            cursor = self.connection.cursor()
            sql_select_order = "SELECT OrderID FROM Orders WHERE OrderID = %s"
            cursor.execute(sql_select_order, (order_id,))
            result = cursor.fetchone()
            if not result:
                raise DAOException("Order not found")
            sql_select_order_details = "SELECT ProductID, Quantity FROM OrderDetails WHERE OrderID = %s"
            cursor.execute(sql_select_order_details, (order_id,))
            order_details = cursor.fetchall()
            for product_id, quantity in order_details:
                sql_update_inventory = ("UPDATE Inventory SET QuantityInStock ="
                                        " QuantityInStock + %s WHERE ProductID = %s")
                cursor.execute(sql_update_inventory, (quantity, product_id))
            sql_delete_order_details = "DELETE FROM OrderDetails WHERE OrderID = %s"
            cursor.execute(sql_delete_order_details, (order_id,))
            sql_delete_order = "DELETE FROM Orders WHERE OrderID = %s"
            cursor.execute(sql_delete_order, (order_id,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print(f"Error deleting product: {e}")
            raise DAOException("Error deleting product")

    def GetOrderDetails(self, order_id):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT * FROM Orders WHERE OrderID = %s"
            cursor.execute(sql, (order_id,))
            results = cursor.fetchall()
            cursor.close()
            orders = []
            if results:
                for result in results:
                    order = Order(result[0], result[1], result[2], result[3])
                    orders.append(order)
                return orders
            else:
                return None
        except mysql.connector.Error as e:
            print(f"Error fetching customer: {e}")
            raise DAOException("Error fetching customer")

    def CalculateTotalAmount(self):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT SUM(TotalAmount) from Orders"
            cursor.execute(sql)
            total_price_info = cursor.fetchone()
            cursor.close()
            if total_price_info:
                return total_price_info
            else:
                return 0
        except mysql.connector.Error as e:
            print(f"Error calculating total amount for order: {e}")
            raise DAOException("Error calculating total amount for order")

    def UpdateOrderStatus(self, order_id):
        try:
            cursor = self.connection.cursor()
            sql_get_order_date = "SELECT OrderDate FROM Orders WHERE OrderID = %s"
            cursor.execute(sql_get_order_date, (order_id,))
            result = cursor.fetchone()
            if result:
                order_date = result[0]
                current_date = datetime.now()
                order_date = datetime.combine(order_date, datetime.min.time())
                difference = current_date - order_date
                if difference.days > 3:
                    return "shipped"
                else:
                    return "Processing"
            else:
                return "Order not found"
        except mysql.connector.Error as e:
            print(f"Error updating order status: {e}")
            raise DAOException("Error updating order status")


class OrderdetailsDAOImpl(OrderdetailsDAO):
    def __init__(self, connection):
        self.connection = connection

    def GetAllOrderDetail(self):
        try:
            cursor = self.connection.cursor()
            sql = "select * from orderdetails"
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except mysql.connector.Error as e:
            print(f"Error fetching all customers: {e}")
            raise DAOException("Error fetching all customers")

    def CalculateSubtotal(self, order_detail_id):
        try:
            cursor = self.connection.cursor()
            sql = ("SELECT p.Price, od.Quantity FROM Products p INNER JOIN OrderDetails od ON p.ProductID ="
                   " od.ProductID WHERE od.OrderDetailID = %s")
            cursor.execute(sql, (order_detail_id,))
            result = cursor.fetchone()
            if result:
                price, quantity = result
                subtotal = price * quantity
                return subtotal
            else:
                return None
        except mysql.connector.Error as e:
            print(f"Error calculating subtotal: {e}")
            raise DAOException("Error calculating subtotal")

    def GetOrderDetailInfo(self, order_detail_id):
        try:
            cursor = self.connection.cursor()
            sql = ("SELECT od.OrderDetailID, o.OrderID, p.ProductName, od.Quantity FROM OrderDetails od INNER JOIN "
                   "Orders o ON od.OrderID = o.OrderID INNER JOIN Products p ON od.ProductID = p.ProductID "
                   "WHERE od.OrderDetailID = %s")
            cursor.execute(sql, (order_detail_id,))
            result = cursor.fetchone()
            if result:
                order_detail_id, order_id, product_name, quantity = result
                print("Order Detail ID:", order_detail_id)
                print("Order ID:", order_id)
                print("Product Name:", product_name)
                print("Quantity:", quantity)
            else:
                print("Order detail not found.")
        except mysql.connector.Error as e:
            print(f"Error getting order detail info: {e}")
            raise DAOException("Error getting order detail info")

    def UpdateQuantity(self, order_detail_id, new_quantity):
        try:
            cursor = self.connection.cursor()
            sql_get_price = ("SELECT p.Price FROM OrderDetails od JOIN Products p ON od.ProductID = "
                             "p.ProductID WHERE od.OrderDetailID = %s")
            cursor.execute(sql_get_price, (order_detail_id,))
            """price = cursor.fetchone()[0]"""
            sql_update_quantity = "UPDATE OrderDetails SET Quantity = %s WHERE OrderDetailID = %s"
            cursor.execute(sql_update_quantity, (new_quantity, order_detail_id))

            sql_update_total_amount = ("UPDATE Orders SET TotalAmount = (SELECT SUM(od.Quantity * p.Price) "
                                       "FROM OrderDetails od JOIN Products p ON od.ProductID = p.ProductID "
                                       "WHERE od.OrderID = (SELECT OrderID FROM OrderDetails "
                                       "WHERE OrderDetailID = %s)) WHERE OrderID = "
                                       "(SELECT OrderID FROM OrderDetails WHERE OrderDetailID = %s)")
            cursor.execute(sql_update_total_amount, (order_detail_id, order_detail_id))

            self.connection.commit()
            print("Quantity updated successfully.")
        except mysql.connector.Error as e:
            print(f"Error updating quantity: {e}")
            raise DAOException("Error updating quantity")

    def AddDiscount(self, order_detail_id, discount_percentage):
        try:
            """cursor = self.connection.cursor()"""
            subtotal = self.CalculateSubtotal(order_detail_id)
            if subtotal is not None:
                discount_amount = subtotal * (discount_percentage / 100)
                discounted_amount = subtotal - discount_amount
                print("Discounted amount:", discounted_amount)
            else:
                print("Order detail not found.")
        except mysql.connector.Error as e:
            print(f"Error adding discount: {e}")
            raise DAOException("Error adding discount")


class InventoryDAOImpl(InventoryDAO):
    def __init__(self, connection):
        self.connection = connection
