class Footman:
    _max_hp = 60

    def __init__(self, hp=_max_hp):
        self._hp = hp
        self._damage = 6

    def __repr__(self):
        return f'Footman(hp={self._hp})'

    def attack(self):
        print(f'Footman zadał {self._damage} pkt. obrażeń')

    def __eq__(self, other):
        if self._hp == other._hp:
            return True
        return False


if __name__ == '__main__':
    f1 = Footman()
    f2 = Footman(80)  # wybitnie wytrzymały rycerz :)

    print(f1 == f2)
    print(f1 != f2)  # to też działa, jako zaprzeczenie __eq__

    f3 = Footman()

    print(f1 == f3)
