#from minesweeper import Minesweeper
import pytest
from minesweeper import Minesweeper

def test_example():
    bombGrid = [
        [ 0, 0, 1, 0, 0, 1 ],
        [ 0, 0, 1, 1, 1, 0 ],
        [ 0, 0, 1, 1, 0, 0 ],
        [ 0, 0, 1, 0, 0, 0 ],
        [ 0, 1, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 0 ]
    ]

    game = Minesweeper(bombGrid)
    game.checkCell(5,5)
    assert game.bombgrid[5][5].value == 1
    game.checkCell(0,3)
    assert game.bombgrid[0][3].value == 4
    game.checkCell(0,0)
    assert game.bombgrid[0][0].value == 0
    assert game.bombgrid[1][0].value == 0
    assert game.bombgrid[2][0].value == 0
    assert game.bombgrid[3][0].value == 1
    assert game.bombgrid[0][1].value == 2
    assert game.bombgrid[1][1].value == 3
    assert game.bombgrid[2][1].value == 3
    assert game.bombgrid[3][1].value == 3
    game.checkCell(0,2)
    assert game.loser == True

def test_empty_board():
    bombGrid = [[]]
    game = Minesweeper(bombGrid)

def test_bad_cell():
    bombGrid = [
        [0, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    game = Minesweeper(bombGrid)
    game.checkCell(-1,0)
    game.checkCell(0,-1)
    game.checkCell(0,10)
    game.checkCell(10,0)
    
def test_all_bombs():
    bombGrid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    game = Minesweeper(bombGrid)
    game.checkCell(0,0)
    assert game.loser == True

def test_no_bombs():
    bombGrid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    game = Minesweeper(bombGrid)
    game.checkCell(1,1)
    assert game.winner == True

def test_win():
    bombGrid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    game = Minesweeper(bombGrid)
    game.checkCell(1,1)
    assert game.winner == False
    game.checkCell(2,2)
    assert game.winner == True

def test_wierd_grid():
    bombGrid = [
        [0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0],
        [0, 0, 0, 1, 0]
    ]
    game = Minesweeper(bombGrid)
    game.checkCell(0,0)
    game.checkCell(1,2)
    game.checkCell(1,3)
    game.checkCell(1,4)
    game.checkCell(3,0)
    game.checkCell(4,4)
    game.checkCell(2,4)
    assert game.winner == True

def test_bad_grid():
    bombGrid = [
        [2, 0, 0],
        [0, 0, 0]
    ]
    with pytest.raises(ValueError):
        game = Minesweeper(bombGrid)

def test_bad_cell_index():
    bombGrid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    game = Minesweeper(bombGrid)
    with pytest.raises(IndexError):
        game.checkCell(0,4)
        game.checkCell(4,0)

def test_bad_type_input():
    bombGrid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    game = Minesweeper(bombGrid)
    with pytest.raises(TypeError):
        game.checkCell("foo",3)
        game.checkCell(4,[0])