import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.max_sum_subary = Solution().maximum_sum_subarray

    def test_case1(self):
        self.assertEqual(self.max_sum_subary([100, 200, 300, 400], 2), 700)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.max_sum_subary([100, 200, 300, 400], 4), 1000)  # add assertion here

    def test_case3(self):
        self.assertEqual(self.max_sum_subary([100, 200, 300, 400], 1), 400)  # add assertion here



if __name__ == '__main__':
    unittest.main()
