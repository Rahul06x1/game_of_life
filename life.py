ALIVE = 'X'
DEAD = 'O'

def get_status(matrix):
    matrix = '\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix])
    status = f"""{matrix}
    Press any key for next
    Press q for quit"""
    return status

def get_cell_positions(matrix,status):
    positions = []
    for row in range(7):
        for col in range(7):
            if status == matrix[row][col]:
                positions.append([row,col])
    return positions

def update_matrix(matrix):
    kill_alive_cell_positions = []
    alive_cell_positions = get_cell_positions(matrix, ALIVE)
    for p in alive_cell_positions:
        count = 0
        row, col = [e for e in p]
        if row > 0 and col > 0:
            if matrix[row-1][col-1] == ALIVE:
                count += 1
        if row > 0:
            if matrix[row-1][col] == ALIVE:
                count += 1   
        if row > 0 and col < 6:
            if matrix[row-1][col+1] == ALIVE:
                count += 1
        if col < 6:
            if matrix[row][col+1] == ALIVE:
                count += 1
        if row < 6 and col < 6:
            if matrix[row+1][col+1] == ALIVE:
                count += 1
        if row < 6:
            if matrix[row+1][col] == ALIVE:
                count += 1
        if row < 6 and col > 0:
            if matrix[row+1][col-1] == ALIVE:
                count += 1
        if col > 0:
            if matrix[row][col-1] == ALIVE:
                count += 1
        if count < 2 or count > 3:
            kill_alive_cell_positions.append(p)
    for elem in kill_alive_cell_positions:
        row, col = [e for e in elem]
        matrix[row][col] = 'O'
    return matrix

def main():
    matrix = [
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","X","X","X","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"],
        ["O","O","O","O","O","O","O"]
    ]
    print(get_status(matrix))
    while True:
        choice = input()
        if choice in ['q','Q']:
            break
        matrix = update_matrix(matrix)
        print(get_status(matrix))

if __name__ == '__main__':
    main()
        
