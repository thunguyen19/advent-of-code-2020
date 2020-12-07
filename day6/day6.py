def get_input_by_group(file_name):
    store = []
    information = ''
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip() + ' '
            if line == ' ':
                store.append(information.strip())
                information = ''
            else:
                information += line
    if information:
        store.append(information.strip())
    return store


def massage_input(data):
    store = []
    for string in data:
        store.append(string.replace(' ', ''))
    return store


def part_1(data):
    count = 0
    data = massage_input(data)
    for answer in data:
        count += len(set(answer))
    return count


def main():
    data = get_input_by_group('input.txt')
    print(part_1(data))


main()
