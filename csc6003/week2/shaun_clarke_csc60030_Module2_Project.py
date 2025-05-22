import random

"""
    -------BATTLESHIPS-------
    Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variables, Methods
    How it will work:
    1. A 10x10 grid will have 5 ships randomly placed about
    2. You can choose a row and column to indicate where to shoot
    3. For every shot that hits or misses it will show up in the grid
    4. If all ships are shot, game over

    Legend:
    1. "." = water
    2. "S" = ship position
    3. "O" = water that was shot with bullet, a miss because it hit no ship
    4. "X" = ship sunk!
"""

# Global variable for grid size
grid_size = 10
# Global variable for grid
grid = [ ['']*grid_size for i in range(grid_size) ]
# Global variable for number of ships to place
num_of_ships = 5

def drawBoard(myboard):
    """
    This function takes the grid as a parameter
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

# Add ships
def add_ships():
    """
    This fucntion takes no parameters
    """
    # Empty set to hold uniqe ship locations
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
    This function takes the grid and the output of add_ships as parameters
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
def get_user_selection(location):

    """
    This function takes 1 parameter:.<br>
    row or column
    This function gets the user inputs for the grid coordinates.<br>
    it returns:<br>
    - The user input if it meets criteria.<br>
    - None if the input is not an integer.<br>
    - "out of range" if the number is not between 0 and 9
    """
    # Getting the user input
    user_input = input(f"\nEnter a {location} Number between 0 and 9:\n:> ")

    # Logic to prevent the user from entering anything other than an int
    if not user_input.isdigit():
       return None
    else:
        user_input = int(user_input)

    if user_input == 0:
        return user_input

    if user_input < 0 or user_input > 9:
        return "out of range"
    else:
        # print(f"\nThe number must be between 0 and 9\n")
        return user_input
        
def hitOrMiss(myboard, row, col):
    # implement the hit or miss functionality here
    location = myboard[row][col]

    if location == "S":
        myboard[row][col] = "X"
        return True
    elif location != "S":
        myboard[row][col] = "O"
        return False


def main(myboard):
    try:
        ship_locations = add_ships()
        setupBoard(grid, ship_locations)

        ship_sunk_counter = 0
        
        while ship_sunk_counter < 5:

            # Displaying the board to the user
            print(f"\n{'Shall we play a game?':^{50}}")
            drawBoard(grid)

            # row and column variables
            row = "row"
            column = "column"

            get_row = get_user_selection(row)
            if get_row == None:
                print(f"\nInvalid {row} your input must be a number between 0 and 9\n")
                continue
            elif get_row == "out of range":
                print(f"\nInvalid {row} your input must between 0 and 9\n")
                continue


            print(get_row)

            get_column = get_user_selection(column)
            if get_column == None:
                print(f"\nInvalid {column} your input must be a number between 0 and 9\n")
                continue
            elif get_column == "out of range":
                print(f"\nInvalid {column} your input must between 0 and 9\n")
                continue
            
            print(get_column)

            contact = hitOrMiss(grid, get_row, get_column)

            if contact:
                ship_sunk_counter += 1
                print(f"You sunk my battleship! sink {num_of_ships - ship_sunk_counter} more ships and you win")
                continue
            else:
                print(f"Are you even trying?")
                continue





        # here do everything like
        #   set up the board
        #   till the game is over
        #     draw the board
        #     ask for a row and column and check it is a hit or a miss
        # when the game is over, print that message!
        # print('Game over!')
    except TypeError as e:
        print(f"\nYour input must be a number\n")
    
# do not forget to call main!
main(grid)






# while True:

#     pass

# def isGameOver(myboard):
#     # check if there are ships remaining on the grid.
#     # if there are ships remaining, return false else return true
#     return False