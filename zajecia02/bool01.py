class Footman:
    _max_hp = 60

    def __init__(self, hp=_max_hp):
        self._hp = hp
        self._damage = 6

    def __repr__(self):
        return f'Footman(hp={self._hp})'

    def __bool__(self):
        if self._hp > 0:
            return True
        return False

    def attack(self):
        if not self:
            raise Exception('Nie można wykonać ataku!')

        print(f'Footman zadał {self._damage} pkt. obrażeń')


if __name__ == '__main__':
    f = Footman()

    print(f)
    print(bool(f))

    f._hp -= 67  # Potężne obrażenia

    print(f)
    print(bool(f))
    # f.attack()  # wykonanie tej linii rzuci wyjątek

    if f:
        print(f'Rycerz jest w pełni zdrowy!')
    else:
        print(f'Rycerz nie jest zdrowy :/')
