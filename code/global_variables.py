timeStep = 32

state = 1

# only even numbers
map_size = 50

hole_colour = b'ppp\xff'
swamp_colour = b'\x82\xd2\xee\xff'
silver_color = b'\x97\x97\x97\xff'

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

FRONT = 0
RIGHT = 1
BACK = 2
LEFT = 3

WHITE = 0
BLACK = 1
SWAMP = 2
SILVER = 3

# Variables related to timers and delays
startTime = 0
duration = 0
victimDetectedGlobal = False
victimTimer = 0

field_size = 0.113
quater_rotation_value = 2.15
