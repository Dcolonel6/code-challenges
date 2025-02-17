import unittest
from prime_time import prime


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(prime(0), [])

    def test_case2(self):
        self.assertEqual(prime(1), [])

    def test_case3(self):
        self.assertEqual(prime(2), [2])

    def test_case4(self):
        self.assertEqual(prime(5), [2,3,5])

    def test_case5(self):
        self.assertEqual(prime(10), [2,3,5,7])

    def test_case6(self):
        self.assertEqual(prime(15), [2,3,5,7,11,13])

    def test_case7(self):
        self.assertEqual(prime(25), [2,3,5,7,11,13,17,19,23])

    def test_case8(self):
        self.assertEqual(prime(35), [2,3,5,7,11,13,17,19,23,29,31])

    def test_case9(self):
        self.assertEqual(prime(50), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])


if __name__ == '__main__':
    unittest.main()
