# [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

Given the root of a binary tree, return the postorder traversal of its nodes' values.

![](https://assets.leetcode.com/uploads/2020/08/28/pre1.jpg)

Example 1:
```
Input: root = [1,null,2,3]
Output: [3,2,1]
```
Example 2:
```
Input: root = []
Output: []
```
Example 3:
```
Input: root = [1]
Output: [1]
```
Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        last = None
        stack = []
        res = []

        while True:
            if root and root is not last:
                stack.append(root)
                root = root.left
            elif stack:
                tos = stack[-1]
                if tos.right and tos.right is not root:
                    root = tos.right
                else:
                    root = last = stack.pop()
                    res.append(last.val)
            else:
                break
        return res
```