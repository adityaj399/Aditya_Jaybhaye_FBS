from students import student
from SYMARKS import SYMARKS
from TYMARKS import TYMARKS

def main():
    sy_student = SYMARKS(computer_total=85,maths_total=90,electronics_total=70)
    ty_student = TYMARKS(practical=98,theory=75)

    s1 = student(roll_no=1, name="Aditya", sy_marks=sy_student, ty_marks=ty_student)
    s1.display_result()

    print("___SY Marks___")
    sy_student.display_marks()
    print("___TY Marks___")
    ty_student.display_marks()

if __name__ == "__main__":
    main()