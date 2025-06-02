count = 1

def get_marks():
    c = int(input("Enter number of students: "))

    marks = []


    for i in range(0,c):
        m_list = []
        print()
        print(f"Enter marks for student {i+1}")
        for i in range(0,3):
            m = float(input(f"Enter marks for subject {i+1}: "))
            m_list.append(m)
    
        marks.append(m_list)
        print()

    return marks

    
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

    global count
    print(f"Grade for student {count}")
    print("Average:", average )
    print("Grade:", grade)
    count = count + 1
    print()


marks = get_marks()
for i in marks:
    check_grades(i)