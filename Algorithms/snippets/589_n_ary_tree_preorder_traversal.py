class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def preorder(self, root):
        out = []

        def dfs(root):
            if root is None:
                return
            out.append(root.val)
            for child in root.children:
                dfs(child)
        dfs(root)
        return out