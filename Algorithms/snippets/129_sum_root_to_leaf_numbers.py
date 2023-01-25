class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def sum_numbers(self, root):
        self.out = 0

        def dfs(root, num):
            if not root.left and not root.right:
                self.out += num * 10 + root.val
            if root.left:
                dfs(root.left, num * 10 + root.val)
            if root.right:
                dfs(root.right, num * 10 + root.val)
        dfs(root, 0)
        return self.out


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(root.sum_numbers(root))