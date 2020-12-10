import re


class Luggage:
    def __init__(self, color, children=[]):
        self.color = color
        self.children = children

    def num_children(self):
        return len(self.children)

    def contains_target_bag(self, bag):
        return bag in self.children


def get_inputs(file_name):
    store = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            store.append(line.strip())
    return store


# shiny orange bags contain 4 muted purple bags, 4 dim silver bags, 5 shiny gold bags, 3 pale orange bags.
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.


def map_bag(store, input_string):
    parent = re.search(r'.+?(?=bag)', input_string)[0].strip()
    children = input_string.split('contain')[1].strip()
    if children == 'no other bags':
        store['no child'].append(parent)
    else:
        children = children.split(',')
        for c in children:
            child = re.search('\D+?(?=bag)', c)[0].strip()
            if child in store:
                store[child].append(parent)
            else:
                store[child] = [parent]
    return store


def count_bags_that_contain_target(bag, store):
    seen = set()
    parents = store[bag]
    for p in parents:
        seen.add(p)
        if p in store:
            for i in store[p]:
                seen.add(i)
    return len(seen)

# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.

# my = Bags('muted yellow')
# thu = Bags('muted yellow')
# bw = Bags('bright white')
# lr = Bags('light red', [bw, my])
#
#
# print(my)
# print(bw)
# print(lr)


if __name__ == '__main__':
    data = get_inputs('input.txt')
    dictionary = {}
    for line in data:
        map_bag(dictionary, line)
    # import json
    # print(json.dumps(dictionary, indent=4))
    print('shiny gold: ', dictionary['shiny gold'])
    parents = dictionary['shiny gold']
    for p in parents:
        if p in dictionary:
            print(p, dictionary[p])
    print(count_bags_that_contain_target('shiny gold', dictionary))
