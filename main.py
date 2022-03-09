from Data import load, split
from PCA import func
from LDA import LDA

if __name__ == '__main__':
    data, labels = load('Dataset')
    train, test, train_labels, test_labels = split(data, labels)
    func(train)
    LDA(train)

