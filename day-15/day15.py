def generate_turns(input_data, turn):
    store = {}
    index = 1
    data = []
    for num in input_data:
        if num not in store:
            store[num] = [index]
            prev_number = num
        else:
            return None
        data.append(prev_number)
        index += 1
    # while index <= turn:

    return data


if __name__ == '__main__':
    print(generate_turns([0, 3, 6], 3))
