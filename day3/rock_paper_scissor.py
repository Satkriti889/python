"""Rock, Paper, Scissors Game
Write a function play_rps() that lets the user play against the computer.
Use a while loop to allow multiple rounds until the user chooses to quit.
Use random.choice(["rock", "paper", "scissors"]) for the computer's move."""

import random

def play_rps():
    quit=0
    while quit<1:
        c=random.randint(1,3)
        if c==1:
            computerplay="r"
        elif c==2:
            computerplay="p"
        else:
            computerplay="s" 
        p=input("enter q to quit or enter your play(R/P/S): ")
        p=p.lower()
        if p=="q":
            break
        
        elif p=="r" and computerplay=="r":
            print("It's a draw!")
        elif p=="r" and computerplay=="p":
            print("You lose!")
        elif p=="r" and computerplay=="s":
            print("You win!")
        elif p=="p" and computerplay=="p":
            print("It's a draw!")
        elif p=="p" and computerplay=="s":
            print("You lose!")
        elif p=="p" and computerplay=="r":
            print("You win!")
        elif p=="s" and computerplay=="s":
            print("It's a draw!")
        elif p=="s" and computerplay=="r":
            print("You lose!")
        elif p=="s" and computerplay=="p":
            print("You lose!")
        else:
            print("Please enter (P/R/S)")
        print("computer:",computerplay)
play_rps()