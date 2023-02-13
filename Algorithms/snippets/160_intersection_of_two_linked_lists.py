class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def get_intersection_node(self, headA, headB):
        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            pointer_a = headB if not pointer_a else pointer_a.next
            pointer_b = headA if not pointer_b else pointer_b.next
        return pointer_a
