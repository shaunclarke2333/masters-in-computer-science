import random

"""
    
"""

# Global variable for grid size
grid_size = 10
# Global variable for grid
grid = [ ['']*grid_size for i in range(grid_size) ]
# Global variable for number of ships to place
num_of_ships = 5

# This function prints the board to the console
def drawBoard(myboard):
    """
    This function prints the battlefield grid to the console.<br>
    Parameters:<br>
    - myboard:<br>
      - This should be the 10x10 list.<br>

    Returns:<br> 
        - None
    """
    # Gettinglength of board to use as marker forprinting grid within range
    lenght_of_board = len(myboard)
    # Getting boder length to print grid with plus signs
    border_length = lenght_of_board + 1
    
    # Printing the plus sing border at top 
    print(f"+{'---+' * border_length}")
    # Looping through to print column numbers
    for c in range(lenght_of_board):
        # Logic to print one row over at begining so we have an empty box
        if c == 0:
            print("|   |", end="")
        # Printing column numbers
        print(f" {c} ", end="")
        # Printing the line at the end of the column numbers row.
        print(f"|", end="")
    print()
    
    # Looping through to fill out the grid
    for i in range(grid_size):
        # Printing the grid separator
        print(f"+{'---+' * border_length}")
        # Printing the number at the beginning of each row
        print(f"| {i} ", end="")
        # Printing the donts and seperator lines in each row
        for j in range(grid_size):
            print(f"| {myboard[i][j]} ", end = "")
        # Printing the line at the end of each grid row
        print(f"|", end="")
        print()
    # Printing the border at the bottom of the grid.
    print(f"+{'---+' * border_length}")

# This function generates the ship coordinates.
def generate_ship_coordinates():
    """
    This function generates 5 random ship coordinates.<br>
    Parameters:<br>
    - None
    
    Returns:<br> 
    - Ship coordinates as a list
    """
    # local variable for empty set to hold ship locations
    ship_locations = set()
    
    # While loop to get random row and column pairs until set is complete
    while len(ship_locations) < num_of_ships:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        # Adding row and column to the ship locations set
        ship_locations.add((row, col))
    
    # Converting the set to a list so it can be updated later
    ship_locations = list(ship_locations)
    return ship_locations

def setupBoard(myboard, ship_locations):
    """
    This function takes the grid and the output of generate_ship_coordinates as parameters.<br>

    Parameters:<br>
    - myboard:<br>
      - This should be the 10x10 list.<br>
    - ship_locations:<br>
      - This should be the list returned from generate_ship_coordinates().<br>

    Returns:<br> 
    - None
    """
    i = j = 0

    while i < grid_size:
        while j < grid_size:
            # store the string "i, j" into the array
            myboard[i][j] = "."
            j += 1
        j = 0
        i += 1
        
    # Adding ship to locations on the grid
    for ship in ship_locations:
        myboard[ship[0]][ship[1]] = 'S'

# This function gets user selection
def get_user_coordinates(location):
    """
    This function gets the user inputs for the grid coordinates.<br>
    Parameters:<br>
    - location:<br>
      - should be a string "row" or "column, one or the other not both at teh same time.<br>

    Returns:<br> 
    - The user input.<br>
      - The user input as an int if it meets criteria.<br>
      - None if the input is not an integer.<br>
      - "out of range" if the number is not between 0 and 9
    """
    while True:
        # Getting the user input
        user_input = input(f"\nEnter a {location} Number between 0 and 9:\n:> ")

        # Logic to prevent the user from entering anything other than an int
        if not user_input.isdigit():
            print(f"\nInvalid {location} your input must be a number between 0 and 9\n")
            continue
        else:
            user_input = int(user_input)

        if user_input == 0:
            return user_input

        if user_input < 0 or user_input > 9:
            print(f"\nInvalid {location} your input must between 0 and 9\n")
            continue
        else:
            return user_input
        
        
def hitOrMiss(myboard, row, col):
    """
    This function checks if the user input was a hit or miss.<br>

    Parameters:<br>
    - myboard:<br>
      - This should be the 10x10 list.<br>
    - row:<br>
      - This should be the row input from user.<br>
    - col:<br>
      - This should be the column input from user.<br>

    Returns:<br> 
    - True.<br>
      - If the user input was a hit on a ship.<br>
    - False.<br>
      - If the user input was not a hit on a ship.<br>
    """
    # Local variable for what is at the coordinates the user entered
    location = myboard[row][col]

    # Logic to validate  if the entered coordinates was a hit or miss.
    if location == "S":
        # Updating board with X to show a hit
        myboard[row][col] = "X"
        return True
    elif location != "S":
        # Updating board with S to show a miss
        myboard[row][col] = "O"
        return False

# Structuring the program with combined logic.
def main(myboard):
    """
    This function ties everyting together and calls the progam.<br>

    Parameters:<br>
    - myboard:<br>
      - This should be the 10x10 list.<br>

    Returns:<br> 
    - None.<br>
    """
    try:
        # Local variable to hold list of ship locations
        ship_locations = generate_ship_coordinates()
        # updating the board and adding the ships
        setupBoard(grid, ship_locations)

        # Local variable for sunken ship counter
        ship_sunk_counter = 0
        
        # While loop to ask for user input until they sink all the ships
        while ship_sunk_counter < 5:

            # Displaying the board to the user
            print(f"\n{'Shall we play a game?':^{50}}")
            drawBoard(myboard)

            # Local variable to hold user row input
            row = get_user_coordinates("row")
            # Local variable to hold user column input
            column = get_user_coordinates("column")

            # Local variable to hold if a ship was hit or missed
            contact = hitOrMiss(myboard, row, column)

            # Logic to verify if the user input hit a ship and return the appropriate user message.
            if contact and ship_sunk_counter == 4:
                ship_sunk_counter += 1

                # Displaying board with all sunken ships
                drawBoard(myboard)
                print(f"\nYou sunk all {ship_sunk_counter} of my battleships!!\nGAME OVER!!")
                break

            if contact:
                ship_sunk_counter += 1
                remaining_ships = num_of_ships - ship_sunk_counter
                print(f"You sunk my battleship! Sink {remaining_ships} more ship{'s' if remaining_ships != 1 else ''} and you win")
                continue

            if not contact:
                print(f"\nAre you even trying?\n")
                continue
    except TypeError as e:
        print(f"\nYour input must be a number\n")

if __name__ == "__main__":
    main(grid)
