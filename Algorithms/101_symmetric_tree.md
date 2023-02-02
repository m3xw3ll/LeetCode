# [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/description/)

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

![](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)

```Input: root = [1,2,2,3,4,4,3]
Output: true
```
Example 2:

![](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)

```
Input: root = [1,2,2,null,3,null,3]
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def checker(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None or left.val != right.val:
                return False
            return checker(left.left, right.right) and checker(left.right, right.left)
        return checker(root.left, root.right)
```