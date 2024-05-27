#Class module to import to main Classes script
#Parent class for defining the hero and monster names/types.
class Char:
    def __init__(character,type,name):
        character.type = type
        character.name = name