from utils import parse_input

FILE_PATH = 'nput.txt'

parsed_input = parse_input(FILE_PATH)


def solution_part_one(parsed_input):
    res = []
    counter = 0

    tree = get_file_structure(parsed_input)
    for key, value in tree.items():



    print(tree)


    return counter


def get_file_structure(parsed_input):
    tree = {"root": {}}
    cur_dir = tree["root"]
    prev_dir = [cur_dir]
    for command in parsed_input:
        if command.startswith("$ cd"):
            [_, _, to_dir_name] = command.split(" ")
            if to_dir_name.isalpha() or to_dir_name == "root":
                prev_dir.append(cur_dir)
                cur_dir = cur_dir[to_dir_name]
            elif to_dir_name == "..":
                cur_dir = prev_dir.pop()
        elif command.startswith("$ ls"):
            continue
        elif command.startswith("dir"):
            [_, dir_name] = command.split(" ")
            cur_dir[dir_name] = {}
        else:
            [size, file_name] = command.split(" ")
            cur_dir[file_name] = int(size)
    return tree


# def solution_part_two(parsed_string):
#     res = []
#     counter = 0
#     for char in parsed_string[0]:
#         if char in res:
#             while char in res:
#                 res.pop(0)
#         res.append(char)
#         counter += 1
#         if len(res) > 13: return counter
#     return counter


print(solution_part_one(parsed_input))
# print(solution_part_two(parsed_input))
