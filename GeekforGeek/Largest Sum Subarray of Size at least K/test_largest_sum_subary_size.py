import unittest
from largest_sum_subary_size_k import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.kadane_with_atleast_k_window = Solution().max_sum_with_k

    def test_case1(self):
        self.assertEqual(self.kadane_with_atleast_k_window([1, -2, 2, -3], 4, 2), 1)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.kadane_with_atleast_k_window([-4,  -2,  1,  -3], 4, 2), -1)

    def test_case3(self):
        self.assertEqual(self.kadane_with_atleast_k_window([1, 1, 1, 1, 1, 1], 6, 2), 6)


if __name__ == '__main__':
    unittest.main()
