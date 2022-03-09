import numpy as np
import cv2


def load(folder):
    x = []
    data = []
    for i in range(1, 41):  # accessing folders of directory
        for k in range(1, 11):  # accessing photos in each folder
            img = cv2.imread('./' + folder + '/s' + str(i) + "/" + str(k) + '.pgm', 0)
            height1, width1 = img.shape[:2]
            img_col = np.array(img, dtype='float64').flatten()  # converting image to 1 dimentional image
            subject = int(i)
            data.append(img_col)
            x.append(subject)

    data = np.array(data)
    labels = []
    for i in range(1, 41):
        name = ''
        name += 's' + str(i)
        labels.append(name)
    return data, labels


def split(data, labels):
    train = data[1::2]  # Elements from list1 starting from 1 iterating by 2
    train_labels = labels[1::2]
    test = data[::2]  # Elements from list1 starting from 0 iterating by 2
    test_labels = labels[::2]
    test = np.array(test)
    train = np.array(train)
    return train, test, train_labels, test_labels
