import unittest
from product_array_except_self import Solution


class TestCase(unittest.TestCase):

    def setUp(self):
        self.product = Solution().product_except_self

    def test_case1(self):
        self.assertEqual(self.product([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_case2(self):
        self.assertEqual(self.product([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])


if __name__ == "__main__":
    unittest.main()
