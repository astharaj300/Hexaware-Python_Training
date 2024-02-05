orders = [
    {'order_id': 11, 'user_id': 1, 'status': 'Processing'},
    {'order_id': 12, 'user_id': 2, 'status': 'Delivered'},
    {'order_id': 13, 'user_id': 3, 'status': 'Cancelled'},
    {'order_id': 14, 'user_id': 4, 'status': 'Processing'},
    {'order_id': 15, 'user_id': 5, 'status': 'Delivered'},
    {'order_id': 16, 'user_id': 6, 'status': 'Cancelled'},
    {'order_id': 17, 'user_id': 7, 'status': 'Processing'},
    {'order_id': 18, 'user_id': 8, 'status': 'Delivered'},
    {'order_id': 19, 'user_id': 9, 'status': 'Cancelled'},
    {'order_id': 20, 'user_id': 10, 'status': 'Processing'},]

def display_Customer_orders(customer_id):
    print(f"Orders for Customer{customer_id}:")
    for order in orders:
        if order['user_id'] == customer_id:
            print(f"Order ID: {order['order_id']}, status: {order['status']}")

customer_id_input = int(input("Enter Customer ID "))
display_Customer_orders(customer_id_input)