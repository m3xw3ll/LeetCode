class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def is_balanced(self, root):
        if root is None:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) <= 1 and self.is_balanced(root.left) and self.is_balanced(root.right):
            return True
        return False


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(10)
    root.right.left =TreeNode(15)
    root.right.right = TreeNode(7)
    print(root.is_balanced(root))