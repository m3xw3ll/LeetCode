class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def sum_root_to_leaf(self, root):
        out = list()

        def dfs(root, a):
            if root:
                a.append(str(root.val))
                dfs(root.left, a)
                dfs(root.right, a)
                if not root.left and not root.right:
                    out.append(int(''.join(a), 2))
                a.pop()
        dfs(root, [])
        return sum(out)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    print(root.sum_root_to_leaf(root))


