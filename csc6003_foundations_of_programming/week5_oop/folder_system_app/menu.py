# importing dependencies
from typing import List
# This class displays the menu and returns the user menu selection
class Menu:
    def __init__(self):
        self.__menu_options = [
            "1) add File",
            "2) add Folder",
            "3) select Folder",
            "4) print Folder",
            "5) count files",
            "6) exit"
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
    def display_menu(self, current_folder: bool = False) -> int:
        # Printing menu header
        print("====MENU====")
        # If there is a current folder, display the current folder
        if current_folder:
            print(f"==current folder:{current_folder}==")
        # Show Menu
        print(*self.__menu_options, sep="\n")

        # Get menu input
        menu_input = self.get_menu_number_input("Choose a menu item to continue", self.__menu_options)

        return menu_input
        
