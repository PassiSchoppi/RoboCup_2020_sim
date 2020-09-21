import robot
import struct
import global_variables


def on_left():
    if robot.left_heat_sensor.getValue() > 37:
        return True
    return False


def on_right():
    if robot.right_heat_sensor.getValue() > 37:
        return True
    return False


# Sends a message to the game controller
def send_message(v1, v2, victim_type):
    message = struct.pack('i i c', v1, v2, victim_type)
    robot.emitter.send(message)
    print('sent: ', victim_type, end='')
    print('      ', v1, end='')
    print('      ', v2)
