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

    def middle_node(self):
        temp = self.head
        count = 0

        while self.head:
            if count & 1:
                temp = temp.next
            self.head = self.head.next

            count += 1

        return temp.data

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
    print(llist.middle_node())