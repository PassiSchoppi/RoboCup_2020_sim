import cv2
import numpy as np
import image_function
import global_variables

path = 'D:/Programmieren/RoboCupSim2020/RoboCup_2020_sim/code/'

def take_picture(camera, debug):

    #debug = False

    img = camera.getImage()
    img = np.array(np.frombuffer(img, np.uint8).reshape((camera.getHeight(), camera.getWidth(), 4)))
    img[:, :, 2] = np.zeros([img.shape[0], img.shape[1]])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if debug:
        image_function.write(gray, 'original.txt')

    height = int(len(gray[0])) - 1
    width = int(len(gray)) - 1

    black = 1
    white = 1

    edit = []
    for i in range(0, int(int(height / 2))):
        edit.append([])
    for i in range(0, int(height / 2)):
        for j in range(0, int(width / 2)):
            if (gray[i * 2][j * 2] <= 20):# 50):  # Grenzwet: 75
                edit[i].append(1)
                black += 1
            else:
                edit[i].append(0)
                white += 1

    if (white / black > 0.25):

        if debug:
            image_function.write(edit, 'edit.txt')

        smaller_edit = edit

        if debug:
            image_function.write(smaller_edit, 'smaller_edit.txt')

        #######################################################
        # sucht Raender des Bildes nach schwarzen Flaechen ab #
        #######################################################
        height = len(smaller_edit) - 1
        width = len(smaller_edit[0]) - 1


        for i in range(0, width):
            if (smaller_edit[0][i] == 1):
                image_function.blop_deleting(i, 0, 0, smaller_edit)
            if (smaller_edit[height][i] == 1):
                image_function.blop_deleting(i, height, 0, smaller_edit)
        for j in range(0, height):
            if (smaller_edit[j][0] == 1):
                image_function.blop_deleting(0, j, 0, smaller_edit)
            if (smaller_edit[j][width] == 1):
                image_function.blop_deleting(width, j, 0, smaller_edit)

        if debug:
            image_function.write(smaller_edit, 'border_less.txt')

        num = 1
        for i in range(0, width):
            for j in range(0, height):
                if (smaller_edit[j][i] == 1):
                    num += 1
                    image_function.blop_deleting(i, j, num, smaller_edit)

        if debug:
            image_function.write(smaller_edit, 'blop.txt')

        index = []
        for i in range(0, num + 1):  # Index Array wird mit dumping Werten gefuellt
            index.append(0)

        for i in range(0, width):  # das Array wird nach den Indexen abgesucht
            for j in range(0, height):  # Haeufigkeit des einzelnen Indexen wird in Array festgehalten
                for k in range(0, num + 1):
                    if (smaller_edit[i][j] == k):
                        index[k] = index[k] + 1

        if debug:
            for l in range(0, len(index)):
                print(str(l) + ': ' + str(index[l]))

        possible_blops = []
        for k in range(1, len(index)):
            if (index[k] > 200) or (index[k] < 10):  # maximal bzw minimal Groesse eines Blopes
                for i in range(1, width):
                    for j in range(1, height):  # ueberschreibt jeden uebrigen Blop der zu Gross bzw. zu Klein ist mit Null
                        if (smaller_edit[j][i] == k):
                            smaller_edit[j][i] = 0
            else:
                possible_blops.append(k)

        if debug:
            image_function.write(smaller_edit, 'letter_only.txt')
    
        results = []
        for index in possible_blops:
            results.append(detect_letter(smaller_edit, index, debug))

        for result in results:
            if (result == 'H') or (result == 'U') or (result == 'S'):
                return result
                break

    else:
        print('to dark')
        print('')
        return 'e'
    return 'e'


def detect_letter(smaller_edit, index, debug):
    height = len(smaller_edit) - 1
    width = len(smaller_edit[0]) - 1

    black_1 = [width, height]  # links oben
    black_2 = [0, 0]  # rechts unten

    for i in range(0, width):
        for j in range(0, height):
            if (smaller_edit[i][j] == index):
                if (black_2[1] < j):
                    black_2[1] = j

    for j in range(0, height):
        for i in range(0, width):
            if (smaller_edit[i][j] == index):
                if (black_2[0] < i):
                    black_2[0] = i

    for i in range(0, width):
        for j in range(0, height):
            if (smaller_edit[width - i][height - j] == index):
                if (black_1[1] > height - j):
                    black_1[1] = height - j

    for j in range(0, height):
        for i in range(0, width):
            if (smaller_edit[width - i][height - j] == index):
                if (black_1[0] > width - i):
                    black_1[0] = width - i


    smaller_edit[black_1[0]][black_1[1]] = 111
    smaller_edit[black_2[0]][black_2[1]] = 222

    if debug:
        image_function.write(smaller_edit, 'point.txt')

    letter_height = black_2[0] - black_1[0] + 1
    letter_width = black_2[1] - black_1[1] + 1

    n = letter_width + 1  # x
    m = letter_height + 1  # y
    crop = [[0] * n for i in range(m)]  # erstellt Array mit dumping Werten in der Groesse des Bereichs des Buchstabens

    for i in range(0, letter_width):
        for j in range(0, letter_height):  # uebergibt Bereich um den Buchstaben in extra Array
            crop[j][i] = smaller_edit[black_1[0] + j][black_1[1] + i]

    if debug:
        image_function.write(crop, 'crop.txt')

    if (len(crop) > 0):
        height = len(crop) - 1
        width = len(crop[0]) - 1
        #letter = 0
        #emty = 0

        #for i in range(width):
        #    for j in range(height):
        #        if (crop[i][j] == 0):
        #            emty = emty + 1
        #        else:
        #            letter = letter + 1

        hit_1 = False
        hit_2 = False
        hit_3 = False
        hit_4 = False

        for k in range(0, round(width / 3)):
            if (crop[round(height / 2)][k] != 0):   # mitte Hoehe; links
                hit_1 = True
            if (crop[round(height / 2)][width - k] != 0): # mitte Hoehe; rechts
                hit_3 = True
        for k in range(0, round(height / 3)):
            if (crop[k][round(width / 2)] != 0):    # mitte Breite; oben
                hit_2 = True
            if (crop[height - k][round(width / 2)] != 0):   # mitte Breite; unten
                hit_4 = True

        if debug:
            print(hit_1)
            print(hit_2)
            print(hit_3)
            print(hit_4)

        letter = False

        if (hit_1) and not(hit_2) and (hit_3) and not(hit_4):
            # print('H')
            # os.rename('images/insert/' + img_name, 'images/letter/H/' + img_name)
            letter = True
            return 'H'
        if (hit_1) and (hit_2) and (hit_3) and (hit_4):
            # print('S')
            # os.rename('images/insert/' + img_name, 'images/letter/S/' + img_name)
            letter = True
            return 'S'
        if (hit_1) and not(hit_2) and (hit_3) and (hit_4):
            # print('U')
            # os.rename('images/insert/' + img_name, 'images/letter/U/' + img_name)
            letter = True
            return 'U'
        if not (letter):
            # os.rename('images/insert/' + img_name, 'images/#/' + img_name)
            # print('no letter')
            return 'e'

        # print('')
    else:
        # os.rename('images/insert/' + img_name, 'images/#/' + img_name)
        # print('weg')
        # print('')
        return 'e'
