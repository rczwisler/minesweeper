'''
Create a minesweeper game

Classes:
    Minesweeper
    Cell
'''
class Minesweeper():
    '''
    A class to represent a game of Minesweeper

    Methods
    -------
    checkCell(row, col)
        checks a cell for mines and reveals the cell
    '''
    def __init__(self, input_bomb_grid):
        try:
            self.bombgrid = self._create_grid(input_bomb_grid)
        except ValueError:
            print("Invalid value in input grid. please try again")
            raise
        self.loser = False
        self.winner = False

    def _create_grid(self, input_bomb_grid):
        '''
        constructs the minesweeper board out of Cells from input grid supplied

        Parameters:
            input_bomb grid : list[list[int]]
                the bomb grid to be played

        Returns:
            bomb_grid : list[list[Cell]]
        '''
        bomb_grid = input_bomb_grid.copy()
        for row in range(len(input_bomb_grid)):
            for col in range(len(input_bomb_grid[row])):
                if input_bomb_grid[row][col] != 0 and input_bomb_grid[row][col] != 1:
                    raise ValueError
                if input_bomb_grid[row][col] == 1:
                    input_bomb_grid[row][col] = "*"
                bomb_grid[row][col] = Cell(input_bomb_grid[row][col])
        return bomb_grid

    def _print_bomb_grid(self):
        '''
        prints the minesweeper grid
        '''
        for row in self.bombgrid:
            print()
            for cell in row:
                if cell.revealed or self.winner:
                    print(str(cell.value), " ", end='')
                else:
                    print("_", " ", end='')
        print()

    def _count_neighboring_bombs(self, row, col):
        '''
        counts the number of bombs in neighboring cells and
        sets the current Cell's value to the number of neighboring bombs

        Parameters:
            row : int
                the row of the Cell to check all neighbors
            col : int
                the column of the Cell to check all neighbors
        '''
        neighboring_bombs = 0
        yend = len(self.bombgrid)
        for y_pos in range(row-1,row+2):
            if y_pos < 0 or y_pos >= yend:
                continue # skip if not in bomb grid
            xend = len(self.bombgrid[y_pos])
            for x_pos in range(col-1, col+2):
                if x_pos == col and y_pos == row:
                    continue
                if x_pos < 0 or x_pos >= xend:
                    continue
                if self.bombgrid[y_pos][x_pos].value == "*":
                    neighboring_bombs += 1
        self.bombgrid[row][col].value = neighboring_bombs

    def _reveal(self, row, col):
        '''
        checks if a cell is a mine or not and reveals the cell.
        if cell value is 0 reveals all neighboring cells

        Parameters:
            row : int
                the row of the Cell to be checked
            col : int
                the column of the cell to be checked
        '''
        cell = self.bombgrid[row][col]
        cell.revealed = True
        if cell.value == "*":
            print('Game over you landed on a mine')
            self.loser = True
        else:
            self._count_neighboring_bombs(row, col)
            if cell.value == 0:
                yend = len(self.bombgrid)
                for y_pos in range(row-1,row+2):
                    if y_pos < 0 or y_pos >= yend:
                        continue
                    xend = len(self.bombgrid[y_pos])
                    for x_pos in range(col-1, col+2):
                        if x_pos == col and y_pos == row:
                            continue
                        if x_pos < 0 or x_pos >= xend:
                            continue
                        cell = self.bombgrid[y_pos][x_pos]
                        if cell.value == "*":
                            continue
                        if cell.revealed:
                            continue
                        self._reveal(y_pos, x_pos)


    def _check_win(self):
        '''
        checks to see if the player has won the game
        '''
        won = True
        for row in self.bombgrid:
            for cell in row:
                if not cell.revealed and cell.value != "*":
                    won = False
        self.winner = won
        if self.winner:
            print("WINNER!")


    def checkCell(self, row, col):
        '''
        Checks to see if cell is bomb or not,
        reveals adjacent non bomb cells and prints the game board

        Parameters:
            row: int
                the row of the cell to be checked
            col: int
                the column of the cell to be checked
        '''
        try:
            if self.winner:
                print("You already won. Please start a new game")
            elif self.loser:
                print("You already lost. Please start a new game")
            else:
                self._reveal(row, col)
        except (IndexError, TypeError):
            print("Cell does not exist. please try again")
            raise
        self._check_win()
        self._print_bomb_grid()

class Cell():
    '''
    Class to represent a cell on a minesweeper board
    '''
    def __init__(self, value):
        self.value = value
        self.revealed = False
