# Sample 2D array for parcel tracking (replace with actual data in a real-world scenario)
parcel_tracking_array = [
    ['123456', 'Parcel in transit'],
    ['789012', 'Parcel out for delivery'],
    ['345678', 'Parcel delivered']
]

def track_parcel(parcel_number):
    for tracking_info in parcel_tracking_array:
        if tracking_info[0] == parcel_number:
            return tracking_info[1]
    return "Parcel not found"

def simulate_tracking_process():
    parcel_number_input = input("Enter parcel tracking number: ")
    status = track_parcel(parcel_number_input)

    if status != "Parcel not found":
        print(f"Tracking number: {parcel_number_input}")
        print(f"Current status: {status}")
        if status == "Parcel in transit":
            print("Next update: Parcel out for delivery")
        elif status == "Parcel out for delivery":
            print("Next update: Parcel delivered")
        else:
            print("Parcel has been delivered.")
    else:
        print("Parcel not found in the tracking system.")

# Example usage:
simulate_tracking_process()
