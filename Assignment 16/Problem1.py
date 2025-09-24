#1. Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book:
    count =0

    def __init__(self,id= None,name = None,price = None,author = None):
        self.id = id
        self.name = name
        self.price = price
        self.author = author

        Book.count += 1

    def __del__(self):
        print(f"Book object with id={self.id} is deleted.")

    def showBook(self):
        print("ID : ",self.id)    
        print("NAME : ",self.name)    
        print("PRICE : ",self.price)    
        print("AUTOHR : ",self.author)  

b1 = Book()  # parameterless constructor
b2 = Book(101, "Python Programming", 450, "Guido van Rossum")
b3 = Book(102, "Learning Java", 500, "James Gosling")

b1.showBook()
b2.showBook()
b3.showBook()

print("Total Book objects created:", Book.count)   