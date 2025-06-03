# 1.  Define a class named `Student`.
# 2.  Implement the `__init__` method. It should take `name` and `age` as arguments and store them as attributes `self.name` and `self.age`.
# 3.  Add a method named `introduce()` that prints a message like: "Hi, my name is [Name] and I am [Age] years old."
# 4.  Create at least two different `Student` objects with different names and ages.
# 5.  Call the `introduce()` method on each of your student objects.

class  student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address=address
        print(f"A new Student object is {self.name} is created!")

    def introduce(self):
        print(f"my name is {self.name}.")

    def show_age(self):
        print(f"i am {self.age}, years old.")

    def show_address(self):
        print(f"I am from {self.address}.")

students=[]

for i in range(1,3):

    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    address = input("Enter student's address: ")
    studentt=student(name,age,address)
    students.append(studentt)

print(f"{students}")

    
for i,student in enumerate(students):
    student.introduce()
    student.show_age()
    student.show_address()
    
