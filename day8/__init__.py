from functools import reduce

from utils import parse_input

FILE_PATH = 'input.txt'

parsed_input = parse_input(FILE_PATH)


def solution_part_one(parsed_input):
    grid = get_grid(parsed_input)

    vis = {}

    ROWS, COLS = len(grid), len(grid[0])

    range_row = range(ROWS)
    range_column = range(COLS)

    scan_from_top_bottom(grid, [-1] * COLS, range_column, range_row, vis)

    range_row = range(ROWS - 1, 0, -1)
    scan_from_top_bottom(grid, [-1] * COLS, range_column, range_row, vis)

    scan_from_side(grid, [-1] * ROWS, range_column, range_row, vis)

    range_column = range(COLS - 1, 0, -1)
    scan_from_side(grid, [-1] * ROWS, range_column, range_row, vis)

    print(len(vis))


def scan_from_top_bottom(grid, max_down, range_column, range_row, vis):
    for row_idx in range_row:
        for col_idx in range_column:
            if grid[row_idx][col_idx] > max_down[col_idx]:
                max_down[col_idx] = grid[row_idx][col_idx]
                vis[(row_idx, col_idx)] = True
            else:
                continue


def scan_from_side(grid, max_right, range_column, range_row, vis):
    for row_idx in range_row:
        for col_idx in range_column:
            if grid[row_idx][col_idx] > max_right[row_idx]:
                max_right[row_idx] = grid[row_idx][col_idx]
                vis[(row_idx, col_idx)] = True
            else:
                continue


def get_empty_grid(COLS, ROWS):
    empty_grid = []
    FOUR_DIRECTIONS = 4
    for row in range(ROWS):
        empty_grid_row = []
        for col in range(COLS):
            directions = [0] * FOUR_DIRECTIONS
            empty_grid_row.append(directions)
        empty_grid.append(empty_grid_row)
    return empty_grid


def get_grid(parsed_input):
    grid = []
    for line in parsed_input:
        row = []
        grid.append(row)
        for char in line:
            row.append(int(char))
    return grid


def solution_part_two(parsed_input):
    grid = get_grid(parsed_input)

    ROWS, COLS = len(grid), len(grid[0])

    empty_grid = get_empty_grid(COLS, ROWS)
    print(empty_grid)

    for row_idx in range(ROWS):
        for col_idx in range(COLS):
            current_tree = grid[row_idx][col_idx]
            # go_up
            counter_index = row_idx
            while counter_index > -1:
                counter_index -= 1
                if counter_index > -1:
                    if current_tree > grid[counter_index][col_idx]:
                        empty_grid[row_idx][col_idx][0] += 1
                    else:
                        empty_grid[row_idx][col_idx][0] += 1
                        break

            # go_down
            counter_index = row_idx
            while counter_index < ROWS:
                counter_index += 1
                if counter_index < ROWS:
                    if current_tree > grid[counter_index][col_idx]:
                        empty_grid[row_idx][col_idx][2] += 1
                    else:
                        empty_grid[row_idx][col_idx][2] += 1
                        break
            # go_left
            counter_index = col_idx
            while counter_index > -1:
                counter_index -= 1
                if counter_index > -1:
                    if current_tree > grid[row_idx][counter_index]:
                        empty_grid[row_idx][col_idx][1] += 1
                    else:
                        empty_grid[row_idx][col_idx][1] += 1
                        break

            # go_right
            counter_index = col_idx
            while counter_index < COLS:
                counter_index += 1
                if counter_index < COLS:
                    if current_tree > grid[row_idx][counter_index]:
                        empty_grid[row_idx][col_idx][3] += 1
                    else:
                        empty_grid[row_idx][col_idx][3] += 1
                        break

    res = []
    for row in empty_grid:
        for col in row:
            res.append(reduce((lambda x, y: x * y), col))

    print(max(res))





# def dfs():
#     if block_tree >= current_tree:
#

print(solution_part_one(parsed_input))
# 488205 fout
# 529468 fout
print(solution_part_two(parsed_input))
