import unittest
from max_product import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.max_product = Solution().maximum_product

    def test_case1(self):
        self.assertEqual(self.max_product([2,-5,-2,-4,3]), 24)

    def test_case2(self):
        self.assertEqual(self.max_product([-2,0,-1]), 0)

    def test_case3(self):
        self.assertEqual(self.max_product([2,3,-2,4]), 6)


if __name__ == '__main__':
    unittest.main()
