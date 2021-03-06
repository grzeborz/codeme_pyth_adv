class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    def __iadd__(self, other):
        print('Zawołano metodę __iadd__()')
        return self + other


if __name__ == '__main__':
    p1 = Point(2, 3)

    print(p1)

    p1 += Point(100, 100)

    print(p1)
