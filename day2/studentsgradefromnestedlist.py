marks=[[80,90,100],[60,20,30],[80.,60,75]]

def sum(marks):
    total = 0
    for i in marks:
        total = total + i

    return total

def check_grades(marks):
    average=sum(marks)/len(marks)

    if average>90:
        grade = "A"
    elif average>80:
        grade = "B"
    elif average>70:
        grade = "C"
    elif average>60:
        grade = "D"
    else:
        grade = "Fail"

    print("Average:", average )
    print("Grade:", grade)

for i in marks:
    check_grades(i)
