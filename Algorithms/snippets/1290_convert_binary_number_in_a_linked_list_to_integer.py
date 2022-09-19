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

    def get_decimal_value(self):
        out = []

        while self.head:
            out.append(str(self.head.data))
            self.head = self.head.next

        return int(''.join(out), 2)

    def print_list(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end="")
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert(1)
    llist.insert(0)
    llist.insert(1)
    llist.print_list()
    print()
    print(llist.get_decimal_value())
