'''2. Create class television that has members to hold the model number ,screen size
and price. Take a member function to take input from user, If more than 4 digits
are entered for model number, if screen size is smaller than 12 inches or greater
than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
exception.
Write a main() that instantiates an object and allows the user to enter and display
data. If exception is caught, replace all data member values with zero'''

class television:
    def __init__(self,model_number=0,screen_size=0,price=0):
        self.model_number = model_number
        self.screen_size = screen_size
        self.price = price

    def get_data(self):
        try: 
            M = int(input("Enter the Model Number: "))
            S = int(input("Enter the Screen Size in inches: "))
            P = int(input("Enter the Price of the Television: "))

            if len(str(M))>4 or S<12 or S<70 or P<0 or P>5000:
                raise Exception("Invalid Input Values ")
            
            self.model_number = M
            self.screen_size = S
            self.price = P
                    
        except Exception as e:
            print ("An unexcepted error",e)
            print("Resetting all values to zero.")
            self.model_number = 0
            self.screen_size = 0
            self.price = 0


    def display_data(self):
        print("\nTelevision Details:")
        print(f"Model Number: {self.model_number}")
        print(f"Screen Size: {self.screen_size} inches")
        print(f"Price: Rs. {self.price}")

def main():
    TV = television()
    TV.get_data()
    TV.display_data()

if __name__ == '__main__':
    main()

  


    
            



