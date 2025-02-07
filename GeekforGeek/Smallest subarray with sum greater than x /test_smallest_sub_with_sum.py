import unittest
from smallest_sub_with_sum import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.smallest_sub = Solution().smallest_sub_with_sum

    def test_case1(self):
        self.assertEqual(self.smallest_sub(51, [1, 4, 45, 6, 0, 19]), 3)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.smallest_sub(100, [1, 10, 5, 2, 7]), 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
