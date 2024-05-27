#CVNP 2646
#Caleb Bertrang
#Project 1
#Grocery List  Creation.

#Declare the Grocery list variable
groceries=[]
print("Let's get started creating our grocery list.")

#While loop to validate user input, and ask if the user would like to create a list.
while True:
    answer=input("Would you like to create a grocery list? Please enter y, or n: ")
    if answer == 'y':
        break
    elif answer == 'n':
        break
    else:
        print("That is not a valid answer, please try again.\n")
#While loop to add items to the grocerry cart that also includes further validation of user input.
while answer == "y":
    answer=input("Would you like to add an item to the list? Please enter in y, or n: ")
    if answer == 'y':
        groceries.append(input("Enter in the item to add to the list: "))
    elif answer == 'n':
        break
    else:
        print("That is not a valid answer, please try again.\n")
        answer = 'y'
#Prints out updated grocery list.        
print("Here is the list we have created: " + str(groceries))