def check_order_status(order_status):
    if order_status == "Delivered":
        print("The order has been delivered.")
    elif order_status == "Processing":
        print("The order is still in processing.")
    elif order_status == "Cancelled":
        print("The order has been cancelled.")
    else:
        print("Invalid order status.")


# Example usage:
order_status_input = input("Enter the order status: ")
check_order_status(order_status_input)
