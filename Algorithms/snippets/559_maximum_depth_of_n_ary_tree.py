class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def max_depth(self, root):
        if root is None:
            return 0

        depth = 0
        for child in self.children:
            depth = max(depth, self.max_depth(child))
        return depth + 1