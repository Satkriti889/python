""""Student Gradebook Management System"
Build a Python program that allows teachers to manage student records, including adding student details, recording grades, calculating averages, and 
generating report cards. 
The system should use file I/O to store data, modular design for different components (e.g., student, grades, reports), and exception handling for 
invalid inputs or missing files."""
import csv,os

from students_record import student_details
from grade_calc import result
from student_details import student_record



filename="studentsrecord.csv"


def add_students():
    print("\n---- Add Students Details ----")
    try:
        total = int(input("Enter the number of students: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(total):
        print(f"\nEnter details of student {i + 1}")
        name, roll_no, address = student_details()
        marks1, marks2, marks3, marks4, marks5, avg, grade = result()

        file_exists = os.path.exists(filename)

       
        mode = "a" if file_exists else "w"

        with open(filename, mode, newline='') as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "Name", "Roll No", "Address",
                    "Database", "Multimedia", "OOP", "Networking", "HTML",
                    "Average", "Grade"
                ])

            writer.writerow([
                name, roll_no, address,
                marks1, marks2, marks3, marks4, marks5,
                avg, grade
            ])

    print("Record added sucessfully.\n")



def menu():
    while True:

        print("\n----- Welcome to Student Record Book -----")
        print("1. Add student details")
        print("2. View records of student")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_students()
        elif choice == "2":
            student_record()
        elif choice == "3":
            print("Thanks for using the system.")
            break
        else:
            print("Invalid input. Please try again.")
            menu()
            continue

menu()

 



