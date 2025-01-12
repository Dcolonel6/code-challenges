import unittest
from min_window_substr import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.min_window = Solution().minimum_window

    def test_case1(self):
        self.assertEqual(self.min_window("ADOBECODEBANC", "ABC"), 4)  # add assertion here

    def test_with_no_substring(self):
        self.assertEqual(self.min_window("a", "aa"), "")  # add assertion here


if __name__ == '__main__':
    unittest.main()
