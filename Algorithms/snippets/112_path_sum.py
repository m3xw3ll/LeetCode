class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def has_path_sum(self, root, target_sum):
        if root is None:
            return False
        if target_sum == root.val and root.left is None and root.right is None:
            return True

        return self.has_path_sum(root.left, target_sum - root.val) or self.has_path_sum(root.right, target_sum - root.val)



if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)
    print(root.has_path_sum(root, 22))