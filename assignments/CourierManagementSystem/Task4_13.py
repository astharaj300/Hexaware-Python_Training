def calculate_shipping_cost(source_add, destination_add, parcel_wt):
    distance = abs(ord(source_add[0]) - ord(destination_add[0]))
    weight_cost = parcel_wt * 2.5
    total_cost = distance + weight_cost
    return total_cost

source_add_input = input("Enter Source Address: ")
destination_add_input = input("Enter Destination Address: ")
parcel_wt_input = float(input("Enter Parcel Wt :"))
shipping_cost = calculate_shipping_cost(source_add_input, destination_add_input, parcel_wt_input)
print("Shipping Cost : ", shipping_cost)