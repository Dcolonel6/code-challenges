import unittest
from first_negative_integer import Solution


class TestCase(unittest.TestCase):

	def setUp(self):
		self.first_negative = Solution().first_negative_integer

	def test_case1(self):
		self.assertListEqual(self.first_negative(), [])
