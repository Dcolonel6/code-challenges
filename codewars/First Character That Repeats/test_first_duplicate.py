import unittest
from first_duplicate import first_dup


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(first_dup('tweet'), 't')

    def test_case2(self):
        self.assertEqual(first_dup('Ode to Joy'), ' ')

    def test_case3(self):
        self.assertEqual(first_dup('ode to joy'), 'o')

    def test_case4(self):
        self.assertEqual(first_dup('bar'), None)

    def test_case5(self):
        self.assertEqual(first_dup('123123'), '1')

    def test_case6(self):
        self.assertEqual(first_dup('!@#$!@#$'), '!')

    def test_case7(self):
        self.assertEqual(first_dup('1a2b3a3c'), 'a')


if __name__ == '__main__':
    unittest.main()
