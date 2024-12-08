import unittest
from square_root_integer import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.sqrt_int = Solution().mySqrt

    def test_case1(self):
        self.assertEqual(self.sqrt_int(9), 3)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.sqrt_int(0), 0)

    def test_case3(self):
        self.assertEqual(self.sqrt_int(1), 1)

    def test_case4(self):
        self.assertEqual(self.sqrt_int(8), 2)

    def test_case5(self):
        self.assertEqual(self.sqrt_int(4), 2)

    def test_case6(self):
        self.assertEqual(self.sqrt_int(10_000_000_000), 100_000)


if __name__ == '__main__':
    unittest.main()
