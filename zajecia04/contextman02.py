class GoodManners:
    def __enter__(self):
        print('Dzień dobry')

    def __exit__(self, *args):
        print('Do widzenia')


if __name__ == '__main__':
    with GoodManners():
        a = 3
        b = 7
        print(a + b)
