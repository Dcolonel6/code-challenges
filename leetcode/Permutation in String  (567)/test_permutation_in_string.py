import unittest
from permutation_in_string import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.check_inclusion = Solution().check_inclusion

    def test_case1(self):
        self.assertTrue(self.check_inclusion("ab", "eidbaooo"))  # add assertion here

    def test_case2(self):
        self.assertFalse(self.check_inclusion("ab", "eidboaoo"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
