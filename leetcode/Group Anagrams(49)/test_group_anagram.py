import unittest
from group_anagram import GroupAnagram


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.group_anagrams = GroupAnagram().group_anagrams

    def test_case1(self):
        self.assertCountEqual(self.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]])  # add assertion here

    def test_case2(self):
        self.assertCountEqual(self.group_anagrams([""]), [[""]])  # add assertion here

    def test_case3(self):
        self.assertCountEqual(self.group_anagrams(["a"]), [["a"]])  # add assertion here


if __name__ == '__main__':
    unittest.main()
