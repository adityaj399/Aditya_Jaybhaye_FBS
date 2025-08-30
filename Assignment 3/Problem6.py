#6. Write a program to calculate profit or loss
sp = float(input("Enter the selling price - "))
cp = float(input("Enter the cost price - "))

if(sp>cp):
    print(f"You made a profit {sp - cp}")
else:
    print(f"You made a loss of {cp - sp}") 