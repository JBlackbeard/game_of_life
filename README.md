# game_of_life

This is a version of Game of Life, or just *Life*. 
It is not really a game, since there is no winning, losing or actual competition going on. It's an instance of a so-called *cellular automaton*, a system of cells that exist on a grid, where they live, die and evolve according to the rules that govern their world. 
It is played on a 2D grid, where each square in the grid contains a cell, and each cell starts the game as either *alive* or *dead*. 
During each round, each cell looks at its 8 immediate neighbors and counts up the number of them that are currently alive. 
The cell then updates its own liveness according to 4 rules:

1. Any live cell iwth 0 or 1 live nieghbors becomes dead, because of underpopulation.
2. Any live cell with 2 or 3 live nieghbors stays alive, because of their ideal neighborhood.
3. Any live cell with more than 3 live neighbors dies of overpopulation.
4. Any dead cell with exactly 3 live neighbors transitions to a living state, through reproduction


![](/imgs/game_of_life.gif)

