class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def min_depth(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return self.min_depth(root.right) + 1

        if root.right is None:
            return self.min_depth(root.left) + 1

        return max(self.min_depth(root.left), self.min_depth(root.right)) + 1



if __name__ == '__main__':
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print(root.min_depth(root))