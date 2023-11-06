def get_status(matrix):
    matrix = '\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix])
    status = f"""{matrix}
    Press space for next
    Press q for quit"""
    return status

def get_element_positions(matrix):
    item = 'X'
    positions = []
    for row in range(7):
        for col in range(7):
            if item == matrix[row][col]:
                positions.append([row,col])
    return positions
