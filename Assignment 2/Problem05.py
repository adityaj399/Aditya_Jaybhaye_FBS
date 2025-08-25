#5. WAP to calculate selling price of book based on cost price and discount.
CP = int(input("Enter the CP - "))
Discount = int(input("Enter the discount percentage - "))

Dis_amt = ((Discount*CP)/100)
SP = CP -Dis_amt
print ('Selling price is ',SP)