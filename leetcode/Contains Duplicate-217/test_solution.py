import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.contains_duplicate = Solution().contains_duplicate

    def test_case1(self):
        self.assertTrue(self.contains_duplicate([1, 2, 3, 1]))

    def test_case2(self):
        self.assertFalse(self.contains_duplicate([1, 2, 3, 4]))

    def test_case3(self):
        self.assertTrue(self.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == "__main__":
    unittest.main()
