from utils import parse_input

parsed_list = parse_input('input.txt')


def sanitize_line(line):
    [string_one, string_two] = line.split(',')
    interval, interval_two = [int(x) for x in string_one.split('-')], [int(x) for x in string_two.split('-')]
    return interval, interval_two


def get_start_end_of_intervals(line):
    interval, interval_two = sanitize_line(line)
    start_one, end_one = interval[0], interval[1]
    start_two, end_two = interval_two[0], interval_two[1]
    return end_one, end_two, start_one, start_two


def solution_part_one(input_list):
    total_score = 0
    for line in input_list:
        end_one, end_two, start_one, start_two = get_start_end_of_intervals(line)
        if start_one >= start_two and end_one <= end_two or start_two >= start_one and end_two <= end_one:
            total_score += 1
    return total_score


def solution_part_two(input_list):
    total_score = 0
    for line in input_list:
        end_one, end_two, start_one, start_two = get_start_end_of_intervals(line)
        if start_two <= start_one <= end_two or start_two <= end_one <= end_two:
            total_score += 1
        elif start_one <= start_two <= end_one or start_one <= end_two <= end_one:
            total_score += 1
    return total_score


print(solution_part_one(parsed_list))
print(solution_part_two(parsed_list))
