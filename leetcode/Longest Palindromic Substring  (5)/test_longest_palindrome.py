import unittest
from longest_palindrome import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.longest = Solution().length_palindrome

    def test_case1(self):
        self.assertIn(self.longest("babad"), ["bab", "aba"])  # add assertion here

    def test_case2(self):
        self.assertEqual(self.longest("cbbd"), "bb")

    def test_case3(self):
        self.assertEqual(self.longest("noon"), "noon")

    def test_case4(self):
        self.assertIn(self.longest("ac"), ["a", "c"])

    def test_case5(self):
        self.assertEqual(self.longest("a"), "a")

    def test_case6(self):
        self.assertEqual(self.longest("aa"), "aa")

    def test_case7(self):
        self.assertEqual(self.longest("racecar"), "racecar")

    def test_case8(self):
        self.assertEqual(self.longest("aacabdkacaa"), "aca")


if __name__ == '__main__':
    unittest.main()
