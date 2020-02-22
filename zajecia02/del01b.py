class Klass:
    def __init__(self):
        print('Nowy obiekt:', self)

    def __del__(self):
        print('Usunięto obiekt:', self)


if __name__ == '__main__':
    k1 = Klass()

    k2 = k1

    del k1  # tutaj obiekt stworzony w linii 10 nie jest usuwany, bo jeszcze można się do niego dostać przez `k2`

    print('po usunięciu k1')

    del k2

    print('Koniec programu')
