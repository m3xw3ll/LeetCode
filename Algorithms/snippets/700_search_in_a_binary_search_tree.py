class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def search_bst(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        elif val > root.val:
            return self.search_bst(root.right, val)
        else:
            return self.search_bst(root.left, val)


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(root.search_bst(root, 2))
