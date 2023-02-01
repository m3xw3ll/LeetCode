# [Sum of Nodes with Even-Valued Grandparent](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/submissions/889641218/)

Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

Example 1:

![](https://assets.leetcode.com/uploads/2021/08/10/even1-tree.jpg)

```
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
```
Example 2:

![](https://assets.leetcode.com/uploads/2021/08/10/even2-tree.jpg)

```
Input: root = [1]
Output: 0
```
Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.s = 0

        def dfs(root):
            if root.val % 2 == 0:
                if root.left:
                    if root.left.left:
                        self.s += root.left.left.val
                    if root.left.right:
                        self.s += root.left.right.val
                if root.right:
                    if root.right.left:
                        self.s += root.right.left.val
                    if root.right.right:
                        self.s += root.right.right.val
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            return
        dfs(root)
        return self.s
```