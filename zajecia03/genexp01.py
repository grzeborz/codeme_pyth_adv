# porównaj z gener04.py

if __name__ == '__main__':
    tn = (item * 1.23 for item in [13, 17, 19])

    print(type(tn))

    print(next(tn))
    print(next(tn))
    print(next(tn))
