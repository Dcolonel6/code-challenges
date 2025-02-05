import unittest
from monotonic_queue import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.max_sliding_windw = Solution().maximum_sliding_window

    def test_case1(self):
        self.assertListEqual(self.max_sliding_windw([1, 3, -1, -3, 5, 3, 6, 7], 3), [3,3,5,5,6,7])  # add assertion here

    def test_case2(self):
        self.assertListEqual(self.max_sliding_windw([7, 2, 4], 2),[7,4])  # add assertion here

    def test_case3(self):
        self.assertListEqual(self.max_sliding_windw([1], 1),[1])  # add assertion here

    def test_case4(self):
        self.assertListEqual(self.max_sliding_windw([5,3,4], 1),[5,3,4])  # add assertion here

    def test_case5(self):
        self.assertListEqual(self.max_sliding_windw([9,11], 2),[11])  # add assertion here

    def test_case6(self):
        self.assertListEqual(self.max_sliding_windw([1, -1], 1),[1,-1])  # add assertion here


if __name__ == '__main__':
    unittest.main()
