
from dao.ICourierUserService import ICourierUserService
from entity.Courier import Courier
from entity.Employee import Employee
from exception.TrackingNumberNotFoundException import TrackingNumberNotFoundException
import datetime

class CourierUserServiceImpl(ICourierUserService):
    def __init__(self, company_obj):
        self.company_obj = company_obj

    def place_order(self, courier_id, sender_name, receiver_name, weight, status):
        tracking_number = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{courier_id}"
        delivery_date = datetime.date.today() + datetime.timedelta(days=3)  # Placeholder for delivery date logic
        courier = Courier(courier_id, sender_name, None, receiver_name, None, weight, status, tracking_number, delivery_date)
        self.company_obj.add_courier(courier)
        return tracking_number

    def get_order_status(self, tracking_number):
        courier = self.find_courier_by_tracking_number(tracking_number)

        if courier:
            return courier.status
        else:
            raise TrackingNumberNotFoundException(f"Tracking number {tracking_number} not found.")

    def cancel_order(self, tracking_number):
        courier = self.find_courier_by_tracking_number(tracking_number)

        if courier:
            courier.status = "Cancelled"
            return True
        else:
            return False

    def get_assigned_orders(self, courier_staff_id):
        assigned_orders = [courier for courier in self.company_obj.get_couriers() if courier.courier_id == courier_staff_id]
        return assigned_orders

    def find_courier_by_tracking_number(self, tracking_number):
        for courier in self.company_obj.get_couriers():
            if courier.tracking_number == tracking_number:
                return courier
        return None
