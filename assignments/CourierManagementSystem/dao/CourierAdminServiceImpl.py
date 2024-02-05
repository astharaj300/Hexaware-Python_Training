# dao/CourierServiceCollectionImpl.py
from dao.CourierUserServiceImpl import CourierUserServiceImpl
from entity.CourierCompanyCollection import CourierCompanyCollection
from entity.Courier import Courier
from entity.Employee import Employee
from exception.TrackingNumberNotFoundException import TrackingNumberNotFoundException
import datetime

class CourierServiceCollectionImpl(CourierUserServiceImpl):
    def __init__(self, company_obj):
        super().__init__(company_obj)

    def place_order(self, sender_name, receiver_name, weight):
        courier_id = self.generate_courier_id()
        status = "Processing"
        tracking_number = super().place_order(courier_id, sender_name, receiver_name, weight, status)

        # Add logic to store the order in the collection
        courier = Courier(courier_id, sender_name, None, receiver_name, None, weight, status, tracking_number, None)
        self.company_obj.add_courier(courier)

        return tracking_number

    def generate_courier_id(self):
        return len(self.company_obj.get_couriers()) + 1

    def cancel_order(self, tracking_number):
        # Add logic to cancel an order in the collection
        courier = self.find_courier_by_tracking_number(tracking_number)

        if courier:
            courier.status = "Cancelled"
            return True
        else:
            return False

    def get_assigned_orders(self, courier_staff_id):
        # Add logic to retrieve assigned orders for a courier staff from the collection
        assigned_orders = [courier for courier in self.company_obj.get_couriers() if courier.courier_id == courier_staff_id]
        return assigned_orders

    def find_courier_by_tracking_number(self, tracking_number):
        # Helper method to find a courier by tracking number in the collection
        for courier in self.company_obj.get_couriers():
            if courier.tracking_number == tracking_number:
                return courier
        return None

    def add_courier_staff(self, name, contact_number):
        # Add logic to add a new courier staff member to the collection
        courier_staff_id = self.generate_courier_staff_id()
        employee = Employee(courier_staff_id, name, contact_number, "Courier Driver", 0)
        self.company_obj.add_courier_staff(employee)
        return courier_staff_id

    def generate_courier_staff_id(self):
        return len(self.company_obj.get_courier_staff()) + 1

    def get_courier_history(self, tracking_number):
        # Add logic to retrieve the delivery history of a specific parcel from the collection
        courier = self.find_courier_by_tracking_number(tracking_number)

        if courier:
            return courier.delivery_history
        else:
            raise TrackingNumberNotFoundException(f"Tracking number {tracking_number} not found.")
