import global_variables
import movements
import wall
import map
import robot
import time
import tile


def nothing():
    movements.stop()
    return 0


def go_forward():
    # TODO swamp does not work
    movements.drive_straight()
    global_variables.counter += 1
    # when he sees a black tile
    if tile.color() == global_variables.BLACK:
        # flee back
        movements.stop()
        global_variables.state = 6
        global_variables.counter = global_variables.counter -1
        # dont clear counter as we need this to decide how far back
        # mark the field as hole
        map.hole_in_front()
    if global_variables.counter > 58:
        # when he is done with going forward
        # then change location on map
        map.move_to(robot.facing)
        print('done going forward')
        # TODO remove sleep
        time.sleep(0.5)
        # decide new state
        global_variables.state = 1
        global_variables.counter = 0
    return 0


def turn_right():
    # TODO state machine! no counter
    movements.turn_right()
    global_variables.counter += 1
    if global_variables.counter > 54:
        global_variables.state = 2
        robot.facing = map.convert_compass_direction(global_variables.RIGHT)
        print('done turning right')
        global_variables.counter = 0
    return 0


def turn_left():
    # TODO state machine! no counter
    movements.turn_left()
    global_variables.counter += 1
    if global_variables.counter > 54:
        global_variables.state = 2
        robot.facing = map.convert_compass_direction(global_variables.LEFT)
        print('done turning left')
        global_variables.counter = 0
    return 0


def go_back():
    # turn left
    movements.turn_left()
    global_variables.counter += 1
    if global_variables.counter > 54:
        # turn left second time
        global_variables.state = 4
        robot.facing = map.convert_compass_direction(global_variables.LEFT)
        print('done turning left (1/2)')
        global_variables.counter = 0
    return 0


def flee_back():
    # TODO swamp does not work
    movements.drive_back()
    global_variables.counter -= 1
    # when he sees a black tile
    if global_variables.counter <= 0:
        # TODO remove sleep
        time.sleep(0.5)
        # decide new state
        global_variables.state = 1
        global_variables.counter = 0
    return 0


def decide_new_state():
    movements.stop()

    print('X: ', robot.position[0])
    print('Y: ', robot.position[1])
    print('F: ', robot.facing)
    map.update_field()
    # map.print_map()

    direction_to_go = map.where_to_drive()
    print('direction to go: ', direction_to_go)
    # print('direction_to_go_to: ', direction_to_go)
    if direction_to_go == map.convert_compass_direction(global_variables.FRONT):
        global_variables.state = 2
    elif direction_to_go == map.convert_compass_direction(global_variables.RIGHT):
        global_variables.state = 3
    elif direction_to_go == map.convert_compass_direction(global_variables.LEFT):
        global_variables.state = 4
    elif direction_to_go == map.convert_compass_direction(global_variables.BACK):
        global_variables.state = 5
    return 0


def change_state():
    # switch statement for all the status cases
    switcher = {
        0: nothing,
        1: decide_new_state,
        2: go_forward,
        3: turn_right,
        4: turn_left,
        5: go_back,
        6: flee_back
    }
    switcher[global_variables.state]()
    # print("state: ", switcher[global_variables.state])
    return 0
