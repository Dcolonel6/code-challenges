import unittest
from valid_palindrome import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.is_palindrome = Solution().isPalindrome

    def test_string_with_non_alphabets(self):
        self.assertTrue(self.is_palindrome("A man, a plan, a canal: Panama"))  # add assertion here

    def test_empty_string_case(self):
        self.assertTrue(self.is_palindrome(""))  # add assertion here

    def test_string_with_one_letter(self):
        self.assertTrue(self.is_palindrome("a"))  # add assertion here

    def test_string_with_two_letter(self):
        self.assertTrue(self.is_palindrome("aa"))  # add assertion here

    def test_string_that_should_fail(self):
        self.assertFalse(self.is_palindrome("race a car"))  # add assertion here

    def test_string_length_two_with_a_non_alpha(self):
        self.assertFalse(self.is_palindrome("0P"))  # add assertion here

    def test_string_even_length(self):
        self.assertTrue(self.is_palindrome("abba"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
