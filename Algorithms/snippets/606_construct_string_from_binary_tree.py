class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def tree_to_str(self, root):
        def dfs(root):
            if not root:
                return ''
            if root.right:
                return str(root.val) + '(' + self.dfs(root.left) + ')(' + self.dfs(root.right) + ')'
            if root.left:
                return str(root.val) + '(' + self.dfs(root.left) + ')'
            return str(root.val)
        return dfs(root)

