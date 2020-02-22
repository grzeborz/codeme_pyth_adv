class Klass:
    number = 17


if __name__ == '__main__':

    k = Klass()

    # print(k.number)
    print(getattr(k, 'number', None))

    # print(Klass.text)
    print(getattr(k, 'text', None))
