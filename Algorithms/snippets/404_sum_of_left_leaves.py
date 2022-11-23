class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def sum_of_left_leaves(self, root):
        self.S = 0
        if not root:
            return 0

        def dfs(root, x):
            if not root.left and not root.right:
                if x == 'left':
                    self.S += root.val

            if root.left:
                dfs(root.left, 'left')
            if root.right:
                dfs(root.right, 'right')

        dfs(root, '')
        return self.S


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(root.sum_of_left_leaves(root))