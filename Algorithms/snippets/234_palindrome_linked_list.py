class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def is_palindrome(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]