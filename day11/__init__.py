import math
import operator
from functools import reduce

from utils import parse_input

FILE_PATH = 'nput.txt'

parsed_input = parse_input(FILE_PATH)


def get_operation(operation_string):
    if operation_string == "*":
        return operator.mul
    elif operation_string == "-":
        return operator.sub
    elif operation_string == "+":
        return operator.add
    elif operation_string == "/":
        return operator.floordiv


def create_operation(operation, operation_number):
    if operation_number.isnumeric():
        return lambda old: operation(old, int(operation_number))
    else:
        return lambda old: operation(old, old)


def create_test(divisible, true_monkey, false_monkey):
    return lambda to_divide: true_monkey if to_divide % divisible == 0 else false_monkey


def get_monkeys(parsed_input):
    monkeys = []
    for index in range(0, len(parsed_input), 7):
        if parsed_input[index].startswith("Monkey"):
            second_line = parsed_input[index + 1].replace("Starting items: ", "")
            starting_items = [int(x) for x in second_line.split(',')]
            third_line = parsed_input[index + 2].replace("Operation: new = old ", "").split(" ")

            operator_function = get_operation(third_line[0])
            operation_number = (third_line[1])
            operation = create_operation(operator_function, operation_number)

            divisible = int(parsed_input[index + 3].replace("Test: divisible by ", ""))
            true_monkey = int(parsed_input[index + 4].replace("If true: throw to monkey ", ""))
            false_monkey = int(parsed_input[index + 5].replace("If false: throw to monkey ", ""))
            test = create_test(divisible, true_monkey, false_monkey)

            count = 0

            monkeys.append([starting_items, operation, test, count])
    return monkeys


def solution_part_one(parsed_input):
    monkeys = get_monkeys(parsed_input)

    for index in range(0, 20):
        for monkey in monkeys:
            while len(monkey[0]) > 0:
                starting_item = monkey[0].pop(0)
                result_operation = monkey[1](starting_item)
                bored_worry_level = math.floor(result_operation // 3)
                to_throw_monkey = monkey[2](bored_worry_level)
                monkeys[to_throw_monkey][0].append(bored_worry_level)
                monkey[3] += 1
    print(reduce(lambda x, y: x * y, sorted([monkey[3] for monkey in monkeys])[-2:]))
    return monkeys


def solution_part_two(parsed_input):
    monkeys = get_monkeys(parsed_input)

    for index in range(0, 10000):
        for monkey in monkeys:
            while len(monkey[0]) > 0:
                starting_item = monkey[0].pop(0)
                result_operation = monkey[1](starting_item)
                to_throw_monkey = monkey[2](result_operation)
                monkeys[to_throw_monkey][0].append(result_operation)
                monkey[3] += 1
    print(reduce(lambda x, y: x * y, sorted([monkey[3] for monkey in monkeys])[-2:]))
    return monkeys


# print(solution_part_one(parsed_input))
print(solution_part_two(parsed_input))
