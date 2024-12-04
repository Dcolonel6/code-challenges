import unittest
from remove_invalid_parenthesis import Solution

class TestSolution(unittest):
    def setUp(self):
        self.remove_invalid = Solution().make_remove_invalid
    def testcase1(self):
        self.assertEqual(self.remove_invalid("(a(b(c)d)"), "ab(c)d")
    def testcase2(self):
        self.assertEqual(self.remove_invalid("lee(t(c)o)de)"), "lee(t(c)o)de")
    def testcase3(self):
        self.assertEqual(self.remove_invalid("))(("), "")
    def testcase4(self):
        self.assertEqual(self.remove_invalid("(a(b(c)d)"), "a(b(c)d)")