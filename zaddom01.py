# Imię i Nazwisko

class MyTime:
    # _minutes = 0
    # _seconds = 0
    #def __init__(self, min=_minutes, sec=_seconds):
    def __init__(self, min, sec):
        self._minutes = min


        self._seconds = sec
        if self._minutes < 0:
            raise ValueError('Expected value > 0')
        elif self._seconds < 0:
            raise ValueError('Expected value > 0')
        elif self._seconds >= 60:
            raise ValueError('Expected value < or = 59')

    def __eq__(self, other):
        if self._minutes == other._minutes and self._seconds == other._seconds:
            return True
        return False
        # pass

    def __add__(self, other):
        added_minutes = self._minutes + other._minutes
        added_seconds = self._seconds + other._seconds
        if added_seconds >= 60:
            added_minutes = added_minutes + 1
            added_seconds = 0 + (added_seconds - 60)
        return MyTime(added_minutes, added_seconds)

    def __repr__(self):
        return f'MyTime(min={self._minutes}, sec={self._seconds})'

    def __lt__(self, other):
        if self._minutes < other._minutes:
            return True
        elif self._seconds < other._seconds:
            return True
        else:
            return False

    def __sub__(self, other):
        substract_minutes = self._minutes - other._minutes
        substract_seconds = self._seconds - other._seconds

        if substract_minutes < 0:
            raise ValueError('Expected value > 0')
        elif substract_seconds < 0:
            substract_minutes = substract_minutes - 1
            substract_seconds = 60 - substract_seconds
            if substract_minutes < 0:
                raise ValueError('Expected value > 0')
            elif substract_seconds >= 60:
                raise ValueError('Expected value < or = 59')
        return MyTime(substract_minutes, substract_seconds)

if __name__ == '__main__':
    t1 = MyTime(10,40)
    t2 = MyTime(10,10)
    #t3 = MyTime(5,61)
    t4 = MyTime(0,21)
    #t5 = MyTime(0, 10)
    # tutaj można pisać dowolny kod, nie wpływa to na testy
    # print(t3 == t2)
    # print(t3 != t2)
    # print(t3 + t2)
    # print(t3 > t2)
    print(t2 - t4)
    # print(t5<t4)
    # print(t5 - t2)
    # print(t3)
   # pass

