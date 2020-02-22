def every_other_number(start=0):
    number = start
    while number < 100:
        yield number
        number += 2


if __name__ == '__main__':
    eon = every_other_number(29)

    print(list(eon))
