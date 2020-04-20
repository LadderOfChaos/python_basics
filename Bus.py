start_passangers_count = int(input())
spirki = int(input())
income = 0
outcome = 0
for x in range(1,spirki+1):
    slizashti = int(input())
    kachvashti = int(input())

    if x % 2 == 0:
        income += kachvashti
        outcome += slizashti + 2

    elif x % 2 != 0:
        outcome += slizashti
        income += kachvashti + 2
final_count = start_passangers_count + income - outcome
print(f"The final number of passengers is : {final_count}")