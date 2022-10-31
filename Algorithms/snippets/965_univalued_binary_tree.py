class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_unival_tree(self, root):
        if not root:
            return True
        if root.left:
            if root.val != root.left.val:
                return False
        if root.right:
            if root.val != root.right.val:
                return False
        return self.is_unival_tree(root.left) and self.is_unival_tree(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(1)
    print(root.is_unival_tree(root))