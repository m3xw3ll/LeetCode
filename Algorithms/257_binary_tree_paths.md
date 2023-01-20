# [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/description/)

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:

![](https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg)

```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```
Example 2:
```
Input: root = [1]
Output: ["1"]
```
Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        out = list()
        s = ''

        def dfs(root, s, out):
            if root:
                s += str(root.val) + '->'
                if not root.left and not root.right:
                    out.append(s[:-2])
                dfs(root.left, s, out)
                dfs(root.right, s, out)

        dfs(root, s, out)
        return out
```