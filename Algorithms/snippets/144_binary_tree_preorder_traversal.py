class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preorder_traversal(self, root):
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res


root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
print(root.preorder_traversal(root))
