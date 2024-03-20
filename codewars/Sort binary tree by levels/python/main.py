class Node:
    def __init__(self, L=None, R = None, n =None):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    if node is None:
        return []
    queue = [node]
    values = []
    
    while len(queue):
        try:
            current = queue.pop(0)
            values.append(current.value)
            if current.left is not None:
                queue = [*queue, current.left]
            if current.right is not None:
                queue = [*queue, current.right]
        except IndexError:
                pass
    
    return values