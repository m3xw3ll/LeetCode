class BSTNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def find_target(self, root, k):
        s = set()
        def helper(root, k):
            if not root:
                return False
            if k - root.val in s:
                return True
            s.add(root.val)

            return helper(root.left, k) or (helper(root.right, k))
        return helper(root, k)


if __name__ == '__main__':
    root = BSTNode(5)
    root.left = BSTNode(3)
    root.right = BSTNode(6)
    root.left.left = BSTNode(2)
    root.left.right = BSTNode(4)
    root.right.right = BSTNode(7)

    print(root.find_target(root, 9))
