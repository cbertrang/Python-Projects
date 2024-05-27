#Tuple/List Loops
#CVNP 2646
#Caleb Bertrang

#Basketball three-point contest with 5 shots.

#Initialize the players, the scores, and the number of shots
players=[]

print("Get ready to start the basketball 3-point contest.\nEach competitor gets 5 shots. Whoever has the most points wins!\nFirst, we'll need the names of our players.")
players.append(input("Please enter in the name of the first player:"))
players.append(input("Please enter in the name of the second player:"))

print("Here are the competitors:" + str(players))
shots=[0,1,2,3,4]
score1=0
score2=0

#First for loop to shoot 5 shots for player 1
print("let's see how " + str(players[0]) + " does.")
print("Ready, start!\n")
for shots in shots:
    result=input("And the shot goes up! Was it a make or a miss? For a make, enter in 'make' and 'miss' if it was a miss:")
    if result.lower() == "make":
        score1=score1 + 3
    elif result.lower() == "miss":
        print("So close!\n")
    else:
        print("That is not a valid answer, you have lost one shot.\n")
    print("The current score for " + str(players[0]) + " is: " + str(score1) + "\n")

#Second for loop to shoot 5 shots for player 2    
shots=[0,1,2,3,4]
print("Now let's see how " + str(players[1]) + " does.")
print("Ready, start!\n")
for shots in shots:
    result=input("And the shot goes up! Was it a make or a miss? For a make, enter in 'make' and 'miss' if it was a miss:")
    if result.lower() == "make":
        score2=score2 + 3
    elif result.lower() == "miss":
        print("So close!\n")
    else:
        print("That is not a valid answer, you have lost one shot.\n")
    print("The current score for " + str(players[1]) + " is: " + str(score2) + "\n")

#Add updated scores to a new list. Compare the scores
scorelist=[]
scorelist.append(score1)
scorelist.append(score2)
if score1 > score2:
    print("And the winner is " + str(players[0]) + " with a score of " + str(max(scorelist)) + ".\n")
elif score2 > score1:
    print("And the winner is " + str(players[1]) + " with a score of " + str(max(scorelist)) + ".\n")
else:
    print("We have a tie! with an equal score of " + str(max(scorelist)) + ".\n")