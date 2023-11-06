ALIVE = 'X'

def get_status(matrix):
    matrix = '\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix])
    status = f"""{matrix}
    Press space for next
    Press q for quit"""
    return status

def get_element_positions(matrix):
    positions = []
    for row in range(7):
        for col in range(7):
            if ALIVE == matrix[row][col]:
                positions.append([row,col])
    return positions

def update_matrix(matrix):
    dead_elements_position = []
    positions = get_element_positions(matrix)
    for p in positions:
        count = 0
        row, col = [e for e in p]
        if row > 0:
            if matrix[row-1][col] == ALIVE:
                count += 1 
            if col > 0:
                if matrix[row-1][col-1] == ALIVE:
                    count += 1
            if col < 6:
                if matrix[row-1][col+1] == ALIVE:
                    count += 1
        if row < 6:
            if matrix[row+1][col] == ALIVE:
                count += 1
            if col < 6:
                if matrix[row+1][col+1] == ALIVE:
                    count += 1
            if col > 0:
                if matrix[row+1][col-1] == ALIVE:
                    count += 1
        if col > 0:
            if matrix[row][col-1] == ALIVE:
                count += 1
        if col < 6:
            if matrix[row][col+1] == ALIVE:
                count += 1
        if count < 2:
            dead_elements_position.append(p)
    for elem in dead_elements_position:
        row, col = [e for e in elem]
        matrix[row][col] = 'O'
    return matrix
        
