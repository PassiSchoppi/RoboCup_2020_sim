import global_variables
import movements
import wall
import time


def nothing():
    movements.stop()
    return 0


def go_forward():
    movements.drive_straight()
    if wall.in_front():
        global_variables.state = 1
    return 0


def turn_right():
    # TODO state machine! no counter
    movements.turn_right()
    global_variables.counter += 1
    if global_variables.counter > 27:
        global_variables.state = 1
        global_variables.counter = 0
    # turn right
    return 0


def turn_left():
    # TODO state machine! no counter
    movements.turn_left()
    global_variables.counter += 1
    if global_variables.counter > 27:
        global_variables.state = 1
        global_variables.counter = 0
    # turn right
    return 0


def decide_new_state():
    movements.stop()
    if not wall.in_front():
        global_variables.state = 2
        return 0
    if not wall.on_right():
        global_variables.state = 3
        return 0
    if not wall.on_left():
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
