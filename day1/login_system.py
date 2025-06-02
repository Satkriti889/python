"""Create a login system using if-else:

username ="admin" and password="1234"

Ask the user to enter username and password.
"""
username=input("Enter username: ")
password=input("Enter password: ")
if username=="admin" and password=="1234":
    print("Access granted")
else:
    print("Access denied")