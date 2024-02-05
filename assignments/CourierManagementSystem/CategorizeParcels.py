def categorize_parcel(weight):
    categories = {
        'Light': weight <= 1.8,
        'Medium': 2.5 <= weight < 3.5,
        'Heavy': weight >= 4.0
    }

    for category, condition in categories.items():
        if condition:
            return category


# Example usage:
parcel_weight_input = float(input("Enter the parcel weight: "))
result = categorize_parcel(parcel_weight_input)
print(f"The parcel is categorized as: {result}")
