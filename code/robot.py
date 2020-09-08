from controller import Robot
import global_variables

# init the robot
robot = Robot()

# init wheels
wheel_left = robot.getMotor("left wheel motor")
wheel_right = robot.getMotor("right wheel motor")

wheel_left.setPosition(float("inf"))
wheel_right.setPosition(float("inf"))

# init sensors
leftSensors = [robot.getDistanceSensor("ps5"), robot.getDistanceSensor("ps6")]
leftSensors[0].enable(global_variables.timeStep)
leftSensors[1].enable(global_variables.timeStep)
rightSensors = [robot.getDistanceSensor("ps1"), robot.getDistanceSensor("ps2")]
rightSensors[0].enable(global_variables.timeStep)
rightSensors[1].enable(global_variables.timeStep)
frontSensors = [robot.getDistanceSensor("ps7"), robot.getDistanceSensor("ps0")]
frontSensors[0].enable(global_variables.timeStep)
frontSensors[1].enable(global_variables.timeStep)
