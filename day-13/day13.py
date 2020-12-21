import re


def get_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        depart_time = int(lines[0])
        raw_input_bus_ids = re.findall(r'(\d+|x)', lines[1])
    return depart_time, raw_input_bus_ids


def get_bus_ids_only(raw_input_bus_ids):
    store = []
    for bus in raw_input_bus_ids:
        if bus != 'x':
            store.append(int(bus))
    return store


# PART 1
def do_part_1(depart_time, raw_input_bus_ids):
    bus_ids = get_bus_ids_only(raw_input_bus_ids)

    def find_min_wait():
        bus, wait = -1, float('inf')
        for b_id in bus_ids:
            b_id = int(b_id)
            mod = depart_time % b_id
            diff = b_id - mod
            if diff < wait:
                wait = diff
                bus = b_id
        return bus, wait

    bus_id, min_wait = find_min_wait()
    return bus_id * min_wait


# PART 2
def find_multiplicative_inverse(a, m):  # naive
    for x in range(1, m):
        if (a * x) % m == 1:
            return x


def get_result_part_2(raw_input_bus_ids):
    bus_ids = get_bus_ids_only(raw_input_bus_ids)

    def get_modulo():
        modulo = []
        product = 1
        for bus in bus_ids:
            product *= bus
        for i in range(len(bus_ids)):
            modulo.append(product // bus_ids[i])
        return product, modulo

    def get_x_i():
        _, modulo_ids = get_modulo()
        x_i = []
        for i in range(len(bus_ids)):
            x_i.append(find_multiplicative_inverse(modulo_ids[i], bus_ids[i]))
        return x_i

    def get_remainders():
        remainders = []
        for i in range(len(raw_input_bus_ids)):
            val = raw_input_bus_ids[i]
            if val == 'x':
                continue
            elif i == 0:
                remainders.append(i)
            else:
                remainders.append(int(val) - i)
        return remainders

    b = get_remainders()
    mod, n = get_modulo()
    x = get_x_i()
    total = 0
    for index in range(len(b)):
        total += b[index] * n[index] * x[index]
    return total % mod


if __name__ == '__main__':
    time, raw_ids = get_input('input.txt')
    assert do_part_1(time, raw_ids) == 6568

    assert get_result_part_2(raw_ids) == 554865447501099
