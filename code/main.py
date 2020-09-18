from controller import Robot
import sys
sys.path.append('D:\\Programmieren\\RoboCup2020\\RoboCup_2020_sim\\code\\')
from movements import *
from setup import *
import take_image


while robot.step(timeStep) != -1:
    speeds[0] = 0
    speeds[1] = 0
    take_image.take_picture(camera, False)

    #for i in range(2):
    #    #for sensors on the left, either
    #    if leftSensors[i].getValue() < 0.05:
    #        turn_right()
    #    #for sensors on the right, either
    #    elif rightSensors[i].getValue() < 0.05:
    #        turn_left()
    
    ##for both front sensors
    #if frontSensors[0].getValue() < 0.1 and frontSensors[1].getValue() < 0.1:
    #    spin()

    #wheel_left.setVelocity(speeds[0])
    #wheel_right.setVelocity(speeds[1])
