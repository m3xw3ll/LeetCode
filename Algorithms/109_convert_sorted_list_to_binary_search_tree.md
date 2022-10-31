# [Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced 
binary search tree.

Example 1:

![](https://assets.leetcode.com/uploads/2020/08/17/linked.jpg)

```
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
```
Example 2:
```
Input: head = []
Output: []
```
Solution
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        def to_bst(nums):
            if not nums:
                return None
            else:
                middle = len(nums) // 2
                root = TreeNode(nums[middle])
                root.left = to_bst(nums[:middle])
                root.right = to_bst(nums[middle+1:])
                return root
        return to_bst(nums)
```