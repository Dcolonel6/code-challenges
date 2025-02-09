import unittest
from length_longest_substring import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.longest = Solution().longest_unique_substring

    def test_case1(self):
        self.assertEqual(self.longest("abdefgabef"), 6)

    def test_case2(self):
        self.assertEqual(self.longest("geeksforgeeks"), 7)

    def test_case3(self):
        self.assertEqual(self.longest("aaaaa"), 1)


if __name__ == "__main__":
    unittest.main()
