class Klass:
    def __init__(self):
        print('Nowy obiekt:', self)

    def __del__(self):
        print('Usunięto obiekt:', self)


if __name__ == '__main__':
    k1 = Klass()

    del k1

    print('Koniec programu')
