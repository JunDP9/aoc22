from utils import parse_input

FILE_PATH = 'input.txt'

parsed_string = parse_input(FILE_PATH)


def solution_part_one(parsed_string):
    res = []
    counter = 0
    for char in parsed_string[0]:
        if char in res:
            while char in res:
                res.pop(0)
        res.append(char)
        counter += 1
        if len(res) > 3: return counter
    return counter


def solution_part_two(parsed_string):
    res = []
    counter = 0
    for char in parsed_string[0]:
        if char in res:
            while char in res:
                res.pop(0)
        res.append(char)
        counter += 1
        if len(res) > 13: return counter
    return counter


print(solution_part_one(parsed_string))
print(solution_part_two(parsed_string))
