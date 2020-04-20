a = int(input())
b = int(input())

for num in range(a,b+1):
    num = str(num)
    num1 = int(num[0])
    num2 = int(num[1])
    num3 = int(num[2])
    num4 = int(num[3])
    num5 = int(num[4])
    num6 = int(num[5])

    odd_sum = num1+num5+num3
    even_sum = num2+num4+num6
    are_equal = odd_sum == even_sum

    if are_equal:
        print(num,end=" ")