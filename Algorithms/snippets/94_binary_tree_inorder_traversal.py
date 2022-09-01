class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder_traversal(self, root):
        stack = []
        res = []

        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right
            else:
                break
        return res


root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
print(root.inorder_traversal(root))
