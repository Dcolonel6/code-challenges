import unittest
from merged_sorted_array import MergeSorted


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.merge = MergeSorted().merge

    def test_with_normal_array(self):
        self.assertEqual(self.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6])  # add assertion here

    def test_second_with_no_length(self):
        self.assertEqual(self.merge([1], 1, [], 0), [1], "Second array was of length 0 with no elemnts")

    def test_first_with_no_length(self):
        self.assertEqual(self.merge([0], 0, [1], 1), [1], "First array was of length 0 with 1 elemnt")


if __name__ == '__main__':
    unittest.main()
