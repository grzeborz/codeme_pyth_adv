class EvenNumbers:
    def __init__(self):
        self.number = 0


if __name__ == '__main__':
    numbers = EvenNumbers()

    # poniższa pętla nie ma prawa działać
    for number in numbers:
        print(number)
