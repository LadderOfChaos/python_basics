guest_star = int(input())
command = input()
total_sum = 0
total_guest = 0
while command != "The restaurant is full":
    guest_count = int(command)
    couvert_price = 100
    if guest_count >= 5:
        couvert_price = 70
    current_sum = guest_count * couvert_price
    total_sum +=current_sum
    total_guest +=guest_count
    command = input()
if total_sum >= guest_star:
    print(f"You have {total_guest} guests and {total_sum - guest_star} leva left.")
else:
    print(f"You have {total_guest} guests and {total_sum} leva income, but no singer.")