def takeinput():
    a=int(input("enter the number: "))
    return a

def reversing(a):
    numbers=[]
    while a>0:
        numbers.append(a) 
        num=str(a)
        new=[]
        for i in num:
            new.append(i)
            new.sort(reverse=True)
        z=""
        for j in new:
            u=str(j)
            z+=u
        print(z)
        break
    if a==0:
        print("Enter number above 0")
a=takeinput()
reversing(a)

