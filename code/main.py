import sys

sys.path.append('C:\\Users\\kalli\\Documents\\RoboCup_2020_sim\\code')

import global_variables
import robot
import state
import movements
import take_image
import tile
import struct
import wall


def smoth_vars(var):
    # print("var:", var)
    return round(var * 100)


while robot.robot.step(global_variables.timeStep) != -1:
    pass
    # movements.stop()
    # try:
    #     print(take_image.take_picture(robot.camera, False))
    # except:
    #     print('Cant process images.')
    # print("left:", smoth_vars(robot.leftSensors[0].getValue()), end="")
    # print("@" * smoth_vars(robot.leftSensors[0].getValue()))
    # print("right:", smoth_vars(robot.rightSensors[0].getValue()), end="")
    # print("@" * smoth_vars(robot.rightSensors[0].getValue()))
    state.change_state()
    print(wall.on_left(), end=" ")
    print(wall.in_front(), end=" ")
    print(wall.on_right())
