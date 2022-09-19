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

    def reverse_list(self):
        prev = None
        current = self.head
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

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
    llist.reverse_list()
    llist.print_list()