class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def kth_smallest(self, root, k):
        def inorder(root, vals):
            if root.left is not None:
                inorder(root.left, vals)
            if root.val is not None:
                vals.append(root.val)
            if root.right is not None:
                inorder(root.right, vals)
            return vals

        arr = []
        inorder(root, arr)
        return arr[k-1]


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(root.kth_smallest(root, 1))