import unittest
from binary_search_sqrt import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.binary_sqrt = Solution().is_perfect_square

    def test_case1(self):
        self.assertTrue(self.binary_sqrt(4))  # add assertion here

    def test_case2(self):
        self.assertTrue(self.binary_sqrt(16))  # add assertion here

    def test_case3(self):
        self.assertFalse(self.binary_sqrt(14))  # add assertion here

    def test_case4(self):
        self.assertTrue(self.binary_sqrt(9))  # add assertion here


if __name__ == '__main__':
    unittest.main()
