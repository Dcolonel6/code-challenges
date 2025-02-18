import unittest
from count_duplicate import duplicate_count


class MyTestCase(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(duplicate_count(""), 0)  # add assertion here

    def test_case2(self):
        self.assertEqual(duplicate_count("abcde"), 0)

    def test_case3(self):
        self.assertEqual(duplicate_count("abcdeaa"), 1)

    def test_case4(self):
        self.assertEqual(duplicate_count("abcdeaB"), 2)

    def test_case5(self):
        self.assertEqual(duplicate_count("Indivisibilities"), 2)


if __name__ == '__main__':
    unittest.main()
