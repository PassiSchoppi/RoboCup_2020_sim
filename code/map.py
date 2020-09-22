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
    matrix = [
        [0, 1, 2, 3],  # facing NORTH
        [1, 2, 3, 0],  # facing EAST
        [2, 3, 0, 1],  # facing SOUTH
        [3, 0, 1, 2]  # facing WEST
    ]
    return matrix[robot.facing][compass_or_direction]


def index_of_smallest_element(array, with_facing=False):
    index = 0
    if array[index] != 0:
        index = 0
    elif array[1] != 0:
        index = 1
    elif array[2] != 0:
        index = 2
    elif array[3] != 0:
        index = 3
    else:
        return 5
    for i in range(1, 4):
        if array[i] < array[index] and array[i] != 0:
            index = i
    if with_facing and not array[robot.facing] == 0 and array[robot.facing] <= array[index]:
        return robot.facing
    return index


def hole_in_front():
    print('marking field as hole: ', end="")
    if robot.facing == global_variables.NORTH:
        print('north')
        map_array[robot.position[0]][robot.position[1] + 1].color = global_variables.BLACK
        map_array[robot.position[0]][robot.position[1] + 1].visited = True
    if robot.facing == global_variables.EAST:
        print('east')
        map_array[robot.position[0] + 1][robot.position[1]].color = global_variables.BLACK
        map_array[robot.position[0] + 1][robot.position[1]].visited = True
    if robot.facing == global_variables.SOUTH:
        print('south')
        map_array[robot.position[0]][robot.position[1] - 1].color = global_variables.BLACK
        map_array[robot.position[0]][robot.position[1] - 1].visited = True
    if robot.facing == global_variables.WEST:
        print('west')
        map_array[robot.position[0] - 1][robot.position[1]].color = global_variables.BLACK
        map_array[robot.position[0] - 1][robot.position[1]].visited = True
    return 0


def search_for_unvisited(start_point, skip_array):
    skip_array.append(start_point)
    if not map_array[start_point[0]][start_point[1]].visited:
        return 1
    results = [0, 0, 0, 0]

    # north child
    child = [start_point[0], start_point[1] + 1]
    if not map_array[start_point[0]][start_point[1]].walls[global_variables.NORTH] and not (child in skip_array) \
            and not map_array[child[0]][child[1]].color == global_variables.BLACK:
        skip_new = skip_array.copy()
        results[global_variables.NORTH] = search_for_unvisited(child, skip_new)
    else:
        results[global_variables.NORTH] = 0

    # east child
    child = [start_point[0] + 1, start_point[1]]
    if not map_array[start_point[0]][start_point[1]].walls[global_variables.EAST] and not (child in skip_array) \
            and not map_array[child[0]][child[1]].color == global_variables.BLACK:
        skip_new = skip_array.copy()
        results[global_variables.EAST] = search_for_unvisited(child, skip_new)
    else:
        results[global_variables.EAST] = 0

    # south child
    child = [start_point[0], start_point[1] - 1]
    if not map_array[start_point[0]][start_point[1]].walls[global_variables.SOUTH] and not (child in skip_array) \
            and not map_array[child[0]][child[1]].color == global_variables.BLACK:
        skip_new = skip_array.copy()
        results[global_variables.SOUTH] = search_for_unvisited(child, skip_new)
    else:
        results[global_variables.SOUTH] = 0

    # west child
    child = [start_point[0] - 1, start_point[1]]
    if not map_array[start_point[0]][start_point[1]].walls[global_variables.WEST] and not (child in skip_array) \
            and not map_array[child[0]][child[1]].color == global_variables.BLACK:
        skip_new = skip_array.copy()
        results[global_variables.WEST] = search_for_unvisited(child, skip_new)
    else:
        results[global_variables.WEST] = 0

    # get nearest
    result_index = index_of_smallest_element(results)
    if result_index != 5:
        # TODO consider swamps with longer time
        return results[result_index] + 1
    else:
        return 0


def where_to_drive():
    distances = [0, 0, 0, 0]
    if not map_array[robot.position[0]][robot.position[1]].walls[global_variables.NORTH] \
            and not map_array[robot.position[0]][robot.position[1] + 1].color == global_variables.BLACK:
        distances[global_variables.NORTH] = map_array[robot.position[0]][robot.position[1] + 1].distance_to_unvisited

    if not map_array[robot.position[0]][robot.position[1]].walls[global_variables.EAST] \
            and not map_array[robot.position[0] + 1][robot.position[1]].color == global_variables.BLACK:
        distances[global_variables.EAST] = map_array[robot.position[0] + 1][robot.position[1]].distance_to_unvisited

    if not map_array[robot.position[0]][robot.position[1]].walls[global_variables.SOUTH] \
            and not map_array[robot.position[0]][robot.position[1] - 1].color == global_variables.BLACK:
        distances[global_variables.SOUTH] = map_array[robot.position[0]][robot.position[1] - 1].distance_to_unvisited

    if not map_array[robot.position[0]][robot.position[1]].walls[global_variables.WEST] \
            and not map_array[robot.position[0] - 1][robot.position[1]].color == global_variables.BLACK:
        distances[global_variables.WEST] = map_array[robot.position[0] - 1][robot.position[1]].distance_to_unvisited

    print('distances of surrounding fields: ', distances)
    return index_of_smallest_element(distances, with_facing=True)


def update_field():
    # wände zu feld hinzufügen
    map_array[robot.position[0]][robot.position[1]].walls[
        convert_compass_direction(global_variables.FRONT)] = wall.in_front()
    map_array[robot.position[0]][robot.position[1]].walls[
        convert_compass_direction(global_variables.RIGHT)] = wall.on_right()
    map_array[robot.position[0]][robot.position[1]].walls[
        convert_compass_direction(global_variables.LEFT)] = wall.on_left()
    print('walls of current field: ', map_array[robot.position[0]][robot.position[1]].walls)

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

    # get distance to nearest unvisited
    for x in range(0, global_variables.map_size):
        for y in range(0, global_variables.map_size):
            child = [x, y]
            skip = []
            map_array[x][y].distance_to_unvisited = search_for_unvisited(child, skip)


def move_to(compass):
    if compass == global_variables.NORTH:
        print('done moving north')
        robot.position[1] = robot.position[1] + 1
    if compass == global_variables.EAST:
        print('done moving east')
        robot.position[0] = robot.position[0] + 1
    if compass == global_variables.SOUTH:
        print('done moving south')
        robot.position[1] = robot.position[1] - 1
    if compass == global_variables.WEST:
        print('done moving west')
        robot.position[0] = robot.position[0] - 1
    return 0


def print_map():
    # for every horizontal line of Fields
    for y in range(global_variables.map_size - 1, 0, -1):
        # for every Field in y line
        for x in range(0, global_variables.map_size):
            # north wall
            if map_array[x][y].walls[global_variables.NORTH]:
                print("████", end="")
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
            if robot.position[0] == x and robot.position[1] == y:
                print("●", end="")
            else:
                if map_array[x][y].visited:
                    # print(" ", end="")
                    print(map_array[x][y].color, end="")
                else:
                    print("»", end="")

            print(map_array[x][y].distance_to_unvisited, end="")

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
                print("████", end="")
            else:
                print("    ", end="")
        print()

    return 0
