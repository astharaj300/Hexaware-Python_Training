# dao/CourierServiceDb.py
from connectionutil.DBConnection import DBConnection
from entity.Courier import Courier
from exception.TrackingNumberNotFoundException import TrackingNumberNotFoundException
import datetime

class CourierServiceDb:
    connection = None

    def __init__(self):
        self.connection = DBConnection.get_connection()

    def place_order(self, courier_id, sender_name, receiver_name, weight, status):
        tracking_number = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{courier_id}"

        # Example SQL query for inserting a new order (customize based on your schema)
        query = "INSERT INTO Courier (CourierID, SenderName, ReceiverName, Weight, Status, TrackingNumber) " \
                "VALUES (%s, %s, %s, %s, %s, %s)"

        data = (courier_id, sender_name, receiver_name, weight, status, tracking_number)

        # Execute the query using self.connection
        # Make sure to handle exceptions and commit the transaction
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, data)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            cursor.close()

        return tracking_number

    def get_order_status(self, tracking_number):
        # Example SQL query for retrieving order status (customize based on your schema)
        query = "SELECT Status FROM Courier WHERE TrackingNumber = %s"
        data = (tracking_number,)

        # Execute the query using self.connection
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, data)
            result = cursor.fetchone()

            if result:
                return result[0]  # Assuming 'Status' is the column name
            else:
                raise TrackingNumberNotFoundException(f"Tracking number {tracking_number} not found.")
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def cancel_order(self, tracking_number):
        # Example SQL query for canceling an order (customize based on your schema)
        query = "UPDATE Courier SET Status = 'Cancelled' WHERE TrackingNumber = %s"
        data = (tracking_number,)

        # Execute the query using self.connection
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, data)
            self.connection.commit()

            # Check if any rows were affected
            if cursor.rowcount > 0:
                return True
            else:
                return False
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            cursor.close()

    def get_assigned_orders(self, courier_staff_id):
        # Example SQL query for retrieving assigned orders for a courier staff (customize based on your schema)
        query = "SELECT * FROM Courier WHERE CourierID = %s"
        data = (courier_staff_id,)

        # Execute the query using self.connection
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, data)
            results = cursor.fetchall()

            assigned_orders = []
            for result in results:
                assigned_orders.append(Courier(*result))  # Assuming Courier class constructor

            return assigned_orders
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def add_courier_staff(self, name, contact_number):
        # Example SQL query for adding a new courier staff member (customize based on your schema)
        query = "INSERT INTO Employee (Name, ContactNumber, Role) VALUES (%s, %s, 'Courier Staff')"
        data = (name, contact_number)

        # Execute the query using self.connection
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, data)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            cursor.close()
