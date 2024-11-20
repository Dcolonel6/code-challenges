import unittest
from find_pivot import  Solution

#[0,3,-3,4,-1] -1 [0,4]
class TestSolutionCase(unittest.TestCase):
    def setUp(self):
        self.find_pivot = Solution().find_pivot
    def test_case1(self):
        self.assertEqual(self.find_pivot([7,8,9,1,2,3,4,5,6]), [3,3])  # add assertion here
    def test_case2(self):
        self.assertEqual(self.find_pivot([4,5,6,7,0,1,2]), [4,4])
    # def test_case3(self):
    #     self.assertEqual(self.find_pivot([3,3]), [0,1])
    # # def test_edge_case1(self):
    #     self.assertEqual(self.find_pivot([-1,-2,-3,-4,-5], -8), [2,4])
    # def test_edge_case2(self):
    #     self.assertEqual(self.find_pivot([0,3,-3,4,-1], -1), [0,4])


if __name__ == '__main__':
    unittest.main()

