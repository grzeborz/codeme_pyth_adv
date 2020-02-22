class RangeNumbers:
    _lower_border = 0
    def __init__(self, upper_border,lower_border=_lower_border, step =1):
        self.number = lower_border
        self.upper_border = upper_border
        self.step = step
        if self.step <= 0:
            raise ValueError(f'Value {self.step} is lower or equal 0')

    def __next__(self):
        self.firstnumber = self.number
        self.number += self.step

        if self.number > self.upper_border:
            raise StopIteration
        return self.firstnumber

    def __iter__(self):
        return self


if __name__ == '__main__':
    numbers = RangeNumbers(20, 2)
    numbers1 = RangeNumbers(20)
    numbers2 = RangeNumbers(10, -10,3)
    numbers3 = RangeNumbers(10, -10,-1)
    print(list(numbers))
    print(list(numbers1))
    print(list(numbers2))
    print(list(numbers3))
    pass  # tutaj możesz testować działanie funkcji
