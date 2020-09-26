import robot
import struct
import global_variables
import take_image



def on_left():
    if robot.left_heat_sensor.getValue() > 35:
        return True
    return False


def on_right():
    if robot.right_heat_sensor.getValue() > 35:
        return True
    return False


def vis_victim():
    vic = take_image.take_picture(robot.cameraL, False)
    if not vic == 'e':
        return vic
    else:
        return False


# Sends a message to the game controller
def send_message(v1, v2, victim_type):
    message = struct.pack('i i c', v1, v2, victim_type)
    robot.emitter.send(message)
    print('sent: ', victim_type, end='')
    print('      ', v1, end='')
    print('      ', v2)
