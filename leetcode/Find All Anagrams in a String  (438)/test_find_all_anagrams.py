import unittest
from find_all_anagrams_in_string import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.find_anagrams = Solution().find_anagrams

    def test_case1(self):
        self.assertEqual(self.find_anagrams("cbaebabacd", "abc"), [0, 6])  # add assertion here

    def test_case2(self):
        self.assertEqual(self.find_anagrams("abab","ab"), [0, 1, 2])  # add assertion here


if __name__ == '__main__':
    unittest.main()
