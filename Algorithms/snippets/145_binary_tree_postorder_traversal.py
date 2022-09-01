class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def postorder_traversal(self, root):
        last = None
        stack = []
        res = []

        while True:
            if root and root is not last:
                stack.append(root)
                root = root.left
            elif stack:
                tos = stack[-1]
                if tos.right and tos.right is not root:
                    root = tos.right
                else:
                    root = last = stack.pop()
                    res.append(last.val)
            else:
                break
        return res


root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
print(root.postorder_traversal(root))
