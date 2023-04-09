class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add_two_numbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            value = v1 + v2 + carry
            value = value % 10
            carry = value // 10
            cur.next = ListNode(value)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        return dummy.next