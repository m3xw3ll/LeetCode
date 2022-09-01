# [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

Given the root of a binary tree, return the inorder traversal of its nodes' values.

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

Example 1: 
```
Input: root = [1,null,2,3]
Output: [1,3,2]
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right
            else:
                break
        return res
```