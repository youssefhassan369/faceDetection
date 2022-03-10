import numpy as np


def covariance(train):
    train = np.array(train)
    mean = train.mean(axis=0)
    mean = np.array(mean)
    centered_data = train - mean.transpose()
    centered_data = np.array(centered_data)
    covariance = (np.dot(centered_data.transpose(), centered_data)) / train.shape[0]
    return covariance


def PCA(train):
    cov = covariance(train)
    eigen_val, eigen_vect = np.linalg.eig(cov)
    print(eigen_val)
    print(eigen_vect)

