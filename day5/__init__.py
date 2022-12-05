from utils import parse_input

FILE_PATH = 'input.txt'

parsed_list = parse_input(FILE_PATH)


def prepare_stacks_and_actions(input_list):
    line_begin_index, stacks = get_empty_stacks_and_line_to_begin(input_list)
    fill_stacks(line_begin_index, stacks)
    actions = get_actions(input_list)

    return stacks, actions


def fill_stacks(line_begin_index, stacks):
    raw_input = get_raw_input()
    while line_begin_index >= 0:
        line_begin_index -= 1
        raw_line = raw_input[line_begin_index]
        for stridx in range(1, len(raw_line)):
            found_char = raw_line[stridx]
            if found_char.isalpha() and found_char.isupper():
                char_index = raw_line.index(found_char)
                stacks[((char_index - 1) // 4)].append(found_char)
                raw_line = raw_line.replace(found_char, ' ', 1)


def get_actions(input_list):
    actions = []
    for line in input_list:
        split_input = line.strip().split(' ')
        if split_input[0].startswith('move'):
            actions.append(line)
    return actions


def get_empty_stacks_and_line_to_begin(input_list):
    line_index = 0
    amount_stacks = 0
    stacks = []
    for line in input_list:
        split_input = line.strip().split(' ')
        if split_input[0].isnumeric():
            amount_stacks = split_input[len(split_input) - 1]
            line_index = input_list.index(line)
    for i in range(int(amount_stacks)):
        stacks.append([])
    return line_index, stacks


def get_raw_input():
    raw_input = []
    with open(FILE_PATH) as f:
        for element in f.readlines():
            raw_input.append(element.split('\n')[0])
    return raw_input


def get_inputs_from_action(action):
    action_points = action.split(" ")
    amount, from_stack, to_stack = int(action_points[1]), int(action_points[3]) - 1, int(action_points[5]) - 1
    return amount, from_stack, to_stack


def solution_part_one(stacks, actions):
    for action in actions:
        amount, from_stack, to_stack = get_inputs_from_action(action)
        for i in range(0, amount):
            if len(stacks[from_stack]) > 0:
                pop = stacks[from_stack].pop()
                stacks[to_stack].append(pop)

    answer = get_last_element_of_each_stack(stacks)
    return answer


def solution_part_two(stacks, actions):
    for action in actions:
        amount, from_stack, to_stack = get_inputs_from_action(action)
        pops = []
        for i in range(0, amount):
            pops.insert(0, stacks[from_stack].pop())
        for pop in pops:
            stacks[to_stack].append(pop)

    answer = get_last_element_of_each_stack(stacks)
    return answer


def get_last_element_of_each_stack(stacks):
    answer = ''
    for sublist in stacks:
        answer += (sublist[-1])
    return answer


print(solution_part_one(prepare_stacks_and_actions(parsed_list)[0], prepare_stacks_and_actions(parsed_list)[1]))
print(solution_part_two(prepare_stacks_and_actions(parsed_list)[0], prepare_stacks_and_actions(parsed_list)[1]))
# DNWWCHNNW
# CWMTGHBDW
