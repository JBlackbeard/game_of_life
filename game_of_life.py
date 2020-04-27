import numpy as np
import random
from time import sleep
import sys
import curses
import os

####################################################
# VARIABLES

# board size
n_rows_init = 55
n_cols_init = 210

# boundary for rounding function
boundary = 0.5
###################################################

# 1. Build a data structure to store the board state

# round values in matrix to be either 0 or 1 
rounder = lambda x: 0 if x < boundary else 1 
vrounder = np.vectorize(rounder)

def random_state(n_rows = n_rows_init, n_cols = n_cols_init):
    """Create np matrix where entries are 0 or 1 by random

    Keyword Arguments:
        n_rows {integer} -- number of columns of the matrix (default: {n_rows})
        n_cols {integer} -- number of rows of the matrix (default: {n_cols})

    Returns:
        rand_matrix -- matrix with randomly assigned values of 0 or 1
    """
    # create matrix with random values between 0 and 1
    rand_matrix = np.random.rand(n_rows, n_cols)
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
    for x in range(game_state.shape[0]):
        for y in range(game_state.shape[1]):
            output += u"\u2588" if game_state[x][y] == 1 else " "
        output+="\n"

    #print(output)
    return output








# 3. Given a starting board state, calculate the next one

def cell_decision(alive, neighbor_count, death_count = [0,1], stay_count = [2,3], reprod_count = 3):
    """Decide if cell should be dead or alive depending on number of living neighbors

    Arguments:
        alive {Boolean} -- is input cell dead or alive
        neighbor_count {integer} -- Number of living neighbors of the cell

    Keyword Arguments:
        death_count {list} -- if neighbors have one of these counts the cell dies (default: {[0,1]})
        stay_count {list} -- if neighbors have one of these counts the cell stays alive (default: {[2,3]})
        reprod_count {int} -- if cell is dead and neighbors have this count, the cell starts to live (default: {3})

    Returns:
        0 or 1 -- returns 0 if cell is dead, 1 otherwise
    """
    if alive:
        if neighbor_count in death_count or neighbor_count > max(stay_count):
            return 0
        else:
            return 1
    else:
        if neighbor_count == reprod_count:
            return 1
        else: 
            return 0





def next_board_state(cur_state):
    """calculate next generation of the game by applying the rules of cell_decision() to current board state

    Arguments:
        cur_state {np.array} -- numpy matrix with 0's and 1's

    Returns:
        np.array -- numpy matrix with 0's and 1's
    """
    new_state = np.zeros((cur_state.shape[0], cur_state.shape[1]))
    n_cols = cur_state.shape[0]
    n_rows = cur_state.shape[1]
    for x in range(n_cols):
        for y in range(n_rows):
            neighbor_count = 0
            for x1 in range((x-1), (x+1)+1):
                if x1 < 0:
                    x1 = n_cols-1
                if x1 >= n_cols:
                    x1 = 0
                for y1 in range((y-1), (y+1)+1):
                    if y1 < 0:
                        y1 = n_rows-1
                    if y1 >= n_rows:
                        y1 = 0
                    if x1 != x or y1 != y:
                        neighbor_count+=cur_state[x1][y1]
                    #print(f"x1:{x1}, y1: {y1}")
                    #print(neighbor_count)
                    #print(cur_state[x1][y1])
            #print(f"{x,y}")
            #print(f"neighbor_count: {neighbor_count} for coord. {x,y}")
            new_state[x][y] = cell_decision(cur_state[x][y], neighbor_count)

    return new_state




# 4. run the game forever 
def main(window):
    initial_state = random_state(os.get_terminal_size().lines-1, os.get_terminal_size().columns-1)
    state = next_board_state(initial_state)
    window.addstr(render(state))
    window.refresh()
    while True:
        window.clear()
        state = next_board_state(state)
        window.addstr(render(state))
        window.refresh()
        sleep(0.05)
curses.wrapper(main)
