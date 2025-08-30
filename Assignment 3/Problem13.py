"""#13. Write a program to input electricity unit charges and calculate total electricity bill
according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill"""

units = int(input("Enter the total amount of units "))

if (units <= 50):
    amt = (units * 0.50)
elif(units<=150):
    amt = (0.5 * 50) + ((units - 50) * 0.75)
elif(units<=250):
    amt = (0.5 * 50) + (0.75 * 100) + ((units - 150)* 1.20)
elif(units>250):
    amt = (0.5 * 50) + (0.75 * 100) + (1.20 * 100) + ((units -250)*1.50)

charge = (amt*20)/100
total_amt = amt + charge      

print ("Total Electricity bill for the Consumed units is ", total_amt)
          

