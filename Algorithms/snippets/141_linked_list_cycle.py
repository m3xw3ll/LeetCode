class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def has_cycle(self, head):
        self.slow_ptr = head
        self.fast_ptr = head

        while self.slow_ptr and self.fast_ptr and self.fast_ptr.next:
            self.slow_ptr = self.slow_ptr.next
            self.fast_ptr = self.fast_ptr.next.next
            if self.slow_ptr == self.fast_ptr:
                return True
        return False