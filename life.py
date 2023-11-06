def get_status(matrix):
    matrix = '\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix])
    status = f"""{matrix}
    Press space for next
    Press q for quit"""
    return status

print(get_status([
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","X","X","X","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"]
    ]))