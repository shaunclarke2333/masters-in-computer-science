# importing dependencies
from animal import Bear
from animal import Elephant
from animal import Penguin
from animal import Animal
# Handles getting user input and pass it to Folder class to retrieve details
class HandleInput:
    
    # Gets user string input
    def get_string_input(self, input_message: str) -> str:
        """
        This method gets the user input and makes sure it is not empty
        """
        while True:
            try:
                user_input: str = input(f"{input_message}\n:>").lower().strip()
                if not user_input:
                    raise ValueError(f"Input cannot be empty.")
                return user_input
            except ValueError as err:
                print(err)
                
    # Gets user number input
    def get_number_input(self, input_message: str) -> str:
        """
        This method gets the user input and makes sure it is not empty
        """
        while True:
            try:
                user_input: float = float(input(f"{input_message}: ").strip())
                # If input didnt trigger value error and 
                if user_input == int(user_input):
                    return user_input
                else:
                    return user_input
            except ValueError:
                print("\nPlease try again\n")
    
    # Gets input and create a bear
    def handle_add_bear(self, bear_class: Bear) -> object:
        # Validating input for name, species and fur color
        name: str = self.get_string_input("Enter the bear's name.")
        species: str = self.get_string_input("Enter the specie of bear.")
        fur_color: str = self.get_string_input("Enter the bear's fur color")
        # Creating a new bear
        create_animal: Bear = bear_class(name, species, "bear", fur_color)
        return create_animal
            
    # Gets input and create an elephant
    def handle_add_elephant(self, elephant_class: Elephant) -> object:
        # Validating input for name, species and weight
        name: str = self.get_string_input("Enter the elephant's name.")
        species: str = self.get_string_input("Enter the specie of elephant.")
        weight: float = self.get_number_input("Enter the elephant's weight.")
        # Creating a new elephant
        create_animal: Elephant = elephant_class(name, species, "elephant", weight)
        return create_animal
    
    # Gets input and create an penguin
    def handle_add_penguin(self, penguin_class: Penguin) -> object:
        # Validating input for name, species and fur color
        name: str = self.get_string_input("Enter the penguin's name.")
        species: str = self.get_string_input("Enter the specie of penguin.")
        height: float = self.get_number_input("Enter the penguin's height(in ft).")
        # Creating a new bear
        create_animal: Penguin = penguin_class(name, species, "penguin", height)
        return create_animal
    
    # This method gets input and returns an animal object
    def handle_select_animal(self, an_animal: Animal, animal_type: str) -> object:
        try:
            # Getting animal object
            animal: object = an_animal.select_animal(animal_type)
            if animal is None:
                raise KeyError(f"\nanimal was not found\n")
            return animal
        except KeyError as err:
            print(err)

