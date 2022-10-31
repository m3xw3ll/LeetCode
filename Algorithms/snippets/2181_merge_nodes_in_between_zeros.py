class Node:
    def __init__(self, val):
        self.val = val
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

    def merge_nodes(self, head):
        s = 0
        pnt1 = head
        pnt2 = head.next

        while pnt2:
            if pnt2.val == 0:
                pnt1 = pnt1.next
                pnt1.val = s
                s = 0
            else:
                s += pnt2.val
            pnt2 = pnt2.next
        pnt1.next = None
        return head.next

    def print_list(self):
        temp = self.head
        while temp:
            print(str(temp.val) + " ", end="")
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert(0)
    llist.insert(3)
    llist.insert(1)
    llist.insert(0)
    llist.insert(4)
    llist.insert(5)
    llist.insert(2)
    llist.insert(0)
    llist.print_list()
    llist.merge_nodes(llist.head)
    print()
    llist.print_list()
