def format_address(street, city, state, zip_code):
    formatted_street = ' '.join(word.capitalize() for word in street.split())
    formatted_city = city.capitalize()
    formatted_state = state.capitalize()
    formatted_zip_code = str(zip_code).zfill(5)  # Ensure zip code is 5 digits

    formatted_address = f"{formatted_street}, {formatted_city}, {formatted_state} {formatted_zip_code}"
    return formatted_address

# Example usage:
street_input = input("Enter street address: ")
city_input = input("Enter city: ")
state_input = input("Enter state: ")
zip_code_input = input("Enter zip code: ")

formatted_address = format_address(street_input, city_input, state_input, zip_code_input)
print(f"Formatted Address: {formatted_address}")
