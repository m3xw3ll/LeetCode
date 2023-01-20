class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def binary_tree_paths(self, root):
        out = list()
        s = ''

        def dfs(root, s, out):
            if root:
                s += str(root.val) + '->'
                if not root.left and not root.right:
                    out.append(s[:-2])
                dfs(root.left, s, out)
                dfs(root.right, s, out)

        dfs(root, s, out)
        return out


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print(root.binary_tree_paths(root))