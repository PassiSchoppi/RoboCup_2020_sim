import global_variables
import robot


def hex_to_rgb(value):
    value = value.lstrip('#')
    return list(int(value[i:i + 2], 16) for i in (0, 2, 4))


def color():
    image = robot.colour_camera.getImage()
    print(image)
    # if it is darker than hole_colour
    if image[0] <= global_variables.hole_colour[0] and \
            image[1] <= global_variables.hole_colour[1] and \
            image[2] <= global_variables.hole_colour[2]:
        return global_variables.BLACK
    # if it is around swamp_color
    tol = 5
    if global_variables.swamp_colour[0] - tol <= image[0] <= global_variables.swamp_colour[0] + tol and \
            global_variables.swamp_colour[1] - tol <= image[1] <= global_variables.swamp_colour[1] + tol and \
            global_variables.swamp_colour[2] - tol <= image[2] <= global_variables.swamp_colour[2] + tol:
        return global_variables.SWAMP
    # if it is around silver_color
    tol = 5
    if global_variables.silver_color[0] - tol <= image[0] <= global_variables.silver_color[0] + tol and \
            global_variables.silver_color[1] - tol <= image[1] <= global_variables.silver_color[1] + tol and \
            global_variables.silver_color[2] - tol <= image[2] <= global_variables.silver_color[2] + tol:
        return global_variables.SILVER
    return global_variables.SILVER
