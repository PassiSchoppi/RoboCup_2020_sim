import robot


def in_front():
    return robot.frontSensors[0].getValue() < 0.075


def on_right():
    return robot.rightSensors[0].getValue() < 0.075


def on_left():
    return robot.leftSensors[0].getValue() < 0.075
