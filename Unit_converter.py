# convert miles to km

def km_to_miles(km):
    return km * 0.621371


# Ask the user for input
km = float(input("Enter distance in kilometers: "))

miles = km_to_miles(km)

print(f"{km} kilometers is equal to {miles:.2f} miles.")
