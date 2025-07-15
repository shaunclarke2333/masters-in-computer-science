"""
Author: Shaun Clarke
Goal:
Create a program that reads a list of Integer numbers from a file named "data.txt" (use your own file with about 10 numbers - no repetitions and one number per line);
Store those numbers into an array a and sort it - a.sort();
Use the linked list and node classes seen in class to store the ordered elements of a into a LinkedList structure L;
Ask the user a Integer value x;
    Look for the position to insert x in L:
    If the value x is already in L, remove it;
If it is not, insert x in the appropriated position so L remains sorted;
Go to your IDE and try to program it (your code must run correctly on IDLE);
Save your program in a .py file and submit it.
"""


# importing dependencies
from typing import List
from create_numbers_list import CreateNumbersList
from linked_list import Linkedlist
from linked_list_actions import LinkedListActions
from user_input import UserInput


# This function is where the program comes together. 
def main():
    # Creating the create numbers list object
    create_list: CreateNumbersList = CreateNumbersList()
    # Reading the data from the txt file
    file_content: str = create_list.read_txt_file("numbers.txt")
    # Getting the sorted list of data from the text file:
    a: List = create_list.create_sorted_list(file_content)

    # Instantiating link list object
    l: Linkedlist = Linkedlist()
    # printing linked list with status message
    l.printList("List created")
    # looping through sorted list and add items to a linked list
    for num in a:
        # adding number to the head of the linked list
        l.insertBeginning(num)
        # printing list with custom message
        l.printList(f"Inserting {num} at Beginning")
    # resetting the current node to the header node at the beggining of linked list
    l.resetCurrent()
    # priting the current state of the list
    l.printList("Current status of the list")

    # Getting user input
    number_input: int = UserInput.get_user_input()

    # instantiating linked list action class
    ll_actions = LinkedListActions(l)
    # Counters to hold the place to insert number or remove number
    insert_counter: int = 0 # To keep track of where insert number
    remove_counter: int = 0 # keep track of where to remove number
    header: int = l.getCurrent() # Keeping track of header when nodes are removed
    start_node: int = l.getCurrent() # Keeping track of header so last item can be updated
#     tracker: int = 0
    # print(f"This is header {header}")
    print(f"Current node before loop: {start_node}")
    # looping through linked list to get the data from each node
    while True:
#         tracker += 1
#         print(f"Looping for {tracker} time")
#         print(f"This is header {header}")
#         if tracker >= 12:
#             break
        # Getting the current node
        current_node: int = l.getCurrent()
#         print(f"This is current node {current_node}\n")
        # checking if user input is already in linked list
        if current_node != number_input:
            remove_counter += 1 
            if insert_counter > 1 and start_node == current_node:
#                 print(f"Attempting to add to the end")
#                 print(f"this is start node: {start_node}")
                ll_actions.insert_item_linked_list(insert_counter, number_input)
                break
            elif current_node < number_input:
                insert_counter += 1
                current_node = l.nextCurrent()
#                 print(f"This is next current: {l.getCurrent()}")
#                 print(f"this is insert counter: {insert_counter}")
#                 print(f"this is start node: {start_node}\n")
            elif current_node > number_input:
                ll_actions.insert_item_linked_list(insert_counter, number_input)
                break
            
        elif current_node == number_input and current_node == header:
            # Deleting header node
            l.removeBeginning()
            # resetting current
            l.resetCurrent()
            header = l.getCurrent()
            # priting the current state of the list
            l.printList("Deleted header node")
            break
        else:
            ll_actions.remove_item_linked_list(remove_counter, number_input)
            break
        
#         if current_node is None:
#             ll_actions.insert_item_linked_list(insert_counter, number_input)
#             break

main()