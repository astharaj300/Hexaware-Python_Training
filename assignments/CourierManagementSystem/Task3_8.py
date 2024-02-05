class Courier:
    def __init__(self, courier_id, current_location):
        self.courier_id = courier_id
        self.current_location = current_location
        self.is_available = True

def find_nearest_courier(order_location, couriers):
        nearest_courier = None
        min_distance = float('inf')

        for courier in couriers:
            distance = abs(ord(order_location) - ord(courier.current_location))

            if courier.is_available and distance < min_distance:
                min_distance = distance
                nearest_courier = courier

        return nearest_courier

# Example usage:

couriers_array = [
    Courier(courier_id='Courier1', current_location='Location1'),
    Courier(courier_id='Courier2', current_location='Location2'),
    Courier(courier_id='Courier3', current_location='Location3')
    ]

order_location_input = input("Enter order location: ")
nearest_courier = find_nearest_courier(order_location_input, couriers_array)

if nearest_courier:
    print(f"The nearest available courier is {nearest_courier.courier_id} at {nearest_courier.courier_location}. ")
else:
    print("No Available couriers")