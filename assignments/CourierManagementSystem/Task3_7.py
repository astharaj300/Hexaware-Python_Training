class Parcel:
    def __init__(self, parcel_id):
        self.parcel_id = parcel_id
        self.tracking_history = []

    def location_update(self, location):
        self.tracking_history.append(location)


parcel1 = Parcel(parcel_id=1)
parcel1.location_update("At the warehouse")
parcel1.location_update("Shipped")
parcel1.location_update("At Delivery Hub")
parcel1.location_update("Delivered")

print(f"Parcel {parcel1.parcel_id} Tracking History: {parcel1.tracking_history}")