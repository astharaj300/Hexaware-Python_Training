couriers = ['courier1', 'courier2', 'courier3', 'courier4']
shipments = ['shipment1', 'shipment1', 'shipment1', 'shipment1']

for shipment in shipments:
    courier_assign = couriers.pop(0)
    print(f"{shipment} assigned to {courier_assign}")
