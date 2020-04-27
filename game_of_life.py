import numpy as np
import random

####################################################
# VARIABLES

# board size
width = 10
height = 10

# boundary for rounding function
boundary = 0.5
###################################################

# 1. Build a data structure to store the board state

# round values in matrix to be either 0 or 1 
rounder = lambda x: 0 if x < boundary else 1 
vrounder = np.vectorize(rounder)

def random_state(width = width, height = height):
    """Create np matrix where entries are 0 or 1 by random

    Keyword Arguments:
        width {integer} -- number of columns of the matrix (default: {width})
        height {integer} -- number of rows of the matrix (default: {height})

    Returns:
        rand_matrix -- matrix with randomly assigned values of 0 or 1
    """
    # create matrix with random values between 0 and 1
    rand_matrix = np.random.rand(width, height)
    return vrounder(rand_matrix)

initial_state = random_state()



# 2. Pretty-print the board to the terminal


def render(game_state):
    """for a matrix of 0's and 1's generate a output where 1's are '#' and 0's
    are spaces " "

    Arguments:
        game_state {numpy matrix} -- numpy matrix with 0's and 1's as entries
    """
    output = ""
    for h in range(game_state.shape[0]):
        for w in range(game_state.shape[1]):
            output += "#" if game_state[h][w] == 1 else " "
        output+="\n"

    print(output)

# test functionality
initial_state = random_state(100,50)
render(initial_state)








# 3. Given a starting board state, calculate the next one


# 4. run the game forever 

