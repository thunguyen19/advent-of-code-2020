import re


def get_inputs(file_name):
    store = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            store.append(line.strip())
    return store


def get_instruction(input_string):
    parts = re.search(r'([N|S|W|E|L|R|F])(\d*)?', input_string)
    action, value = parts.group(1), parts.group(2)
    return action, int(value)


class Coordinate:
    def __init__(self, x, y, direction='E'):
        self.x = x
        self.y = y
        self.direction = direction
        self.store_action = {
            0: 'E',
            1: 'S',
            2: 'W',
            3: 'N'
        }

    def get_coordinate(self):
        return self.x, self.y

    def get_manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def get_direction_index(self):
        for index, direction in self.store_action.items():
            if self.get_direction() == direction:
                return index

    def get_direction(self):
        return self.direction

    def update_direction(self, direction):
        self.direction = direction

    def update_x(self, x):
        self.x = x

    def update_y(self, y):
        self.y = y

    def update_coordinate(self, x, y):
        self.x, self.y = x, y

    def forward(self, value):
        action = self.get_direction()
        self.move(action, value)

    def move(self, action, value):
        if action == 'N':
            self.y += value
            return
        if action == 'S':
            self.y -= value
            return
        if action == 'W':
            self.x -= value
            return
        if action == 'E':
            self.x += value
            return

    def turn(self, action, value):
        value = value // 90
        current_direction_index = self.get_direction_index()
        direction = ''
        if action == 'R':
            target = (current_direction_index + value) % 4
            direction = self.store_action[target]
        elif action == 'L':
            num = current_direction_index - value
            if num < 0:
                target = 4 + num
            else:
                target = num % 4
            direction = self.store_action[target]
        self.update_direction(direction)

    # PART 1
    @staticmethod
    def calculate_manhattan_dist_from_ship(data, coordinate):
        for d in data:
            action, value = get_instruction(d)
            if action == 'F':
                coordinate.forward(value)
            elif action == 'R' or action == 'L':
                coordinate.turn(action, value)
            else:
                coordinate.move(action, value)
        return coordinate.get_manhattan_distance()

    # PART 2
    def calculate_manhattan_dist_from_way_point(self, data, ship_coordinate, way_point_coordinate):
        for d in data:
            action, value = get_instruction(d)
            if action == 'F':
                self.move_ship_to_way_point(ship_coordinate, way_point_coordinate, value)
            elif action in ['N', 'E', 'S', 'W']:
                way_point_coordinate.move(action, value)
            else:
                way_point_coordinate.turn_update_way_point(way_point_coordinate, action, value)
        return ship_coordinate.get_manhattan_distance()

    @staticmethod
    def move_ship_to_way_point(ship_coordinate, way_point_coordinate, value):
        wp_x, wp_y = way_point_coordinate.get_coordinate()
        ship_x, ship_y = ship_coordinate.get_coordinate()
        ship_coordinate.update_coordinate(ship_x + value * wp_x, ship_y + value * wp_y)

    @staticmethod
    def turn_update_way_point(way_point_coordinate, action, value):
        wp_x, wp_y = way_point_coordinate.get_coordinate()
        if value % 360 == 0:
            return
        if value % 180 == 0:
            way_point_coordinate.update_coordinate(-wp_x, -wp_y)
        else:
            value = (value // 90) % 4
            if action == 'R':
                if value == 1:
                    way_point_coordinate.update_coordinate(wp_y, -wp_x)
                elif value == 3:
                    way_point_coordinate.update_coordinate(-wp_y, wp_x)
            elif action == 'L':
                if value == 1:
                    way_point_coordinate.update_coordinate(-wp_y, wp_x)
                elif value == 3:
                    way_point_coordinate.update_coordinate(wp_y, -wp_x)


if __name__ == '__main__':
    input_data = get_inputs('input.txt')
    point = Coordinate(0, 0)
    assert point.calculate_manhattan_dist_from_ship(input_data, point) == 445

    way_point = Coordinate(10, 1)
    ship = Coordinate(0, 0)
    assert ship.calculate_manhattan_dist_from_way_point(input_data, ship, way_point) == 42495
