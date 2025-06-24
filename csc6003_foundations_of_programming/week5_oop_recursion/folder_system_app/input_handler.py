# importing dependencies
from folder import Folder


# Handles getting user input and pass it to Folder class to retrieve details
class HandleInput:
    # Gets user input
    def get_input(self, input_message: str) -> str:
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
    
    # Gets input and create a sub fodler
    def handle_add_folder(self, folder_object: Folder) -> str:
        while True:
            try:
                # Validating sub folder name input
                sub_folder_name: str = self.get_input("Enter the name of the folder you want to add.")
                # Creating a new sub folder
                sub_folder: object = folder_object.add_folder(sub_folder_name)
                # Making sure no duplilcates
                if sub_folder == "folder exists":
                    raise KeyError(f"\nFolder already exists.\n")
                # making sure user tries again if folder wasnt added
                if sub_folder == "folder not added":
                    raise RuntimeError(f"\nfolder not added\n")
                return sub_folder
            except KeyError as err:
                print(err)
            except RuntimeError as err:
                print(err)
    
    # This method gets input and returns a folder object
    def handle_select_folder(self, folder_object: Folder) -> object:
        # Validating folder name input
        while True:
            try:
                folder_name: str = self.get_input("Enter the name of the folder you want select")
                # Getting folder object
                folder: object = folder_object.select_folder(folder_name)
                if folder is None:
                    raise KeyError(f"\nfolder was not found\n")
                return folder
            except KeyError as err:
                print(err)
                continue
    
    
    # This adds a file to a folder
    def handle_add_file_to_folder(self, folder_object: object) -> bool:
        # Validating folder name input
        while True:
            try:
                file_name: str = self.get_input("Enter the name of the file you want to add")
                # Making sure file does not exist
                if not folder_object.does_file_exist(file_name):
                    # Adding file to fodler
                    folder_object.add_file_to_folder(file_name)
                    # checking if file was added
                    if folder_object.does_file_exist(file_name):
                        return f"\nFile added to {folder_object.folder_name} folder\n"
                raise KeyError(f"\nfile already exists\n")
            except KeyError as err:
                print(err)
                continue
    
    # This method prints the active folder
    def handle_print_folder(self, folder_object: object) -> str:
        print(folder_object)

    # THis method counts all the files in folder and sub folders
    def handle_count_files(self, folder_object) -> str:
        count = len(folder_object)
        print(f"\n{folder_object.folder_name} folder contains {count} file{'s' if count != 1 else ''}\n")
        
        
