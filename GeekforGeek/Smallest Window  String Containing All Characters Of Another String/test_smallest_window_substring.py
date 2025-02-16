import unittest
from smallest_window_substring import Solution


class SolutionTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.smallest_window_substring = Solution().min_window

    def test_both_empty_string(self):
        self.assertEqual(self.smallest_window_substring("", ""), "")

    def test_s1_empty_string(self):
        self.assertEqual(self.smallest_window_substring("", "c"),"" )

    def test_s2_empty_string(self):
        self.assertEqual(self.smallest_window_substring("c", ""), "c")

    def test_single_character_both_same(self):
        self.assertEqual(self.smallest_window_substring("c", "c"), "c")

    def test_single_character_both_different(self):
        self.assertEqual(self.smallest_window_substring("a", "d"), "")

    def test_single_character_s1(self):
        self.assertEqual(self.smallest_window_substring("c", "asfc"),"" )

    def test_single_character_s2(self):
        self.assertEqual(self.smallest_window_substring("asfc", "c"), "c")

    def test_case1(self):
        self.assertEqual(self.smallest_window_substring("timetopractice", "toc"), "toprac")

    def test_case2(self):
        self.assertEqual(self.smallest_window_substring("zoomlazapzo", "oza"), "apzo")

    def test_case3(self):
        self.assertEqual(self.smallest_window_substring("zoom", "zooe"), "")


if __name__ == "__main__":
    unittest.main()