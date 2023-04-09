class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_valid_bst(self, root):
        out = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            out.append(root.val)
            inorder(root.right)

        inorder(root)
        return out == sorted(set(out))


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(root.is_valid_bst(root))

