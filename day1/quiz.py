import random

def quiz():
    correct = 0
    incorrect=0
    questions = 0
    while questions<5:
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            answer = a * b

            user_answer = int(input(f"What is {a} x {b}? "))

            if user_answer == answer:
                print("Correct!")
                correct+=1
            else:
                print("incorrect")
                incorrect+=1
            questions+=1
    
    print(f"Correct answer {correct} and incorrect answers {incorrect}")
    
quiz()
