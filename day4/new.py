def create_tuple():
    a = []
    n = int(input("Enter number of elements in a tuple: "))
    for i in range(n):
        b = int(input(f"Enter element for index {i} for the tuple: "))
        a.append(b)

    return tuple(a)

def count_elements(t, elm):
    return t.count(elm)

def index_element(t, elm):
    try:
        return f"Element {elm} present at index {t.index(elm)}"
    
    except:
        return "Element not present in tuple"
    
while True:
    print("Enter 1 to create a tuple")
    print("Enter 2 to display tuple")
    print("Enter 3 to display count of an element")
    print("Enter 4 to display index of an element")
    print("Enter 5 to exit")
    print()

    choice = int(input("Enter choice: "))

    if choice == 1:
        t = create_tuple()

    elif choice == 2:
        try:
            for i in t:
                print(i, end = " ")

            print()
            
        except:
            print("No tuple has been created.")
            print()

    elif choice == 3:
        elm = int(input("Enter an element to display count of: "))
        print(f"The count of {elm} in tuple is {count_elements(t, elm)}")

    elif choice == 4:
        elm = int(input("Enter an element to display index of: "))
        print(index_element(t, elm))

    elif choice == 5:
        print("Goodbye")
        break

    else:
        continue

    
    