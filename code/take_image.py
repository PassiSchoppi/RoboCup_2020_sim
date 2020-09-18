import cv2
import numpy as np
import sys

import image_function

path = sys.path[-1]


def take_picture(camera, debug):
    img = camera.getImage()
    img = np.array(np.frombuffer(img, np.uint8).reshape((camera.getHeight(), camera.getWidth(), 4)))
    img[:, :, 2] = np.zeros([img.shape[0], img.shape[1]])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    width = int(len(gray[0]) / 2) - 1
    height = int(len(gray) / 2) - 1

    edit = []
    edit = [edit[offset:offset + width] for offset in range(0, width * height, width)]  # edit[height][width]
    for i in range(height):
        for j in range(width):
            if gray[i * 2][j * 2] < 75:  # Grenzwet: 75
                edit[i].append(1)
            else:
                edit[i].append(0)

    image_function.write(edit, 'edit.txt')

    smaller_edit = edit

    image_function.write(smaller_edit, 'smaller_edit.txt')

    num = 1
    for i in range(width):  # sucht nach schwarzen Flaechen(blops)
        for j in range(height):  # jeder Blop erhaelt einen eigenen Index
            if smaller_edit[i][j] == 1:
                num = num + 1
                image_function.blop_naming(i, j, num, height, width, smaller_edit)

    image_function.write(smaller_edit, 'blop.txt')

    for i in range(height):  # geht die Raender des Bildes ab
        if smaller_edit[0][i] >= 1:  # sucht nach Blops, die am Rand liegen
            image_function.blop_deleting(0, i, 0, height, width,
                                         smaller_edit)  # ueberschreibt diese Blops rekursiev mit Null
        if smaller_edit[width - 1][i] >= 1:
            image_function.blop_deleting(width - 1, i, 0, height, width, smaller_edit)

    image_function.write(smaller_edit, 'border_less.txt')

    index = []
    for i in range(0, num + 1):  # Index Array wird mit dumping Werten gefuellt
        index.append(0)

    for i in range(0, width):  # das Array wird nach den Indexen abgesucht
        for j in range(0, height):  # Haeufigkeit des einzelnen Indexen wird in Array festgehalten
            for k in range(0, num + 1):
                if smaller_edit[i][j] == k:
                    index[k] = index[k] + 1

    if debug:
        for l in range(0, len(index)):
            print(f'{str(l)}: {str(index[l])}')

    up = height
    down = 0

    for k in range(1, len(index)):
        if (index[k] > 300) or (index[k] < 30):  # maximal bzw minimal Groesse eines Blopes
            for i in range(1, width):
                for j in range(1, height):  # ueberschreibt jeden uebrigen Blop der zu Gross bzw. zu Klein ist mit Null
                    if smaller_edit[i][j] == k:
                        smaller_edit[i][j] = 0

    image_function.write(smaller_edit, 'letter_only.txt')

    black_1 = [width - 1, height - 1]  # links oben
    black_2 = [0, 0]  # rechts unten

    for i in range(2, width):
        for j in range(2, height):
            if smaller_edit[i][j] != 0:
                if black_2[1] < j:
                    black_2[1] = j + 2

    for j in range(2, height):
        for i in range(2, width):
            if smaller_edit[i][j] != 0:
                if black_2[0] < i:
                    black_2[0] = i + 2

    for i in range(2, width - 2):
        for j in range(2, height - 2):
            if smaller_edit[width - i][height - j] != 0:
                if black_1[1] > height - j:
                    black_1[1] = height - j - 2

    for j in range(2, height - 2):
        for i in range(2, width - 2):
            if smaller_edit[width - i][height - j] != 0:
                if black_1[0] > width - i:
                    black_1[0] = width - i - 2

    image_function.write(smaller_edit, 'point.txt')

    letter_width = black_2[0] - black_1[0]
    letter_height = black_2[1] - black_1[1]

    n = letter_width + 2  # x
    m = letter_height + 2  # y
    crop = [[0] * m for i in range(n)]  # erstellt Array mit dumping Werten in der Groesse des Bereichs des Buchstabens

    for i in range(letter_width):
        for j in range(letter_height):  # uebergibt Bereich um den Buchstaben in extra Array
            crop[i + 1][j + 1] = smaller_edit[black_1[0] + i][black_1[1] + j]

    image_function.write(crop, 'crop.txt')

    if len(crop) > 0:
        width = len(crop)
        height = len(crop[1])
        letter = 0
        emty = 0

        for i in range(width):
            for j in range(height):
                if (crop[i][j] == 0):
                    emty = emty + 1
                else:
                    letter = letter + 1

        hit_1 = False
        hit_2 = False
        hit_3 = False
        hit_4 = False

        for k in range(1, round(width / 3)):
            if crop[k][round(height / 2)] != 0:
                hit_1 = True
            if crop[width - k][round(height / 2)] != 0:
                hit_3 = True
        for k in range(1, round(height / 3)):
            if crop[round(width / 2)][k] != 0:
                hit_2 = True
            if crop[round(width / 2)][height - k] != 0:
                hit_4 = True

        if debug:
            print(hit_1)
            print(hit_2)
            print(hit_3)
            print(hit_4)

        letter = False

        if not hit_1 and hit_2 and not hit_3 and not hit_4:
            if debug:
                print('H')
            letter = True
            return 'H'
        if hit_1 and not hit_2 and hit_3 and hit_4:
            if debug:
                print('S')
            letter = True
            return 'S'
        if not hit_1 and hit_2 and hit_3 and hit_4:
            if debug:
                print('U')
            letter = True
            return 'U'
        if not letter:
            if debug:
                print('no letter')
            return 'e'

        # print('')
    else:
        pass
        # print('weg')
        # print('')
    return 'e'
