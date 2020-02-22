def countdown():
    print('rozpoczynam odliczanie!')

    yield 3
    yield 2
    yield 1

    print('i ostatnie moje słowo...')

    yield 0

    print('odliczanie się już skończyło')


if __name__ == '__main__':
    cd = countdown()

    print(next(cd))
    print(next(cd))
    print(next(cd))
    print(next(cd))
    print(next(cd))
