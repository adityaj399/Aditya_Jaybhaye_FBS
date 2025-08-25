#4. Write a program to enter P, T, R and calculate simple Interest. 

P = int(input("Enter the Principal amt "))
T = int(input("Enter the Time "))
R = int(input("Enter the Rate of int. "))

SI = (P*T*R)/100
print ('Simple Interest is ', SI)