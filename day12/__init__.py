import heapq
import string

from utils import parse_input

FILE_PATH = 'input.txt'

parsed_input = parse_input(FILE_PATH)


def get_alphanumeric_value(char):
    return string.ascii_lowercase.index(char) + 1


def get_grid_start_end(parsed_input):
    grid, start, end = get_grid_st_en(parsed_input)

    return get_weighted_start_end(grid, start, end)


def get_grid_st_en(parsed_input):
    grid = []
    start, end = (0, 0), (0, 0)
    for row_index in range(len(parsed_input)):
        row = []
        grid.append(row)
        for col_index in range(len(parsed_input[row_index])):
            char = parsed_input[row_index][col_index]
            if char == "S":
                start = (row_index, col_index)
                row.append(0)
            elif char == "E":
                end = (row_index, col_index)
                row.append(27)
            else:
                row.append(get_alphanumeric_value(char))
    return grid, start, end


def get_weighted_start_end(grid, start, end):
    weighted_grid = []
    for row_index in range(len(grid)):
        weighted_row = []
        weighted_grid.append(weighted_row)
        for col_index in range(len(grid[row_index])):
            value = grid[row_index][col_index]

            north_weight = get_difference(row_index - 1, col_index, grid, value)
            south_weight = get_difference(row_index + 1, col_index, grid, value)
            east_weight = get_difference(row_index, col_index + 1, grid, value)
            west_weight = get_difference(row_index, col_index - 1, grid, value)

            weighted_row.append([north_weight, east_weight, south_weight, west_weight])
    return weighted_grid, start, end


def get_difference(row_index, col_index, grid, origin_value):
    if (-1 < row_index < len(grid)) and \
            (-1 < col_index < len(grid[0])):
        return grid[row_index][col_index] - origin_value
    else:
        return 1000


def solution_part_one(parsed_input):
    visited = set()
    [grid, start, end] = get_grid_start_end(parsed_input)
    minHeap = [(0, start)]
    t = 0
    counter = 0

    while minHeap and end not in visited:
        weight, position = heapq.heappop(minHeap)
        [row_index, col_index] = position

        if position in visited:
            continue
        visited.add(position)
        [north_value, east_value, south_value, west_value] = (grid[row_index][col_index])
        t = max(t, counter)
        counter += 1

        north_position = (row_index - 1, col_index)
        east_position = (row_index, col_index + 1)
        south_position = (row_index + 1, col_index)
        west_position = (row_index, col_index - 1)

        if north_value <= 1 and north_position not in visited:
            heapq.heappush(minHeap, (weight + 1, north_position))
        if east_value <= 1 and east_position not in visited:
            heapq.heappush(minHeap, (weight + 1, east_position))
        if south_value <= 1 and south_position not in visited:
            heapq.heappush(minHeap, (weight + 1, south_position))
        if west_value <= 1 and west_position not in visited:
            heapq.heappush(minHeap, (weight + 1, west_position))
        print(minHeap)
    print(counter)
    return t


def solution_part_two(parsed_input):
    visited = {}
    [grid, start, end] = get_grid_st_en(parsed_input)

    ROWS, COLS = len(grid), len(grid[0])
    counter = 0

    def dfs(node, vis, prev_value):
        [char, row_index, col_index] = node

        if char <= prev_value + 1 or \
                node in vis or \
                row_index == ROWS or \
                col_index == COLS:
            return

        if node == end:
            return counter

        vis[node] = True
        dfs((row_index + 1, col_index), vis, char)
        dfs((row_index - 1, col_index), vis, char)
        dfs((row_index, col_index + 1), vis, char)
        dfs((row_index, col_index - 1), vis, char)

    dfs((start, 0, 0), visited, 0)

    return grid


def solution_part_one_alternate(parsed_input):
    visited = {}
    [grid, start, end] = get_grid_st_en(parsed_input)

    ROWS, COLS = len(grid), len(grid[0])
    queue = [(grid[start[0]][start[1]], start[0], start[1], 0)]

    while len(queue) > 0:
        node = queue.pop(0)
        [char_value, row_index, col_index, counter] = node
        if (row_index, col_index) in visited:
            visited[(row_index, col_index)] = min(counter, visited[(row_index, col_index)])
            continue
        visited[(row_index, col_index)] = counter

        if row_index + 1 < ROWS and grid[row_index + 1][col_index] <= char_value + 1:
            queue.append((grid[row_index + 1][col_index], row_index + 1, col_index, counter + 1))
        if 0 <= row_index - 1 and grid[row_index - 1][col_index] <= char_value + 1:
            queue.append((grid[row_index - 1][col_index], row_index - 1, col_index, counter + 1))
        if col_index + 1 < COLS and grid[row_index][col_index + 1] <= char_value + 1:
            queue.append((grid[row_index][col_index + 1], row_index, col_index + 1, counter + 1))
        if 0 <= col_index - 1 and grid[row_index][col_index - 1] <= char_value + 1:
            queue.append((grid[row_index][col_index - 1], row_index, col_index - 1, counter + 1))

    return grid


print(solution_part_one_alternate(parsed_input))
# print(solution_part_two(parsed_input))
