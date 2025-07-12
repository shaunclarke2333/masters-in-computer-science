# importing dependencies
from linked_list import Linkedlist

# This class handles the linked list interactions
class LinkedListActions:
    def __init__(self, ll_object: Linkedlist):
        self.l = ll_object # Linked list object

    # This function replaces item in list
    def insert_item_linked_list(self, num_places: int, number: int) -> None:
        """
        Executes nextcurrent n times.
        Then insert number.
        """
        # defining global variable
#         global header
        # if number of places is not 0 subtract 1
        if num_places != 0:
            num_places -= 1

        # if it is the beginning of the linked list isert number at the beginning
        if num_places == 0:
            # placing number at the beginning of the list
            self.l.insertBeginning(number)
            self.l.resetCurrent()
            # updating global variable
            header = self.l.getCurrent()
            self.l.printList(f"{number} was added")
            return 0
        
        # resetting current so number is inserted in correct place
        self.l.resetCurrent()
        # looping number of places to move to next current in linked list
        for _ in range(num_places):
#             print("calling method")
            self.l.nextCurrent()
        # adding number into linked list at designated spot
        self.l.insertCurrentNext(number)
        # resetting current
        self.l.resetCurrent()
        # updating global variable
        header =  self.l.getCurrent()
        # printing status of list
        self.l.printList(f"{number} was added")
        return 0
    
    # This function deletes item from the list
    def remove_item_linked_list(self,num_places: int, number: int) -> None:
        """
        Executes nextcurrent n times.
        """
         # defining global variable
        global header
        # subtracting one so the location is correct when locating node to remove
        num_places -= 1
        
        # If it is the beginning of the linked list delete the header.
        if num_places == 0:
            # remove the header
            self.l.removeBeginning()
            self.l.resetCurrent()
            # updating global variable
            header =  self.l.getCurrent()
            # printing status and state of list
            self.l.printList(f"{number} was removed")
            return 0

        # Changing current to the head of the list before starting delete process
        self.l.resetCurrent()
        # looping number of places to move to next current in linked list
        for _ in range(num_places):
            # moving to next node
            self.l.nextCurrent()

        # removing specified node from linked list
        self.l.removeCurrentNext()
        # resetting current
        self.l.resetCurrent()
        # updating global variable
        header =  self.l.getCurrent()
        # printing status of list
        self.l.printList(f"{number} was removed")
        return 0
