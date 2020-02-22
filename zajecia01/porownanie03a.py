class Footman:
    _max_hp = 60

    def __init__(self, hp=_max_hp):
        self._hp = hp
        self._damage = 6

    def __repr__(self):
        return f'Footman(hp={self._hp})'

    def attack(self):
        print(f'Footman zadał {self._damage} pkt. obrażeń')


if __name__ == '__main__':
    f1 = Footman()
    f2 = Footman(80)  # wybitnie wytrzymały rycerz :)

    print(f1 == f2)  # UWAGA! to nie działa tak jak podpowiada intuicja

    # W przypadku niezdefiniowania metody __eq__, obiekty są sobie równe tylko, gdy jest to ten sam obiekt

    f3 = Footman()

    print(f1 == f3)
    print(f1 == f1)

    # https://docs.python.org/3/reference/datamodel.html#object.__hash__
