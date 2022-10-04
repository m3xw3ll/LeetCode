class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def evaluate_tree(self, root):
        if root.val == 0:
            return False
        if root.val == 1:
            return True
        if root.val == 2:
            return self.evaluate_tree(root.left) or self.evaluate_tree(root.right)
        if root.val == 3:
            return self.evaluate_tree(root.left) and self.evaluate_tree(root.right)


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    root.right.left = Node(0)
    root.right.right = Node(1)
    print(root.evaluate_tree(root))