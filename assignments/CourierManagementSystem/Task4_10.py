import re

def validate_customer_info(data, detail):
    if detail == 'name':
        # Ensure that names contain only letters and are properly capitalized
        if data.isalpha() and data.istitle():
            return True
        else:
            return False
    elif detail == 'address':
        # Ensure that addresses do not contain special characters
        if data.isalnum() or all(c.isspace() for c in data):
            return True
        else:
            return False
    elif detail == 'phone':
        # Ensure that phone numbers follow the specific format ###-###-####
        phone_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
        if phone_pattern.match(data):
            return True
        else:
            return False
    else:
        return False

# Example usage:
name_result = validate_customer_info("Astha Raj", 'name')
print(f"Name is valid: {name_result}")

address_result = validate_customer_info("Motihar", 'address')
print(f"Address is valid: {address_result}")

phone_result = validate_customer_info("555-123-4567", 'phone')
print(f"Phone number is valid: {phone_result}")
