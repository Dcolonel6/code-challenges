import unittest
from main import valid_braces

class TestValidBraces(unittest.TestCase):

    def test_valid(self):
        self.assertTrue(valid_braces("()"))
        self.assertTrue(valid_braces("{}" ))
        self.assertTrue(valid_braces("{}()[]") )
        self.assertTrue(valid_braces("([{}])"))
        self.assertTrue(valid_braces("[]"))

    def test_invalid(self):
        self.assertFalse(valid_braces("(}"))
        self.assertFalse(valid_braces("[(])"))
        self.assertFalse(valid_braces(")(}{]["))


if __name__ == '__main__':
    unittest.main()