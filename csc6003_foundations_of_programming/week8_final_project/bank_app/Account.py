# ThiS class creates a bank account 
class Account:
    # a set to hold used account numbers to stay uniqe
    __used_account_numbers: set = set()
    # a set to hold used pin numbers to stay unique
    __used_pin_numbers: set = set()
    def __init__(self):
        self.__owner_first_name = None
        self.__owner_last_name = None
        self.__ssn: str = None
        self.__balance: int = 0.00
        self.account_number: int = None
        self.__pin: int = None
        

    # This method will allow us to compare an account object to a string.
    def __eq__(self, other_account_number: str) -> bool:
        if isinstance(other_account_number, Account):
            if self.account_number == other_account_number.account_number:
                return True
        return False
    
    # returns the first name
    def get_owner_first_name(self) -> str:
        """
        Getter method that returns first name
        """
        return self.__owner_first_name
    
    # updates the first name
    def set_owner_first_name(self, first_name: str) -> bool:
        """
        Setter method that updates first name
        """
        # updating first name
        self.__owner_first_name = first_name
        # If update was not successful
        if self.__owner_first_name != first_name:
            return False
        # If update was successful
        return True
    
    # returns the last name
    def get_owner_last_name(self) -> str:
        """
        Getter method that returns last name
        """
        return self.__owner_last_name
    
    # updates the last name
    def set_owner_last_name(self, last_name: str) -> bool:
        """
        Setter method that updates last name
        """
        # updating name
        self.__owner_last_name = last_name
        # If update was not successful
        if self.__owner_last_name != last_name:
            return False
        # If update was successful
        return True
        
    # returns the SSN
    def get_ssn(self) -> str:
        """
        Getter method that returns ssn
        """
        return self.__ssn
    
    # updates the ssn
    def set_ssn(self, ssn: str) -> bool:
        """
        Setter method that updates ssn
        """
        # updating ssn
        self.__ssn = ssn
        # If update was not successful
        if self.__ssn != ssn:
            return False
        # If update was successful
        return True
    
    # returns the balance
    def get_balance(self) -> float:
        """
        Getter method that returns balance
        """
        # Returning balance 
        return self.__balance
    
    # updates the balance
    def set_balance(self, amount: float) -> bool:
        """
        Setter method that updates balance
        """
        # updating balance with amount 
        self.__balance = amount
        # If update was not successful
        if self.__balance != amount:
            return False
        # If update was successful
        return True
    
    # returns the pin
    def get_pin(self) -> int:
        """
        Getter method that returns pin
        """
        return self.__pin
    
    # updates the pin
    def set_pin(self, pin: int) -> bool:
        """
        Setter method that updates balance
        """
        # updating pin
        self.__pin = pin
        # If update was not successful
        if self.__pin != pin:
            return False
        # If update was successful
        return True 
    
    # returns the account number
    def get_account_number(self) -> int:
        """
        Getter method that returns account number
        """
        return self.account_number
    
    # updates the account number
    def set_account_number(self, account_number: int) -> bool:
        """
        Setter method that updates account number
        """
        # updating account number
        self.account_number = account_number
        # If update was not successful
        if self.account_number != account_number:
            return False
        # If update was successful
        return True 
                
    # This method adds the deposit to the acc balance returns the updated amount
    def deposit(self, amount: int) -> int:
        """
        This method adds the entered amount to the present balance.<br>
        It also returns the updated balance.
        """
        # holding balance before change for comaprison
        previous_balance = self.__balance
        # Updating account balance with deposit amount
        self.__balance += amount
        # Checking if balance was updated
        if self.__balance - amount == previous_balance:
            # returning balance converted to dollars
            return self.__balance
        else:
            return False
    
    # This method subtracts the amount from the balance and returns updated amount
    def withdraw(self, amount: int) -> int:
        """
        This mehtod subtracts the entered amount from the present balance.<br>
        It also returns the updated balance.
        """
        # making sure there is enough money in account
        if self.__balance < amount:
            return "insufficient funds"
        # holding balance before change for comaprison
        previous_balance = self.__balance
        # Updating the account with withdrawal
        self.__balance -= amount
        # Checking if balance was updated
        if self.__balance + amount == previous_balance:
            return self.__balance
        else:
            return False
    
    # This method checks if a pin is valid and returns a boolean output
    def is_pin_valid(self, pin: str) -> bool:
        """
        This method checks if a pin is valid and returns a boolean output.
        """
        # checking if pin is valid
        if self.__pin == pin:
            return True
        else:
            return False
        
    # This method returns account information as a formatted string
    def __tostring(self) -> str:
        """
        This method returns account information as a formatted string.
        """
        # converting cents to dollars
        balance = self.__balance / 100
        return (
            f"Account Number: {self.account_number}\n"
            f"Owner First Name: {self.__owner_first_name}\n"
            f"Owner Last Name: {self.__owner_last_name}\n"
            f"Owner SSN: xxx-xx-{self.__ssn[-4:]}\n"
            f"PIN: {self.__pin}\n"
            f"Balance: ${balance:.2f}"
        )

    # Allows the print(object) to display the formatted output
    def __repr__(self) -> str:
        """
        Allowing the class to display readable format when printed
        """
        return self.__tostring()
        
