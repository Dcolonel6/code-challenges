import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.longest_substr = Solution().length_of_longest_substring_diff_approach

    def test_case1(self):
        self.assertEqual(self.longest_substr("abcabcbb"), 3)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.longest_substr("bbbbb"), 1)  # add assertion here

    def test_case3(self):
        self.assertEqual(self.longest_substr("pwwkew"), 3)  # add assertion here

    def test_case4(self):
        self.assertEqual(self.longest_substr("aab"), 2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
