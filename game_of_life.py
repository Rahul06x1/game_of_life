from curses import (
    curs_set,
    mousemask,
    ALL_MOUSE_EVENTS,
    KEY_ENTER,
    KEY_MOUSE,
    getmouse,
    wrapper,
)
from life import (
    update_matrix,
    toggle_cell_state,
    DEAD,
    ALIVE,
    DISPLAY_ALIVE,
    DISPLAY_DEAD,
)


message = """Press ENTER to generate
Press ESC to exit
"""


def display_matrix(win, matrix):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == DEAD:
                win.addch(i, j * 2, DISPLAY_DEAD)  # Display dead cells
            elif value == ALIVE:
                win.addch(i, j * 2, DISPLAY_ALIVE)  # Display alive cells

    win.addstr(len(matrix) + 1, 0, message)


def main(stdscr):
    matrix = [[DEAD for _ in range(7)] for _ in range(7)]
    curs_set(0)
    stdscr.keypad(1)
    mousemask(ALL_MOUSE_EVENTS)

    while True:
        stdscr.clear()
        display_matrix(stdscr, matrix)
        stdscr.refresh()

        key = stdscr.getch()
        if key == 27:  # Exit on 'Esc' key
            break
        elif (
            key == KEY_ENTER or key == 10 or key == 13
        ):  # Generate matrix on 'Enter' key
            stdscr.clear()
            matrix = update_matrix(matrix)
            stdscr.addstr(len(matrix) + 1, 0, message)
            stdscr.refresh()
        elif key == KEY_MOUSE:
            _, mx, my, _, _ = getmouse()
            row, col = my, mx // 2  # Convert mouse coordinates to matrix coordinates
            if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
                matrix = toggle_cell_state(matrix, row, col)


if __name__ == "__main__":
    wrapper(main)
