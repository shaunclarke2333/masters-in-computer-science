# import dependencies
from typing import List
from creature import Creature

# This class creates and prints the creature tree
class CreatureTree:
    def __init__(self):
        self.root = None
    # This method adds the root node
    def add_root(self, name: str) -> str:
        #if the root node exists
        if self.root is not None:
            return "Root already exists."
        # create the root node
        self.root = Creature(name)
        return f"{name} has been added as the root creature."
    
    # This method finds a specific node using recursion
    def find(self, node: Creature, name: str) -> object:
        # if the there is no creature object
        if node is None:
            return None
        # If the specific node is found, return it.
        if node.name == name:
            return node
        # recursively checking the left subtree if node was not found
        found_left = self.find(node.left, name)
        # if node was found return it
        if found_left is not None:
            return found_left
        else:
            # recursively checking the right subtree if node was not found on the left
            found_right = self.find(node.right, name)
            return found_right


    # This method adds q creature to a parent node using recursion
    def add_creature(self, parent_name: str, side: str, child_name: str) -> str:
        # finding the parent node
        parent = self.find(self.root, parent_name)
        # if parent node was not found
        if not parent:
            return f"{parent_name} not found in tree."
        # if the user entered L
        if side.lower() == "l":
            # if there is nothing at this location
            if parent.left is None:
                # add the specified creature at this location
                parent.left = Creature(child_name)
                return f"{child_name} added to the left of {parent_name}"
            else:
                # if there is a creature here use recursion to find the next empty left location
                parent.left.add_creature(parent_name, side, child_name)
                # if the user entered R
        elif side.lower() == "r":
            # if there is nothing at this location
            if parent.right is None:
                # add the specified creature at this location
                parent.right = Creature(child_name)
                return f"{child_name} added to the right of {parent_name}"
            else:
                # if there is a creature here use recursion to find the next empty right location
                parent.right.add_creature(parent_name, side, child_name)
        # If the user did not enter L or R let them know their input was incorrect.
        return "Invalid side. Use 'L' or 'R'."
    
    #  This method prints the tree structure
    def print_tree(self):
        # If the root node doesn't exist, let the user know
        if self.root is None:
            print("Tree is empty.")
            return

        # print level 1, the root node for the root of the tree
        print("         " + self.root.name)

        # print level 2 the cildren nodes 1 level down from root
        # if let or  right node exists add both or either to variable
        has_left: bool = self.root.left is not None
        has_right: bool = self.root.right is not None
        
        # logic to select the left or right node if they exist
        if has_left or has_right:
            # If the left node exists
            if has_left:
                #save it to the variable
                left: str = self.root.left.name
            else:
                # if left didnt exist leave it empty
                left = ""
            # If the right node exists
            if has_right:
                #save it to the variable
                right: str = self.root.right.name
            else:
                # if right didnt exist leave it empty
                right = ""

            # if there is a left node, print the connector
            if has_left:
                print("       /", end="")
            else:
                # if not fill the space so the tree is aligned
                print("        ", end="")  # align spacing
            # if there is a right node, print the connector
            if has_right:
                print("         \\")
            else:
                print()
            # Print the left and right node below the connectors
            print(f"   {left:<10}   {right}")

        # # print level 3 the children of level 2 left and right nodes
        left_left = ""
        left_right = ""
        right_left = ""
        right_right = ""
        # if there is a left node
        if self.root.left:
            # if there is a left node on the left node
            if self.root.left.left:
                # save the name to the variable for later
                left_left: str = self.root.left.left.name
            # if the left node has a right node
            if self.root.left.right:
                # save the name to the variable for later
                left_right: str = self.root.left.right.name
        # if there is a right node
        if self.root.right:
            # if there is a left node on the right node
            if self.root.right.left:
                # save the name to the variable for later
                right_left: str = self.root.right.left.name
            # if the right node has a right node
            if self.root.right.right:
                # save the name to the variable for later
                right_right: str = self.root.right.right.name
        # if any of the 3rd level grandchildren nodes exist
        if any([left_left, left_right, right_left, right_right]):
            print()
            # if its a left or right, left level 3 node
            if left_left or left_right:
                # print connectors
                print("  /", end="")
                print("     \\", end="  ")
            else:
                print("            ", end="")
            # if there is a right or left, right level 3 node 
            if right_left or right_right:
                print("    /", end="")
                print("     \\")
            else:
                print()
            # print the grandchildren nodes
            print(f"{left_left:<6} {left_right:<8} {right_left:<6} {right_right}")

    # again... using recursion to get the acenstors of a specific creature
    def get_ancestors(self, node: Creature, target: str, path: List) -> bool:
        # If the node doesn't exist return False
        if node is None:
            return False
        # If the current node's name matches the target name, creature was found
        if node.name == target:
            return True
        # using recursion to search the left and right children
        found_in_left: bool = self.get_ancestors(node.left, target, path)
        found_in_right: bool = self.get_ancestors(node.right, target, path)
        # If the target was found in either left or right child:
        if found_in_left or found_in_right:
            # Add the current node's name to the path because it is an ancestor
            path.append(node.name)
            return True
        # If target was not found in either left or right child, return False
        return False

    # This method calls get_ancestors and formats the specific ancestor lineage into a sentence
    def print_ancestors(self, name: str) -> str:
        # list to store the names of ancestors
        path: List = []
        # start searching from the root
        found = self.get_ancestors(self.root, name, path)  
        # If we didn't find the specific creature
        if not found:
            return f"{name} not found in tree."
        # Start building the sentence from the creature's name
        sentence: str = f"The {name}"
        # looping through each ancestor and adding the node plus wording to the sentence
        for ancestor in path:
            sentence += f" is descended from the {ancestor}"
        return sentence