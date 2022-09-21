# [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, 
and return the new head.

Example 1:

![](https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg)

```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
```
Example 2:
```
Input: head = [], val = 1
Output: []
```
Example 3:
```
Input: head = [7,7,7,7], val = 7
Output: []
```
Solution
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
            
        prev = None
        current = head
        
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return head
```
