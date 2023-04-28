class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def bst_to_gst(self, root):
        self.s = 0
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            root.val = self.s = self.s + root.val
            dfs(root.left)
        dfs(root)
        return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.left.right.right = TreeNode(3)
    root.right.right.right = TreeNode(8)
    print(root.bst_to_gst(root))
