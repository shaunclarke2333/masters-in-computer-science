# importing dependencies
from typing import List
from animal import Bear
from animal import Elephant
from animal import Penguin
from animal import Animal
from inputs import HandleInput
# This class handles display runs the program
class Main:
    def __init__(self, bear_class: Bear, elephant_class: Elephant, penguin_class: Penguin, input_object: HandleInput) -> None:
        self.bear_class = bear_class
        self.elephant_class = elephant_class
        self.penguin_class = penguin_class
        self.handle_input = input_object()
        # Variable to hold an animal object that will be used to access animals dict later
        self.an_animal = None
        self.__menu_options: List = [
            "1) add animals",
            "2) print all",
            "3) print specific",
            "4) End Program"
        ]
        self.__add_animal_menu: List = [
            "1) add bear",
            "2) add elephant",
            "3) add penguin"
        ]
        self.__print_specific_menu: List = [
            "1) print bear",
            "2) print elephant",
            "3) print penguin"
        ]

    # This function Gets menu number input
    def get_menu_number_input(self,input_message: str, menu_options: List) -> str:
        while True:
            try:
                # Getting user input
                user_input: int = int(input(f">\n{input_message}\n:>").strip())
                # Making sure input is not empty
                if not user_input:
                    raise KeyError(f"Input cannot be empty.\n")
                # Using the length of the menu list to validate that menu input is within range
                if user_input >= 1 and user_input <= len(menu_options):
                    return user_input
                else:
                    print(f"\nOnly menu number options will be accepted\n")
            except ValueError:
                print("You must enter a menu number\n")
            except KeyError as err:
                print(err)    

    # This method displays the menu and returns the selection
    def display_menu(self, menu: List) -> int:
        # Menu footer border
        footer_border = "================"
        # Printing menu header
        print("====Zoo MENU====")
        # Show Menu
        print(*menu, sep="\n")
        # adding border below menu
        print(footer_border)

        # Get menu input
        menu_input = self.get_menu_number_input("Choose a menu item to continue", menu)

        return menu_input
    # This method calls the program
    def main(self):
        

        while True:
            try:
                #Displaying main menu and getting user selection
                menu_selection: int = self.display_menu(self.__menu_options)
                # CHecking if we need to display a sub menu
                if menu_selection == 1:
                    # displaying add animals sub menu
                    menu_selection: int = self.display_menu(self.__add_animal_menu)
                    # checking return
                    if menu_selection == 1: # add bear
                        # adding bear
                        animal_added = self.handle_input.handle_add_bear(self.bear_class)
                        # if animal was added make it active animal
                        if animal_added:
                            self.an_animal = animal_added
                            print(f"{self.an_animal.name} was added")
                    elif menu_selection == 2: # add elephant
                        # adding elephant
                        animal_added = self.handle_input.handle_add_elephant(self.elephant_class)
                        # if animal was added make it active animal
                        if animal_added:
                            self.an_animal = animal_added
                            print(f"{self.an_animal.name} was added")
                    elif menu_selection == 3: # add penguin
                        # adding penguin
                        animal_added = self.handle_input.handle_add_penguin(self.penguin_class)
                        # if animal was added make it active animal
                        if animal_added:
                            self.an_animal = animal_added
                            print(f"{self.an_animal.name} was added")
                elif menu_selection == 2:
                    # If no animals exist
                    if self.an_animal is None:
                        print(f"\nYou must add an animal before you can use this option.\n")
                        continue
                    
                    # If we have animals
                    for key, animal in self.an_animal.get_all_animals().items():
                        print(f"\n{animal}\n")
                elif menu_selection == 3:
                    # displaying add animals sub menu
                    menu_selection: int = self.display_menu(self.__print_specific_menu)
                    # checking return
                    if menu_selection == 1: # print bear
                        # Getting animal
                        if self.an_animal == None:
                            print(f"\nYou must add an animal before you can use this option.\n")
                            continue
                            
                        # get menu string from list
                        animal_type = self.__print_specific_menu[0]
                        # slicing the animal from string
                        animal_type = animal_type.split()[-1]
                        # get bear
                        animal = self.an_animal.select_animal(animal_type)
                        # making sure specific animal exists
                        if animal:
                            # display animal
                            print(f"\n{animal}\n") 
                        else:
                            print(f"\nanimal not found\n") 
                            continue
                    elif menu_selection == 2: # print elephant
                        # Getting animal
                        if self.an_animal == None:
                            print(f"\nYou must add an animal before you can use this option.\n")
                            continue
                            
                        # get menu string from list
                        animal_type = self.__print_specific_menu[1]
                        # slicing the animal from string
                        animal_type = animal_type.split()[-1].strip()
                        # get elephant
                        animal = self.an_animal.select_animal(animal_type)
                        # making sure specific animal exists
                        if animal:
                            # display animal
                            print(f"\n{animal}\n") 
                        else:
                            print(f"\nanimal not found\n") 
                            continue
                    elif menu_selection == 3: # print penguin
                        # Getting animal
                        if self.an_animal == None:
                            print(f"\nYou must add an animal before you can use this option.\n")
                            continue
                            
                        # get menu string from list
                        animal_type = self.__print_specific_menu[2]
                        # slicing the animal from string
                        animal_type = animal_type.split()[-1].strip()
                        # get penguin
                        animal = self.an_animal.select_animal(animal_type)
                        # making sure specific animal exists
                        if animal:
                            # display animal
                            print(f"\n{animal}\n") 
                        else:
                            print(f"\nanimal not found\n") 
                            continue
                elif menu_selection == 4:
                    raise SystemExit(F"Bye Now.")

            except SystemExit as err:
                print(err)
                exit()
            except KeyboardInterrupt:
                print("\nLove Peace and Hair Grease")
                exit()


               

# Create the main object
run_program = Main(Bear,Elephant,Penguin,HandleInput)
# Call the main method to run the program.       
run_program.main()
