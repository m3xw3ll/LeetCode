# [Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/)

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:

![](https://assets.leetcode.com/uploads/2020/08/21/largest_e1.jpg)

```
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
```
Example 2:
```
Input: root = [1,2,3]
Output: [1,3]
```
Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        def dfs(root, h):
            if not root:
                return
            if h >= len(out):
                out.append(root.val)
            else:
                out[h] = max(out[h], root.val)

            dfs(root.left, h + 1)
            dfs(root.right, h + 1)
        dfs(root, 0)
        return out


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(-1)
    print(root.largestValues(root))
```