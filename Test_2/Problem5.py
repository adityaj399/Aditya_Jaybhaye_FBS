# A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST.

p1 = int(input("Enter the Price of product 1 : ")) 
p2 = int(input("Enter the Price of product 2 : ")) 
p3 = int(input("Enter the Price of product 3 : ")) 
p4 = int(input("Enter the Price of product 4 : ")) 
p5 = int(input("Enter the Price of product 5 : "))

sum = p1 + p2 + p3 + p4 + p5
print('Sum of bill is',sum)

total_bill = sum + (sum*18)/100

print("total bill incluing GST is ", total_bill)