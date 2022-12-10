from utils import parse_input

FILE_PATH = 'input.txt'

parsed_input = parse_input(FILE_PATH)


def solution_part_one(commands):
    stack = get_cycle_stack(commands)
    specials = [20, 60, 100, 140, 180, 220]

    return sum(sum(stack[:special]) * special for special in specials)


def get_cycle_stack(commands):
    stack = [1]
    for command in commands:
        stack.append(0)
        if command == "noop":
            pass
        else:
            stack.append(int(command.split(" ")[1]))
    return stack


def solution_part_two(commands):
    stack = get_cycle_stack(commands)

    specials = [0, 40, 80, 120, 160, 200, 240]

    res = []

    sprite_left_index, sprite_middle_index, sprite_right_index = 0, 1, 2
    for index in range(0, len(specials) - 1):
        sprite_left_index, sprite_middle_index, sprite_right_index = generate_line(res, (stack[specials[index]:specials[index + 1]]), sprite_left_index, sprite_middle_index, sprite_right_index)
    print(''.join(res[:40]))
    print(''.join(res[40:80]))
    print(''.join(res[80:120]))
    print(''.join(res[120:160]))
    print(''.join(res[160:200]))
    print(''.join(res[200:240]))

    return "none"


def generate_line(res, split, sprite_left_index, sprite_middle_index, sprite_right_index):
    for stack_index in range(0, len(split)):

        if sprite_left_index == stack_index or sprite_middle_index == stack_index or sprite_right_index == stack_index:
            res.append("#")
        else:
            res.append(" ")

        sprite_middle_index += split[stack_index]
        sprite_left_index = sprite_middle_index - 1
        sprite_right_index = sprite_middle_index + 1

    return sprite_left_index, sprite_middle_index, sprite_right_index


print(solution_part_one(parsed_input))
print(solution_part_two(parsed_input))
