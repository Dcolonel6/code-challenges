import unittest
from maximum_subarray import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.max_subarry = Solution().maximum_subarray

    def test_case1(self):
        self.assertEqual(self.max_subarry([-2,1,-3,4,-1,2,1,-5,4]), 6)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.max_subarry([1]), 1)  # add assertion here

    def test_case3(self):
        self.assertEqual(self.max_subarry([5,4,-1,7,8]), 23)  # add assertion here


if __name__ == '__main__':
    unittest.main()
