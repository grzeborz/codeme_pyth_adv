import unittest

from zajecia01.zadanie_domowe.zaddom01_grzegorz import MyTime


class TestEtap3(unittest.TestCase):
    def test_addition(self):
        result = MyTime(1, 1) + MyTime(2, 2)
        self.assertTrue(result == MyTime(3, 3))

    def test_overflow(self):
        result = MyTime(0, 59) + MyTime(0, 59)
        self.assertTrue(result == MyTime(1, 58))


if __name__ == '__main__':
    unittest.main()
