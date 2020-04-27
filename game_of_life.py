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
    # create matrix with random values between 0 and 1
    rand_matrix = np.random.rand(width, height)
    return vrounder(rand_matrix)

initial_state = random_state()



# 2. Pretty-print the board to the terminal

# 3. Given a starting board state, calculate the next one

# 4. run the game forever 

