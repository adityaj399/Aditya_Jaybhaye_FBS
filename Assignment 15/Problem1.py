# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:
    def __init__(self,bid=None,bname=None,price=None,author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def showBook(self):
        print (f"Member id :",self.bid)
        print (f"Book Name :",self.bname)
        print (f"Price :",self.price)
        print (f"Author Name :",self.author)

    def __del__(self):
        print("BOOk Destroyed")

B1 = Book()   
B1.showBook()    
print("###################################")
B2 = Book(507,"Art Of Letting Go",180,"Chetan Bhagat")     
B2.showBook()
        