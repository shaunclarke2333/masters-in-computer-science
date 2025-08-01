# importing dependencies
from typing import Dict

# Animal parent class
class Animal:
    # Dictionary to hold animals
    __zoo_keeper: Dict = {}
        
    def __init__(self, name: str, species: str,  animal: str):
        self.name = name
        self.species = species
        self.animal = animal
        self.__add_animal()

    # Adding animal to zoo keepr dict
    def __add_animal(self):
        """
        This method adds the animal to the zoo dict.<br>
        Using the animal's name as the key.
        """
        # adding animal to dict
        self.__class__.__zoo_keeper[self.name] = self

    # This method allows us to select an animal from the zoo dict
    def select_animal(self, animal: str) -> object:
        """
        This method allows us to select an animal from the zoo dict.
        """
        for name, zoo_object in self.__class__.__zoo_keeper.items():
            if zoo_object.animal == animal:
                return zoo_object
            
        return False

    
    # This method returns the animals sound
    def make_sound(self) -> str:
        return "booooooo"
    # This method returns the animal info formatted
    def info(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Species: {self.species}\n"
            f"Sound: {self.make_sound()}\n"
            f""
        )
    
    def get_all_animals(self) -> Dict:
        return self.__class__.__zoo_keeper
    
    # This dunder method displays the animal info formatted
    def __str__(self) -> str:
        return self.info()
    
# Bear subclass
class Bear(Animal):
    """
    This Bear class is a subclass of Animal and inherits from it.<br>
    The info and make_sound methods are overwritten in this sub class
    """
    def __init__(self, name: str, species: str, animal: str, fur_color: str):
        super().__init__(name, species, animal)
        self.fur_color: str = fur_color
    
    # Overriding the make_sound method to include this naimals unique sound
    def make_sound(self) -> str:
        return "roar"
    
    # This method returns the animal info formatted
    def info(self) -> str:
        # overriding info method to include new attributes
        return "".join([
            f"{self.name} is a {self.animal} ",
            f"of the {self.species} species, ",
            f"who makes a {self.make_sound()} sound ",
            f"and has {self.fur_color} fur"
        ]) 

# Elephant subclass
class Elephant(Animal):
    def __init__(self, name: str, species: str, animal: str, weight: float):
        super().__init__(name, species, animal)
        self.weight = weight
     
    # Overriding the make_sound method to include this naimals unique sound
    def make_sound(self) -> str:
        return "trumpet"
    
    # This method returns the animal info formatted
    def info(self) -> str:
        # overriding info method to include new attributes
        return "".join([
            f"{self.name} is a {self.animal} ",
            f"of the {self.species} species ",
            f"who makes a {self.make_sound()} sound ",
            f"and weighs {self.weight}lbs"
        ])

# Penguin subclass
class Penguin(Animal):
    def __init__(self, name: str, species: str, animal: str, height: float):
        super().__init__(name, species,animal)
        self.height: str = height
    
    # Overriding the make_sound method to include this naimals unique sound      
    def make_sound(self) -> str:
        return "squawk"
    
    # This method returns the animal info formatted
    def info(self) -> str:
        # overriding info method to include new attributes
        return "".join([
            f"{self.name} is a {self.animal} ",
            f"of the {self.species} species ",
            f"who makes a {self.make_sound()} sound ",
            f"and stands at a height of {self.height}ft"
        ]) 
