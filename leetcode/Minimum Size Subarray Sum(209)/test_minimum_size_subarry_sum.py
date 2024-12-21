import unittest
from minimum_size_subarry_sum import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.min_subary_length = Solution().min_sub_array_len

    def test_case1(self):
        self.assertEqual(self.min_subary_length(7, [2, 3, 1, 2, 4, 3]), 2)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.min_subary_length(4, [1, 4, 4]), 1)  # add assertion here

    def test_case3(self):
        self.assertEqual(self.min_subary_length(11, [1, 1, 1, 1, 1, 1, 1, 1]), 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
