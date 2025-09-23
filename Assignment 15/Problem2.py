#2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product:
    def __init__(self,bid= None,pname=None,price=None,quantity=None):
        self.bid = bid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print (f"Product ID: ",self.bid)
        print (f"Name of Product: ",self.bid)
        print (f"Price: ",self.bid)
        print (f"Quantity: ",self.bid)

    def __del__ (self):
        print("Product Destroyed")   

P1 = Product()
P1.showProduct()
print("######################")
P2 = Product(109,'Choclate',500,550)
P2.showProduct()
print("######################")
P3 = Product(110,'Biscuit',400,750)
P3.showProduct()

