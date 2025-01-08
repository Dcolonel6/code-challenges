import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.search_insert = Solution().searchInsert

    def testcase1(self):
        self.assertEqual(self.search_insert([1, 3, 5, 6], 5), 2)

    def testcase2(self):
        self.assertEqual(self.search_insert([1, 3, 5, 6], 2), 1)

    def testcase3(self):
        self.assertEqual(self.search_insert([1, 3, 5, 6], 7), 4)

    def testcase4(self):
        self.assertEqual(self.search_insert([1, 3, 5, 6], 0), 0)

    def testcase5(self):
        self.assertEqual(self.search_insert([1], 1), 0)

    def testcase6(self):
        self.assertEqual(self.search_insert([1], 0), 0)

    def testcase7(self):
        self.assertEqual(self.search_insert([1], 2), 1)


if __name__ == "__main__":
    unittest.main()
