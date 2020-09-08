import robot


def in_front():
    return robot.frontSensors[0].getValue() < 0.08


def on_right():
    return robot.frontSensors[0].getValue() < 0.08


def on_left():
    return robot.frontSensors[0].getValue() < 0.08
