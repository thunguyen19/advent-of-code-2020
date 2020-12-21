def get_length(lst):
    return len(lst)


def get_difference(lst):
    return lst[1] - lst[0]


def get_target_turn(input_data, turn):
    def pop_and_push(dictionary, key, value):
        if key in dictionary:
            lst = dictionary[key]
            if get_length(lst) <= 1:
                lst.append(value)
            else:
                lst.pop(0)
                lst.append(value)
        else:
            dictionary[key] = [value]

    def generate_turns():
        data = []
        store = {}
        index = 0
        prev_number = -1
        for num in input_data:
            if num not in store:
                store[num] = [index]
                prev_number = num
            else:
                if get_length(store[num]) == 1:
                    store[num].append(index)
                    prev_number = get_difference(store[num])
            data.append(prev_number)
            index += 1

        while index < turn:
            if get_length(store[prev_number]) == 1:
                prev_number = 0
            else:
                prev_number = get_difference(store[prev_number])

            pop_and_push(store, prev_number, index)
            data.append(prev_number)
            index += 1

        return data

    result = generate_turns()
    return result[turn - 1]


if __name__ == '__main__':
    target_turn = 2020
    assert get_target_turn([0, 3, 6], target_turn) == 436
    assert get_target_turn([1, 3, 2], target_turn) == 1
    assert get_target_turn([2, 1, 3], target_turn) == 10
    assert get_target_turn([3, 1, 2], target_turn) == 1836
    assert get_target_turn([1, 2, 3], target_turn) == 27
    assert get_target_turn([0, 8, 15, 2, 12, 1, 4], target_turn) == 289

    target_turn = 30000000
    assert get_target_turn([0, 8, 15, 2, 12, 1, 4], target_turn) == 1505722
