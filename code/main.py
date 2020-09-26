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
import victim
import time

first = True
second = False
third = False

while robot.robot.step(global_variables.timeStep) != -1:
    pass
    # get which direction the robot is facing
    if first:
        location = robot.gps.getValues()
        robot.latest_gps_position = robot.gps.getValues()
        first = False
    if robot.facing == 5:
        robot.wheel_left.setVelocity(movements.max_velocity / 2)
        robot.wheel_right.setVelocity(movements.max_velocity / 2)
        print('1: ', robot.gps.getValues())
        print('2: ', location)
        acc = 3
        if round(robot.gps.getValues()[0], acc) > round(location[0], acc):
            print(round(robot.gps.getValues()[0], acc), end=" > ")
            print(round(location[0], acc))
            robot.wheel_left.setVelocity(0)
            robot.wheel_right.setVelocity(0)
            robot.facing = global_variables.EAST
            print('found facing direction: ', robot.facing)
            second = True
        elif round(robot.gps.getValues()[0], acc) < round(location[0], acc):
            print(round(robot.gps.getValues()[0], acc), end=" < ")
            print(round(location[0], acc))
            robot.wheel_left.setVelocity(0)
            robot.wheel_right.setVelocity(0)
            robot.facing = global_variables.WEST
            print('found facing direction: ', robot.facing)
            second = True
        elif round(robot.gps.getValues()[2], acc) < round(location[2], acc):
            print(round(robot.gps.getValues()[2], acc), end=" < ")
            print(round(location[2], acc))
            robot.wheel_left.setVelocity(0)
            robot.wheel_right.setVelocity(0)
            robot.facing = global_variables.NORTH
            print('found facing direction: ', robot.facing)
            second = True
        elif round(robot.gps.getValues()[2], acc) > round(location[2], acc):
            print(round(robot.gps.getValues()[2], acc), end=" > ")
            print(round(location[2], acc))
            robot.wheel_left.setVelocity(0)
            robot.wheel_right.setVelocity(0)
            robot.facing = global_variables.SOUTH
            print('found facing direction: ', robot.facing)
            second = True
    if second:
        robot.wheel_left.setVelocity(- movements.max_velocity)
        robot.wheel_right.setVelocity(- movements.max_velocity)
        if robot.facing == global_variables.EAST:
            if robot.gps.getValues()[0] < location[0]:
                robot.wheel_left.setVelocity(0)
                robot.wheel_right.setVelocity(0)
                second = False
                third = True
        if robot.facing == global_variables.WEST:
            if robot.gps.getValues()[0] > location[0]:
                robot.wheel_left.setVelocity(0)
                robot.wheel_right.setVelocity(0)
                second = False
                third = True
        if robot.facing == global_variables.NORTH:
            if robot.gps.getValues()[2] > location[2]:
                robot.wheel_left.setVelocity(0)
                robot.wheel_right.setVelocity(0)
                second = False
                third = True
        if robot.facing == global_variables.SOUTH:
            if robot.gps.getValues()[2] < location[2]:
                robot.wheel_left.setVelocity(0)
                robot.wheel_right.setVelocity(0)
                second = False
                third = True
    if third:
        # movements.stop()
        # try:
        # print(take_image.take_picture(robot.cameraC, False))
        # except:
        #     print('Cant process images.')
        # print("left:", smoth_vars(robot.leftSensors[0].getValue()), end="")
        # print("@" * smoth_vars(robot.leftSensors[0].getValue()))
        # print("right:", smoth_vars(robot.rightSensors[0].getValue()), end="")
        # print("@" * smoth_vars(robot.rightSensors[0].getValue()))
        state.change_state()
        # print(take_image.take_picture(robot.cameraL, False), end=" : ")
        # print(take_image.take_picture(robot.cameraC, False), end=" : ")
        # print(take_image.take_picture(robot.cameraR, False))
        # print(robot.compass)
        # print(robot.colour_camera.getImage())
