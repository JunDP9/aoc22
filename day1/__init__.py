from utils import parse_input

sanitized_list = parse_input('input.txt')

res = []
index = 0
newIndex = 0

while index < len(sanitized_list):
    value = sanitized_list[index]
    index = index + 1
    if value:
        try:
            res[newIndex] += int(value)
        except IndexError:
            res.append(int(value))
    else:
        newIndex = newIndex + 1

print(sum((sorted(res))[-3:]))
print(res.index(max(res)) + 1, max(res))

# 209691
# 29 71300
# 251 71300
