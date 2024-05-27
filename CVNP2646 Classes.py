#CVNP 2646
#Caleb Bertrang
#Classes
#This code walks the user through creating a hero and fighting a randomly generated monster.
#Import needed modules
import random
from Characters import Char

#Creates a random list of Monster names and types that will generate the boss.
Monster_Names = ('Voldemort','Alduin','Saruman')
Monster_Types = ('Slime','Orc','Troll')


#Child class that specifies the hp and mana of the hero/monster. 
#If the user does not choose Barbarian or Wizard, their stats will default to the same as the Monster.
#The child class prints out all of the class attributes at the end.
class stats(Char):
    def __init__(character,type,name,hp,mana):
        super().__init__(type,name)
        if type == "Barbarian":
            character.hp = 200
            character.mana = 50

        elif type == "Wizard":
            character.hp = 100
            character.mana = 150
        
        else:
            character.hp = 150
            character.mana = 100
        print("\n" + name + " the " + type + " has " + str(character.hp) + " hp and " + str(character.mana) + " mana.")

#Initialize the hero and monster.
hero_name = input("Please enter in the name of your hero: ")
hero_type = input(("Please enter in the type of hero you want. If you enter 'Barbarian' or 'Wizard', your hero's stats will be affected. Otherwise, you will have the same stats as the monster: "))
Hero = stats(hero_type,hero_name,0,0)
Monster = stats(random.choice(Monster_Types),random.choice(Monster_Names),0,0)

#While loop that prompts the hero to attack the monster until either of their HP's is below or equal to 0.
while Monster.hp > 0 and Hero.hp > 0:
    print("1. Basic Attack")
    print("2. Spell Attack")
    print("3. Replenish HP")
    print("4. Replenish Mana")
    choice = input ("Enter in a number 1-4 to choose your next move: ")
    if choice == "1":
        Monster.hp -= 25
        print("The Monster has been hit for 25 damage!")
        print("The monster's health is " + str(Monster.hp))
    elif choice == "2":
        if Hero.mana >= 25:
            Monster.hp -= 50
            Hero.mana -= 25
            print("The monster has been hit for 50 damage!")
            print("The monster's health is " + str(Monster.hp))
            print("The hero's mana is now " + str(Hero.mana))
        else:
            print("You do not have enough mana!")
    elif choice == "3":
        Hero.hp += 50
        print("The Hero has been healed 50 points. The hero's new health is " + str(Hero.hp))
    elif choice == "4":
        Hero.mana += 25
        print("The Hero has replenished 25 points of mana. The hero's new mana is " + str(Hero.mana))
    else:
        print("That is not a valid option, your turn for attack has been lost.")
    Hero.hp -= 30
    print("The monster has damaged the hero for 30 points. The new hero health is " + str(Hero.hp))
    print("The monster's current health is " + str(Monster.hp) + ".\n")

#Compares the HP of monster and hero and determines a winner.
if Monster.hp > Hero.hp:
    print(Monster.name + " the " + Monster.type + " has outlasted the hero!\n")
else:
    print(Hero.name + " the " + Hero.type + " has outlasted the Monster!\n")
