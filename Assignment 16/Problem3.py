# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class Shirt:
    # static dictionary for size-based price increments
    size_price = {"small": 0,     "medium": 10,  "large": 20,    "xlarge": 30    }

    def __init__(self, sid=None, sname=None, type=None, price=0, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print(f"Shirt with ID {self.sid} is destroyed.")

    def showShirt(self):
        print("ID   :", self.sid)
        print("Name :", self.sname)
        print("Type :", self.type)
        print("Price:", self.price)
        print("Size :", self.size)
        print("-" * 30)

    def applySize(self):
        if self.size in Shirt.size_price:
            percent = Shirt.size_price[self.size]
            final_price = self.price + (self.price * percent / 100)
            print(f"Final price of {self.size} shirt '{self.sname}' is {final_price}")
            return final_price
        else:
            print("Invalid size")
            return self.price

s1 = Shirt(101, "H&M", "Casual", 1000, "small")
s2 = Shirt(102, "H&M", "Formal", 1000, "medium")
s3 = Shirt(103, "Zara", "Casual", 1000, "large")
s4 = Shirt(104, "Zara", "Casual", 1000, "xlarge")

s1.showShirt()
s2.showShirt()
s3.showShirt()
s4.showShirt()

s1.applySize()
s2.applySize()
s3.applySize()
s4.applySize()





