import unittest

from numpy.ma.testutils import assert_equal

from search import Solution

class TestCase(unittest.TestCase):
    def setUp(self):
        self.search = Solution().search

    def testcase1(self):
        self.assertEqual(self.search([4,5,6,7,0,1,2],0),4)
    def testcase2(self):
        self.assertEqual(self.search([4,5,6,7,0,1,2],3),-1)
    def testcase3(self):
        self.assertEqual(self.search([-1],0),-1)

if __name__ == "__main__":
    unittest.main()