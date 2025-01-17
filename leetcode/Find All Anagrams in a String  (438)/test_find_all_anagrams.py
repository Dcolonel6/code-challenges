import unittest
from find_all_anagrams_in_string import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.find_anagrams = Solution().findAnagrams

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
