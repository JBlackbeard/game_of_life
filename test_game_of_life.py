import unittest
import numpy as np
from game_of_life import next_board_state, cell_decision

class TestGameOfLife(unittest.TestCase):

    def test_next_board_state(self):
        init_state1 = np.zeros((3,3))
        expected_next_state1 = np.zeros((3,3))

        self.assertIsNone(np.testing.assert_array_equal(next_board_state(init_state1), expected_next_state1))
        
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

        self.assertIsNone(np.testing.assert_array_equal(next_board_state(init_state2),expected_next_state2))

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

        self.assertIsNone(np.testing.assert_array_equal(next_board_state(init_state3),expected_next_state3))


    def test_cell_decision(self):
        # cell without neighbors should die
        self.assertEqual(cell_decision(1, 0), 0)

        self.assertEqual(cell_decision(1,3), 1)

        self.assertEqual(cell_decision(1,5), 0)

        self.assertEqual(cell_decision(0,3), 1)

        self.assertEqual(cell_decision(0,5), 0)





if __name__ == "__main__":
    unittest.main()