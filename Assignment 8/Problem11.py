# Write a progrmam to print Armstrong Number. 

def is_armstrong(num):
    power = len(str(num))
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    return total == num

n = int(input("Enter a number: "))
if is_armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")