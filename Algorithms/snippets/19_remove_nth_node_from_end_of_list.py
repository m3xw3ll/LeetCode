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

    def remove_nth_from_end(self, n):
        fast = self.head
        slow = self.head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return self.head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

    def print_list(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end="")
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.insert(5)
    llist.print_list()
    llist.remove_nth_from_end(2)
    print()
    llist.print_list()