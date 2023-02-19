class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_all_elements(root1, root2):
    def dfs(root):
        if not root:
            return []
        return dfs(root.right) + [root.val] + dfs(root.left)

    l1 = dfs(root1)
    l2 = dfs(root2)
    l = l1 + l2
    return sorted(l)


if __name__ == '__main__':
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(3)
    print(get_all_elements(root1, root2))