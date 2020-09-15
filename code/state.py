import global_variables
import movements
import wall
import map
import robot


def nothing():
    movements.stop()
    return 0


def go_forward():
    movements.drive_straight()
    global_variables.counter += 1
    if global_variables.counter > 29:
        global_variables.state = 1
        global_variables.counter = 0
    return 0


def turn_right():
    # TODO state machine! no counter
    movements.turn_right()
    global_variables.counter += 1
    if global_variables.counter > 27:
        global_variables.state = 1
        global_variables.counter = 0
    return 0


def turn_left():
    # TODO state machine! no counter
    movements.turn_left()
    global_variables.counter += 1
    if global_variables.counter > 27:
        global_variables.state = 1
        global_variables.counter = 0
    return 0


def decide_new_state():
    movements.stop()

    print('X: ', robot.position[0])
    print('Y: ', robot.position[1])
    print('F: ', robot.facing)
    map.update_field()
    map.print_map()
    if not wall.in_front():
        map.move_to(robot.facing)
        global_variables.state = 2
        return 0
    if not wall.on_right():
        print('turning right')
        robot.facing = map.convert_compass_direction(global_variables.RIGHT)
        global_variables.state = 3
        return 0
    if not wall.on_left():
        print('turning left')
        robot.facing = map.convert_compass_direction(global_variables.LEFT)
        global_variables.state = 4
        return 0
    return 0


def go_back():
    # TODO not tested
    movements.drive_back()
    global_variables.counter += 1
    if global_variables.counter > 27:
        global_variables.state = 1
        global_variables.counter = 0
    return 0


def change_state():
    # switch statement for all the status cases
    switcher = {
        0: nothing,
        1: decide_new_state,
        2: go_forward,
        3: turn_right,
        4: turn_left,
        5: go_back
    }
    switcher[global_variables.state]()
    # print("state: ", switcher[global_variables.state])
    return 0
