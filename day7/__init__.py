from utils import parse_input
from collections import defaultdict

FILE_PATH = 'input.txt'

parsed_input = parse_input(FILE_PATH)


def solution_part_one():
    tree, dirs = get_file_structure()
    # sum_sizes = 0
    # for size in dirs.values():
    #     if size <= 100000:
    #         sum_sizes += size
    return sum(size for size in dirs.values() if size <= 100000)


def get_file_structure():
    path = []
    dirs = defaultdict(int)
    for command in parsed_input:
        if command.startswith("$ cd"):
            [_, _, to_dir_name] = command.split(" ")
            if to_dir_name == "..":
                path.pop()
            else:
                path.append(to_dir_name)
        elif command.startswith("$ ls"):
            continue
        elif not command.startswith("dir"):
            [size, _] = command.split(" ")
            for i in range(len(path)):
                dirs[tuple(path[: i + 1])] += int(size)
    return path, dirs


def solution_part_two():
    tree, dirs = get_file_structure()
    required = 30000000 - (70000000 - dirs[("/",)])
    # min_list = []
    # for size in dirs.values():
    #     if size >= required:
    #         min_list.append(size)
    # print(min(min_list))
    # oneliner thank u reddit
    return min(size for size in dirs.values() if size >= required)


print(solution_part_one())
print(solution_part_two())
# 488205 fout
# 529468 fout
