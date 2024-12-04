import unittest
from solution import Solution

class TestCase(unittest.TestCase):
    def setUp(self):
        self.is_valid = Solution().is_valid

    def testcase1(self):
        self.assertTrue(self.is_valid("()[]{}"))
    def testcase2(self):
        self.assertTrue(self.is_valid("([])"))
    def testcase3(self):
        self.assertFalse(self.is_valid("([)]"))

if __name__ == "__main__":
    unittest.main()