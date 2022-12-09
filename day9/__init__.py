import math

from utils import parse_input

FILE_PATH = 'put.txt'

parsed_input = parse_input(FILE_PATH)


def solution_part_one(commands):
    vis = {}
    cur_pos_h = (0, 0)
    cur_pos_t = cur_pos_h
    prev_pos_h = cur_pos_h

    for command in commands:
        [direction, steps] = command.split(" ")
        for step in range(0, int(steps)):
            cur_pos_h = adjust_accordingly(cur_pos_h, direction)
            distance_h_t = get_absolute_distance(cur_pos_h, cur_pos_t)
            if not distance_h_t == math.sqrt(2) and distance_h_t > 1:
                cur_pos_t = prev_pos_h
            vis[cur_pos_t] = "#"
            prev_pos_h = cur_pos_h

    return len(vis)


def get_absolute_distance(cur_pos_h, cur_pos_t):
    return math.sqrt((cur_pos_h[0] - cur_pos_t[0]) ** 2 + (cur_pos_h[1] - cur_pos_t[1]) ** 2)


def adjust_accordingly(cur_pos, direction):
    if direction == "R":
        cur_pos = (cur_pos[0] + 1, cur_pos[1])
    elif direction == "L":
        cur_pos = (cur_pos[0] - 1, cur_pos[1])
    elif direction == "U":
        cur_pos = (cur_pos[0], cur_pos[1] - 1)
    elif direction == "D":
        cur_pos = (cur_pos[0], cur_pos[1] + 1)
    return cur_pos


def solution_part_two(commands):
    vis = {}
    snake = [(0, 0)] * 9
    old_snake = [(0, 0)] * 9

    for command in commands:
        [direction, steps] = command.split(" ")
        for step in range(0, int(steps)):
            for current_snake_index in range(0, len(snake)):
                snake[current_snake_index] = adjust_accordingly(snake[current_snake_index], direction)
                if snake[current_snake_index] == old_snake[current_snake_index]:
                    continue
                prev_snake_index = current_snake_index - 1
                distance_current_next = get_absolute_distance(snake[current_snake_index], snake[prev_snake_index])

                if not distance_current_next == math.sqrt(2) and distance_current_next > 1:
                    snake[current_snake_index] = old_snake[prev_snake_index]

                old_snake[prev_snake_index] = snake[current_snake_index]
                vis[snake[-1]] = "#"
            print("every step", snake)

        print("every command", snake)


    return len(vis)


print(solution_part_one(parsed_input))
print(solution_part_two(parsed_input))
