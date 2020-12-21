import re

# class Luggage:
#     def __init__(self, color, children=[]):
#         self.color = color
#         self.children = children
#
#     def num_children(self):
#         return len(self.children)
#
#     def contains_target_bag(self, bag):
#         return bag in self.children


def get_inputs(file_name):
    store = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            store.append(line.strip())
    return store


# (\d\s)?(\w+ \w+) bag(?:s)?(?:,)?
def map_bag(store, input_string): # PART 1
    parent = re.search(r'.+?(?=bag)', input_string)[0].strip()
    children = input_string.split('contain')[1].strip()
    if 'no other' in children:
        store[parent] = []
    else:
        children = children.split(',')
        for c in children:
            print(children)
            child = re.search('\D+?(?=bag)', c)[0].strip()
            print(child)
            if parent not in store:
                store[parent] = []
            store[parent].append(child)
    return store


seen = set()


def count_bags_that_contain_target(bag, top_parent, store):
    children = store[bag]
    if 'shiny gold' in children:
        seen.add(top_parent)
        return
    if len(children) == 0:
        return
    for child in children:
        count_bags_that_contain_target(child, top_parent, store)


def map_bag_part_2(store, input_string):  # PART 2
    parent = re.search(r'.+?(?=bag)', input_string)[0].strip()
    children = input_string.split('contain')[1].strip()
    if 'no other' in children:
        store[parent] = []
    else:
        children = re.findall(r'(\d\s)?(\w+ \w+) bag(?:s)?(?:,)?', children)
        store[parent] = {}
        for c in children:
            bag_name, value = c[1].strip(), int(c[0].strip())
            store[parent][bag_name] = value
    return store


def get_total_bags(bag, store):
    total = 0
    for k, v in store[bag].items():
        if v == []:
            return
        total += (v + v * get_total_bags(k, store))
    return total


def total_bags_in_shiny_gold(store):
    total = 0
    for k, v in store['shiny gold'].items():
        print(k, v)
        num = v + v * get_total_bags(k, store)
        total += num
    return total


if __name__ == '__main__':
    data = get_inputs('input.txt')
    dictionary = {}
    for d in data:
        # map_bag(dictionary, d)
        map_bag_part_2(dictionary, d)

    print(dictionary)
    print(total_bags_in_shiny_gold(dictionary))

    # for k, v in dictionary.items():
    #     count_bags_that_contain_target(k, k, dictionary)
    # print('seen: ', seen)
