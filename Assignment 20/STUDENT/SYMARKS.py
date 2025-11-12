class SYMARKS:
    def __init__(self,computer_total,maths_total,electronics_total):
        self.computer_total = computer_total
        self.maths_total = maths_total
        self.electronics_total = electronics_total

    def display_marks(self):
        print("computer total",self.computer_total)
        print("maths total",self.maths_total)
        print("electronics total",self.electronics_total)
        print("overall total: ",self.computer_total + self.maths_total + self.electronics_total)    