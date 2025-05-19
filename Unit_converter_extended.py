# convert miles to km

def km_to_miles(km):
    return km * 0.621371

while True:
    try:
        km = float(input("Enter distance in kilometers: "))
        if km < 0:
            print("Distance cannot be negative. Please enter a valid number.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

miles = km_to_miles(km)
print(f"{km} kilometers is equal to {miles:.2f} miles.")

