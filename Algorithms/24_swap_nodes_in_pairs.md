# [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/description/?envType=list&envId=eiocrakj)

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying 
the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

![](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg)

```
Input: head = [1,2,3,4]
Output: [2,1,4,3]
```
Example 2:
```
Input: head = []
Output: []
```
Example 3:
```
Input: head = [1]
Output: [1]
```
Solution
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        rem_head = head.next.next
        new_head = head.next
        new_head.next = head
        head.next = self.swapPairs(rem_head)
        
        return new_head
```
