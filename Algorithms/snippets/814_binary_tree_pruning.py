class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right =right

    def prune_tree(self, root):
        if root is None:
            return
        l = self.prune_tree(root.left)
        r = self.prune_tree(root.right)
        return root if root.val == 1 or l or r else None


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(0)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    print(root.prune_tree(root))