import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.contains_duplicate = Solution().contains_nearby_duplicate

    def test_case1(self):
        self.assertTrue(self.contains_duplicate([1, 2, 3, 1], 3))  # add assertion here

    def test_case2(self):
        self.assertTrue(self.contains_duplicate([1, 0, 1, 1 ], 1))  # add assertion here

    def test_case3(self):
        self.assertFalse(self.contains_duplicate([1, 2, 3, 1, 2, 3], 2))  # add assertion here

    def test_case4(self):
        self.assertTrue(self.contains_duplicate([4, 1, 2, 3, 1, 5], 3))  # add assertion here


if __name__ == '__main__':
    unittest.main()
