class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_subtree(self, root, subroot):
        if not subroot:
            return True
        if not root:
            return False
        if self.same_tree(root, subroot):
            return True
        return self.is_subtree(root.left, subroot) or self.is_subtree(root.right, subroot)

    def same_tree(self, root, subroot):
        if not root and not subroot:
            return True
        if root and subroot and root.val == subroot.val:
            return self.same_tree(root.left, subroot.left) and self.same_tree(root.right, subroot.right)
        return False