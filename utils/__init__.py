def parse_input(file_path='input.txt'):
    converted_list = []
    with open(file_path) as f:
        for element in f.readlines():
            converted_list.append(element.strip())
    return converted_list
