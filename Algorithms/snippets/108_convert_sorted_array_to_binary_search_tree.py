class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(nums):
    if not nums:
        return None

    middle = len(nums) // 2
    root = TreeNode(nums[middle])
    root.left = sorted_array_to_bst(nums[:middle])
    root.right = sorted_array_to_bst(nums[middle+1:])

    return root


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    sorted_array_to_bst(nums)