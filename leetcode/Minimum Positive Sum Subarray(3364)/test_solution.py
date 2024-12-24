import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.min_sum_subary = Solution().minimum_sum_subarray

    def test_case1(self):
        self.assertEqual(self.min_sum_subary([3, -2, 1, 4], 2, 3), 1)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.min_sum_subary([-2, 2, -3, 1], 2, 3), -1)  # add assertion here

    def test_case3(self):
        self.assertEqual(self.min_sum_subary([1, 2, 3, 4], 2, 4), 3)  # add assertion here

    def test_case4(self):
        self.assertEqual(self.min_sum_subary([-12, 8], 1, 1), 8)  # add assertion here

    def test_case5(self):
        self.assertEqual(self.min_sum_subary([-3, 17], 1, 2), 14)  # add assertion here


if __name__ == '__main__':
    unittest.main()
