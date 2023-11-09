ALIVE = True
DEAD = False
DISPLAY_ALIVE = "■"
DISPLAY_DEAD = "□"


def toggle_cell_state(matrix, row, col):
    if matrix[row][col] == DEAD:
        matrix[row][col] = ALIVE
    elif matrix[row][col] == ALIVE:
        matrix[row][col] = DEAD
    return matrix


def get_cell_positions(matrix, status):
    positions = []
    for row in range(7):
        for col in range(7):
            if status == matrix[row][col]:
                positions.append([row, col])
    return positions


def get_neighbor_cell_positions(position, matrix, status):
    cell_positions = []
    for p in position:
        count = 0
        row, col = [e for e in p]
        if row > 0:
            if matrix[row - 1][col] == ALIVE:
                count += 1
            if col > 0:
                if matrix[row - 1][col - 1] == ALIVE:
                    count += 1
            if col < 6:
                if matrix[row - 1][col + 1] == ALIVE:
                    count += 1
        if row < 6:
            if matrix[row + 1][col] == ALIVE:
                count += 1
            if col < 6:
                if matrix[row + 1][col + 1] == ALIVE:
                    count += 1
            if col > 0:
                if matrix[row + 1][col - 1] == ALIVE:
                    count += 1
        if col > 0:
            if matrix[row][col - 1] == ALIVE:
                count += 1
        if col < 6:
            if matrix[row][col + 1] == ALIVE:
                count += 1
        if status == ALIVE:
            if count < 2 or count > 3:
                cell_positions.append(p)
        if status == DEAD:
            if count == 3:
                cell_positions.append(p)
    return cell_positions


def update_matrix(matrix):
    dead_cell_positions = get_cell_positions(matrix, DEAD)
    alive_cell_positions = get_cell_positions(matrix, ALIVE)
    kill_alive_cell_positions = get_neighbor_cell_positions(
        alive_cell_positions, matrix, ALIVE
    )
    revive_dead_cell_positions = get_neighbor_cell_positions(
        dead_cell_positions, matrix, DEAD
    )
    for elem in kill_alive_cell_positions:
        row, col = [e for e in elem]
        matrix[row][col] = DEAD
    for elem in revive_dead_cell_positions:
        row, col = [e for e in elem]
        matrix[row][col] = ALIVE
    return matrix
