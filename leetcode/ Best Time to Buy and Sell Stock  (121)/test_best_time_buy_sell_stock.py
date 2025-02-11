import unittest
from best_time_buy_sell_stock import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.max_profit = Solution().max_profit

    def test_case1(self):
        self.assertEqual(self.max_profit([7, 1, 5, 3, 6, 4]), 5)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.max_profit([7, 6, 4, 3, 1]), 0)

    def test_case3(self):
        self.assertEqual(self.max_profit([23, 54, 6, 7, 67, 78]), 72)


if __name__ == '__main__':
    unittest.main()
