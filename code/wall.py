import robot

wall_range = 0.15


def in_front():
    return (robot.frontSensors[0].getValue() + robot.frontSensors[1].getValue()) / 2 < wall_range


def on_right():
    return robot.rightSensors[1].getValue() < wall_range


def on_left():
    return robot.leftSensors[0].getValue() < wall_range
