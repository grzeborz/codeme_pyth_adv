# tutaj wpisz swoje imię i nazwisko


def number_of_digits(numbers):
    numbers_list = [(number, len(str(abs(number)))) for number in numbers]
    return numbers_list


if __name__ == '__main__':
    numbers = [91111, -7108079251, 405883740, 7942725602, 345220, 2915371507, 30, 9438104, 5736286, 984, 0]

    print(number_of_digits(numbers))
