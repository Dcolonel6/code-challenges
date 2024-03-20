import unittest
from main import Node, tree_by_levels

class TestNode(unittest.TestCase):

    def setUp(self) -> None:
        self.node = Node(2, 3, 10)

