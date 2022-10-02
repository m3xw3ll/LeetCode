class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == '__main__':
    p = Node(1)
    p.left = Node(2)
    p.right = Node(3)

    q = Node(1)
    q.left = Node(2)
    q.right = Node(3)
    print(is_same_tree(p, q))