import datetime

def generate_order_confirmation_email(customer_name, order_number, delivery_address):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    expected_delivery_date = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")

    email_subject = f"Order Confirmation - Order #{order_number}"
    email_body = f"Dear {customer_name},\n\nThank you for placing your order with us. Your order details are as follows:\n\n"
    email_body += f"Order Number: {order_number}\n"
    email_body += f"Delivery Address: {delivery_address}\n"
    email_body += f"Expected Delivery Date: {expected_delivery_date}\n\n"
    email_body += "We appreciate your business and look forward to serving you.\n\nBest regards,\nThe XYZ Store Team"

    email = {
        'subject': email_subject,
        'body': email_body
    }

    return email

# Example usage:
customer_name_input = input("Enter customer's name: ")
order_number_input = input("Enter order number: ")
delivery_address_input = input("Enter delivery address: ")

confirmation_email = generate_order_confirmation_email(customer_name_input, order_number_input, delivery_address_input)

print("\nOrder Confirmation Email:")
print(f"Subject: {confirmation_email['subject']}")
print("\nBody:")
print(confirmation_email['body'])
