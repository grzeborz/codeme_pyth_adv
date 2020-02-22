class Klass:
    number = 17


if __name__ == '__main__':
    k = Klass()

    attribute = input('Podaj nazwę atrybutu: ')  # UWAGA! ryzykowne! Można przysłonić coś ważnego!
    value = input(f'Podaj wartosc dla atrybutu {attribute}: ')

    setattr(k, attribute, value)

    print(k)
    print(k.__dir__())
