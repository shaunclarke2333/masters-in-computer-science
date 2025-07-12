# This class prompts the user for an input
class UserInput:
    """
    This class does not need to be instantiated.
    It prompts the user to input an integer.
    """
    # This static method prompts the user for input
    @staticmethod
    def get_user_input():
        # While loop to prompt user until input is satisfied
        while True:
            try:
                # Prompting the user to enter an integer
                user_input: int = int(input(f"Enter a number, any number\n: ").strip())
                return user_input
            except ValueError:
                print("\nYour input must be a number\n")

