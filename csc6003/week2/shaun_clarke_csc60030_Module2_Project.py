import random

"""
Title: Battleship Game Algorithm
Goal: Mimics the game battleship, where the users plays until they sink all ships.

Steps:
1.	Import random module.
2.	Instantiate grid_size global variable to determine the board size.
3.	Instantiate grid global variable to hold list of lists which represents myboard.
4.	Instantiate num_of_ships global variable for ships on the board.
5.	Define a function drawBoard(myboard):
    a.	This function prints the battlefield grid to the console.
    b.	This function takes myboard as a parameter.
    c.	This function returns nothing.
6.	Define a function generate_ship_coordinates():
    a.	This function generates 5 random ship coordinates to later add to the board.
    b.	This function accepts no parameters.
    c.	It returns a list of 5 randomly generated ship coordinates.
7.	Define a function setupBoard(myboard, ship_locations):
    a.	This function set's up the board with the ship icons and dots for the water.
    b.	This function accepts 2 parameters myboard and ship_locations.
    c.	This function returns nothing.
8.	Define a function get_user_coordinates(location):
    a.	This function gets the user inputs for the grid coordinates.
    b.	This function takes one parameter, location
    c.	This function returns:
        i.	The user input if it meets criteria
        ii.	None if the input is not an int
        iii.	‘out of range’ if the int is not between 0 and 9
9.	Define a function hitorMiss(myboard, row, col):
    a.	This function checks if the users input was a hit or a miss and updates the board.
    b.	This function accepts 3 parameters:
        i.	myboard, which is the grid variable
        ii.	row, which is the output from get_user_coordinates(“row”)
        iii.	column, which is the output from get_user_coordinates(“column”)
    c.	This function returns True or False:
        i.	True if the combination of row and column coordinates was a hit.
            1.	Update board to reflect hit
        ii.	False if the combination of row and column coordinates was a miss.
            1.	Update board to reflect miss
10.	Define a function main(myboard):
    a.	This function ties everything together and calls the program.
    b.	This function accepts one input, myboard.
    c.	Call generate_ship_coordinates() and save output
    d.	Call setupboard(grid, ship_locations)
    e.	Instantiate ship_sunk_counter with zero
    f.	While loop that runs as long as ship_sunk_counter is less than zero.
        i.	Call drawBoard(myboard).
        ii.	Call get_user_coordinates(“row”) and save the output.
        iii.	Call get_user_coordinates(“column”) and save the output.
        iv.	Call hitormiss(myboard, row, col) and save output
        v.	If a ship was hit and ship_sunk_counter is equal to 4
            1.	Increment ship_sunk_counter by 1
            2.	Call drawboard(myboard).
            3.	print game over
            4.	Break loop to end the game.
        vi.	If a ship was hit 
            1.	Increment ship_sunk_counter by 1
            2.	Calculate how many ships remaining on board
            3.	Print status message that includes the number of remaining ships.
            4.	Continue loop
        vii.	If no ship was hit
            1.	Print status message
            2.	Continue loop
        viii.	When all ships have been hit, GAME OVER!
11.	Call the main function to run the program if the script is executed directly.
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

def setupboard(myboard, ship_locations):
    """
    This function set's up the board with the ship icons and dots for the water.<br>

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
        try:
            # Getting the user input
            user_input = input(f"\nEnter a {location} Number between 0 and 9:\n:> ")

            # Logic to prevent the user from entering anything other than an int
            if not user_input.isdigit():
                raise ValueError(f"\nInvalid {location} your input must be a number between 0 and 9\n")
            else:
                user_input = int(user_input)

            if user_input == 0:
                return user_input

            if user_input < 0 or user_input > 9:
                raise ValueError(f"\nInvalid {location} your input must between 0 and 9\n")
            else:
                return user_input
        except ValueError as err:
            print(err)
        
        
def hitorMiss(myboard, row, col):
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
        setupboard(grid, ship_locations)

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
            contact = hitorMiss(myboard, row, column)

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
