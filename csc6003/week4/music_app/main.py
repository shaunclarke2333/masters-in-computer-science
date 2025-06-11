# Importing dependencies
from typing import Tuple
from typing import Dict
from typing import List
from typing import Union
from menu import UserMenu
from input_handler import UserInput


class Main:
    def __init__(self, user_input_object: object, user_menu_object: object):
        self.user_menu_object = user_menu_object
        self.user_input_object = user_input_object
        self.user_counter: int = 0
        self.current_user: object = None
        self.current_username: str = None


    # This function Gets menu number input
    def get_menu_number_input(self,input_message: str, num_of_menu_options: int) -> str:
        while True:
            try:
                # Getting user input
                user_input: int = int(input(f">\n{input_message}\n:>").lower().strip())
                if not user_input:
                    raise KeyError(f"Input cannot be empty.")
                # Using the length of the menu list to validate that menu input is within range
                if user_input >= 1 and user_input <= num_of_menu_options:
                    return user_input
                else:
                    print(f"\nOnly menu number options will be accepted\n")
            except ValueError:
                print("You must enter a menu number")
            except KeyError as err:
                print(err)

    # This method prints the menu
    def format_menu_display(self,menu_header: str, current_user: str, user_menu_object_method: object, username_header: str) -> Tuple[List,int]:
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
        menu_number_input: int = self.get_menu_number_input("Choose a menu item to continue", num_of_menu_options)
        # Findind the menu item that corresponds to the selected menu number by subtracting 1
        menu_list_item_index: int = menu_number_input - 1 # one was added when dynamically numbering menu options

        return menu, menu_list_item_index

    # This function prints a Lightsaber
    def print_lightsaber(self) -> None:
        blade = "    ||    "
        hilt = [
            "    ||    ",
            "   ||||   ",
            "    ||    ",
            "    ||    "
        ]

        # Blade
        for _ in range(6):
            print(f"\n{blade}", end='')

        # Hilt 
        for line in hilt:
            print(line)

    # This is the main function that runs the program
    def main(self):
        while True:
            try:
                menu_header: str = "\n|====Menu====|"
                username_header: str = f"Username: {self.current_username}\n"

                # Formatting, displaying the Main menu and getting the Main menu input
                menu,menu_list_item_index = self.format_menu_display(menu_header,self.current_user,self.user_menu_object.display_menu,username_header)
                
                # Logic to call the correct method that corresponds with the menu selection to handle user actions
                if "Add user" in menu[menu_list_item_index]:
                    # Create user
                    user: object = self.user_input_object.handle_add_user()
                    # Increment counter
                    self.user_counter += 1
                    if not self.current_user:
                        self.current_username: str = user.get_username()
                        self.current_user: object = user
                elif "Change User" in menu[menu_list_item_index]:
                    # Formatting, displaying the change user menu and getting the chnage user menu input
                    sub_menu,sub_menu_list_item_index = self.format_menu_display(menu_header,self.current_user,self.user_menu_object.display_sub_menu,username_header)

                    # Logic to call the correct method that corresponds with the menu selection to handle user actions
                    if "Add a user" in sub_menu[sub_menu_list_item_index]:
                        # Create user
                        user: object = self.user_input_object.handle_add_user()
                        # Increment counter
                        self.user_counter += 1
                        if not self.current_user:
                            self.current_username: str = user.get_username()
                            self.current_user: object = user
                    elif "Select a user" in sub_menu[sub_menu_list_item_index]:
                        # Formatting, displaying the select user menu and getting the select user menu input
                        user_select_menu_list,user_select_menu_list_index = self.format_menu_display(menu_header,self.current_user,self.user_menu_object.display_user_selection_menu,username_header)
                        # Checking which user was selected
                        for user in user_select_menu_list:
                            if user == user_select_menu_list[user_select_menu_list_index]:
                                # stripping away leading number and returning just username
                                username: str = user.split(") ")[1]
                                # Updating current user with selected user
                                self.current_user: object = self.user_input_object.handle_change_user(self.current_user, username)
                                # updating current username with selected user
                                self.current_username: str = self.current_user.get_username()
                elif "Add a song" in menu[menu_list_item_index]:
                    # Adding song to user library
                    song: str = self.user_input_object.handle_add_song(self.current_user)
                    print(song.title())        
                elif "Retrieve song details" in menu[menu_list_item_index]:
                    # Getting song details
                    song_details: Dict = self.user_input_object.handle_retrieve_song_details(self.current_user)
                    # Displaying song details
                    print(f"\n>Song Details<")
                    print(f'Artist: {song_details["artist"].title()}\nGenre: {song_details["genre"].title()}')
                elif "Update song details" in menu[menu_list_item_index]:
                    # Updating song in library
                    update_song: str = self.user_input_object.handle_update_song(self.current_user)
                    print(f"\n{update_song.title()}\n")
                elif "Delete a song" in menu[menu_list_item_index]:
                    # Deleting song from library
                    deleted_song: str = self.user_input_object.handle_delete_song(self.current_user)
                    print(deleted_song.title())
                elif "Display all songs" in menu[menu_list_item_index]:
                    # Getting all songs from library
                    get_all_songs: Union[Dict,str] = self.user_input_object.handle_display_all_songs(self.current_user)
                    # Checking is string or dict and format accordingly
                    if type(get_all_songs) != str:
                        for title,details in get_all_songs.items():
                            print(f'\nTitle: {title.title()}\nArtist: {details["artist"].title()}\nGenre: {details["genre"].title()}\n')
                    else:
                        print(f"\n{get_all_songs}\n")
                elif "Exit" in menu[menu_list_item_index]:
                    # Display easter egg
                    print(f"\nI find your lack of faith disturbing.")
                    print(f"You will be escorted to the edge of the galaxy.\n")
                    print(f"     <=o=>    <=o=>")
                    print(f"<=o=>    <=o=>\n")
                    exit()
            except KeyboardInterrupt as keyboardint:
                    # Gracefully handle keyboard interrupt and display easter egg.
                    self.print_lightsaber()
                    print(f"\nI am not your failure, Obi-Wan. You didn't kill Anakin Skywalker, I did\n")
                    exit()


run_program = Main(UserInput(),UserMenu()) 

if __name__ == "__main__":
    run_program.main()