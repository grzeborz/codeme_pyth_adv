def even_numbers():
    number = 0
    while number < 100:
        number += 2
        yield number


if __name__ == '__main__':

    en = even_numbers()

    # print(type(en))

    for number in en:
        print(number)

# porównaj z `iter02.py`
