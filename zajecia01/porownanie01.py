class Footman:
    _max_hp = 60

    def __init__(self, hp=_max_hp):
        self._hp = hp
        self._damage = 6

    def __str__(self):
        return f'Footman: hp:{self._hp}/{self._max_hp}, damage: {self._damage}'

    def attack(self):
        print(f'Footman zadał {self._damage} pkt. obrażeń')


if __name__ == '__main__':
    f1 = Footman()
    f2 = Footman(80)  # wybitnie wytrzymały rycerz :)

    print(f1 < f2)  # to nie zadziała
