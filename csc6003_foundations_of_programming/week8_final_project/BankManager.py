# Importing dependencies
from typing import Union
from typing import List
from typing import Dict
from typing import Optional
from typing import Tuple
import random
from Bank import Bank
from BankUtility import BankUtility
from Account import Account

class BankManager:
    def __init__(self, bank: Bank, bank_util: BankUtility, account: Account):
        self.bank_object = bank()
        self.bank_util_object = bank_util()
        self.account = account
    
        # This is where you will implement your ‘main’ method and start
        # the program from.  The BankManager class should create an instance
        # of a Bank object when the program runs and use that instance to
        # manage the Accounts in the bank
    
    # Testing
    def testing(self):
        def create_account_object():
            account_object = Account()
            return account_object
        
        test_users = [["Shaun", "Clarke", 250, "000291234"],["Jerry", "West", 210, "000292654"],["Kat", "Clarke", 225.00, "000297852"]]

        counter = 0
        account_counter = 0
        user_objects = []
        for user in test_users:
            # creating account emoty object
            account_object = create_account_object()
            
            account_counter += 1
            first_name = account_object.set_owner_first_name(user[0])
            last_name = account_object.set_owner_last_name(user[1])
            balance = account_object.set_balance(user[2])
            ssn = account_object.set_ssn(user[3])
            account_num = 12345671+account_counter
            account_number = account_object.set_account_number(12345671+account_counter)
            pin_num =1231+account_counter
            pin = account_object.set_pin(pin_num)

            self.bank_object.add_account_to_bank(account_object)
            print(account_object)
            counter +=1
            print("\n")
        print(f"This is counter: {counter}")
    # testing
          
    # This method prompt the user to enter an account number then pin
    def prompt_for_account_and_pin(self, bank_object: Bank) -> object:
        # looping until acvcount number criteria is met
        while True:
            try:
                # Get user input for account number
                acc_input: int = int(input(f"\nEnter account number.\n:>"))
                # making sure acc is 8 digits
                if len(str(acc_input)) != 8:
                    print(f"Account numbner must be 8 digits: {acc_input}")
                    continue
                # Getting account number from bank
                bank_account = bank_object.find_account(acc_input)
                # If the account was not found 
                if not bank_account:
                    print(f"Account not found for account number: {acc_input}")
                    continue
                # If the account was found exit while loop
                break              
            except ValueError:
                print("\nInvalid entry.\n")

        # looping until pin criteria is met
        while True:
            try:
                # Get user input for pin number
                pin_input: int = int(input(f"\nEnter Pin.\n:>"))
                # making sure pin is 4 digits
                if len(str(pin_input)) != 4:
                    print(f"Pin numbner must be 4 digits: {pin_input}")
                    continue
                # Checking if pin matches
                if bank_account.get_pin() == pin_input:
                    return bank_account
                else:
                    print(f"Invalid Pin")
                    continue
            except ValueError:
                print("\nInvalid entry.\n")

    def run_program(self):
        # calling test function
        self.testing()
        test = self.prompt_for_account_and_pin(self.bank_object)
        print(test)

run_program = BankManager(Bank, BankUtility, Account)

run_program.run_program()

