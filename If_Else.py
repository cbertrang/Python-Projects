#generate random integer values
from random import seed
from random import randint
#Adding Time module
import time 

Answer=randint(0,100)

print("Welcome to the Random Number Guessing Game, in 3 seconds, we will begin.")
time.sleep(3)
print(1)
time.sleep(1)
print(2)
time.sleep(1)
print(3)
time.sleep(1)
print("Please input your guess using a number from 0-100:\n")
Guess=input()
Guess = int(Guess)
Answer = int(Answer)

while (Guess!=Answer):
    if (Guess < Answer):
        print("Too low! Try again:\n")
        Guess=int(input())

    elif (Guess > Answer):
        print("Too high! Try again:\n")
        Guess=int(input())
    else:
        print("That is not a valid number, try again:\n")
        Guess=int(input())
         
print("Great Job, you got it!")