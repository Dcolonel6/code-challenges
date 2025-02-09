import unittest
from symmetric_strings import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.symetric = Solution().solution
    def test_case1(self):
        self.assertEqual(self.symetric("<<<>>>"), 6)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.symetric("<><??>>"), 4)  # add assertion here

    def test_case3(self):
        self.assertEqual(self.symetric("??????"), 6)  # add assertion here

    def test_case4(self):
        self.assertEqual(self.symetric("<>"), 2)  # add assertion here

    def test_case5(self):
        self.assertEqual(self.symetric("<<?"), 2)  # add assertion here

    def test_case6(self):
        self.assertEqual(self.symetric("??><??"), 4)  # add assertion here

    def test_case7(self):
        self.assertEqual(self.symetric("????????"), 8)  # add assertion here

    def test_case8(self):
        self.assertEqual(self.symetric("<<>>??"), 4)  # add assertion here

    def test_case9(self):
        self.assertEqual(self.symetric("?<>?"), 4)  # add assertion here

    def test_case10(self):
        self.assertEqual(self.symetric(""), 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
