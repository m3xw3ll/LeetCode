# [Leaf Similar Trees](https://leetcode.com/problems/leaf-similar-trees/description/)

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png)

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:

![](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg)

```
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
```
Example 2:

![](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg)

```
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
```
Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root:
                if not root.left and not root.right:
                    return [root.val]
                else:
                    return dfs(root.left) + dfs(root.right)

            return []

        return dfs(root1) == dfs(root2)
```