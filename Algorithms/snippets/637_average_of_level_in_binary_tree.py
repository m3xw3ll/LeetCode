from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def average_of_levels(self, root):
        x = defaultdict(float)
        y = defaultdict(int)

        def dfs(root, h):
            if not root:
                return
            dfs(root.left, h + 1)
            dfs(root.right, h + 1)

            x[h] += root.val
            y[h] += 1

        dfs(root, 0)

        out = list()
        for i in range(len(x)):
            out.append(x[i] / y[i])
        return out


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(root.average_of_levels(root))