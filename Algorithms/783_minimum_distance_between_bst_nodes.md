# [Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/)

Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different 
nodes in the tree.

Example 1:

![](https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg)

```
Input: root = [4,2,6,1,3]
Output: 1
```
Example 2:

![](https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg)

```
Input: root = [1,0,48,null,null,12,49]
Output: 1
```
Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        t = []
        out = float('inf')

        def dfs(root):
            if root:
                dfs(root.left)
                t.append(root.val)
                dfs(root.right)
            return t

        tt = dfs(root)

        for i in range(1, len(tt)):
            out = min(out, tt[i] - tt[i-1])
        return out
```