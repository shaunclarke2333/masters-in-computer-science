# This is the creature class
class Creature:
    # This runs when you create a new creature
    def __init__(self, name: str):
        # creature name
        self.name = name
        # left child
        self.left = None 
        # right child
        self.right = None  

    # Dunder method to print name when class is printed
    def __str__(self):
        # returning object/creature name
        return self.name
