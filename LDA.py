import numpy as np


def LDA(train):
    mean = []
    for i in range(1, 41):
        temp =[]
        for j in range(((i - 1) * 5), (i * 5) ):
            temp.append(train[j])
        temp=np.array(temp)
        meanVector = temp.mean(axis=0)
        meanVector = np.array(meanVector)
        mean.append(meanVector)

    mean = np.array(mean)
    temp = np.array(temp)
    print(mean.shape)

    overall_mean = mean.mean(axis=0)
    print(overall_mean.shape)



