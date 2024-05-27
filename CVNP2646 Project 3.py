#CVNP 2646
#Caleb Bertrang
#Python Project 3 JSON 
#Importing json module
import json

#Loading json file to be viewable in the python script
filename = "Text.json"
with open(filename) as file:
    CustomerInfo = json.load(file)

#Asks the user to enter in the ID number of an employee they would like to see the info for.
search = input("Please enter in the ID number of the employee you would like more info about(0-5): ")

#While loop that validates the requested ID. User is prompted to input an ID again if they do not choose a number 0-5.
while True:
    if search == "0":
        print("The customer's name is " + CustomerInfo["Customers"][0]["name"])
        print("The customer's street address is " + CustomerInfo["Customers"][0]["street address"])
        print("The customer's city is " + CustomerInfo["Customers"][0]["city"])
        print("The customer's age is " + CustomerInfo["Customers"][0]["age"] + "\n")
        break
    elif search == "1":
        print("The customer's name is " + CustomerInfo["Customers"][1]["name"])
        print("The customer's street address is " + CustomerInfo["Customers"][1]["street address"])
        print("The customer's city is " + CustomerInfo["Customers"][1]["city"])
        print("The customer's age is " + CustomerInfo["Customers"][1]["age"] + "\n")
        break
    elif search == "2":
        print("The customer's name is " + CustomerInfo["Customers"][2]["name"])
        print("The customer's street address is " + CustomerInfo["Customers"][2]["street address"])
        print("The customer's city is " + CustomerInfo["Customers"][2]["city"])
        print("The customer's age is " + CustomerInfo["Customers"][2]["age"] + "\n")
        break
    elif search == "3":
        print("The customer's name is " + CustomerInfo["Customers"][3]["name"])
        print("The customer's street address is " + CustomerInfo["Customers"][3]["street address"])
        print("The customer's city is " + CustomerInfo["Customers"][3]["city"])
        print("The customer's age is " + CustomerInfo["Customers"][3]["age"] + "\n")
        break
    elif search == "4":
        print("The customer's name is " + CustomerInfo["Customers"][4]["name"])
        print("The customer's street address is " + CustomerInfo["Customers"][4]["street address"])
        print("The customer's city is " + CustomerInfo["Customers"][4]["city"])
        print("The customer's age is " + CustomerInfo["Customers"][4]["age"] + "\n")
        break
    elif search == "5":
        print("The customer's name is " + CustomerInfo["Customers"][5]["name"])
        print("The customer's street address is " + CustomerInfo["Customers"][5]["street address"])
        print("The customer's city is " + CustomerInfo["Customers"][5]["city"])
        print("The customer's age is " + CustomerInfo["Customers"][5]["age"] + "\n")
        break
    else:
        print("That is not a valid ID, please try again.")
        search = input("Please enter in the ID number of the employee you would like more info about(0-5): ")

#Additional input prompt where the user is asked if they would like to view 1 piece of info one more time about the employee.
answer = input("If you would like to view only 1 piece of info about the employee chosen, please enter in 'name', 'street address', 'city', or 'age': ")
if answer == "name" or answer == "street address" or answer == "city" or answer == "age":
    print(CustomerInfo["Customers"][int(search)][answer])
else:
    exit()