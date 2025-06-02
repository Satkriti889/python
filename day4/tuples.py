""" Display value at particular index of a tuple, if tuple is empty say tuple is empty
* Use count() to display number of occurrences of an element
* Use index() to find first index occurrence of an element"""

def take_input():
        t=[]
        n = int(input("Enter the number of elements in the tuple  you want to add: "))
        for _ in range(0,n):
            add_tuple=int(input("Enter the tuple  you want to add : "))
            t.append(add_tuple)
        print("t",t)
        tup = tuple(t)
    
    
        return(tup)


    
   
def count_element(t,elm):
    print(t.count(elm))
    return t.count(elm) 

def show_element_index(t,elm):
    try:

        return t.index(elm)

        
    except:
        print(" element not present in tuple : ")
        



def main():
     while True:
        print("Enter \n1 to add elements \n2 to see the element of the index  \n3 to see the index of the element  \n4 to quit")
        choose=int(input())
        
        if choose in range(1,5):  
            if choose==1:
                t=take_input()
            elif choose==2:
                elm = int(input("Enter an element to display count of: "))
                print(t)
                print(f"The count of {elm} in tuple is {count_element(t,elm)}")

            elif choose==3:
                elm = int(input("Enter an element to display index  of: "))
                print(f"The index of {elm} in tuple is {show_element_index(t,elm)}")
                
            else:
                break
        else:
            print("Invalid input please try again")
            return main()
main()
     


    
    
