import unittest
from count_palindromic_substring import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.count_palindromes = Solution().count_substring

    def test_case1(self):
        self.assertEqual(self.count_palindromes("abc"), 3)

    def test_case2(self):
        self.assertEqual(self.count_palindromes("aaa"), 6)

    def test_case3(self):
        self.assertEqual(self.count_palindromes("aa"), 3)

    def test_case4(self):
        self.assertEqual(self.count_palindromes("aaaaa"), 15)

    def test_case5(self):
        self.assertEqual(self.count_palindromes("a"), 1)

    def test_case6(self):
        self.assertEqual(self.count_palindromes(""), 0)

    def test_case7(self):
        self.assertEqual(self.count_palindromes(" "), 1)


if __name__ == '__main__':
    unittest.main()
