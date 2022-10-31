class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_data):
        new_node = ListNode(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_list_to_bst(head):
    nums = []
    while head:
        nums.append(head.val)
        head = head.next

    def to_bst(nums):
        if nums is None:
            return None
        else:
            middle = len(nums) // 2
            root = TreeNode(nums[middle])
            root.left = to_bst(nums[:middle])
            root.right = to_bst(nums[middle+1:])
            return root
    return to_bst(nums)


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert(-10)
    llist.insert(-3)
    llist.insert(0)
    llist.insert(5)
    llist.insert(9)
    sorted_list_to_bst(llist.head)