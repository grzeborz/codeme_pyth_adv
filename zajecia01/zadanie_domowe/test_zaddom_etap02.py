import unittest

from zajecia01.zadanie_domowe.zaddom01_grzegorz import MyTime


class TestEtap2(unittest.TestCase):
    def test_equality(self):
        self.assertTrue(MyTime(3, 3) > MyTime(2, 2))
        self.assertTrue(MyTime(2, 3) > MyTime(2, 2))

        self.assertTrue(MyTime(1, 1) == MyTime(1, 1))
        self.assertTrue(MyTime(0, 1) != MyTime(0, 2))

        self.assertFalse(MyTime(0, 1) < MyTime(0, 1))


if __name__ == '__main__':
    unittest.main()
