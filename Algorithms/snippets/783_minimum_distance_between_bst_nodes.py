class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def min_diff_in_bst(self, root):
        t = []
        out = float('inf')

        def dfs(root):
            if root:
                dfs(root.left)
                t.append(root.val)
                dfs(root.right)
            return t

        tt = dfs(root)

        for i in range(1, len(tt)):
            out = min(out, tt[i] - tt[i-1])
        return out


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(root.min_diff_in_bst(root))