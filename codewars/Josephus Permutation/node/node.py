class Node():
    def __init__(self, value, index):
        self.val = value
        self.index = index
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"{self.val}"


