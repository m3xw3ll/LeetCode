# [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/description/)

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.

Example 1:

![](https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
```
Example 2:

![](https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg)

```
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
```
Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        x = defaultdict(float)
        y = defaultdict(int)

        def dfs(root, h):
            if not root:
                return
            dfs(root.left, h + 1)
            dfs(root.right, h + 1)

            x[h] += root.val
            y[h] += 1

        dfs(root, 0)

        out = list()
        for i in range(len(x)):
            out.append(x[i] / y[i])
        return out
```