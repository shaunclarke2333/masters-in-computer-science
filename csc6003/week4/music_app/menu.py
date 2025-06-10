# Importing dependencies
from typing import Optional
from typing import Tuple
from typing import Dict
from typing import List
from typing import Union
from user import User

# This class displays menu items based on the user and or music in the library
class UserMenu:
    def __init__(self):
        self.__menu_options = [ # This List holds the main menu options
            "Add user",
            "Change User",
            "Add a song",
            "Retrieve song details",
            "Update song details",
            "Delete a song",
            "Display all songs",
            "Exit"
        ]
        self.__sub_menu_options = [
            "Add a user",
            "Select a user",
            "Exit"
        ]
        
    # Checks if there is at least one user
    def __user_exists(self, user_object: Optional[User] = None) -> bool:
        if user_object is None:
            return False
        elif len(user_object.get_users()) > 0:
            return True
    
    # Checks if there are multiple users
    def __multiple_users_exist(self, user_object: Optional[User] = None) -> bool:
        all_users = user_object.get_users()
        
        if len(all_users) > 1:
            return True
        elif user_object is None:
            return False
        else:
            return False
        
    # CHecks if the library has any songs
    def __library_has_songs(self, user_object: Optional[User] = None) -> bool:
        if user_object is None:
            return False
        all_songs = len(user_object.get_music_collection())
        if all_songs > 0:
            return True
        else:
            return False
        
    # This method takes the List of selected menu input and dynamically assigns the numbering
    def __create_temp_menu(self, list_of_options: List) -> List:
        # Empty List to hold temp menu
        temp_menu = []
        # Dynamically assigning menu numbers and creating a new List
        for index, item in enumerate(list_of_options):
            index += 1
            menu_option_with_number = f"{index}) {item}"
            temp_menu.append(menu_option_with_number)
        
        return temp_menu
            
            
    # Displays the menu based on user and music library state
    def display_menu(self, user_object: Optional[User] = None) -> List[str]:
        if not self.__user_exists(user_object):
            # If no users exist return add user and exit menu options
            filtered_menu = [self.__menu_options[0], self.__menu_options[7]]
            temp_menu = self.__create_temp_menu(filtered_menu)
            return temp_menu
        # if multiple users exist and no songs in library
        elif self.__multiple_users_exist(user_object) and not self.__library_has_songs(user_object):
            filtered_menu = [self.__menu_options[0], self.__menu_options[1], self.__menu_options[2], self.__menu_options[7]]
            temp_menu = self.__create_temp_menu(filtered_menu)
            return temp_menu
        elif self.__user_exists(user_object) and not self.__library_has_songs(user_object):
            # If user exists and no songs return add user, add song and exit
            filtered_menu = [self.__menu_options[0], self.__menu_options[2], self.__menu_options[7]]
            temp_menu = self.__create_temp_menu(filtered_menu)
            return temp_menu
        # if multiple users exist and we have songs in library
        elif self.__multiple_users_exist(user_object) and self.__library_has_songs(user_object):
            filtered_menu = self.__menu_options.copy()
            temp_menu = self.__create_temp_menu(filtered_menu)
            return temp_menu
        elif self.__user_exists(user_object) and self.__library_has_songs(user_object):
            filtered_menu = self.__menu_options.copy()
            filtered_menu.pop(1)
            temp_menu = self.__create_temp_menu(filtered_menu)
            return temp_menu
       
    # Displays the chnage user submenu
    def display_sub_menu(self, user_object: User) -> List[str]:
        # If we have more than one user
        if len(user_object.get_users()) > 1:
            temp_sub_menu = self.__sub_menu_options.copy()
            temp_sub_menu = self.__create_temp_menu(temp_sub_menu)
            return temp_sub_menu
        else:
            return ["No other users exist", self.__sub_menu_options[0]]
        
    # Displays the sub menu based on user state and main menu selection
    def display_user_selection_menu(self, user_object: Optional[User] = None) -> List[str]:
        # List to hold user selection options.
        choose_user_list = []
        
        counter = 0
        # looping through user dict and getting username and user_object
        for username, user_object in user_object.get_users().items():
            # Incremeting the counter by one so it can be used as menu number
            counter += 1
            # Adding user option to choose user menu
            choose_user_list.append(f"{counter}) {username}")
        # Copying List to avoid returning original List
        copied_choose_user_list = choose_user_list.copy()
        copied_choose_user_list = self.__create_temp_menu(copied_choose_user_list)
        return copied_choose_user_list
    
