class Footman:
    _max_hp = 60

    def __init__(self, hp=_max_hp):
        self._hp = hp
        self._damage = 6

    def __str__(self):
        return f'Footman: hp:{self._hp}/{self._max_hp}, damage: {self._damage}'

    def __repr__(self):
        return f'Footman(hp={self._hp})'

    def attack(self):
        print(f'Footman zadał {self._damage} pkt. obrażeń')


if __name__ == '__main__':
    f = Footman()
    print(f)  # __str__ jest używane zamiast __repr__
    f.attack()

    # Jeśli bardzo chcemy, to wciąż możemy dostać się do __repr__
    print(f.__repr__())
