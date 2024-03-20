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



