class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def postorder(self, root):
        out = []

        def dfs(root):
            if root is None:
                return
            for child in root.children:
                dfs(child)
            out.append(root.val)
        dfs(root)
        return out