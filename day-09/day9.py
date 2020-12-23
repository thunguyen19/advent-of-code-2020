def get_inputs(file_name):
    store = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            store.append(int(line.strip()))
    return store


# PART 1
def find_invalid_number(input_array, length):
    def find_two_sum(array, target):
        dictionary = {}
        for a in array:
            r = target - a
            dictionary[r] = a

        for a in array:
            if a in dictionary:
                if dictionary[a] != a:  # found target that is not added by same numbers
                    return True
        return False

    arr = input_array[:length]
    for index in range(length, len(input_array)):
        current = input_array[index]
        if find_two_sum(arr, current):
            arr.pop(0)
            arr.append(current)
        else:
            return index, current


# PART 2
def get_encryption_weakness(input_array, end_index, target):

    def find_list_sum_to_invalid_number():
        start, end = 0, 1
        total = input_array[start] + input_array[end]
        while end <= end_index:
            if total == target:
                return input_array[start:end + 1]
            if total < target:
                end += 1
                total += input_array[end]
            else:
                total -= input_array[start]
                start += 1

    array = find_list_sum_to_invalid_number()
    return min(array) + max(array)


if __name__ == '__main__':
    data = get_inputs('input.txt')
    preamble_length = 25
    i, val = find_invalid_number(data, preamble_length)

    assert val == 90433990
    assert get_encryption_weakness(data, i, val) == 11691646
