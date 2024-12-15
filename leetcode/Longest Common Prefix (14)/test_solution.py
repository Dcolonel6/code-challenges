import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.longest_common_prefix = Solution().longest_common_prefix

    def test_case1(self):
        self.assertEqual(self.longest_common_prefix(["flower", "flow", "flight"]), "fl")  # add assertion here

    def test_case2(self):
        self.assertEqual(self.longest_common_prefix(["dog", "racecar", "car"]), "")  # add assertion here

    def test_case3(self):
        self.assertEqual(self.longest_common_prefix(["cir", "car"]), "c")  # add assertion here

    def test_case4(self):
        self.assertEqual(self.longest_common_prefix(["aa",  "ab"]), "a")  # add assertion here

    def test_case5(self):
        self.assertEqual(self.longest_common_prefix(["aa", "aa"]), "aa")  # add assertion here

    def test_case6(self):
        self.assertEqual(self.longest_common_prefix([""]), "")  # add assertion here

    def test_case7(self):
        self.assertEqual(self.longest_common_prefix(["a"]), "a")  # add assertion here


if __name__ == '__main__':
    unittest.main()
