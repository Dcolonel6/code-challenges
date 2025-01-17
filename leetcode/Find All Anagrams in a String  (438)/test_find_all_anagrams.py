import unittest
from find_all_anagrams_in_string import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.find_anagrams = Solution().find_anagrams

    def test_case1(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
