# [Merge Nodes in Between Zeros](https://leetcode.com/problems/merge-nodes-in-between-zeros/)

You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of 
the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of 
all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

Example 1:

![](https://assets.leetcode.com/uploads/2022/02/02/ex1-1.png)

```
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.
```
Example 2:

![](https://assets.leetcode.com/uploads/2022/02/02/ex2-1.png)

```
Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.
```
Solution
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
            s = 0
            pnt1 = head
            pnt2 = head.next

            while pnt2:
                if pnt2.val == 0:
                    pnt1 = pnt1.next
                    pnt1.val = s
                    s = 0
                else:
                    s += pnt2.val
                pnt2 = pnt2.next
            pnt1.next = None
            return head.next
```