import unittest
from slow_approach import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.find_min = Solution().findMin

    def test_case1(self):
        self.assertEqual(self.find_min([2, 2, 2, 0, 1]), 0)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.find_min([1, 3, 3]), 1)  # add assertion here

    def test_case3(self):
        self.assertEqual(self.find_min([2, 2, 2, 0, 1]), 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
