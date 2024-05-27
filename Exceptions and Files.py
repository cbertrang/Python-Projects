#CVNP 2646
#Caleb Bertrang
#Files and Exceptions
#Game show that the contestant always wins as long as they correctly select one of the 3 doors.
#Initializes the prizes the user can win.
with open("Prize1.txt") as prize1:
    door1 = prize1.read()
with open("Prize2.txt") as prize2:
    door2 = prize2.read()
with open("Prize3.txt") as prize3:
    door3 = prize3.read()

door = input("Welcome to the show! To win a prize, please enter in '1', '2', or '3' to pick one of the prizes: ")

#Tests if the input is an integer. If the answer is not an integer, quits the program.
try:
   int(door)
except:
    print("You did not enter in an integer, so you have lost the game. Try again.")
    quit()


if int(door) == 1:
    print("Your prize is " + door1)
elif int(door) == 2:
    print("Your prize is " + door2)
elif int(door) == 3:
    print("Your prize is " + door3)
else:
    print("That was not a valid answer. Try again.")


