import numpy as np
import cv2


def load(folder):
    x = []
    y = []
    for i in range(1, 41):  # accessing folders of directory
        for k in range(1, 11):  # accessing photos in each folder
            img = cv2.imread('./' + folder + '/s' + str(i) + "/" + str(k) + '.pgm', 0)
            height1, width1 = img.shape[:2]
            img_col = np.array(img, dtype='float64').flatten()  # converting image to 1 dimentional image
            subject = int(i)
            y.append(img_col)
            x.append(subject)

    y = np.array(y)
    target_names = []
    print(y.shape)
    print(y)
    for i in range(1, 41):
        name = ''
        name += 's' + str(i)
        target_names.append(name)
