def get_input(file_name):
    store = []
    group = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line == '':
                store.append(group)
                group = []
            else:
                group.append(line)
    if group:
        store.append(group)
    return store


# PART 1
def num_questions_anyone_answer(data):
    result = 0
    for group in data:
        string = ''
        for person in group:
            string += person
        result += len(set(string))
    return result


# PART 2
def store_answer_per_group(group):
    store = {}
    for member in group:
        for i in range(len(member)):
            answer = member[i]
            if store.get(answer):
                store[answer] += 1
            else:
                store[answer] = 1
    return store


def num_questions_everyone_answer(data):
    result = 0
    for group in data:
        total_people = len(group)
        store = store_answer_per_group(group)
        for k, v in store.items():
            if v == total_people:
                result += 1
    return result


def main():
    data = get_input('input.txt')
    assert num_questions_anyone_answer(data) == 6596
    assert num_questions_everyone_answer(data) == 3219


main()
