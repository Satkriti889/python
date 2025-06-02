def result():
    print("\n--- Enter Subject Marks (0 to 100) ---")

    subject1 = float(input("Enter marks for Database: "))
    subject2 = float(input("Enter marks for Multimedia: "))
    subject3 = float(input("Enter marks for OOP: "))
    subject4 = float(input("Enter marks for Networking: "))
    subject5 = float(input("Enter marks for HTML: "))

    if not (0 <= subject1 <= 100 and 0 <= subject2 <= 100 and 0 <= subject3 <= 100 and 0 <= subject4 <= 100 and 0 <= subject5 <= 100):
        print("Please enter marks between 0 to 100.")
        return result()
    average = (subject1 + subject2 + subject3 + subject4 + subject5) / 5
    rounded_average_marks="{:.2f}".format(average)
    if average < 50:
        grade = "Fail"
    elif average < 60:
        grade = "C+"
    elif average < 70:
        grade = "B"
    elif average < 80:
        grade = "B+"
    elif average < 90:
        grade = "A"
    else:
        grade = "A+"

    return subject1, subject2, subject3, subject4, subject5,  rounded_average_marks, grade
