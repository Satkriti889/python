def student_details():
    try:
        name=input("Enter the name of student :")
        roll_no=int(input("Enter the Roll number of student :"))
        address=input("Enter the address of student : ")
        print("Students detail recorded sucessfully.")
    except:
        ValueError
        print("Invalid input")
        return student_details()
    
    print("Please enter the valid details")
    return name,roll_no,address