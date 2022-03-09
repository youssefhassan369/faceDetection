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
    for i in range(1, 41):
        name = ''
        name += 's' + str(i)
        target_names.append(name)
    return y


def split(data):
    train = data[1::2]  # Elements from list1 starting from 1 iterating by 2
    test = data[::2]  # Elements from list1 starting from 0 iterating by 2
    test = np.array(test)
    train = np.array(train)
    return train, test
