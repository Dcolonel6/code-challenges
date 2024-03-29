import unittest
from main import Node, tree_by_levels

class TestNode(unittest.TestCase):

    def setUp(self) -> None:
        self.node = Node(2, 3, 10)

    def test_node_creation(self):
        self.assertEqual(self.node.left, 2) 
        self.assertEqual(self.node.right, 3)  
        self.assertEqual(self.node.value, 10)     
        self.assertIsInstance(self.node, Node)



class TestTreeByLevel(unittest.TestCase):

    def setUp(self) -> None:
        self.empty_tree = tree_by_levels(None)
        self.tree = tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1))

    def test_empty_tree(self):
       self.assertIsInstance(self.empty_tree, list)
       self.assertListEqual(self.empty_tree, [])
    
    def test_tree(self):
       self.assertIsInstance(self.tree, list)
       self.assertListEqual(self.tree, [1, 2, 3, 4, 5, 6])



if __name__ == '__main__':
    unittest.main()