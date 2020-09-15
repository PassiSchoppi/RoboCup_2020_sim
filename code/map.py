import global_variables
import robot
import wall


# class of Field
class Field:
    def __init__(self, walls, visited, color):
        self.walls = walls
        self.visited = visited
        self.color = color
        self.distance_to_unvisited = 0


# creating map array
map_array = []
for _ in range(0, global_variables.map_size):
    row = []
    for __ in range(0, global_variables.map_size):
        row.append(Field([1, 1, 1, 1], 0, 0))
    map_array.append(row)


# convert compass to direction and back
def convert_compass_direction(compass_or_direction):
    # TODO
    matrix = [
        [0, 1, 2, 3],  # facing NORTH
        [1, 2, 3, 0],  # facing EAST
        [2, 3, 0, 1],  # facing SOUTH
        [3, 0, 1, 2]  # facing WEST
    ]
    return matrix[robot.facing][compass_or_direction]


def get_direction_to_go():
    return 0


def update_field():
    # wände zu feld hinzufügen
    map_array[robot.position[0]][robot.position[1]].walls[
        convert_compass_direction(global_variables.FRONT)] = wall.in_front()
    map_array[robot.position[0]][robot.position[1]].walls[
        convert_compass_direction(global_variables.RIGHT)] = wall.on_right()
    map_array[robot.position[0]][robot.position[1]].walls[
        convert_compass_direction(global_variables.LEFT)] = wall.on_left()

    # update walls of surrounding field
    map_array[robot.position[0]][robot.position[1] - 1].walls[global_variables.NORTH] = \
        map_array[robot.position[0]][robot.position[1]].walls[global_variables.SOUTH]
    map_array[robot.position[0] + 1][robot.position[1]].walls[global_variables.WEST] = \
        map_array[robot.position[0]][robot.position[1]].walls[global_variables.EAST]
    map_array[robot.position[0]][robot.position[1] + 1].walls[global_variables.SOUTH] = \
        map_array[robot.position[0]][robot.position[1]].walls[global_variables.NORTH]
    map_array[robot.position[0] - 1][robot.position[1]].walls[global_variables.EAST] = \
        map_array[robot.position[0]][robot.position[1]].walls[global_variables.WEST]

    # mark current field as visited
    map_array[robot.position[0]][robot.position[1]].visited = 1


def move_to(compass):
    if compass == global_variables.NORTH:
        print('moving north')
        robot.position[1] = robot.position[1] + 1
    if compass == global_variables.EAST:
        print('moving east')
        robot.position[0] = robot.position[0] + 1
    if compass == global_variables.SOUTH:
        print('moving south')
        robot.position[1] = robot.position[1] - 1
    if compass == global_variables.WEST:
        print('moving west')
        robot.position[0] = robot.position[0] - 1
    return 0


def print_map():
    # for every horizontal line of Fields
    for y in range(global_variables.map_size - 1, 0, -1):
        # for every Field in y line
        for x in range(0, global_variables.map_size):
            # north wall
            if map_array[x][y].walls[global_variables.NORTH]:
                if map_array[x][y].walls[global_variables.WEST]:
                    print("█", end="")
                else:
                    print(" ", end="")
                print("██", end="")
                if map_array[x][y].walls[global_variables.EAST]:
                    print("█", end="")
                else:
                    print(" ", end="")
            else:
                print("    ", end="")
        print()

        # for every Field in y line
        for x in range(0, global_variables.map_size):
            # west wall of that field
            if map_array[x][y].walls[global_variables.WEST]:
                print("█", end="")
            else:
                print(" ", end="")

            # visited status of that field
            # print(map_array[i][o].distance_to_unvisited, end="")
            if map_array[x][y].visited:
                print("░░", end="")
            else:
                print("┐└", end="")

            # east wall of that field
            if map_array[x][y].walls[global_variables.EAST]:
                print("█", end="")
            else:
                print(" ", end="")
        print()

        # for every Field in y line
        for x in range(0, global_variables.map_size):
            # south wall of that field
            if map_array[x][y].walls[global_variables.SOUTH]:
                if map_array[x][y].walls[global_variables.WEST]:
                    print("█", end="")
                else:
                    print(" ", end="")
                print("██", end="")
                if map_array[x][y].walls[global_variables.EAST]:
                    print("█", end="")
                else:
                    print(" ", end="")
            else:
                print("    ", end="")
        print()

    return 0


print_map()
