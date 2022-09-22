class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def range_sum_bst(self, root, low, high):
        if not root:
            return 0
        if root.val < low:
            return self.range_sum_bst(root.right, low, high)
        if root.val > high:
            return self.range_sum_bst(root.left, low, high)
        return root.val + self.range_sum_bst(root.right, low, high) + self.range_sum_bst(root.left, low, high)



if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    print(root.range_sum_bst(root, 7, 15))