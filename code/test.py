import numpy as np

height = 10
width = 5

edit = []
edit = [edit[offset:offset+width] for offset in range(0, width*height, width)]
for i in range(height):
    for j in range(width):
        edit[i].append(0)

edit[1][2] = 4
for i in range(len(edit)):
    print(str(edit[i]))
