import unittest
from valid_anagram import Anagram


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.anagram = Anagram().is_anagram

    def test_case1(self):
        self.assertTrue(self.anagram("anagram", "nagaram"))  # add assertion here

    def test_case2(self):
        self.assertFalse(self.anagram("rat", "car"))  # add assertion here

    def test_case3(self):
        self.assertFalse(self.anagram("ac", "bb"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
