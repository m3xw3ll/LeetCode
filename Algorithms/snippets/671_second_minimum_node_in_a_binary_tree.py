class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def find_second_minimum_value(self, root):
        def preorder(root, vals):
            if root.val not in vals:
                vals.append(root.val)
            if root.left is not None:
                preorder(root.left, vals)
            if root.right is not None:
                preorder(root.right, vals)
            return vals

        arr = []
        preorder(root, arr)
        arr.sort()
        return arr[1] if len(arr) > 1 else -1


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(8)
    root.right = TreeNode(5)
    print(root.find_second_minimum_value(root))
