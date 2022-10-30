# [Second Minimum Node in a Binary Tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/)

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has 
exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two 
sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the 
whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

![](https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg)

```
Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
```
Example 2

![](https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg)

```
Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
```
Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def preorder(root, vals):
            if root.val not in vals:
                vals.append(root.val)
            if root.left is not None:
                preorder(root.left, vals)
            if root.right is not None:
                preorder(root.right, vals)
            return vals

        arr = []
        preorder(root, arr)
        arr.sort()
        return arr[1] if len(arr) > 1 else -1
```