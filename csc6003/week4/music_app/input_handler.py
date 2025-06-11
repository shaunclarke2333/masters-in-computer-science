# Importing dependencies
from typing import Optional
from typing import Tuple
from typing import Dict
from typing import List
from typing import Union
from user import MusicUser


# This class handles user input validation and returns
class UserInput:
        
    # Gets user input
    def get_input(self, input_message: str) -> str:
        while True:
            try:
                user_input: str = input(f"{input_message}\n:>").lower().strip()
                if not user_input:
                    raise ValueError(f"Input cannot be empty.")
                return user_input
            except ValueError as err:
                print(err)
                
    # Gets input and creates a new user
    def handle_add_user(self) -> object:
        # Validating first name input
        first_name: str = self.get_input("\nEnter user's first name")
        # Validating last name input
        last_name: str = self.get_input("\nEnter user's last name")
        # Creating a new user
        new_user: object = MusicUser(first_name, last_name)
        return new_user
    
    # Seclects a different user
    def handle_change_user(self, user_object: MusicUser, username: str) -> MusicUser:
        # username: str = self.get_input("")
        selected_user: object = user_object.change_user(username)
        return selected_user
    
    # Gets input and add a song to the library
    def handle_add_song(self, user_object: MusicUser) -> str:
        while True:
            try:
                # Validating title input
                title: str = self.get_input("\nEnter song title")
                # Validating artist input
                artist: str = self.get_input("\nEnter artist name")
                # Validating genre input
                genre: str = self.get_input("\nEnter genre")
                    
                # Adding song to music library
                new_music: str = user_object.add_music_to_library(title, artist, genre)
                # Validate song was added
                if new_music == "exists":
                    raise FileExistsError(f"Song already in Library") 
                
                if new_music == "song not added":
                    raise ValueError("Song could not be added to library")
                
                return new_music
            except FileExistsError as fileex:
                print(fileex)
                continue
            except ValueError as err:
                print(err)
                continue
            
    
    # Gets input and returns song details
    def handle_retrieve_song_details(self, user_object: MusicUser) -> Dict:
        # Validating title input
        while True:
            try:
                title: str = self.get_input("\nEnter song title you would like to see.")
                # Getting song details 
                song: Dict = user_object.retrieve_song_details(title)

                if song == "song not found":
                    raise KeyError(song)
                
                return song
            except KeyError as err:
                print(err)
                continue
    
    # Gets input and pass them to music user method to update son info
    def handle_update_song(self, user_object: MusicUser) -> str:
        # Validating title input
        while True:
            try:
                # Validating title input
                title: str = self.get_input("\nEnter song title you would like to update")
                # If song is not in library
                if not user_object.is_song_in_library(title):
                    raise KeyError(f"\nsong not found")
                
                # Validating artist input
                artist: str = self.get_input("\nEnter new artist name")
                # Validating genre input
                genre: str = self.get_input("\nEnter new genre")
                # Updating artist name in library
                update_song = user_object.update_song_details(title, artist, genre)
                
                # Making sure user doesnt continue until song is updated.
                if update_song == "details not updated":
                    raise RuntimeError("details not updated")
                
                return update_song
            except KeyError as err:
                print(err)
            except RuntimeError as runtime:
                print(runtime)
            
    # 
    def handle_delete_song(self, user_object: MusicUser) -> str:
        while True:
            try:
                # Validating title input
                title : str = self.get_input("\nEnter the title of the song you want to delete")
                # If song is not in library
                if not user_object.is_song_in_library(title):
                    raise KeyError(f"\nsong not found")
                # Deleting song
                deleted_song: str = user_object.delete_song(title)
                # Making sure user doesnt continue if song was not deleted.
                if deleted_song == "song not deleted":
                    raise RuntimeError("song not deleted")
                
                return deleted_song
            except KeyError as err:
                print(err)
            except RuntimeError as runtime:
                print(runtime)
            
    def handle_display_all_songs(self, user_object: MusicUser) -> Union[Dict,str]:
        # Returning the dictionary with all the users songs.
        return user_object.get_music_collection()
     

