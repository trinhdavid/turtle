class Turtle:
    '''
    start_x - origin at x position
    start_y - origin at y position
    direction - the direction in which the turtle is facing. By default, the turtle is facing NORTH.
    '''

    ####### CONSTANTS - Do not change value
    # The direction the turtle is facing
    NORTH = 0
    EAST = 90
    SOUTH = 180
    WEST = 270

    ####### CONSTANTS - Do not change value
    # Turtle movements
    RIGHT = 90  # turn 90 degrees
    LEFT = -90  # turn negative 90 degrees
    FORWARD = 1 # step forward by 1

    # maximum and minimum x and y positions in which the turtle has travelled
    x_min = 0
    y_min = 0
    x_max = 0
    y_max = 0

    visited_more_than_once = set()
    visited_more_than_once_in_sequence = []

    def __init__(self, start_x, start_y, direction=NORTH):
        self.position = [start_x, start_y]
        self.direction = direction
        self.visited = {(start_x, start_y)}
        self.visited_full_path_in_sequence = [(start_x, start_y)]

    def turn_right(self):
        self.direction += self.RIGHT

        # if turtle turns full circle then set direction to NORTH
        if self.direction == 360:
            self.direction = self.NORTH

    def turn_left(self):
        if self.direction == self.NORTH:
            self.direction = self.WEST
        else:
            self.direction += self.LEFT

    def move_forward(self):
        if self.direction == self.NORTH:
            self.position[1] += 1
        elif self.direction == self.SOUTH:
            self.position[1] -= 1
        elif self.direction == self.EAST:
            self.position[0] += 1
        elif self.direction == self.WEST:
            self.position[0] -= 1

        current_position = (self.position[0], self.position[1])

        # get maximum and minimum positions for x and y
        if current_position[0] < self.x_min:
            self.x_min = current_position[0]

        if current_position[0] > self.x_max:
            self.x_max = current_position[0]

        if current_position[1] < self.y_min:
            self.y_min = current_position[1]

        if current_position[1] > self.x_max:
            self.y_max = current_position[1]

        self.visited_full_path_in_sequence.append(current_position)

        if self.has_visited(current_position):
            if current_position not in self.visited_more_than_once:
                self.visited_more_than_once.add(current_position)
                self.visited_more_than_once_in_sequence.append(current_position)
        else:
            self.visited.add(current_position)

    def has_visited(self, position):
        if position in self.visited:
            return True

        return False

    def print_visited_more_than_once(self):
        print('Visited more than once:\n{}\n'.format(self.visited_more_than_once_in_sequence))

    def print_visited(self):
        print('Visited:\n{}\n'.format(self.visited))

    def print_full_path(self):
        print('Full Path:\n{}\n'.format(self.visited_full_path_in_sequence))

    def full_path(self):
        return self.visited_full_path_in_sequence

    def visited_multiple_times(self):
        return self.visited_more_than_once_in_sequence

    def current_position(self):
        return (self.position[0], self.position[1])
