import unittest
from total_fruit import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.total_fruit = Solution().total_fruit

    def test_case1(self):
        self.assertEqual(self.total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]), 5)

    def test_case2(self):
        self.assertEqual(self.total_fruit([1, 2, 3, 2, 2]), 4)

    def test_case3(self):
        self.assertEqual(self.total_fruit([0, 1, 2, 2]), 3)

    def test_case4(self):
        self.assertEqual(self.total_fruit([1, 2, 1]), 3)

    def test_case5(self):
        self.assertEqual(self.total_fruit([1, 0, 1, 4, 1, 4, 1, 2, 3]), 5)


if __name__ == '__main__':
    unittest.main()
