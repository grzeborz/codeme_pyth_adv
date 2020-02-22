class EvenNumbers:
    def __init__(self):
        self.number = 0

    # obiekt, który ma tę metodę jest iteratorem (eng. "iterator")
    def __next__(self):
        self.number += 2
        return self.number

    # obiekt, który ma metodę __iter__, która zwraca iterator, nazywamy iterowalnym (eng. "iterable")
    def __iter__(self):
        return self


if __name__ == '__main__':
    numbers = EvenNumbers()

    for number in numbers:
        print(number)
        # UWAGA! Nieskończona pętla!
