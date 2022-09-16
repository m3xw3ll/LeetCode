# [Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg)
```
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
```
Example 2:

![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg)
```
Input: root = [5,3,6,2,4,null,7], k = 28
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        def helper(root, k):
            if not root:
                return False
            if k - root.val in s:
                return True
            s.add(root.val)

            return helper(root.left, k) or (helper(root.right, k))
        return helper(root, k)
```