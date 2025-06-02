""""Sum Until Zero

Create a function that repeatedly asks the user for a number.
Keep a running total.
Stop when the user enters 0 and then return the sum.
"""

def number():
    numbers=[]
    number=int(input("enter the number"))
    sum=0
    while number!=0:
    
        numbers.append(number)
        number=int(input("enter the number"))
    if number==0:
        global total
        for i in numbers:
            sum+=i
            
        
    return sum

summ=number()

print(summ)
   

