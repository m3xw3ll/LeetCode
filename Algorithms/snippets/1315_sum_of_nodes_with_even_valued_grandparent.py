class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def sum_even_grandparent(self, root):
        self.s = 0

        def dfs(root):
            if root.val % 2 == 0:
                if root.left:
                    if root.left.left:
                        self.s += root.left.left.val
                    if root.left.right:
                        self.s += root.left.right.val
                if root.right:
                    if root.right.left:
                        self.s += root.right.left.val
                    if root.right.right:
                        self.s += root.right.right.val
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            return
        dfs(root)
        return self.s


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(7)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(9)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    print(root.sum_even_grandparent(root))