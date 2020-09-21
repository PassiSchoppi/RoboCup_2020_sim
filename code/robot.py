from controller import Robot
import global_variables

# init the robot
robot = Robot()

# init orientation variables
position = [round(global_variables.map_size/2), round(global_variables.map_size/2)]
facing = global_variables.NORTH

# init wheels
wheel_left = robot.getMotor("left wheel motor")
wheel_right = robot.getMotor("right wheel motor")

wheel_left.setPosition(float("inf"))
wheel_right.setPosition(float("inf"))

left_pos_sensor = robot.getPositionSensor("left wheel sensor")
left_pos_sensor.enable(global_variables.timeStep)
right_pos_sensor = robot.getPositionSensor("right wheel sensor")
right_pos_sensor.enable(global_variables.timeStep)

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

# init heat/temperature sensor
left_heat_sensor = robot.getLightSensor("left_heat_sensor")
right_heat_sensor = robot.getLightSensor("right_heat_sensor")

left_heat_sensor.enable(global_variables.timeStep)
right_heat_sensor.enable(global_variables.timeStep)

# init cameras
camera = robot.getCamera("camera_centre")
camera.enable(global_variables.timeStep)
cameraR = robot.getCamera("camera_right")
cameraR.enable(global_variables.timeStep)
cameraL = robot.getCamera("camera_left")
cameraL.enable(global_variables.timeStep)

colour_camera = robot.getCamera("colour_sensor")
colour_camera.enable(global_variables.timeStep)

# other stuff
emitter = robot.getEmitter("emitter")

gps = robot.getGPS("gps")
gps.enable(global_variables.timeStep)

latest_gps_position = [0, 0, 0]
latest_lws_value = 0
latest_rws_value = 0
