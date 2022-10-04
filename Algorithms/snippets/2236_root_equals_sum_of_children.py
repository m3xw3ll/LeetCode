class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def check_tree(self, root):
        return root.val == root.left.val + root.right.val


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(4)
    root.right = Node(6)
    print(root.check_tree(root))