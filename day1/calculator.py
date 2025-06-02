while True:
    x=int(input("Enter \n1.for addition \n 2.for subtraction\n 3.for multiplication \n 4.for division\n:"))
    if x>0 and x<5:
        num1=int(input("Enter first number :"))
        num2=int(input("Enter second number :"))

        if (x==1):
            
            sum=num1+num2
            print(sum)
        elif (x==2):
            
            sub=num1-num2
            print(sub)
        elif (x==3):
            
            multi=num1*num2
            print(multi)
        elif(x==4):
    
            division=num1//num2
            print(division)
        
        else:
            print("invalid number")
    else:
        print("enter the valid number between 1 to 4")

        break