class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def leaf_similar(self, root1, root2):
        def dfs(root):
            if root:
                if not root.left and not root.right:
                    return [root.val]
                else:
                    return dfs(root.left) + dfs(root.right)
            return []

        return dfs(root1) == dfs(root2)


if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root2 = TreeNode(5)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    print(root1.leaf_similar(root1, root2))