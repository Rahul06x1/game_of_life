from life import *


def test_get_status():
    matrix = [
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, ALIVE, ALIVE, ALIVE, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
    ]
    assert (
        get_status(matrix)
        == f"""{DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   

{DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   

{DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   

{DEAD}   {DEAD}   {ALIVE}   {ALIVE}   {ALIVE}   {DEAD}   {DEAD}   

{DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   

{DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   

{DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   {DEAD}   
    Press any key for next
    Press q for quit"""
    )


def test_get_cell_positions_alive():
    status = ALIVE
    matrix = [
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, ALIVE, ALIVE, ALIVE, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
    ]
    assert get_cell_positions(matrix, status) == [[3, 2], [3, 3], [3, 4]]


def test_get_cell_positions_dead():
    status = DEAD
    matrix = [
        [ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE],
        [ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE],
        [ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE],
        [ALIVE, ALIVE, DEAD, DEAD, DEAD, ALIVE, ALIVE],
        [ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE],
        [ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE],
        [ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE],
    ]
    assert get_cell_positions(matrix, status) == [[3, 2], [3, 3], [3, 4]]


def test_update_matrix_less_than_two_alive_neighbors():
    matrix = [
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD],
        [DEAD, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, DEAD],
        [DEAD, DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
    ]
    matrix = update_matrix(matrix)
    assert matrix[1][3] == DEAD
    assert matrix[3][1] == DEAD
    assert matrix[3][5] == DEAD
    assert matrix[5][3] == DEAD


def test_update_matrix_alive_cell_in_sides():
    matrix = [
        [ALIVE, DEAD, DEAD, ALIVE, DEAD, DEAD, ALIVE],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, ALIVE],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [ALIVE, DEAD, DEAD, ALIVE, DEAD, DEAD, ALIVE],
    ]
    expected_matrix = [
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
    ]

    assert update_matrix(matrix) == expected_matrix


def test_update_matrix_more_than_three_alive_neighbors():
    matrix = [
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, ALIVE, DEAD, DEAD],
        [DEAD, DEAD, ALIVE, ALIVE, ALIVE, DEAD, DEAD],
        [DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
    ]
    matrix = update_matrix(matrix)
    assert matrix[3][3] == DEAD


def test_update_matrix_revive_dead_cell_having_three_alive_neighbors():
    matrix = [
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, "0", DEAD, DEAD],
        [DEAD, DEAD, ALIVE, ALIVE, ALIVE, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
    ]
    matrix = update_matrix(matrix)
    assert matrix[2][3] == ALIVE
    assert matrix[2][3] == ALIVE

def test_toggle_cell_state():
    row = 0
    col = 0 
    matrix = [
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
    ]
    expected_matrix = [
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
    ]
    assert toggle_cell_state(matrix, row, col) == expected_matrix
