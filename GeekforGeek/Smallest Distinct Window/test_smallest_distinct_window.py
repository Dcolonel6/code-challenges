import unittest
from smallest_distinct_window import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.smallest_distinct = Solution().smallest_distinct_window

    def test_case1(self):
        self.assertEqual(self.smallest_distinct("GEEKSGEEKSFOR"), 8)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.smallest_distinct("AABBBCBBAC"), 3)

    def test_case3(self):
        self.assertEqual(self.smallest_distinct("aaab"), 2)

    def test_case4(self):
        self.assertEqual(self.smallest_distinct("ACbCACAcACaB"), 10)


if __name__ == '__main__':
    unittest.main()
