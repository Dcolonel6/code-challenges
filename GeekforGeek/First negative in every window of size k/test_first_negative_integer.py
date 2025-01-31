import unittest
from first_negative_integer import Solution


class TestCase(unittest.TestCase):

	def setUp(self):
		self.first_negative = Solution().first_negative_integer

	def test_case1(self):
		self.assertListEqual(self.first_negative([-8, 2, 3, -6, 10], 2), [-8, 0, -6, -6])

	def test_case2(self):
		self.assertListEqual(self.first_negative([12, -1, -7, 8, -15, 30, 16, 28], 3),
							 [-1, -1, -7, -15, -15, 0])

	def test_case3(self):
		self.assertListEqual(self.first_negative([12, 1, 3, 5], 3), [0,0])

if __name__ == "__main__":
	unittest.main()