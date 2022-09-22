class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_into_bst(self, root, val):
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insert_into_bst(root.right, val)
        else:
            root.left = self.insert_into_bst(root.left, val)
        return root



if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.insert_into_bst(root, 5)
    print(root.right.left.val)