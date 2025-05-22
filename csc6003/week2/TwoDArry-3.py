'''
GK  - A program to set up and display a 2 d array of strings
'''

# the size of the 2 d array
grid_size = 10
# this is the array declaration
twoDarry = [ ['']*grid_size for i in range(grid_size) ]

# display the grid (2d array)
def displayArray(thearray):
    for i in range(grid_size):
        for j in range(grid_size):
            print('['+thearray[i][j]+']', end = "")
        print()

# initilize the 2 d array (the grid)
def setupArray(thearray):
    i = j = 0

    while i < grid_size:
        while j < grid_size:
            # store the string "i, j" into the array
            thearray[i][j] = str(i) + "," + str(j)# + " "
            j += 1
        j = 0
        i += 1

# the main function!
def main(thearray):
    # first set up the array
    setupArray(thearray)

    # now display the array
    displayArray(thearray)

# don't forget to call the main function
# lastly do NOT forget to pass the array we declared
main(twoDarry)






