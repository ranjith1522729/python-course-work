'''
modifiers = input("Enter the seat type: ")
booking_days = int(input("enter the booking days: "))
season = input("Enter the season or not: ").lower() == "True"
age = int(input("enter the age: "))

price = 5000

# modifiers
if modifiers == "Business":
    price += price * 0.40
elif modifiers == "Premium Economy":
    price += price * 0.20

# Booking days
if booking_days > 30:
    price -= price * 0.10
elif booking_days < 7:
    price += price * 0.25

# season
if season:
    price += price * 0.20

# Senior citizen
if age >= 60:
    price -= price * 0.15

print(price)
'''

age = int(input("Enter the age: "))
health_score = int(input("Enter the score: "))
vehicle_type = input("enter the vehicle: ").lower()

premium = 10000.0

if age < 25:
    premium += premium * 0.20
elif age > 50:
    premium += premium * 0.15

if health_score >= 80:
    premium -= premium * 0.10
elif health_score < 60:
    premium += premium * 0.20

if vehicle_type == "sports":
    premium += premium * 0.30
elif vehicle_type == "suv":
    premium += premium * 0.15

print(premium)