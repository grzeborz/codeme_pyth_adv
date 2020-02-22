class Klass:
    number = 17

    def __getattr__(self, item):
        print(f'Nie ma takiego atrybutu "{item}"')
        setattr(self, item, 'default')  # skoro go nie ma, możemy go stworzyć


if __name__ == '__main__':
    k = Klass()
    print(k.number)
    print(k.text)
    print(k.text)
    print(k.text)
