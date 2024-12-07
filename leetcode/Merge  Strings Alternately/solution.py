import unittest
from merge_strings_alternately import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.merge = Solution().mergeAlternately

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
