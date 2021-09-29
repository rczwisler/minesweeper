class Minesweeper():
    def __init__(self, input_bomb_grid):
        try:
            self.bombgrid = self._create_grid(input_bomb_grid)
        except ValueError:
            raise
            print("Invalid Board")
            self.bombgrid = [[]]
        self._fill_grid()
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

    def _fill_grid(self):
        '''
        fills the grid with values based on bomb locations
        '''
        for y_pos in range(len(self.bombgrid)):
            for x_pos in range(len(self.bombgrid[y_pos])):
                if self.bombgrid[y_pos][x_pos].value == "*":
                    self._increment_neighbors(y_pos,x_pos)

    def _increment_neighbors(self, bomb_row, bomb_col):
        '''
        increments all neighbor values by 1
        '''
        yend = len(self.bombgrid)
        for y_pos in range(bomb_row-1,bomb_row+2):
            if y_pos < 0 or y_pos >= yend: continue # skip if not in bomb grid
            xend = len(self.bombgrid[y_pos])
            for x_pos in range(bomb_col-1, bomb_col+2):
                if x_pos == bomb_col and y_pos == bomb_row: continue # only increment neighbors
                elif x_pos < 0 or x_pos >= xend: continue # skip if not in bomb grid
                else:
                    cell = self.bombgrid[y_pos][x_pos]
                    if cell.value == "*": continue # skip if bomb
                    else: cell.value += 1 # increment square
    
    def _print_bomb_grid(self):
        '''
        prints the minesweeper grid
        '''
        for row in self.bombgrid:
            print()
            for cell in row:
                if cell.revealed or self.winner or self.loser:
                    print(str(cell.value), " ", end='')
                else:
                    print("_", " ", end='')
        print()

    def _reveal(self, row, col):
        '''
        checks if a cell is a mine or not and reveals the cell.
        if cell value is 0 recursively reveals all neighboring cells

        Parameters:
            row : int
                the row of the Cell to be checked
            col : int
                the column of the cell to be checked
        '''
        cell = self.bombgrid[row][col]
        cell.revealed = True
        if cell.value == "*":
            self.loser = True
            print("Game over you landed on a mine")
        elif cell.value == 0:
            yend = len(self.bombgrid)
            for y_pos in range(row-1,row+2):
                if y_pos < 0 or y_pos >= yend: continue # skip if not in bomb grid
                xend = len(self.bombgrid[y_pos])
                for x_pos in range(col-1, col+2):
                    if x_pos == col and y_pos == row: continue
                    elif x_pos < 0 or x_pos >= xend: continue # skip if not in bomb grid
                    else:
                        cell = self.bombgrid[y_pos][x_pos]
                        if cell.value == "*": continue # skip if bomb
                        elif cell.revealed:  continue
                        else:
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
    def __init__(self, value):
        self.value = value
        self.revealed = False
