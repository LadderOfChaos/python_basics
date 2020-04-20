month = input()
stay = int(input())
total_price1 = 0
total_priceA = 0
per_night = 0
per_nightA = 0
if stay <=7:
    if month == "May" or month == "October":
        per_night = 50
        per_nightA = 65
        total_price1 = per_night * stay
        total_priceA = per_night * stay
    if month == "June" or month == "September":
        per_night = 75.2
        per_nightA = 68.7
        total_price1 = per_night * stay
        total_priceA = per_nightA * stay
    if month == "July" or month == "August":
        per_night = 76
        per_nightA = 77
        total_price1 = per_night * stay
        total_priceA = per_nightA * stay
if stay > 7 and stay <= 14:
    if month == "May" or month == "October":
        per_night = 50
        per_nightA = 65
        total_price1 = per_night * stay * 0.95
        total_priceA = per_night * stay
    if month == "June" or month == "September":
        per_night = 75.2
        per_nightA = 68.7
        total_price1 = per_night * stay
        total_priceA = per_nightA * stay
    if month == "July" or month == "August":
        per_night = 76
        per_nightA = 77
        total_price1 = per_night * stay
        total_priceA = per_nightA * stay
if stay > 14:
    if month == "May" or month == "October":
        per_night = 50
        per_nightA = 65
        total_price1 = per_night * stay * 0.7
        total_priceA = per_nightA * stay * 0.9
    if month == "June" or month == "September":
        per_night = 75.2
        per_nightA = 68.7
        total_price1 = per_night * stay * 0.8
        total_priceA = per_nightA * stay * 0.9
    if month == "July" or month == "August":
        per_night = 76
        per_nightA = 77
        total_price1 = per_night * stay
        total_priceA = per_nightA * stay * 0.9
print(f"Apartment: {total_priceA:.2f} lv.")
print(f"Studio: {total_price1:.2f} lv.")
