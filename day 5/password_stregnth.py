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

    if has_upper==0:
        print("password should have atleast one uppercase.")
        check_password(user_input())
    elif has_lower==0:
        print("password should have atleast one lowercase.")
        check_password(user_input())
    elif has_number==0:
        print("password should have atleast one number.")
        check_password(user_input())

    elif has_char==0:
        print("password should have atleast one character.")
        check_password(user_input())

        
    main(has_upper,has_lower,has_number,has_char)


def main(has_upper,has_lower,has_number,has_char):

    compare = has_upper + has_lower + has_number + has_char

    if compare == 4:
        print("Very Strong")
        return 
    elif compare == 3:
        print("Strong")
        return
    elif compare == 2:
        print("Medium")
        return
    elif compare==1:
        print("Weak")
        return
    else:
        print("Very Weak")

check_password(password1)
