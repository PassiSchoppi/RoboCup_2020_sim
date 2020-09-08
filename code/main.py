import sys

sys.path.append('C:\\Users\\kalli\\Documents\\RoboCup_2020_sim\\code')

import global_variables
import robot
import state

while robot.robot.step(global_variables.timeStep) != -1:
    state.state_change()
