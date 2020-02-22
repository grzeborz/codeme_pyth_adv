class ColouredText:
    def __enter__(self):
        print('\033[91m', end='')

    def __exit__(self, *args):
        print('\033[0m', end='')


if __name__ == '__main__':
    with ColouredText():
        print('hej!')

    print('hej!')
