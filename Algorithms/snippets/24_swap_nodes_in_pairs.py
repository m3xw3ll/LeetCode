class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def swap_pairs(self, head):
        if head is None or head.next is None:
            return head

        rem_head = head.next.next
        new_head = head.next
        new_head.next = head
        head.next = self.swap_pairs(rem_head)

        return new_head