from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def largest_values(self, root):
        out = []
        def dfs(root, h):
            if not root:
                return
            if h >= len(out):
                out.append(root.val)
            else:
                out[h] = max(out[h], root.val)

            dfs(root.left, h + 1)
            dfs(root.right, h + 1)
        dfs(root, 0)
        return out


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(-1)
    print(root.largest_values(root))
