# importing dependencies
from typing import List
from typing import Union

# This folder class represents a folder in a file system. It creates and modifies a folder.
class Folder:
    def __init__(self, folder_name: str):
        self.folder_name = folder_name
        self.files: List = []
        self.sub_folders: List = []
            
    # This methods returns true if two folders have the same name
    def __eq__(self, other_folder) -> bool:
        return self.folder_name == other_folder
            
        
    # This method checks if the folder exists
    def does_folder_exist(self, folder_name: str)-> bool:
        """
        This method uses the folder name to check if a folder exists
        """
        # Checking if folder exist
        for folder in self.sub_folders:
            if folder.folder_name == folder_name:
                return True
        return False
            
    # This method checks if the file exists in the folder
    def does_file_exist(self, file_name: str) -> bool:
        """
        This method uses file_name to check if it exists in the user folder.<br>
        Returns True or False.
        """
        # Checking if the file exists
        if file_name in self.files:
            return True
        else:
            return False 
        
    # This method adds a sub folder to a folder
    def add_folder(self, folder_name: str) -> str:
        """
        This method adds a folder object to the main folder.
        """
        # CHecking if folder exists
        if self.does_folder_exist(folder_name):
            return "folder exists"
        # acreating sub folder object
        creating_sub_folder = Folder(folder_name)
        # adding it to the sub folders list
        self.sub_folders.append(creating_sub_folder)
        # Chekcing if folder was added
        if self.does_folder_exist(folder_name):
            return "\nfolder added\n"
        return "folder not added"
    
    # This method gets a subfodler
    def select_folder(self, folder_name: str) -> object:
        #
        # Getting folder if it is in list
        for folder in self.sub_folders:
            # return folder if found in subfolder list
            if folder.folder_name == folder_name:
                return folder
            # Using recusrion to check sun folders of folders in list
            result =  folder.select_folder(folder_name)
            if result is not None:
                return result
        #If folder name is root folder return the root folder object
        if self.folder_name == "root":
            return self
        return None
                
    # This method adds a file to a folder
    def add_file_to_folder(self, file_name: str) -> Union[bool,str]:
        """
        This method adds the file to the folder by adding it to the folder class list.
        It
        """
        # checking if file exists in sub folder
        if self.does_file_exist(file_name):
            return "file exist"
        # File doesn't exist so adding it
        self.files.append(file_name)
        # Makin sure the file was added
        if self.does_file_exist(file_name):
            return True
        else:
            return False
    
    # This method counts all the files in the folder and sub fodlers
    def __count_files(self) ->int:
        count = len(self.files)
        for sub in self.sub_folders:
            count += sub.__count_files()  # Recursive call
        return count
    
    # calling __count_files when __len__ is called.
    def __len__(self) -> str:
        # calling cout files to count a files 
        return self.__count_files()

    # This methods outputs a visual tree layout of the folder structure
    def __tree_view(self, prefix=""):
        # a list with the tree connector added to the bigning of the folder name
        lines = [prefix + self.folder_name]
        # Loop through the lis tof files and add the tree separator to the name
        for i, f in enumerate(self.files):
            # adding file name under folder with indent
            lines.append(prefix + "├── " + f)
        # Loop through sub folder getting index and sub folder
        for i, sf in enumerate(self.sub_folders):
            # Checking if last sub folder
            is_last = (i == len(self.sub_folders) - 1)
            # use the correct connector based on if last sub fodler or not
            connector = "└── " if is_last else "├── "
            # Indentation prefix for sub_folder level
            sub_prefix = prefix + ("    " )
            #Using recursion here to get the tree string and add it to the lines while removign whiteapce.
            lines.append(prefix + connector + sf.__tree_view(sub_prefix).lstrip())
        return "\n".join(lines)
        
    # This method calls __tree_view to print a folder tree
    def __str__(self) -> str:
        return self.__tree_view() 
            
