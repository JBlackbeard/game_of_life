import numpy as np
from game_of_life import next_board_state

def compare_states(init_state, expected_next_state, test_num = 0):
    """Compare an expected and an actual board state and check if they're equal

    Arguments:
        init_state {np.array} -- initial board state that we calculate the next iteration from 
        expected_next_state {np.array} -- the next state of init_state after applying the next_board_state() function
        test_num {integer} -- Number of the test
    """
    actual_next_state = next_board_state(init_state)
    
    if np.array_equal(actual_next_state ,expected_next_state):
        print(f"PASSED {test_num}")
    else:
        print(f"FAILED {test_num}")
        print(f"Initial: \n {init_state}") 
        print(f"Expected: \n {expected_next_state}")
        print(f"Actual: \n {actual_next_state}")


if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors 
    # should stay dead
    init_state1 = np.zeros((3,3))
    expected_next_state1 = np.zeros((3,3))
    compare_states(init_state1, expected_next_state1, 1)

    # TEST 2: all cells should come alive
    init_state2 = np.array([
        [0,0,1],
        [0,1,1],
        [0,0,0]
        ])
    expected_next_state2 = np.array([
        [1,1,1],
        [1,1,1],
        [1,1,1],
    ])

    compare_states(init_state2, expected_next_state2,2)

    # TEST 3: all cells should die
    init_state3 = np.array([
        [0,0,1],
        [0,1,0],
        [0,0,0]
        ])
    expected_next_state3 = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ])

    compare_states(init_state3, expected_next_state3, 3)