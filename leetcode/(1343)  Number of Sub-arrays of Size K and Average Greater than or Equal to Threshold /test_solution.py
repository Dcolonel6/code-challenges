import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.fn = Solution().num_of_subarrays

    def test_array_that_should_pass(self):
        self.assertEqual(self.fn([2, 2, 2, 2, 5, 5, 5, 8], 3, 4), 3)

    def test_array_that_should_pas(self):
        self.assertEqual(self.fn([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5), 6, "The array is basic")

    def test_array_elements_less_than_k(self):
        self.assertEqual(self.fn([11, 13], 3, 5), 0, "Array has less elements than k")

    def test_array_elements_will_never_meet_threshold(self):
        self.assertEqual(self.fn([-11, -13, 17, -23, -29, -31, -7, -5, 2, 3], 3, 5), 0, "Array has elements that will never meet the threshold")


if __name__ == '__main__':
    unittest.main()
