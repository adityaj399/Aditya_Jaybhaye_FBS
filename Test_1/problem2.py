#2. Write a program to calculate simple interest based on Principal, Rate and Time(SI = P*R*T/100)

p=  int(input("Enter the Principle amt "))
r = float(input("Enter the rate percentage "))
t = int(input("Enter the time "))
si =(p*r*t)/100
print ('Simple interest is ', si)