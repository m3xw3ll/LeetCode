class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def get_target_copy(self, original, cloned, target):
        if original is None and original == target:
            return target
        self.get_target_copy(original.left, cloned.left, target) or \
        self.get_target_copy(original.right, cloned.right, target)