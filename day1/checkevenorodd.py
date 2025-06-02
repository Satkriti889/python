
def take_input():
    numbers=[]
    for i in range (10):
        user_input=int(input("enter the number"))
        numbers.append(user_input)
    return numbers
def check(numbers):
    even=0
    odd=0
    for j in numbers:
        if j%2==0:
            even+=1
        else:
            odd+=1
    print(f"{even}are even and{odd}are odd")

numbers=take_input()
check(numbers)


