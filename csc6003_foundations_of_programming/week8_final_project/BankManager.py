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
from CoinCollector import CoinCollector

class BankManager:
    def __init__(self, bank: Bank, bank_util: BankUtility, account: Account, CoinCollector: CoinCollector):
        self.bank_object: Bank = bank()
        self.bank_util_object: BankUtility = bank_util()
        self.account: Account = account
        self.coin_collector = CoinCollector
        self.banking_menu: List = [
            "1. Open an account",
            "2. Get account information and balance",
            "3. Change PIN",
            "4. Deposit money in account",
            "5. Transfer money between accounts",
            "6. Withdraw money from account",
            "7. ATM withdrawal",
            "8. Deposit change",
            "9. Close an account",
            "10. Add monthly interest to all accounts",
            "11. End Program"
        ]
    
        # This is where you will implement your ‘main’ method and start
        # the program from.  The BankManager class should create an instance
        # of a Bank object when the program runs and use that instance to
        # manage the Accounts in the bank
          
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
                # Using acc number to get account from bank
                bank_account: Account = bank_object.find_account(acc_input)
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

    # This function Gets menu number input
    def get_menu_number_input(self,input_message: str, menu_options: List) -> int:
        while True:
            try:
                # Getting user input
                user_input: int = int(input(f"{input_message}: ").strip())
                # Making sure input is not empty
                if not user_input:
                    raise KeyError(f"Input cannot be empty.\n")
                # Using the length of the menu list to validate that menu input is within range
                if user_input >= 1 and user_input <= len(menu_options):
                    return user_input
                else:
                    print(f"\nOnly menu number options will be accepted\n")
            except ValueError:
                print("You must enter a menu number\n")
            except KeyError as err:
                print(err)

    # This method formats the balance converting it from cents to dollars
    def format_balance_output(self, balance: int) -> str:
        balance = balance / 100
        return f"${balance:.2f}"
    
    # This method calculates the number of bills in ATM transaction
    def calculate_bills(self, amount: int) -> dict:
        # dict to hold count for each bill
        bills = {}
        # getting the number of times 20 goes into the amount
        bills['$20 bills'] = amount // 20
        # Updating amount with whats left after removing $20 bills
        amount %= 20
        # getting the number of times 10 goes into the amount
        bills['$10 bills'] = amount // 10
        # Updating amount with whats left after removing $10 bills
        amount %= 10
        # getting the number of times 5 goes into the amount
        bills['$5 bills'] = amount // 5
        # Updating amount with whats left after removing $5 bills
        amount %= 5

        return bills

    # This method displays the menu and returns the selection
    def display_menu(self) -> str:
        # Defining menu border and header
        border: str = "============================================================"
        # Printing menu border
        print(f"\n{border}")
        # Show Menu
        print(*self.banking_menu, sep="\n")
        print(border)
        # Get menu input
        menu_input:str = self.get_menu_number_input("What do you want to do?", self.banking_menu)

        return menu_input

    # This main method is what runs the program.
    def main(self):
        while True:
            # Display menu and get input
            menu_selection: int = self.display_menu()

            # Triggering appropriate menu option based on user selection
            match menu_selection:
                case 1: # Open Account
                    # get users first name
                    first_name: str = self.bank_util_object.get_string_input("Enter Account Owner's First Name:")
                    # get users last name
                    last_name: str = self.bank_util_object.get_string_input("Enter Account Owner's Last Name:")
                    # get users SSN
                    while True:
                        try:
                            ssn: str = self.bank_util_object.get_string_input("Enter Account Owner's SSN (9 digits):")
                            # Making sure the ssn is all digits
                            check_digits = self.bank_util_object.is_numeric(ssn)
                            # making sure the ssn is 9 digits
                            if len(ssn) != 9:
                                raise ValueError(f"\nSSN must be 9 digits: {ssn}\n")
                            elif not check_digits:
                                raise ValueError(f"\nSSN must be 9 digits: {ssn}\n")
                            # breaking loop if ssn is 9 digits
                            break
                        except ValueError as err:
                            print(err)
                    

                    # creating account instance
                    account_owner: Account = self.account()
                    # adding name, ssn, account number, pin and balance to account.
                    account_owner.set_owner_first_name(first_name) 
                    account_owner.set_owner_last_name(last_name) 
                    account_owner.set_ssn(ssn) 
                    account_owner.set_account_number(self.bank_util_object.number_generator(20000000, 99999999)) 
                    account_owner.set_pin(self.bank_util_object.number_generator(2000, 9999)) 
                    account_owner.set_balance(0.00) 
                    # adding account to bank
                    add_account = self.bank_object.add_account_to_bank(account_owner)
                    # Print account details if account was added
                    if add_account:
                        # displaying account if it was added
                        print(f"\n{account_owner}\n")
                
                case 2: #Get account information and balance
                    # Prompting user for account and pin
                    account: Account = self.prompt_for_account_and_pin(self.bank_object)
                    # Displaying account info
                    print(f"\n{account}")

                case 3: #Change PIN
                    # Prompting user for account and pin
                    account: Account = self.prompt_for_account_and_pin(self.bank_object)
                    # Ask user to enter new pin.
                    while True:
                        try:
                            # asking user for new pin
                            new_pin:str = self.bank_util_object.get_string_input("Enter new PIN:")
                            # checking if pin meets requirements
                            if self.bank_util_object.is_numeric(new_pin) and len(new_pin) == 4:
                                break
                            else:
                                raise ValueError(f"Please enter a new 4 digit pin.")
                        except ValueError as err:
                            print(err)

                    # ask user ot enter new pin again
                    while True:
                        try:
                            # asking user for second new pin
                            second_new_pin: str = self.bank_util_object.get_string_input("Enter new PIN again to confirm: ")
                            # If pin is not a number
                            if not self.bank_util_object.is_numeric(new_pin):
                                raise ValueError(f"\n{new_pin} is not a number\n")
                            # If pin is not 4 digits
                            if len(new_pin) != 4:
                                raise ValueError(f"\nPIN must be 4 digits, try again.\n")
                            # chekc if new pin and second new pin match
                            if new_pin != second_new_pin:
                                raise ValueError(f"\nPINs do not match, try again.\n")
                            # Breaking loop if both new pins match
                            break
                        except ValueError as err:
                            print(err)

                    # converting new pin to int and updating account
                    pin_updated = account.set_pin(int(new_pin))

                    if pin_updated:
                        print(f"\nPIN updated\n")

                case 4: #Deposit money in account
                    # Prompting user for account and pin to return account
                    account: Account = self.prompt_for_account_and_pin(self.bank_object)
                    # Getting deposit
                    while True:
                        try:
                            # Getting the user amount input
                            amount: int = self.bank_util_object.prompt_user_for_positive_umber("Enter amount to deposit in dollars and cents (e.g. 2.57)")
                            # Making sure input is not zero
                            if amount > 0:
                                # converting deposit to cents
                                amount_in_cents = self.bank_util_object.convert_dollars_and_cents(amount)
                                # making deposit
                                make_deposit = account.deposit(amount_in_cents)
                                # confirming deposit
                                if make_deposit:
                                    # get balance and format output
                                    balance = self.format_balance_output(make_deposit)
                                    print(f"\nNew balance:{balance}\n")
                                    break
                                else:
                                    raise RuntimeError(f"Balance was not update. Try again.")
                            else:
                                raise ValueError(f"\nAmount cannot be negative. Try again.\n")
                        except ValueError as err:
                            print(err)
                        except RuntimeError as err:
                            print(err)

                case 5: # Transfer money between accounts
                    print("Account to Transfer From:")
                    # Prompting user for account and pin for from account
                    from_account: Account = self.prompt_for_account_and_pin(self.bank_object)
                    # Getting info for account to transfer to
                    print("Account to Transfer To:")
                    # Prompting user for account and pin for to account
                    to_account: Account = self.prompt_for_account_and_pin(self.bank_object)
                    
                    # Getting transfer amount and making transfer
                    while True:
                        try:
                            # Getting the user amount input
                            amount: int = self.bank_util_object.prompt_user_for_positive_umber("Enter amount to transfer in dollars and cents (e.g. 2.57)")
                            # Making sure input is not zero
                            if amount > 0:
                                # converting to cents
                                amount_in_cents = self.bank_util_object.convert_dollars_and_cents(amount)
                                # attempting withdrawal
                                withdraw = from_account.withdraw(amount_in_cents)
                                # if not enough funds, go back to main menu
                                if withdraw == "insufficient funds":
                                    print(f"Insufficient funds in account {from_account.get_account_number()}")
                                    break
                                # Account had enough funds so continue with transfer
                                make_deposit = to_account.deposit(amount_in_cents)
                                # confirming deposit
                                if make_deposit:
                                    # get balance and format output for from account and to account
                                    from_account_balance = self.format_balance_output(from_account.get_balance())
                                    to_account_balance = self.format_balance_output(to_account.get_balance())
                                    # Displaying balance for from and to account
                                    print(f"\nNew balance in from account:{from_account.get_account_number()} is:{from_account_balance}")
                                    print(f"New balance in to account:{to_account.get_account_number()} is:{to_account_balance}")
                                    break
                                else:
                                    raise RuntimeError(f"Balance was not update. Try again.")
                            else:
                                raise ValueError(f"\nAmount cannot be negative. Try again.\n")
                        except ValueError as err:
                            print(err)
                        except RuntimeError as err:
                            print(err)

                case 6: #Withdraw money from account
                    # Prompting user for account and pin to return account
                    account: Account = self.prompt_for_account_and_pin(self.bank_object)
                    # Getting deposit
                    while True:
                        try:
                            # Getting the user amount input
                            amount: int = self.bank_util_object.prompt_user_for_positive_umber("Enter amount to withdraw in dollars and cents (e.g. 2.57)")
                            # Making sure input is not zero
                            if amount > 0:
                                # converting withdrawal to cents
                                amount_in_cents = self.bank_util_object.convert_dollars_and_cents(amount)
                                # making widrawal
                                make_withdraw = account.withdraw(amount_in_cents)
                                # confirming withdrawal
                                if make_withdraw:
                                    # get balance and format output
                                    balance = self.format_balance_output(account.get_balance())
                                    print(f"\nNew balance:{balance}\n")
                                    break
                                else:
                                    raise RuntimeError(f"Balance was not updated. Try again.")
                            else:
                                raise ValueError(f"\nAmount cannot be negative. Try again.\n")
                        except ValueError as err:
                            print(err)
                        except RuntimeError as err:
                            print(err)

                case 7: #ATM withdrawal
                    # Prompting user for account and pin to return account
                    account: Account = self.prompt_for_account_and_pin(self.bank_object)
                    # Getting deposit
                    while True:
                        try:
                            # Getting the user amount input
                            amount: int = self.bank_util_object.prompt_user_for_positive_umber("Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000)")
                            # Making sure input is not zero, not less than 5, not graeater than 100 and divisible by 5
                            if amount > 0 and amount >= 5  and amount <= 1000 and amount % 5 == 0:
                                # calculating how many 20s,10s,5s
                                bills = self.calculate_bills(amount)
                                # displaying breakdown of bills
                                for bill_type, count in bills.items():
                                    print(f"Number of {bill_type}-dollars bills: {round(count)}")
                                # converting withdrawal to cents
                                amount_in_cents = self.bank_util_object.convert_dollars_and_cents(amount)
                                # making widrawal
                                make_withdraw = account.withdraw(amount_in_cents)
                                # confirming withdrawal
                                if make_withdraw:
                                    # get balance and format output
                                    balance = self.format_balance_output(make_withdraw)
                                    print(f"\nNew balance:{balance}\n")
                                    break
                                else:
                                    raise RuntimeError(f"Balance was not updated. Try again.")
                            else:
                                raise ValueError(f"\nInvalid amount. Try again.\n")
                        except ValueError as err:
                            print(err)
                        except RuntimeError as err:
                            print(err)

                case 8: # Deposit change
                    # Prompting user for account and pin to return account
                    account: Account = self.prompt_for_account_and_pin(self.bank_object)
                    # Getting deposit
                    while True:
                        try:
                            # Getting the user amount input
                            coins: str = self.bank_util_object.get_string_input("Deposit coins")
                            # Making sure input is not zero
                            if len(coins) > 0:
                                # counting coins
                                parsed_change,invalid_coins = self.coin_collector.parseChange(coins)
                                # display invalid coins
                                print("\nInvalid Coin:", *invalid_coins, sep=" ")
                                # converting deposit to cents
                                amount_in_cents = self.bank_util_object.convert_dollars_and_cents(parsed_change)
                                # making deposit
                                make_deposit = account.deposit(amount_in_cents)
                                # confirming deposit
                                if make_deposit:
                                    # get balance and format output
                                    balance = self.format_balance_output(make_deposit)
                                    print(f"\nNew balance:{balance}\n")
                                    break
                                else:
                                    raise RuntimeError(f"Balance was not update. Try again.")
                            else:
                                raise ValueError(f"\nAmount cannot be negative. Try again.\n")
                        except ValueError as err:
                            print(err)
                        except RuntimeError as err:
                            print(err)
                
                case 9: #Close an account
                    # Prompting user for account and pin to return account
                    account: Account = self.prompt_for_account_and_pin(self.bank_object)
                    # Attempting to remove account
                    while True:
                        # holding account number
                        acc_num = account.get_account_number()
                        # removing account 
                        is_removed = self.bank_object.remove_account_from_bank(account)
                        # checking if account was removed.
                        if is_removed:
                            print(f"\nAccount {acc_num} closed")
                            break
            
                case 10: #Add monthly interest to all accounts
                    # Getting interest
                    while True:
                        try:
                            # Getting the user interest input
                            amount: int = self.bank_util_object.prompt_user_for_positive_umber("Enter annual interest rate percentage (e.g. 2.75 for 2.75%)")
                            # Making sure input is not zero
                            if amount > 0:
                                # add interest
                                self.bank_object.add_monthly_interest(amount)
                                break
                            else:
                                raise ValueError(f"\nAmount cannot be negative. Try again.\n")
                        except ValueError as err:
                            print(err)
                        except RuntimeError as err:
                            print(err)
                case 11: # exit program
                    exit ()





                    



run_program = BankManager(Bank, BankUtility, Account, CoinCollector)

run_program.main()
