def three_numbers():
    for item in [13, 17, 19]:
        yield item


if __name__ == '__main__':
    print(next(three_numbers()))
    print(next(three_numbers()))

    # Powyżej stworzyliśmy dwa odrębne generatory i z każdego wzięliśmy pierwszy element
