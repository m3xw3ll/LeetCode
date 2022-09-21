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

    def remove_elements(self, val):
        while self.head and self.head.data == val:
            self.head = self.head.next

        prev = None
        current = self.head

        while current:
            if current.data == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return self.head



    def print_list(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end="")
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert(1)
    llist.insert(2)
    llist.insert(6)
    llist.insert(3)
    llist.insert(4)
    llist.insert(5)
    llist.insert(6)
    llist.print_list()
    print()
    llist.remove_elements(6)
    llist.print_list()