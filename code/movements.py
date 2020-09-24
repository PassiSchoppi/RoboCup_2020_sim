import robot
import wall
import global_variables

max_velocity: float = 6.28

#        [left wheel speed, right wheel speed]
speeds = [0, 0]


def drive_straight():
    # set left wheel speed
    speeds[0] = max_velocity - .2
    # set right wheel speed
    speeds[1] = max_velocity - .2
    mult = 100
    if robot.facing == global_variables.NORTH:
        speeds[0] = speeds[0] + mult * (robot.latest_gps_position[0] - robot.gps.getValues()[0])
        speeds[1] = speeds[1] - mult * (robot.latest_gps_position[0] - robot.gps.getValues()[0])
    if robot.facing == global_variables.EAST:
        speeds[0] = speeds[0] + mult * (robot.latest_gps_position[2] - robot.gps.getValues()[2])
        speeds[1] = speeds[1] - mult * (robot.latest_gps_position[2] - robot.gps.getValues()[2])
    if robot.facing == global_variables.SOUTH:
        speeds[0] = speeds[0] - mult * (robot.latest_gps_position[0] - robot.gps.getValues()[0])
        speeds[1] = speeds[1] + mult * (robot.latest_gps_position[0] - robot.gps.getValues()[0])
    if robot.facing == global_variables.WEST:
        speeds[0] = speeds[0] - mult * (robot.latest_gps_position[2] - robot.gps.getValues()[2])
        speeds[1] = speeds[1] + mult * (robot.latest_gps_position[2] - robot.gps.getValues()[2])
    robot.wheel_left.setVelocity(speeds[0])
    robot.wheel_right.setVelocity(speeds[1])


def drive_back():
    # set left wheel speed
    speeds[0] = -max_velocity + .2
    # set right wheel speed
    speeds[1] = -max_velocity + .2
    mult = 100
    if robot.facing == global_variables.NORTH:
        speeds[0] = speeds[0] - mult * (robot.latest_gps_position[0] - robot.gps.getValues()[0])
        speeds[1] = speeds[1] + mult * (robot.latest_gps_position[0] - robot.gps.getValues()[0])
    if robot.facing == global_variables.EAST:
        speeds[0] = speeds[0] - mult * (robot.latest_gps_position[2] - robot.gps.getValues()[2])
        speeds[1] = speeds[1] + mult * (robot.latest_gps_position[2] - robot.gps.getValues()[2])
    if robot.facing == global_variables.SOUTH:
        speeds[0] = speeds[0] + mult * (robot.latest_gps_position[0] - robot.gps.getValues()[0])
        speeds[1] = speeds[1] - mult * (robot.latest_gps_position[0] - robot.gps.getValues()[0])
    if robot.facing == global_variables.WEST:
        speeds[0] = speeds[0] + mult * (robot.latest_gps_position[2] - robot.gps.getValues()[2])
        speeds[1] = speeds[1] - mult * (robot.latest_gps_position[2] - robot.gps.getValues()[2])
    robot.wheel_left.setVelocity(speeds[0])
    robot.wheel_right.setVelocity(speeds[1])


def turn_right(speed=0.3):
    # TODO faster turning
    # set left wheel speed
    speeds[0] = speed * max_velocity
    # set right wheel speed
    speeds[1] = -speed * max_velocity
    robot.wheel_left.setVelocity(speeds[0])
    robot.wheel_right.setVelocity(speeds[1])


def turn_left(speed=0.3):
    # TODO faster turning
    # set left wheel speed
    speeds[0] = -speed * max_velocity
    # set right wheel speed
    speeds[1] = speed * max_velocity
    robot.wheel_left.setVelocity(speeds[0])
    robot.wheel_right.setVelocity(speeds[1])


def stop():
    # set left wheel speed
    speeds[0] = 0
    # set right wheel speed
    speeds[1] = 0
    robot.wheel_left.setVelocity(speeds[0])
    robot.wheel_right.setVelocity(speeds[1])
