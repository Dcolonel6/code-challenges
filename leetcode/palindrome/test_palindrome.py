import unittest
from palindrome import  Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.is_palindrome = Solution().isPalindrome

    def test_case1(self):
        self.assertEqual(self.is_palindrome(123), False)  # add assertion here

    def test_case2(self):
        self.assertTrue(self.is_palindrome(11))

    def test_case3(self):
        self.assertTrue(self.is_palindrome(1001))


if __name__ == '__main__':
    unittest.main()
