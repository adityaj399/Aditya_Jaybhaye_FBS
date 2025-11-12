from SYMARKS import SYMARKS
from TYMARKS import TYMARKS

class student:
    def __init__(self,roll_no,name,sy_marks,ty_marks):
        self.roll_no =roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_grade(self):
        total = self.sy_marks.computer_total + self.ty_marks.Practical
        avg = total/2

        if avg >= 70:
            grade = "A"
        elif avg >= 60:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        elif avg >= 40:
            grade = "Pass"
        else:
            grade = "fail"

        return total,grade    

    
    def display_result(self):
        total, grade = self.calculate_grade()
        print(f"\nRoll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"SY Computer Total: {self.sy_marks.computer_total}")
        print(f"TY Practical: {self.ty_marks.Practical}")
        print(f"Total: {total}")
        print(f"Grade: {grade}")             