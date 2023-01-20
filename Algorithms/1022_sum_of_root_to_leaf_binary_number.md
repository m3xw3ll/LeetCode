# [Sum of Root To Leaf Binary Number](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/)

You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary 
number starting with the most significant bit.

- For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of 
these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

Example 1:

![](https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png)

```
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
```
Example 2:
```
Input: root = [0]
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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        out = list()

        def dfs(root, a):
            if root:
                a.append(str(root.val))
                dfs(root.left, a)
                dfs(root.right, a)
                if not root.left and not root.right:
                    out.append(int(''.join(a), 2))
                a.pop()
        dfs(root, [])
        return sum(out)
```