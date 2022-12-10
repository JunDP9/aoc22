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
    res = []
    stack = get_cycle_stack(commands)
    specials = [0, 40, 80, 120, 160, 200, 240]
    sprite = (0, 1, 2)
    for index in range(0, len(specials) - 1):
        sprite = generate_line(res, (stack[specials[index]:specials[index + 1]]), sprite)
        print(''.join(res[specials[index]:specials[index + 1]]))

    return "See above"


def generate_line(res, split, sprite):
    for stack_index in range(0, len(split)):
        if sprite[0] == stack_index or sprite[1] == stack_index or sprite[2] == stack_index:
            res.append("#")
        else:
            res.append(" ")

        new_middle_index = sprite[1] + split[stack_index]
        sprite = (new_middle_index-1, new_middle_index, new_middle_index+1)

    return sprite


print(solution_part_one(parsed_input))
print(solution_part_two(parsed_input))
