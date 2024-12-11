import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.roman_to_int = Solution().romanToInt

    def test_case1(self):
        self.assertEqual(self.roman_to_int("III"), 3)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.roman_to_int("IV"), 4)

    def test_case3(self):
        self.assertEqual(self.roman_to_int("LVIII"), 58)

    def test_case4(self):
        self.assertEqual(self.roman_to_int("MCMXCIV"), 1994)


if __name__ == '__main__':
    unittest.main()
