import unittest
from two_sum import  Solution

#[0,3,-3,4,-1] -1 [0,4]
class TestSolutionCase(unittest.TestCase):
    def setUp(self):
        self.two_sum = Solution().twoSum
    def test_case1(self):
        self.assertEqual(self.two_sum([2,7,11,15], 9), [0,1])  # add assertion here
    def test_case2(self):
        self.assertEqual(self.two_sum([3,2,4],  6), [1,2])
    def test_case3(self):
        self.assertEqual(self.two_sum([3,3], 6), [0,1])
    def test_edge_case1(self):
        self.assertEqual(self.two_sum([-1,-2,-3,-4,-5], -8), [2,4])
    def test_edge_case2(self):
        self.assertEqual(self.two_sum([0,3,-3,4,-1], -1), [0,4])


if __name__ == '__main__':
    unittest.main()

