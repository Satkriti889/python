import random
secret= random.randint(1,30)
guess_number=int(input("enter the number:"))
attempt=1

while guess_number!=secret:

    if guess_number>secret:
        print("the guessed number is  high")

    else:
        print("the guessed number is  low")
    
    guess_number=int(input("enter the number"))
    attempt+=1

if guess_number==secret:
    print(f"you have guessed the correct number i.e {secret} at {attempt} attempt")
    print(secret)