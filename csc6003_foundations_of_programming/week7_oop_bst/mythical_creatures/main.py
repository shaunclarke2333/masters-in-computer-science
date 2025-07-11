# importing dependencies
from tree import CreatureTree

# This function prints the menu options
def display_menu(root_exists):
    print("\n=== Menu ===")
    # If no root has been added yet, only show menu to add root
    if not root_exists:
        print("0) Add Root Creature")
    else:
        # Show main menu after root is created
        print("1) Add Creature")
        print("2) Print All")
        print("3) Print Specific")
        print("4) Exit")
        

# This is the main function that runs the program
def main():
    # Create a new creature tree object
    tree = CreatureTree()  
    while True:
        try:
            # if root exists show the menu by allowing tree.root to pass in True
            display_menu(tree.root is not None)

            # Get user input
            choice: str = input(">>input: ").strip()
            # if option 0 is selected Add the root creature once
            if choice == "0" and tree.root is None:
                # get users input
                name = input(">>input Name: ").strip().title()
                # Calling the add_root method
                print(tree.add_root(name))  
            # if the user selects option 1 Add a new creature under a parent node
            elif choice == "1":
                # printing menu header
                print("=== Creatures ===")
                # displaying the current tree
                tree.print_tree()
                # Get user input for parent name
                parent = input(">>input Node name: ").strip().title()
                # Get user input for left or right branch
                side = input(">>input L or R child: ").strip()
                # Get user input for child node
                child = input(">>input Name: ").strip().title()
                # calling add_creature to add the new creature
                print(tree.add_creature(parent, side, child))  

            # if the user selects option 2, Print the whole tree
            elif choice == "2":
                # printing header
                print("\n=== Creature Tree ===")
                # printing the whole tree
                tree.print_tree()
            # If the user selects option 3, Print ancestors of a specific creature
            elif choice == "3":
                # get user input 
                name = input(">>input Node name: ").strip().title()
                # printing the specific ancestor lineage as a sentence.
                print(tree.print_ancestors(name))
            # If the user selects option 4, Exit the program
            elif choice == "4":
                # dueces
                print("Goodbye.")
                break
            # If the user enters a menu option tha t doesnt exist
            else:
                raise ValueError("Invalid selection.")
        except ValueError as err:
            print(err)

# This ensures the main function only runs if the file is executed directly
if __name__ == "__main__":
    main()

