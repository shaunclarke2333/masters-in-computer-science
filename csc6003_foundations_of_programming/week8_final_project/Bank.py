from typing import Union
import Account

# This class mimics some of the basic functions of a bank
class Bank:
#     # List to hold all bank accounts
#     __accounts = []
#     # Variable for total allowed bank accounts
#     __total_accounts = 0
    def __init__(self):
        self.__class__.__accounts = []
        self.__class__.__total_accounts = 0
    
    # This method checks if an account is already in accounts
    def __does_account_exist(self, account: Account) -> bool:
        """
        This method checks if an account is already in accounts.
        """
        # Checking for duplicates
        for acc in self.__class__.__accounts:
            if acc == account:
                return True
        return False
    
    # This method adds the Account object to the bank
    def add_account_to_bank(self, account: Account) -> Union[bool,str]:
        """
        This method adds an account object to the accounts list.<br>
        It also make sure they are no duplicates and only allows 100 accounts.
        """
        # Checking if we reached account limit
        if self.__class__.__total_accounts == 100:
            print(f"\nNo more accounts available\n")
            return False
        # Checking for duplicates
        if self.__does_account_exist(account):
            return f"account already exists"
        # Adding account to bank if they are no duplicates
        self.__class__.__accounts.append(account)
        #updating total accounts count by adding 1 to represent a new account
        self.__class__.__total_accounts += 1
        return True
        
    # This method removes an account object from the accounts list
    def remove_account_from_bank(self, account: Account) -> bool:
        """
        This method allows us to remnove an account from the account list
        """
        # checking each account in the list
        for index,acc in enumerate(self.__class__.__accounts):
            if acc is not None:
                # if we have a match
                if acc == account:
                    # replace the account with None
                    self.__class__.__accounts[index] = None
                    #updating total accounts count by subtracting 1 to represent closing an account
                    self.__class__.__total_accounts -= 1
                    return True
                else:
                    return False
        # return false if account doesnt exist
        return False
    
    # This method finds the specified account and return it
    def find_account(self, account_number: int) -> Account:
        # checking each account in the list
        for acc in self.__class__.__accounts:
            if acc is not None:
                # If there is an account number match, return the account
                if acc.get_account_number() == account_number:
                    return acc
        # Return false if the account was not found
        return False
    
    # This method adds monthly interest to all accounts using a submitted rate
    def add_monthly_interest(self, interest_rate: float) -> bool:
        for acc in self.__class__.__accounts:
            if acc is not None:
                # Get balance in cents
                balance = acc.get_balance()
                # Calculate interest in cents (rounded to nearest cent)
                interest = round(balance * (interest_rate / 100))
                # Deposit interest (in cents)
                acc.deposit(interest)
                # Format interest and new balance
                interest_dollars = interest / 100
                new_balance_dollars = acc.get_balance() / 100
                # Display output
                print(f"Deposited interest:${interest_dollars:,.2f} into account number:{acc.get_account_number()}, new balance:${new_balance_dollars:,.2f}")

        
                