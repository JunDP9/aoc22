from utils import parse_input

FILE_PATH = 'input.txt'

parsed_input = parse_input(FILE_PATH)


def solution_part_one(commands):
    # suboptimal two iterations solution
    stack = [1]
    for command in commands:
        stack.append(0)
        if command == "noop":
            pass
        else:
            stack.append(int(command.split(" ")[1]))

    print(stack)

    specials = [20,
                60,
                100,
                140,
                180,
                220]

    total_sum = 0
    for special in specials:
        total_sum += sum(stack[:special]) * special
    return total_sum


print(solution_part_one(parsed_input))
# print(solution_part_two(parsed_input))
