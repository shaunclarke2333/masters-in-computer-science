# Importing dependencies
from typing import Optional
from typing import Tuple
from typing import Dict
from typing import List
from typing import Union
from user import MusicUser
from menu import UserMenu
from input_handler import UserInput



# Get menu number input
def get_menu_number_input(input_message: str, num_of_menu_options: int) -> str:
    while True:
        try:
            user_input: int = int(input(f">\n{input_message}\n:>").lower().strip())
            if not user_input:
                raise KeyError(f"Input cannot be empty.")
            if user_input >= 1 and user_input <= num_of_menu_options:
                return user_input
            else:
                print(f"\nOnly menu number options will be accepted\n")
        except ValueError:
            print("You must enter a menu number")
        except KeyError as err:
            print(err)

# This method prints the menu
def format_menu_display(menu_header: str, current_user: str, user_menu_object_method: object, username_header: str) -> Tuple[List,int]:
    """
    This function formats, displays the  menu and get the menu input
    """
    # Dynamically getting menu options
    menu: list = user_menu_object_method(current_user)
    # Getting number of items in list
    num_of_menu_options: int = len(menu)

    #Printing menu header
    print(menu_header)
    # logic to print username if they exist or selected
    if current_user:
        print(username_header)
    # Displaying the menu items
    print('\n' .join(menu))

    # getting the menu selection 
    menu_number_input: int = get_menu_number_input("Choose a menu item to continue", num_of_menu_options)
    # Findind the menu item that corresponds to the selected menu number by subtracting 1
    menu_list_item_index: int = menu_number_input - 1 # one was added when dynamically numbering menu options

    return menu, menu_list_item_index


# This is the main function that runs the program
def main():
    user_menu_object: object = UserMenu()
    user_input_object: object = UserInput()
    user_counter: int = 0
    current_user: str = None
    current_username: str = None

    while True:
        menu_header: str = "\n|====Menu====|"
        username_header: str = f"Username: {current_username}\n"

        # Formatting, displaying the Main menu and getting the Main menu input
        menu,menu_list_item_index = format_menu_display(menu_header,current_user,user_menu_object.display_menu,username_header)
        
        # Logic to call the correct method that corresponds with the menu selection to handle user actions
        if "Add user" in menu[menu_list_item_index]:
            # Create user
            user = user_input_object.handle_add_user()
            # Increment counter
            user_counter += 1
            if not current_user:
                current_username = user.get_username()
                current_user = user
        elif "Change User" in menu[menu_list_item_index]:
            # Formatting, displaying the change user menu and getting the chnage user menu input
            sub_menu,sub_menu_list_item_index = format_menu_display(menu_header,current_user,user_menu_object.display_sub_menu,username_header)

            # Logic to call the correct method that corresponds with the menu selection to handle user actions
            if "Add a user" in sub_menu[sub_menu_list_item_index]:
                 # Create user
                user: object = user_input_object.handle_add_user()
                # Increment counter
                user_counter += 1
                if not current_user:
                    current_username: str = user.get_username()
                    current_user: object = user
            elif "Select a user" in sub_menu[sub_menu_list_item_index]:
                # Formatting, displaying the select user menu and getting the select user menu input
                user_select_menu_list,user_select_menu_list_index = format_menu_display(menu_header,current_user,user_menu_object.display_user_selection_menu,username_header)
                # Checking which user was selected
                for user in user_select_menu_list:
                    if user == user_select_menu_list[user_select_menu_list_index]:
                        # stripping away leading number and returning just username
                        username: str = user.split(") ")[1]
                        # Updating current user with selected user
                        current_user: object = user_input_object.handle_change_user(current_user, username)
                        # updating current username with selected user
                        current_username: str = current_user.get_username()
        elif "Add a song" in menu[menu_list_item_index]:
            # Adding song to user library
            song: str = user_input_object.handle_add_song(current_user)
            print(song)        
        elif "Retrieve song details" in menu[menu_list_item_index]:
            # Getting song details
            song_details: Dict = user_input_object.handle_retrieve_song_details(current_user)
            # Displaying song details
            print(f"\n>Song Details<")
            print(f"Artist: {song_details["artist"]}\nGenre: {song_details["genre"]}")
        elif "Exit" in menu[menu_list_item_index]:
            print(f"\nI find your lack of faith disturbing.")
            print(f"You will be escorted to the edge of the galaxy.\n")
            print(f"     <=o=>    <=o=>")
            print(f"<=o=>    <=o=>")
            exit()


main()              
