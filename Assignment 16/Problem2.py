# 2. Create a class Product with members as pid,pname,price and quantity .Add following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:
    discount = 0

    def __init__(self,id=None,name=None,price=None,quantity=None):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __del__(self):   
        print(f"Product with ID:{self.id} is deleted")

    def showProduct(self):
        print("ID ",self.id)    
        print("NAME ",self.name)    
        print("PRICE ",self.price)    
        print("QUANTITY ",self.quantity)  
        print("-"*30) 

    def applydiscount(self):
        if Product.discount > 0:
            finalprice =  self.price - (self.price * Product.discount / 100)  
            print(f"Final price of {self.name} after Discount of {Product.discount} is {finalprice}")
            return finalprice
        else:
            print("No Discount applied") 
            return self.price
        
    @staticmethod
    def setdiscount(value):
        Product.discount = value

p1 =Product()
p2 = Product(101,"biscuit",345,1000)
p3 = Product(102,"Choclate",500,2000)

p1.showProduct()
p2.showProduct()
p3.showProduct()

Product.setdiscount(5)

p2.applydiscount()
p3.applydiscount()

print("Static Discount value for all product is",Product.discount)