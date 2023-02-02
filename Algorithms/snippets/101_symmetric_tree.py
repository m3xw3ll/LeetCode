class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_symmetric(self, root):
        if not root:
            return True

        def checker(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None or left.val != right.val:
                return False
            return checker(left.left, right.right) and checker(left.right, right.left)
        return checker(root.left, root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left =TreeNode(4)
    root.right.right = TreeNode(3)
    print(root.is_symmetric(root))