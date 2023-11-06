from life import *

def test_get_status():
    matrix = [
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","X","X","X","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"]
    ]
    assert get_status(matrix) == """O   O   O   O   O   O   O   
O   O   O   O   O   O   O   
O   O   O   O   O   O   O   
O   O   X   X   X   O   O   
O   O   O   O   O   O   O   
O   O   O   O   O   O   O   
O   O   O   O   O   O   O   
    Press any key for next
    Press q for quit"""

def test_get_cell_positions_alive():
    status = ALIVE
    matrix = [
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","X","X","X","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"]
    ]
    assert get_cell_positions(matrix,status) == [[3, 2], [3, 3], [3, 4]]

def test_update_matrix_less_than_two_alive_neighbors():
    matrix = [
        ["O","O","O","O","O","O","O"],
        ["O","O","O","X","O","O","O"],
        ["O","O","O","X","O","O","O"],
        ["O","X","X","X","X","X","O"],
        ["O","O","O","X","O","O","O"],
        ["O","O","O","X","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ]
    matrix = update_matrix(matrix)
    assert matrix[1][3] == DEAD
    assert matrix[3][1] == DEAD
    assert matrix[3][5] == DEAD
    assert matrix[5][3] == DEAD

def test_update_matrix_alive_cell_in_sides():
    matrix = [
        ["X","O","O","X","O","O","X"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["X","O","O","O","O","O","X"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["X","O","O","X","O","O","X"]
    ]
    expected_matrix = [
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"]
    ]

    assert update_matrix(matrix) == expected_matrix

def test_update_matrix_more_than_three_alive_neighbors():
    matrix = [
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","X","O","O"],
        ["O","O","X","X","X","O","O"],
        ["O","O","X","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"]
    ]
    matrix = update_matrix(matrix)
    assert matrix[3][3] == DEAD

def test_update_matrix_revive_dead_cell_having_three_alive_neighbors():
    matrix = [
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","0","O","O"],
        ["O","O","X","X","X","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"]
    ]
    matrix = update_matrix(matrix)
    assert matrix[2][3] == ALIVE
    assert matrix[2][3] == ALIVE