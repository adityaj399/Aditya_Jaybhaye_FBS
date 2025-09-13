#4. Write a program to check if given number is Armstrong number or not.(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 
# , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +4*4*4*4)

num = int(input("Enter a number: "))
n = len(str(num))

temp = num
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit ** n
    temp //= 10

if sum_digits == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is NOT an Armstrong number")
