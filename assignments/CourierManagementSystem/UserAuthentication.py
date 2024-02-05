# Sample user data (replace with actual user data in a real-world scenario)
user_data = {
    'employee': {
        'ishita.sharma@gmail.com': {'password': 'employee123', 'role': 'Courier Driver'},
        'sanvi.khanna@gmail.com': {'password': 'employee456', 'role': 'Manager'},
    },
    'customer': {
        'astha.raj@gmail.com': {'password': 'customer123', 'role': 'Customer'},
        'asmita.si@gmail.com': {'password': 'customer456', 'role': 'Customer'}
    }
}

def authenticate_user(user_type, email, password):
    users = user_data.get(user_type, {})

    # Make email comparison case-insensitive and strip whitespaces
    email = email.lower().strip()

    if email in users:
        user = users[email]
        if user['password'] == password:
            return user
    return None


# Example usage:
user_type_input = input("Enter user type (employee/customer): ").lower()
email_input = input("Enter your email: ")
password_input = input("Enter your password: ")

authenticated_user = authenticate_user(user_type_input, email_input, password_input)

if email_input in user_data.get(user_type_input, {}) and authenticated_user is not None:
    print(f"Authentication successful. Welcome {authenticated_user['role']}!")
else:
    print("Authentication failed. Please check if the user type, email, and password are valid.")
