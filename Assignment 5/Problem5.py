#5. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount. 
# (Use looping to optimizethe problem)

amt = int(input("Enter the integer amount : "))

notes = [2000,1000,500,200,100,50,20,10,5,2,1]

for note in notes:
    if amt>=note:
        count = amt // note
        amt = amt % note
        print(f"total money is :{note} {count} ")
