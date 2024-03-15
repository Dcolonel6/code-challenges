class Node():
    def __init__(self, value, index):
        self.val = value
        self.index = index
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"{self.val}"


def make_circular_linked_list(items):
    start_node = None
    last_node = None
    prev_node = None
    for index, item in enumerate(items):
        n = Node(item, index)
        if index == 0:
            start_node = n
        if index == len(items) - 1:
            last_node = n
            n.next = start_node
            start_node.prev = n
        n.prev = prev_node
        try:
            prev_node.next = n
        except AttributeError:
            print(f"try setting {prev_node} next")
        prev_node = n
    start_node.prev = last_node

    return start_node
