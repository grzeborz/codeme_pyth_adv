class EvenNumbers:
    def __init__(self):
        self.number = 0

    def __next__(self):
        self.number += 2

        if self.number > 100:  # najwyraźniej, nie chcemy liczb parzystych większych niż 100 :)
            raise StopIteration
        return self.number

    def __iter__(self):
        return self


if __name__ == '__main__':
    numbers = EvenNumbers()

    for number in numbers:
        print(number)

    numbers = EvenNumbers()  # UWAGA! aby kod poniżej działał, należy stworzyć nowy iterator EvenNumbers

    list_of_numbers = list(numbers)
    print(list_of_numbers)
