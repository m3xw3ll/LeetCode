# [Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/description/)

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than or equal to the node's key.
- The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:

![](https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg)

```
Input: root = [1,null,2,2]
Output: [2]
```
Example 2:
```
Input: root = [0]
Output: [0]
```
Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict = {}
        out = list()
        def dfs(root):
            if root is None:
                return
            if root.val not in dict:
                dict[root.val] = 1
            else:
                dict[root.val] += 1
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        maxval = max(dict.values())
        for k, v in dict.items():
            if v == maxval:
                out.append(k)
        return out
```