import numpy as np

def LDA(train):
    meanVector=train.mean(axis=0)
    meanVector=np.array(meanVector)
    print(meanVector);