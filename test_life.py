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
    Press space for next
    Press q for quit"""