class Klass:
    number = 17

    # poniższy jest wołany tylko, gdy dany artybut nie został znaleziony
    def __getattr__(self, item):
        print(f'Nie ma takiego atrybutu "{item}"')


if __name__ == '__main__':
    k = Klass()
    print(k.number)
    print(k.text)
    print(k.text)
    print(k.text)
