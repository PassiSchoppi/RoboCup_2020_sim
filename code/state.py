import global_variables
import movements
import wall


def nothing():
    movements.stop()
    return 0


def go_forward():
    movements.drive_straight()
    if wall.in_front():
        global_variables.state = 1
    return 0


def turn_right():
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
    return 0


def state_change():
    # switch statement for all the status cases
    switcher = {
        0: nothing,
        1: decide_new_state,
        2: go_forward,
        3: turn_right
    }
    switcher[global_variables.state]()
    # print("state: ", switcher[global_variables.state])
    return 0
