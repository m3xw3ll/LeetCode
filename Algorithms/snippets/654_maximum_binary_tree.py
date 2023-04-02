class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def construct_maximum_binary_tree(self, nums):
        if not nums:
            return

        elem = max(nums)
        idx = nums.index(elem)
        root = TreeNode(elem)
        root.left = self.construct_maximum_binary_tree(elem[0:idx])
        root.right = self.construct_maximum_binary_tree(elem[idx + 1:])
        return root

