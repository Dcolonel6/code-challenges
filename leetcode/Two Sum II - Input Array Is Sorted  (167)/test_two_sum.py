import unittest
from two_sum import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.two_sum = Solution().two_sum_binary_search

    def test_case1(self):
        self.assertEqual(self.two_sum([2, 7, 11, 15], 9), [1, 2])

    def test_case2(self):
        self.assertEqual(self.two_sum([2, 3, 4], 6), [1, 3])

    def test_case3(self):
        self.assertEqual(self.two_sum([-1, 0], -1), [1, 2])


if __name__ == '__main__':
    unittest.main()
