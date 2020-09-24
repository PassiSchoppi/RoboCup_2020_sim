import global_variables
import movements
import wall
import map
import robot
import time
import tile
import victim
import take_image


def nothing():
    movements.stop()
    return 0


def go_forward():
    # when he sees a black tile
    if tile.color() == global_variables.BLACK:
        # flee back
        movements.stop()
        global_variables.state = 6
        # mark the field as hole
        map.hole_in_front()
    # if there is a heated victim
    if (victim.on_left() or victim.on_right()) and global_variables.time_trying < global_variables.max_time_trying:
        movements.stop()
        if global_variables.time_trying < 1:
            victim.send_message(int(robot.gps.getValues()[0] * 100),
                                int(robot.gps.getValues()[2] * 100),
                                bytes('T', "utf-8"))
        global_variables.time_trying = global_variables.time_trying + 1
    else:
        global_variables.time_trying = 0
        # if not take_image.take_picture(robot.cameraC, debug=False) == 'e':
        #     # movements.stop()
        #     print('found vis victim')
        #     while True:
        #         victim.send_message(int(robot.gps.getValues()[0] * 100),
        #                             int(robot.gps.getValues()[2] * 100),
        #                             bytes('H', "utf-8"))
        # else:
        # determine how far to drive
        distance_to_drive = 0
        if robot.facing == global_variables.NORTH:
            distance_to_drive = robot.gps.getValues()[2] - (robot.latest_gps_position[2] - global_variables.field_size)
        if robot.facing == global_variables.EAST:
            distance_to_drive = - robot.gps.getValues()[0] + (
                        robot.latest_gps_position[0] + global_variables.field_size)
        if robot.facing == global_variables.SOUTH:
            distance_to_drive = - robot.gps.getValues()[2] + (
                        robot.latest_gps_position[2] + global_variables.field_size)
        if robot.facing == global_variables.WEST:
            distance_to_drive = robot.gps.getValues()[0] - (robot.latest_gps_position[0] - global_variables.field_size)
        if distance_to_drive <= 0:
            movements.stop()
            # when he is done with going forward
            # then change location on map
            map.move_to(robot.facing)
            print('done going forward')
            # decide new state
            global_variables.state = 1
        else:
            movements.drive_straight()

    return 0


def turn_right():
    if (victim.on_left() or victim.on_right()) and global_variables.time_trying < global_variables.max_time_trying:
        movements.stop()
        if global_variables.time_trying < 1:
            victim.send_message(int(robot.gps.getValues()[0] * 100),
                                int(robot.gps.getValues()[2] * 100),
                                bytes('T', "utf-8"))
        global_variables.time_trying = global_variables.time_trying + 1
    else:
        distance_to_drive = (robot.left_pos_sensor.getValue() - robot.latest_lws_value) - (
                robot.right_pos_sensor.getValue() - robot.latest_rws_value)
        if distance_to_drive >= 2 * global_variables.quarter_rotation_value:
            movements.stop()
            global_variables.state = 2
            robot.facing = map.convert_compass_direction(global_variables.RIGHT)
            print('done turning right')
        else:
            if global_variables.time_trying == 0:
                movements.turn_right()
            else:
                movements.turn_right(3)
        global_variables.time_trying = 0

    return 0


def turn_left():
    if (victim.on_left() or victim.on_right()) and global_variables.time_trying < global_variables.max_time_trying:
        movements.stop()
        if global_variables.time_trying < 1:
            victim.send_message(int(robot.gps.getValues()[0] * 100),
                                int(robot.gps.getValues()[2] * 100),
                                bytes('T', "utf-8"))
        global_variables.time_trying = global_variables.time_trying + 1
    else:
        distance_to_drive = (robot.right_pos_sensor.getValue() - robot.latest_rws_value) - (
                robot.left_pos_sensor.getValue() - robot.latest_lws_value)
        if distance_to_drive >= 2 * global_variables.quarter_rotation_value:
            global_variables.state = 2
            robot.facing = map.convert_compass_direction(global_variables.LEFT)
            print('done turning left')
        else:
            if global_variables.time_trying == 0:
                movements.turn_left()
            else:
                movements.turn_left(3)
        global_variables.time_trying = 0

    return 0


def go_back():
    # turn left
    if (victim.on_left() or victim.on_right()) and global_variables.time_trying < global_variables.max_time_trying:
        movements.stop()
        if global_variables.time_trying < 1:
            victim.send_message(int(robot.gps.getValues()[0] * 100),
                                int(robot.gps.getValues()[2] * 100),
                                bytes('T', "utf-8"))
        global_variables.time_trying = global_variables.time_trying + 1
    else:
        distance_to_drive = (robot.right_pos_sensor.getValue() - robot.latest_rws_value) - (
                robot.left_pos_sensor.getValue() - robot.latest_lws_value)
        if distance_to_drive >= 2 * global_variables.quarter_rotation_value:
            # turn left second time
            movements.stop()
            global_variables.state = 4
            robot.facing = map.convert_compass_direction(global_variables.LEFT)
            # reset latest rotation sensor values
            print('updating latest wheel sensor values')
            robot.latest_lws_value = robot.left_pos_sensor.getValue()
            robot.latest_rws_value = robot.right_pos_sensor.getValue()
            print('done turning left (1/2)')
        else:
            if global_variables.time_trying == 0:
                movements.turn_left()
            else:
                movements.turn_left(3)
        global_variables.time_trying = 0
    return 0


def flee_back():
    if (victim.on_left() or victim.on_right()) and global_variables.time_trying < global_variables.max_time_trying:
        movements.stop()
        if global_variables.time_trying < 1:
            victim.send_message(int(robot.gps.getValues()[0] * 100),
                                int(robot.gps.getValues()[2] * 100),
                                bytes('T', "utf-8"))
        global_variables.time_trying = global_variables.time_trying + 1
    else:
        global_variables.time_trying = 0
        # when he sees a black tile
        distance_to_drive = 0
        if robot.facing == global_variables.NORTH:
            distance_to_drive = - robot.gps.getValues()[2] + robot.latest_gps_position[2]
        if robot.facing == global_variables.EAST:
            distance_to_drive = + robot.gps.getValues()[0] - robot.latest_gps_position[0]
        if robot.facing == global_variables.SOUTH:
            distance_to_drive = + robot.gps.getValues()[2] - robot.latest_gps_position[2]
        if robot.facing == global_variables.WEST:
            distance_to_drive = - robot.gps.getValues()[0] + robot.latest_gps_position[0]
        if distance_to_drive <= 0:
            # decide new state
            movements.stop()
            global_variables.state = 1
        else:
            movements.drive_back()

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
    elif direction_to_go == 5:  # if the whole map is done:
        # and he is on the starting tile
        if robot.position[0] == round(global_variables.map_size / 2) and \
                robot.position[1] == round(global_variables.map_size / 2):
            print('SENDING "E" TO CONTROLLER!')
            victim.send_message(int(0),
                                int(0),
                                bytes('E', 'utf-8'))
            print('DONE!!!!!!!!')
        else:
            print('returning to start...')
            # mark starting tile as unvisited
            map.map_array[round(global_variables.map_size / 2)][round(global_variables.map_size / 2)].visited = False

    print('updating latest values')
    robot.latest_gps_position = robot.gps.getValues()
    robot.latest_lws_value = robot.left_pos_sensor.getValue()
    robot.latest_rws_value = robot.right_pos_sensor.getValue()

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
