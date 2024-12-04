import unittest
from remove_invalid_parenthesis import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.remove_invalid = Solution().make_remove_invalid

    def testcase1(self):
        self.assertIn(self.remove_invalid("(a(b(c)d)"), ["(a(bc)d)", "a(b(c)d)"])

    def testcase2(self):
        self.assertEqual(self.remove_invalid("lee(t(c)o)de)"), "lee(t(c)o)de")

    def testcase3(self):
        self.assertEqual(self.remove_invalid("))(("), "")




if __name__ == "__main__":
    unittest.main()