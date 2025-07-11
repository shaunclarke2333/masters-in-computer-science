# Importing dependencies
from typing import Dict
from typing import List
from typing import Union


# This PARENT class creates a new user, and holds their music collection
class User:
    # Making the users class variable Dict private.
    __users: Dict = {}
    
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = (last_name+first_name[0]).lower() # Using last name and first initial for username
        self.manage_duplicate_name_range = [x  for x in range(1,100)]
        self.music_collection = {}
        self.register_user()



    # This method registers the user
    def register_user(self) -> None:
        """
        This method registers a user and makes sure they are no duplicate user names.
        """
        
        # Add username if it does not exist
        if self.username not in self.__class__.__users:
            self.__class__.__users[self.username] = self
            return 0
        # Checking for duplicates and modifying username
        for i in range(len(self.manage_duplicate_name_range)):
            duplicate_count = str(i+1)
            # Add digit to username
            self.username = self.username + duplicate_count
            # Checking if updated username exists
            if self.username not in self.__class__.__users:
                # Adding updated username
                self.__class__.__users[self.username] = self
                break

            
        
    # This method gets a user from the user dictionary
    def change_user(self, username: str) -> Union[object,str]:
        """
        This method gets a user from the user dictionary
        """
        try:
            return self.__class__.__users.get(username)
        except IndexError:
            return f"user not found"
    
    # This method returns the username 
    def get_username(self) -> str:
        """
        This method returns the username 
        """
        if not self.username:
            return 'user not found'
        return self.username
    
    # This method gets the music collection
    def get_music_collection(self) -> Dict:
        return self.music_collection
    
     # This method gets users
    def get_users(self) -> Dict:
        return self.__class__.__users


# This CHILD CLASS inherits the parent class USER and handles user actions
class MusicUser(User):
    def __init__(self,first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        
    # This method checks if library is empty and is only accessible from inside.
    def __is_collection_empty(self) -> bool:
        if  len(self.music_collection) == 0:
            return True
        else:
            return False
        
    # This method checks if a song already exists in the library and is only accessible from inside.
    def is_song_in_library(self, title: str) -> bool:
        if title in self.music_collection:
            return True
        else:
            return False
    
    # This method adds music to the collection
    def add_music_to_library(self, title: str, artist: str, genre: str) -> str:
        # Checking if the song already exists
        if self.is_song_in_library(title):
            return f"exists"
        # Adding song to library
        self.music_collection[title]={"artist": artist, "genre": genre}
        # Making sure song was added 
        if self.is_song_in_library(title):
            return f"{title} song added"
        else:
            return f"song not added"
    
    # This method retrieves the song details
    def retrieve_song_details(self, title: str) -> Union[Dict,str]:
        # Checking if song is in library
        if not self.is_song_in_library(title):
            return f"song not found"
        # Getting song details, artist and genre
        return self.music_collection[title]
        
    # This method updates a song's details in the user library
    def update_song_details(self, title, artist, genre) -> str:
        # Checking if song is in library
        if not self.is_song_in_library(title):
            return f"song not found"
        # Updating song details, artist and genre
        new_artist = self.music_collection[title]['artist'] = artist
        new_genre = self.music_collection[title]['genre'] = genre
        # Checking if details were updated
        if self.music_collection[title]['artist'] == new_artist and self.music_collection[title]['genre'] == new_genre:
            return "details updated"
        else:
            return "details not updated"
        
    # This method deletes song details
    def delete_song(self, title: str) -> str:
        # deleting song from music library
        if not self.is_song_in_library(title):
            return f"song not found"
        # Deleting song 
        del self.music_collection[title]
        # Making sure song was deleted 
        if not self.is_song_in_library(title):
            return f"song deleted"
        else:
            return f"song not deleted"
        
    # This method displays all songs in the users collections
    def display_all_songs(self) -> Union[str,Dict]:
        # Checking of library is empty
        if  self.__is_collection_empty():
            return f"library is empty"
        return self.music_collection
