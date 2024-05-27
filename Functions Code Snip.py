#CVNP2646
#Caleb Bertrang
#Functions-Code Snip

#Importing Time Module 
import time

#Initiliaze List
users=[]

#Define Function to add users to list.
def user_add(user):
    users.append(user)

#Defining a loop function to utilize the add user function to add users to the list.
def user_loop():
    while True:
        answer = input("Would you like to add a name to the list? Enter in 'y' or 'Y' to add them: ")
        if answer.lower() == 'y':
            response = input("Please enter in a name to add to the list.\n")
            user_add(response)
        else:
            break
#Calls the loop function
user_loop()
print("Here is the list of added users: ")

#Utilizing the imported module.
time.sleep(3)
print(users)
 