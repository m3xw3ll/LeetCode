class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def diameter_of_binary_tree(self, root):
        self.max_diameter = 0

        def traverse(root):
            if not root:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            diameter = left + right
            self.max_diameter = max(self.max_diameter, diameter)
            return max(left, right) + 1
        traverse(root)
        return self.max_diameter


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(root.diameter_of_binary_tree(root))