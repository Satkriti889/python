import string
def user_input():
    password1=input("enter the password ")
    if len(password1)>=8:
        return password1
    else:
        print("The password must be equal to or greater than 8")
        user_input()

password1=user_input()


def check_password(password1):
    
    has_upper=0
    has_lower=0
    has_number=0
    has_char=0

    for i in password1:
        if i.isupper():
            has_upper=1
        elif i.islower():
            has_lower=1
        elif i.isdigit():
            has_number=1
        elif i in string.punctuation:
            has_char = 1

    main(has_upper,has_lower,has_number,has_char)


def main(has_upper,has_lower,has_number,has_char):

    compare = has_upper + has_lower + has_number + has_char

    if compare == 4:
        print("Very Strong")
         
    elif compare == 3:
        print("Strong")
        
    elif compare == 2:
        print("Medium")
        
    elif compare==1:
        print("Weak")
        
    else:
        print("Very Weak")

    confirm(password1)
    
def confirm(password1):
    password2=input("Enter confirm password: ")
    if password1==password2:
        print(f"{password1} password has ben set")
    else:
        confirm(password1)

check_password(password1)
