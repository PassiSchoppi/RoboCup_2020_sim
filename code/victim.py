import robot
import struct
import global_variables
import math


def on_left():
    if robot.left_heat_sensor.getValue() > 35:
        return True
    return False


def on_right():
    if robot.right_heat_sensor.getValue() > 35:
        return True
    return False


def visible():
    obj = robot.cameraC.getRecognitionObjects()
    for item in obj:
        # print(item)
        # print(item.get_position())
        if math.sqrt((item.get_position()[0] ** 2) + (item.get_position()[2] ** 2)) < global_variables.victim_proximity:
            # print(item.get_id())
            return 'U'
    obj = robot.cameraL.getRecognitionObjects()
    for item in obj:
        # print(item.get_position())
        if math.sqrt((item.get_position()[0] ** 2) + (item.get_position()[2] ** 2)) < global_variables.victim_proximity:
            return 'U'
    obj = robot.cameraR.getRecognitionObjects()
    for item in obj:
        # print(item.get_position())
        if math.sqrt((item.get_position()[0] ** 2) + (item.get_position()[2] ** 2)) < global_variables.victim_proximity:
            return 'U'
    return False


def is_close():
    if on_left() or on_right():
        return 'T'
    if visible():
        return visible()
    return 0


# Sends a message to the game controller
def send_message(v1, v2, victim_type):
    message = struct.pack('i i c', v1, v2, victim_type)
    robot.emitter.send(message)
    print('sent: ', victim_type, end='')
    print('      ', v1, end='')
    print('      ', v2)
