def get_input(file_name):
    store = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            store.append(int(line.strip()))
    return store


def part_1(entries, target):
    dictionary = {}
    for e in entries:
        entry = int(e)
        r = target - entry
        dictionary[r] = entry

    result = 0
    for e in entries:
        entry = int(e)
        if entry in dictionary:
            result = max(result, entry * dictionary[entry])
    return result


def part_2(entries, target):
    entries = sorted(entries)
    length = len(entries)
    result = 0
    for i in range(length):
        low = i + 1
        high = length - 1
        if low >= length:
            break
        while low < high:
            current = entries[i]
            low_value, high_value = entries[low], entries[high]
            total = current + low_value + high_value
            if total == target:
                result = max(result, current * low_value * high_value)
                low += 1
                high -= 1
            elif total < target:
                low += 1
            else:
                high -= 1
    return result


def main():
    example = ['1721', '979', '366', '299', '675', '1456']
    assert part_1(example, 2020) == 514579

    inputs = get_input('input.txt')
    assert part_1(inputs, 2020) == 980499
    assert part_2(inputs, 2020) == 200637446


main()
