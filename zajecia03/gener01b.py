def even_numbers():
    number = 0
    while number < 100:
        yield number
        number += 2


if __name__ == '__main__':

    en = even_numbers()

    for number in en:
        print(number)
