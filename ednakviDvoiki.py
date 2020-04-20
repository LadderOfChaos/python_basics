dvoiki = int(input())             #x
sum = 0
max_diff= 0
for i in range(dvoiki):
    num1 = int(input())
    num2 = int(input())
    current_sum = num1 + num2


    if i == 0:
        sum = current_sum

    if not current_sum == sum:
        current_diff = abs(current_sum - sum)
        if current_diff > max_diff:
            max_diff = current_diff
        sum = current_sum
if max_diff == 0:
    print(f"Yes, Value={sum}")
else:
    print(f"No, maxdiff={max_diff}")




