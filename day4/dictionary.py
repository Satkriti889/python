d={}


    
def print_dict():
    print(d)

def key_of_dict():
    print(d.keys())

def view():
    print(d.items())




def add_values():
    add_key=input("Enter the key you want to add : ")

    add_value=input("Enter the values you want to add :  ")
    d[add_key]=add_value

def update_value():
    key=input("Enter the key you want to update : ")
    update_value=input("enter the value you want to update : ")
    d.update({key:update_value})
 
def delete_values():
    key=input("Enter the key you want to delete : ")
   
    d.pop(key)

def access():
    key=input("Enter the key you want to access : ")
    print (d.get(key),"\n")

def check():
    while True:
        print("Enter \n1 to add item \n2 to update the value for the given key \n3 to delete the item \n4 to access the given element \n 5 to view dictionary \n6 to quit")
        choose=int(input("= "))

        if choose in range(1,6):  
                if choose==1:
                    key_of_dict()
                    add_values()
                    print_dict()
                elif choose==2:
                    key_of_dict()
                    update_value()
                    print_dict()
                elif choose==3:
                    key_of_dict()
                    delete_values()
                    print_dict()
                elif choose==4:
                    key_of_dict()
                    access()
                elif choose==5:
                    view()
                else:
                    break
        else:
            print("Invalid input please try again")
            return check()
     
check()



