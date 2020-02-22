class Footman:
    _max_hp = 60

    def __init__(self, hp=_max_hp):
        self._hp = hp
        self._damage = 6

    def __str__(self):
        # czytelny dla użytkownika opis obiektu; jeśli jest, __str__ zastępuje __repr__
        return f'Footman: hp:{self._hp}/{self._max_hp}, damage: {self._damage}'

    def __repr__(self):
        # powinien przypominać tworzenie opisywanego obiektu
        return f'Footman(hp={self._hp})'

    def attack(self):
        print(f'Footman zadał {self._damage} pkt. obrażeń')


if __name__ == '__main__':
    f1 = Footman()
    print(f1)  # __str__ jest używane zamiast __repr__

    f2 = Footman(80)  # wybitnie wytrzymały rycerz :)
    print(f2)

    footmen = [f1, f2]
    print(footmen)  # UWAGA! Tutaj jest używany __repr__ !
