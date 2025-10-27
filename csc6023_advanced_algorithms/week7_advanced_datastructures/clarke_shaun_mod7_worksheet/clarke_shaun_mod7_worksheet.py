"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 7 Advanced DaTA Structures
Assignment: 

    Create a program that asks repeatedly the user positive integer numbers and stores/deletes it in an AVL tree (use the code saw in the third example)

    If the user enters a number already in the tree, delete it

    If the user enters a number that is not in the tree, insert it

    After each insertion/deletion, the program prints the current tree using the printHelper method

    When the user enters a non-positive integer, the program ends

    Besides the implementation of your program, write a short report describing your experiences.
"""



from typing import Optional
import sys
import time


# User input utilities 
class UserInput:
    @staticmethod
    def get_int() -> int:
        """
        - Prompt the user to enter an integer.
        - Keeps asking until the user enters a valid integer.
        """
        while True:
            try:
                # Asking user for input and stripping whitespace
                user_input: int = int(input("\nEnter a positive integer or enter 0, to quit: ").strip())
                return user_input
            except ValueError:
                print("You must enter a whole number. Let's try that again.")


# AVL Tree Node
class TreeNode(object):
    def __init__(self, key: int):
        # key held by this node
        self.key: int = key
        # left child pointer
        self.left: Optional[TreeNode] = None
        # right child pointer
        self.right: Optional[TreeNode] = None
        # height field for AVL balancing
        self.height: int = 1

# AVL Tree
class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root: Optional[TreeNode], key: int) -> TreeNode:
      
        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        # Update node height from children
        root.height = 1 + max(self.getHeight(root.left),
        self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # Node with two children
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z: TreeNode) -> TreeNode:
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z: TreeNode) -> TreeNode:
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return root.height

    # Get balance factor of the node
    def getBalance(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root: TreeNode) -> TreeNode:
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # Print the tree
    def printHelper(self, currPtr: Optional[TreeNode], indent: str, last: bool) -> None:
        if currPtr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

    
    # Added this contains method, since you said i can't use a data structure lol
    def contains(self, root: Optional[TreeNode], key: int) -> bool:
        """
        This method searches the AVL for the user's integer input.
        Returns True if found and False f not.
        """
        current = root
        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False


# Where the magic happens
def main() -> None:
    """
    RUBRIC:
    - Repeatedly ask the user for a positive integer.
    - If the integer is already in the tree then we will delete it.
    - If the integer is not in the tree we will insert it.
    - After each insertion or deletion the tree is printed using the printHelper method.
    - Exit if the user enters a non-positive integer.
    """

    myTree = AVLTree()
    root: Optional[TreeNode] = None

    print("\nLETS PLAY A GAME ...\n")
    time.sleep(2)
    print("Naah im just kidding ...\n")
    while True:
        # Prompting user for input
        n: int = UserInput.get_int()

        # If the number is no positive, break the loop
        if n <= 0:
            print("\nEnding program. Final tree:")
            myTree.printHelper(root, "", True)
            break

        # If number exists, delete iff not insert
        if myTree.contains(root, n):
            print(f"\n{n} is already in the tree and will be deleted.")
            root = myTree.delete_node(root, n)
        else:
            print(f"\n{n} is not in the tree and will be insterted.")
            root = myTree.insert_node(root, n)

        # Print the current tree after the operation
        print("\nCurrent AVL tree:")
        myTree.printHelper(root, "", True)

if __name__ == "__main__":
    main()
 

