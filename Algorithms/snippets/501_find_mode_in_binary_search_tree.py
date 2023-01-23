class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def find_mode(self, root):
        dict = {}
        out = list()
        def dfs(root):
            if root is None:
                return
            if root.val not in dict:
                dict[root.val] = 1
            else:
                dict[root.val] += 1
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        maxval = max(dict.values())
        for k, v in dict.items():
            if v == maxval:
                out.append(k)
        return out


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    print(root.find_mode(root))