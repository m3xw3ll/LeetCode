class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def delete_middle(self):
        if self.head is None or self.head.next is None:
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next

    def print_list(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end="")
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert(1)
    llist.insert(3)
    llist.insert(4)
    llist.insert(7)
    llist.insert(1)
    llist.insert(2)
    llist.insert(6)
    llist.print_list()
    llist.delete_middle()
    print()
    llist.print_list()