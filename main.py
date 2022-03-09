from Data import load, split

if __name__ == '__main__':
    data, labels = load('Dataset')
    split(data, labels)
