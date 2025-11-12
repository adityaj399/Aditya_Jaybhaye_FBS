'''1. Develop a simple calculator program that performs basic arithmetic operations (+,
-, *, /) on two numbers provided by the user. The program should ask the user for
the numbers and the operator. However, the program should handle the following
exceptions:
a. Invalid Number: If the user enters a number that is not valid, catch the
exception and display an error message.
b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
"/", catch the exception and display an error message.
c. Division by Zero: If the user tries to divide by zero, catch the exception and
display an error message.
Write a program that performs the requested arithmetic operation and
handles the exceptions as described above.'''

try:

    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))

    operator = input("Enter a operator(+,-,*,/):")

    if operator not in ('+','-','*','/'):
        raise ValueError('invalid operator')
    
    if operator == '+':
        result = num1 +num2

    elif operator == '-':
        result = num1 - num2

    elif operator == '*':
        result = num1 * num2 

    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2

    print(f"result:{num1} {operator} {num2} = {result}")   


except ValueError as ve:
    print("error", ve)
    print("Please enter the valid operator(+,-,*,/) ") 

except ZeroDivisionError:
    print("Error: Division by zero is not allowed ")

except Exception as e:
    print("An unexcepted error")           

