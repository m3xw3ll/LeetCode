class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def deepest_leaves_sum(self, root):
        self.out = 0

        def get_depth(root):
            if not root:
                return 0
            return max(get_depth(root.left), get_depth(root.right)) + 1

        def get_sum(root, d):
            if not root:
                return
            if d == depth:
                self.out += root.val
            get_sum(root.left, d+1)
            get_sum(root.right, d+1)

        depth = get_depth(root)
        get_sum(root, 1)
        return self.out


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.right.right.right = TreeNode(8)
    print(root.deepest_leaves_sum(root))
