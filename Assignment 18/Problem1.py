#1. Create a class Complex Number with data members as real and imag and add following methods : 
# a. Constructor b. Destructor c. Overload +,- operator

class ComplexNumber:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __del__(self):
        print("Real & Iamg destroyed")

    def __add__(self,other):
        return ComplexNumber(self.real + other.real , self.imag + other.imag)
    
    def __sub__(self,other):
        return ComplexNumber(self.real - other.real , self.imag - other.imag)
    
    def __str__(self):
        return f'{self.real , self.imag}'
    

c1 = ComplexNumber(5,3)   
c2 = ComplexNumber(4,9) 

print("c1:", c1)
print("c2:", c2)

c3 = c1 + c2
print("c1 + c2 =", c3)

c4 = c1 - c2
print("c1 - c2 =", c4)

