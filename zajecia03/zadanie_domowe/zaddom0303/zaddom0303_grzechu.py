# tutaj wpisz swoje imię i nazwisko

def counter_generator(start=0, digits=2):
    # tutaj wpisz swój kod
    start = 00
    yield (str(start).zfill(digits))
    while start < 99:
        start += 1
        yield (str(start).zfill(digits))

    return start


if __name__ == '__main__':
    # tutaj możesz przetestować swój kod

    # print(counter_generator)
    en = counter_generator(2)
    for number in en:
        print(number)
        # print(str(number).zfill(2))

    pass

    # tl = (number * 1.23 for number in [13, 17, 19])
    #
    # numbers_with_tax = list(tl)
    #
    # print(numbers_with_tax)
