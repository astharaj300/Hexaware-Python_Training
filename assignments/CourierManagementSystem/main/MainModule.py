# main/MainModule.py
from dao.CourierServiceDb import CourierServiceDb
from entity.CourierCompanyCollection import CourierCompanyCollection
from exception.TrackingNumberNotFoundException import TrackingNumberNotFoundException


def main():
    courier_service_db = CourierServiceDb()
    courier_company_collection = CourierCompanyCollection()

    while True:
        print("1. Place Order")
        print("2. Get Order Status")
        print("3. Cancel Order")
        print("4. Get Assigned Orders")
        print("5. Add Courier Staff")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            courier_id = input("Enter courier ID: ")
            sender_name = input("Enter sender name: ")
            receiver_name = input("Enter receiver name: ")
            weight = float(input("Enter parcel weight: "))
            status = "Processing"  # Initial status
            tracking_number = courier_service_db.place_order(courier_id, sender_name, receiver_name, weight, status)
            print(f"Order placed successfully. Tracking Number: {tracking_number}")

        elif choice == '2':
            tracking_number = input("Enter tracking number: ")
            try:
                status = courier_service_db.get_order_status(tracking_number)
                print(f"Order status: {status}")
            except TrackingNumberNotFoundException as e:
                print(f"Error: {e}")

        elif choice == '3':
            tracking_number = input("Enter tracking number: ")
            success = courier_service_db.cancel_order(tracking_number)
            if success:
                print(f"Order with tracking number {tracking_number} canceled successfully.")
            else:
                print(f"Unable to cancel order with tracking number {tracking_number}.")

        elif choice == '4':
            courier_staff_id = input("Enter courier staff ID: ")
            assigned_orders = courier_service_db.get_assigned_orders(courier_staff_id)
            print(f"Orders assigned to courier staff {courier_staff_id}: {assigned_orders}")

        elif choice == '5':
            name = input("Enter courier staff name: ")
            contact_number = input("Enter courier staff contact number: ")
            courier_service_db.add_courier_staff(name, contact_number)
            print("Courier staff added successfully.")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
