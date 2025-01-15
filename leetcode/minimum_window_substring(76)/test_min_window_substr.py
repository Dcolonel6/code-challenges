import unittest
from min_window_substr import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.min_window = Solution().minimum_window

    def test_case1(self):
        self.assertEqual(self.min_window("ADOBECODEBANC", "ABC"), "BANC")  # add assertion here

    def test_with_no_substring(self):
        self.assertEqual(self.min_window("a", "aa"), "")  # add assertion here

    def test_case3(self):
        self.assertEqual(self.min_window("a", "a"), "a")  # add assertion here

    def test_case4(self):
        self.assertEqual(self.min_window("cabwefgewcwaefgcf", "cae"), "cwae")  # add assertion here

    def test_case5(self):
        self.assertEqual(self.min_window("a", "b"), "")  # add assertion here


if __name__ == '__main__':
    unittest.main()
