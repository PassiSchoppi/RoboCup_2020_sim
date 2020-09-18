import robot

max_velocity: float = 6.28

#        [left wheel speed, right wheel speed]
speeds = [0, 0]


def drive_straight():
    # set left wheel speed
    speeds[0] = max_velocity
    # set right wheel speed
    speeds[1] = max_velocity
    robot.wheel_left.setVelocity(speeds[0])
    robot.wheel_right.setVelocity(speeds[1])


def drive_back():
    # set left wheel speed
    speeds[0] = -0.4 * max_velocity
    # set right wheel speed
    speeds[1] = -0.4 * max_velocity
    robot.wheel_left.setVelocity(speeds[0])
    robot.wheel_right.setVelocity(speeds[1])


def turn_right():
    # set left wheel speed
    speeds[0] = 0.4 * max_velocity
    # set right wheel speed
    speeds[1] = -0.4 * max_velocity
    robot.wheel_left.setVelocity(speeds[0])
    robot.wheel_right.setVelocity(speeds[1])


def turn_left():
    # set left wheel speed
    speeds[0] = -0.4 * max_velocity
    # set right wheel speed
    speeds[1] = 0.4 * max_velocity
    robot.wheel_left.setVelocity(speeds[0])
    robot.wheel_right.setVelocity(speeds[1])


def stop():
    # set left wheel speed
    speeds[0] = 0
    # set right wheel speed
    speeds[1] = 0
    robot.wheel_left.setVelocity(speeds[0])
    robot.wheel_right.setVelocity(speeds[1])
