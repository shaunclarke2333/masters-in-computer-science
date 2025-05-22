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

def drawBoard(myBoard):
    # implement draw board here
    return

def setupBoard(myBoard):
    # implement setup board here
    # initialize all grid[i][j] = '.'
    # now place the ships
    # you can get a random row by using
    randomRow = random.randint(0, grid_size - 1)
    randomCol = random.randint(0, grid_size - 1)
    # remember to call myBoard[randomRow][randomCol] = 'S' for every ship

def hitOrMiss(myBoard, row, col):
    # implement the hit or miss functionality here
    return

def isGameOver(myBoard):
    # check if there are ships remaining on the grid.
    # if there are ships remaining, return false else return true
    return False

def main(myBoard):
    # here do everything like
    #   set up the board
    #   till the game is over
    #     draw the board
    #     ask for a row and column and check it is a hit or a miss
    # when the game is over, print that message!
    print('Game over!')
    
# do not forget to call main!
main(grid)
