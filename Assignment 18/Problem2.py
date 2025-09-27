# 2. Create a class Distance with data members as km,m and cm and add following methods : a. Constructor b. Destructor

class Distance:

    def __init__(self,km,m,cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __del__(self):
        print("Distance successfully deleted")

    def __str__(self):
        return f'{self.km}km : {self.m}m : {self.cm}cm'        
    
d = Distance(60,45,23)
print(d)    