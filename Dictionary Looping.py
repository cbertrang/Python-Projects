#Dictionary Looping with hashing 
#CVNP 2646
#Caleb Bertrang


#initialize the dictionary.
dict = {}
print("For this program, we will be asking for a password to hash, then returning the hashed password that is requested from our dictionary.\n")
answer = input("Would like to add some passwords to the dictionary? Please enter in 'y' or 'Y'. ")

#Add values to the dictionary.
while answer.lower() == "y":
    password = input("What password would you like to add to the hashing dictionary? ")
    dict_hash = hash(password)
    dict[password] = dict_hash
    answer = input("Would you like to add another password? Please enter in 'y' or 'Y'. ")

print("Now we will search the dictionary for the requested passwords and display the hash.\n")

#Loops through the number of items in the dictionary, and then prompts to display the hash of a requested password.
for key, value in dict.items():
    search_key=input("What password would you like to view the hash of? ")
    print(dict.get(search_key, "Password is not present."))

#Prints the final contents of the dictionary.    
print("Here are the full contents of the dictionary: " + str(dict) + " .\n")    
