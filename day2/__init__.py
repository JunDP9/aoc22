from utils import parse_input

sanitized_list = parse_input('input.txt')

translate_action = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSOR"
}
translate_reaction = {
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSOR"
}
WIN = {
    "ROCK": "SCISSOR",
    "PAPER": "ROCK",
    "SCISSOR": "PAPER"
}
LOSS = {
    "ROCK": "PAPER",
    "PAPER": "SCISSOR",
    "SCISSOR": "ROCK"
}
points = {
    "PAPER": 2,
    "SCISSOR": 3,
    "ROCK": 1
}

DRAW_POINTS = 3
WIN_POINTS = 6


def solution_part_one(input_list):
    total_score = 0
    for line in input_list:
        [action, reaction] = line.split(' ')
        if translate_reaction[reaction] == WIN[translate_action[action]]:
            total_score += points[translate_reaction[reaction]]
        elif translate_reaction[reaction] == LOSS[translate_action[action]]:
            total_score += WIN_POINTS + points[translate_reaction[reaction]]
        elif translate_reaction[reaction] == translate_action[action]:
            total_score += DRAW_POINTS + points[translate_reaction[reaction]]
    return total_score


def solution_part_two(input_list):
    total_score = 0
    for line in input_list:
        [action, reaction] = line.split(' ')
        if reaction == 'X':
            total_score += points[WIN[translate_action[action]]]
        elif reaction == 'Z':
            total_score += WIN_POINTS + points[LOSS[translate_action[action]]]
        elif reaction == 'Y':
            total_score += DRAW_POINTS + points[translate_action[action]]
    return total_score


print(solution_part_one(sanitized_list))
print(solution_part_two(sanitized_list))
