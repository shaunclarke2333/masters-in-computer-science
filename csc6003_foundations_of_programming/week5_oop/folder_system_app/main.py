# importing dependencies
from folder import Folder
from input_handler import HandleInput
from menu import Menu
import sys


# This class handles display runs the program
class Main:
    def __init__(self, folder_object: Folder, input_object: HandleInput, menu_object: Menu) -> None:
        self.folder_object = folder_object
        self.handle_input = input_object
        self.menu_object = menu_object
        self.root_folder: object = None
        self.active_folder: object = None
        self.active_folder_name: str = None

    # This method calls the program
    def main(self):
        # Create root folder
        self.root_folder = self.folder_object("root")
        self.active_folder = self.root_folder
        self.active_folder_name = self.active_folder.folder_name
        print(self.active_folder_name)

        while True:
            try:
                #Displaying menu and getting user selection
                menu_selection: int = self.menu_object.display_menu(self.active_folder_name)

                # Do folder action based on menu input
                if menu_selection == 1:
                    file = self.handle_input.handle_add_file_to_folder(self.active_folder)
                    print(file)
                # if option 2, ask the user to add a folder
                elif menu_selection == 2:
                    folder = self.handle_input.handle_add_folder(self.active_folder)
                    print(folder)
                # if option 3, ask user to select folder
                elif menu_selection == 3:
                    selected_folder = self.handle_input.handle_select_folder(self.root_folder)
                    self.active_folder = selected_folder
                    self.active_folder_name = self.active_folder.folder_name
                # if option 4, print folder structure
                elif menu_selection == 4:
                    self.handle_input.handle_print_folder(self.active_folder)
                # if option 5, count all files in all folders
                elif menu_selection == 5:
                    self.handle_input.handle_count_files(self.active_folder)
                # if option 6, exit program.
                elif menu_selection == 6:
                    raise SystemExit("Peace Out Home Slice")
            except SystemExit:
                exit()    

# Create the main object
run_program = Main(Folder,HandleInput(),Menu())
# Call the main method to run the program.       
run_program.main()
