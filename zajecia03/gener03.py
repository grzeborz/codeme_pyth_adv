def three_numbers():
    for item in [13, 17, 19]:
        yield item


if __name__ == '__main__':
    tn = three_numbers()

    print(type(tn))

    print(next(tn))
    print(next(tn))
    print(next(tn))
