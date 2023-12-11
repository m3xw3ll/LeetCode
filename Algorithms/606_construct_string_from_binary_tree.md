# [Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/description/)

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the 
preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the 
original binary tree.

Example 1

![](https://assets.leetcode.com/uploads/2021/05/03/cons1-tree.jpg)

```
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"

```
Example 2

![](https://assets.leetcode.com/uploads/2021/05/03/cons2-tree.jpg)

```
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
```
Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def tree_to_str(self, root):
        def dfs(root):
            if not root:
                return ''
            if root.right:
                return str(root.val) + '(' + self.dfs(root.left) + ')(' + self.dfs(root.right) + ')'
            if root.left:
                return str(root.val) + '(' + self.dfs(root.left) + ')'
            return str(root.val)
        return dfs(root)
```