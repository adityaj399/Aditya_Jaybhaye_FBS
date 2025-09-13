# 3. WAP to print sum of series upto n.

#Using While Loop

n =int(input("Enter the number to print sum of series upto n. n = "))
i=1
total = 0
while(i<=n):
    total +=i
    i+=1

    print(total)


#Using for Loop

n =int(input("Enter the number to print sum of series upto n. n = "))
total =0
for i in range(1,n+1):
    total +=i
    print(total)

