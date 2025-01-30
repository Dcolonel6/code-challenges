import unittest
from count_distinct import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.count_distinct = Solution().count_distinct
    def test_case1(self):
        self.assertListEqual(self.count_distinct([1, 2, 1, 3, 4, 2, 3], 4), [3, 4, 4, 3])  # add assertion here

    def test_case2(self):
        self.assertListEqual(self.count_distinct([4,1,1], 2), [2, 1])  # add assertion here

    def test_case3(self):
        self.assertListEqual(self.count_distinct( [1, 1, 1, 1, 1], 3), [1, 1, 1])  # add assertion here


if __name__ == '__main__':
    unittest.main()
