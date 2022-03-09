import numpy as np


def func(train):
    mean = train.mean(axis=0)
    mean = np.array(mean)
    centered_data = train - np.dot(1, mean.transpose())
    centered_data=np.array(centered_data)
    covariance = np.dot(centered_data, centered_data.transpose())
    print(np.cov(centered_data))
