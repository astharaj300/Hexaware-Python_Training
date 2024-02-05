import random
import time


def track_courier(courier_id):
    print(f"Tracking Courier {courier_id}")

    while True:
        current_location = random.choice(['Location1', 'Location2', 'Location3', 'Location4'])
        print(f"Current Location: {current_location}")

        if current_location == 'Location3':
            print("Courier has reached the destination.")
            break

        time.sleep(2)


courier_id_input = input("Enter Courier ID: ")
track_courier(courier_id_input)