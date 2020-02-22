def three_numbers_with_tax():
    for item in [13, 17, 19]:
        yield item * 1.23


if __name__ == '__main__':
    tn = three_numbers_with_tax()

    print(type(tn))

    print(next(tn))
    print(next(tn))
    print(next(tn))
