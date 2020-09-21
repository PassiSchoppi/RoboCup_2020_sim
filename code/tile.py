import global_variables
import robot


def color():
    image = robot.colour_camera.getImage()
    # if it is darker than hole_colour
    tolerance = 5
    if image[0] <= global_variables.hole_colour[0] + tolerance and \
            image[1] <= global_variables.hole_colour[1] + tolerance and \
            image[2] <= global_variables.hole_colour[2] + tolerance:
        return global_variables.BLACK
    # if it is around swamp_color
    tolerance = 5
    if global_variables.swamp_colour[0] - tolerance <= image[0] <= global_variables.swamp_colour[0] + tolerance and \
            global_variables.swamp_colour[1] - tolerance <= image[1] <= global_variables.swamp_colour[1] + tolerance and \
            global_variables.swamp_colour[2] - tolerance <= image[2] <= global_variables.swamp_colour[2] + tolerance:
        return global_variables.SWAMP
    # if it is around silver_color
    tolerance = 5
    if global_variables.silver_color[0] - tolerance <= image[0] <= global_variables.silver_color[0] + tolerance and \
            global_variables.silver_color[1] - tolerance <= image[1] <= global_variables.silver_color[1] + tolerance and \
            global_variables.silver_color[2] - tolerance <= image[2] <= global_variables.silver_color[2] + tolerance:
        return global_variables.SILVER
    return global_variables.SILVER
