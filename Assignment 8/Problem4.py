#4. Sum of all odd numbers between 1 to n

def Oddno():
    n = int(input("Enter the n number for printing Odd numbers"))

    for i in range(1,n+1):
        if(i%2!=0):
            print(i)
            i+=1

Oddno()            
    
