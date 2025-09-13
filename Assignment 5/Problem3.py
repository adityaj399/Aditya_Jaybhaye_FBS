#3. Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate 
# total amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.


P = int(input("Enter the no. of Passengers: "))
cost = int(input("Enter the cost of per ticket: "))
total = 0

for i in range(P):
    age = int(input(f"Enter the age of passenger {i+1}: "))

    if age < 12:   # child
        ticket = cost - (cost * 30 / 100)
    elif age > 59:  # senior citizen
        ticket = cost - (cost * 50 / 100)
    else:           # others
        ticket = cost

    print(f"Ticket cost for passenger {i+1}: {ticket}")
    total += ticket 

print(f"Total amount for all passengers = {total}")
    

    