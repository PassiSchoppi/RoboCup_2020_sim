import robot


wall_range = 0.080


def in_front():
    return robot.frontSensors[0].getValue() < wall_range


def on_right():
    return robot.rightSensors[0].getValue() < wall_range


def on_left():
    return robot.leftSensors[0].getValue() < wall_range
