# [Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/description/)

Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:

![](https://assets.leetcode.com/uploads/2019/07/31/1483_ex1.png)

```
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
```
Example 2:
```
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
```
Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.out = 0

        def get_depth(root):
            if not root:
                return 0
            return max(get_depth(root.left), get_depth(root.right)) + 1

        def get_sum(root, d):
            if not root:
                return
            if d == depth:
                self.out += root.val
            get_sum(root.left, d+1)
            get_sum(root.right, d+1)

        depth = get_depth(root)
        get_sum(root, 1)
        return self.out


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.right.right.right = TreeNode(8)
    print(root.deepest_leaves_sum(root))
```