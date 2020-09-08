import global_variables
import movements


def nothing():
    movements.stop()
    return 0


def go_forward():
    movements.drive_straight()
    return 0


def state_change():
    # switch statement for all the status cases
    switcher = {
        0: nothing,
        1: go_forward,
    }
    switcher[global_variables.state]()
    # print("state: ", switcher[global_variables.state])
    return 0
