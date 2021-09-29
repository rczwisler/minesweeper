# minesweeper

## Two versions
- minesweeper.py
    - minesweeper implemented as per the instructions
    - evaluates neighboring squares as the player chooses cells
- myminesweeper.py
    - minesweeper with slightly different implementation
    - evaluates all cells on creation
 ## To play the game
 - import the module
     - `from minesweeper import Minesweeper` or `from myminesweeper import Minesweeper`
 - define a board grid
     - `bombGrid = [
        [ 0, 0, 1, 0, 0, 1 ],
        [ 0, 0, 1, 1, 1, 0 ],
        [ 0, 0, 1, 1, 0, 0 ],
        [ 0, 0, 1, 0, 0, 0 ],
        [ 0, 1, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 0 ]]`
- create the game 
    - `game = Minesweeper(bombGrid)`
- play by checking cells using the checkCell method 
    - `game.checkCell(0,0)`
