def calculate_base():
    """
    Instructions
    Write a Python program that:

    Asks the user a number as a string (to set a maximum number of digits in your program is ok);
    Your program should ask which is the base (an Integer from 2 to 16);
    With that information, your program should compute the binary and decimal representations of the number, then print it out as a string;

    For example:
    If the user enters: FA and 16, your program should print out:
        "FA in base 16 is: 250 in base 10 and 11111010 in base 2";
    If the user enters: 34 and 5, your program should print:
        "34 in base 5 is: 19 in base 10 and 10011 in base 2"
    """
    # Initializing number_input_length 
    number_input_length = 2

    # Promting user and saving input
    number_input = input(f"Please enter a number that is {number_input_length} digits or less: ")
    if number_input == "exit":
            exit()

    # get the length of the string the user entered
    len_user_input = len(number_input)

    # While loop to make sure that the user did not enter more than 3 digits.
    while len_user_input > number_input_length:
        user_number_input = input(f"Please enter a number that is {number_input_length} digits or less: ")
        if user_number_input == "exit":
            exit()
        len_user_input = len(user_number_input)
        
    # Asking the user to enter the base for the previous number
    base_input = input(f"Please enter the base, which should be betweeen 2 and 16: ")
    if base_input == "exit":
            exit()
    # Converting the string to an int
    base_input = int(base_input)

    # While loop to make sure the base input meets criteria
    while base_input < 2 or base_input > 16:
        base_input = input(f"Please enter the base, which should be betweeen 2 and 16: ")
        if base_input == "exit":
            exit()

    # converting the user input to their specified base
    base_ten = int(number_input,base_input)

    # Converting the base_ten output to binary
    binary_output = bin(base_ten)

    # removing the leading 0b from the binary output using split and selecting the second index
    binary_output = binary_output.split("b")[1]

    print(f"{number_input} in base {base_input} is: {base_ten} in base 10 and {binary_output} in base 2")

def main():
    calculate_base()

if __name__ == "__main__":
    main()
