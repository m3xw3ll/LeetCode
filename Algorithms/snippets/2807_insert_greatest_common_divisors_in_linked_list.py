import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert_greatest_common_divisors(self, head):
        dummy = head
        next = head.next
        while next:
            tmp = ListNode(math.gcd(head.val, next.val))
            head.next = tmp
            tmp.next = next

            head = next
            next = next.next
        return dummy