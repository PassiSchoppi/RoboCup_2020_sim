import robot
import struct


# Sends a message to the game controller
def sendMessage(v1, v2, victimType):
    message = struct.pack('i i c', v1, v2, victimType)
    robot.emitter.send(message)


# Sents a message of the game controller that a victim (of a certain type) has been detected
def sendVictimMessage(victimType='N'):
    global messageSent
    position = robot.gps.getValues()

    if not messageSent:
        # robot type, position x cm, position z cm, victim type
        # The victim type is hardcoded as "H", but this should be changed to different victims for your program
        # Harmed = "H"
        # Stable = "S"
        # Unharmed = "U"
        # Heated (Temperature) = "T"
        sendMessage(int(position[0] * 100), int(position[2] * 100), victimType)
        messageSent = True
