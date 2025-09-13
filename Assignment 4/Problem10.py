# 10. WAP to check if given number is Perfect Number.

num = int(input("Enter a number: "))
sum = 0
for i in range (1,int(num/2)+1):
    if(num%i==0):
        sum+=i
if(num == sum):
    print("it is a perfect number")
else:
  print('it is not a perfect number')            
