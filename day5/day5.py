import re


def get_input(filename):
    store = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            store.append(line.strip())
    return store


def get_position(input_string, start, end, lower_half, upper_half):
    s, e = start, end
    for char in input_string:
        mid = s // 2 + e // 2
        if char == lower_half:
            e = mid
        elif char == upper_half:
            s = mid + 1
    return s


def get_seat_id(input_string):
    find = re.search(r'([F|B]+)([L|R]+)', input_string)
    row_string, col_string = find.group(1), find.group(2)
    return get_position(row_string, start=0, end=127, lower_half='F', upper_half='B') * 8 + \
           get_position(col_string, start=0, end=7, lower_half='L', upper_half='R')


def get_all_seat_ids(inputs):
    store = []
    for string in inputs:
        store.append(int(get_seat_id(string)))
    return store


# PART 1
def get_highest_seat_id(inputs):
    seat_id = 0
    for string in inputs:
        seat_id = max(seat_id, get_seat_id(string))
    return seat_id


# PART 2
def get_your_seat_id(inputs):
    seat_ids = sorted(get_all_seat_ids(inputs))
    for i in range(len(seat_ids) - 1):
        if seat_ids[i + 1] == seat_ids[i] + 1:
            continue
        else:
            return seat_ids[i] + 1


def main():
    example = 'FBFBBFFRLR'
    assert get_seat_id(example) == 357

    data = get_input('input.txt')
    assert get_highest_seat_id(data) == 822
    assert get_your_seat_id(data) == 705


main()
