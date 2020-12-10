import re


def get_inputs(file_name):
    store = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            string = str(i) + ' ' + lines[i].strip()
            store.append(string)
    return store


def parse_instruction(instruction):
    return instruction.split(' ')


def do_the_math(value, argument):
    find = re.search(r'([+|-])(\d+)', argument)
    sign, number = find.group(1), int(find.group(2))
    if sign == '+':
        return value + number
    elif sign == '-':
        return value - number


# PART 1
def calculate_accumulator(inputs):
    seen = set()
    accumulator = 0
    i = 0
    while 0 <= i < len(inputs):
        index, operation, argument = parse_instruction(inputs[i])
        if index in seen:
            return accumulator
        seen.add(index)
        if operation == 'nop':
            i += 1
        elif operation == 'acc':
            i += 1
            accumulator = do_the_math(accumulator, argument)
        elif operation == 'jmp':
            i = do_the_math(i, argument)


# PART 2


if __name__ == '__main__':
    data = get_inputs('input.txt')
    assert calculate_accumulator(data) == 1394
