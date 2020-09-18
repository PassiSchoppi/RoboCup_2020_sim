from controller import Robot

timeStep = 32

robot = Robot()

#wheel_left = robot.getMotor("left wheel motor")
#wheel_right = robot.getMotor("right wheel motor")

camera = robot.getCamera("camera_centre")
camera.enable(timeStep)
camerar = robot.getCamera("camera_right")
camerar.enable(timeStep)
cameral = robot.getCamera("camera_left")
cameral.enable(timeStep)

leftSensors = []
rightSensors = []
frontSensors = []

frontSensors.append(robot.getDistanceSensor("ps7"))
frontSensors[0].enable(timeStep)
frontSensors.append(robot.getDistanceSensor("ps0"))
frontSensors[1].enable(timeStep)

rightSensors.append(robot.getDistanceSensor("ps1"))
rightSensors[0].enable(timeStep)
rightSensors.append(robot.getDistanceSensor("ps2"))
rightSensors[1].enable(timeStep)

leftSensors.append(robot.getDistanceSensor("ps5"))
leftSensors[0].enable(timeStep)
leftSensors.append(robot.getDistanceSensor("ps6"))
leftSensors[1].enable(timeStep)

#wheel_left.setPosition(float("inf"))
#wheel_right.setPosition(float("inf"))
