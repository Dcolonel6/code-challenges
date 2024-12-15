import unittest
from pivot_index import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.pivot_index = Solution().pivot_index

    def test_case1(self):
        self.assertEqual(self.pivot_index([1, 7, 3, 6, 5, 6]), 3)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.pivot_index([2, 1, -1]), 0)  # add assertion here

    def test_case3(self):
        self.assertEqual(self.pivot_index([1, 2, 3]), -1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
