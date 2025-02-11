import unittest
from search_with_anagrams import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.search = Solution().search

    def test_case1(self):
        self.assertEqual(self.search("geeks", "eke"), True)  # add assertion here

    def test_case2(self):
        self.assertEqual(self.search("programming", "rain"), False)

    # def test_case3(self):
    #     self.assertEqual(True, False)
    #
    # def test_case4(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
