import csv

def student_record():
    with open("studentsrecord.csv", "r") as file:
        content = csv.reader(file)
        for row in content:
            print(row)
