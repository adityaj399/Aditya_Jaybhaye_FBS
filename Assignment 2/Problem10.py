#10. Write a program to reverse three-digit number.
 
num = int(input("Three digit no. "))

digit1 = num // 100          
digit2 = (num // 10) % 10   
digit3 = num % 10           

reverse_num = (digit3 * 100) + (digit2 * 10) + digit1

print("Reversed number is:", reverse_num)
