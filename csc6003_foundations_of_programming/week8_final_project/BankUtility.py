# Importing dependencies
from typing import Union
import random

# This class is like a swiss army knife with methods that carry out bank actions
class BankUtility:
    # a set to hold used generated numbers
    __used_numbers: set = set()
    
    # Gets user strin ginput
    def get_string_input(self, input_message: str) -> str:
        while True:
            try:
                user_input: str = input(f"{input_message}\n:>").lower().strip()
                if not user_input:
                    raise ValueError(f"Input cannot be empty.")
                return user_input
            except ValueError as err:
                print(err)
                
    # Get user number input
    def prompt_user_for_positive_umber(self, input_message: str) -> Union[float, str]:
        """
        This method asks the user to enter a number and returns it.
        If they enter a string it asks the user to try again
        """
        while True:
            try:
                user_input: float = float(input(f"{input_message}\n:>"))
                # If input didnt trigger value error and 
                if user_input == int(user_input):
                    return user_input
                else:
                    return user_input
            except ValueError:
                print("\nPlease try again\n")
    
    # Generates a uniqe 8 or 4 digit numbr that does not start with 0.
    def number_generator(self,minimum: int, maximum: int) -> int:
        """
        This method generates a unique 8 or 4 digit number.<br>
        The 8 digit number is used as an account number.<br>
        The 4 digit number is used as a pin bumber.
        """
        while True:
            # loop until a uniqe 8 or 4 digit number is selected
            number: int = random.randint(minimum, maximum)
            # check if number already used or if it starts with 0
            if number not in self.__class__.__used_numbers and str(number)[0] != "0":
                # add number to set
                self.__class__.__used_numbers.add(number)
                return number
        
    
    # This method converts dollars to cents and back
    def convert_dollars_and_cents(self, amount: int, switch: bool = False) -> int:
        """
        This method uses a switch to convert dollars to cents.<br>
        Swtich set to default False which converts dollars to cents.<br>
        If switch is set to True convert cents to dollars.
        """
        # Convert dollars to cents
        cents: int = int(round(amount * 100))
        return cents
