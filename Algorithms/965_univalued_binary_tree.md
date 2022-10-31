# [Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree/)

A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

Example 1:

![](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png)

```
Input: root = [1,1,1,1,1,null,1]
Output: true
```
Example 2:

![](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png)

```
Input: root = [2,2,2,5,2]
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
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left:
            if root.val != root.left.val:
                return False
        if root.right:
            if root.val != root.right.val:
                return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
```