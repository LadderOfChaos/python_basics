budget = float(input())
stunts = int(input())
price_per_unit = float(input())

dekor = budget * 0.1
total_price_unit = price_per_unit * stunts
if stunts > 150:
    total_price_unit *= 0.9
total_sum = dekor + total_price_unit

if budget >= total_sum:
    print("Action!")
    money_left = budget - total_sum
    print(F"Wingard starts filming with {money_left:.2f} leva left.")
else:
    print("Not enough money!")
    money_needed = abs(total_sum - budget)
    print(f"Wingard needs {money_needed:.2f} leva more.")