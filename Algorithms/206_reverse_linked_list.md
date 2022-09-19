# [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/submissions/)

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

Example 2

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

```
Input: head = [1,2]
Output: [2,1]
```

Example 3
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
        
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        next = None
        
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        
        return head
```