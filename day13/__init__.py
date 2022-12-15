from utils import parse_input

FILE_PATH = 'nput.txt'

parsed_input = parse_input(FILE_PATH)


def special_compare(pair_left, pair_right):
    for left_index in range(0, len(pair_left)):
        if left_index > len(pair_right) - 1:
            return False
        if isinstance(pair_left[left_index], int) and isinstance(pair_right[left_index], int):
            if pair_left[left_index] > pair_right[left_index]:
                return False
        elif isinstance(pair_left[left_index], list) and isinstance(pair_right[left_index], int):
            temp_right_list = [pair_right[left_index]]
            return special_compare(pair_left[left_index], temp_right_list)
        elif isinstance(pair_left[left_index], int) and isinstance(pair_right[left_index], list):
            temp_left_list = [pair_left[left_index]]
            return special_compare(temp_left_list, pair_right[left_index])
        elif isinstance(pair_left[left_index], list) and isinstance(pair_right[left_index], list):
            if len(pair_left[left_index]) > 0 and len(pair_right[left_index]) == 0:
                return False
            if special_compare(pair_left[left_index], pair_right[left_index]):
                continue
            else:
                return False
    return True


def solution_part_one(input_list):
    pairs = get_pairs(input_list)
    correct_indices = []
    for pair_left, pair_right in pairs:
        if special_compare(pair_left, pair_right):
            correct_indices.append(pairs.index((pair_left, pair_right)) + 1)
    print(correct_indices)
    # 1744
    first_p = [[1], [2, 3, 4]]
    second_p = [[1], 4]
    print(special_compare(first_p, second_p))

    return sum(correct_indices)


def create_list(char_idx, pair):
    stack = []
    while char_idx < len(pair):
        if pair[char_idx] == '[':
            char_idx, created_list = create_list(char_idx + 1, pair)
            stack.append(created_list)
        elif pair[char_idx] == ']':
            return char_idx, stack
        elif pair[char_idx] != ',':
            stack.append(int(pair[char_idx]))
        char_idx += 1

    return char_idx, stack


def get_pairs(input_list):
    pairs = []
    for idx in range(0, len(input_list), 3):
        if input_list[idx]:
            first_pair = input_list[idx]
            second_pair = input_list[idx + 1]
            _, processed_first_pair = create_list(1, first_pair)
            _, processed_second_pair = create_list(1, second_pair)
            pairs.append((processed_first_pair, processed_second_pair))
    return pairs


def solution_part_two(commands):
    return None


print(solution_part_one(parsed_input))
# print(solution_part_two(parsed_input))
