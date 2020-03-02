import unittest

from zaddom01 import MyTime


class TestEtap3(unittest.TestCase):
    def test_addition(self):
        wynik = MyTime(1, 1) + MyTime(2, 2)
        self.assertTrue(wynik == MyTime(3, 3))

    def test_overflow(self):
        wynik = MyTime(0, 59) + MyTime(0, 59)
        self.assertTrue(wynik == MyTime(1, 58))


if __name__ == '__main__':
    unittest.main()
