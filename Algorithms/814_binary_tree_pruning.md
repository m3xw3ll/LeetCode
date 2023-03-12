# [Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/description/)

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has 
been removed.

A subtree of a node node is node plus every node that is a descendant of node.

Example 1:

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png)

```
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
```
Example 2:

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png)

```
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
```
Example 3:

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png)

```
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
```
Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root if root.val == 1 or root.left or root.right else None
```