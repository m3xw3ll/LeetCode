class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.curr = self.iterator.next() if self.iterator.hasnext() else None

    def peek(self):
        return self.curr

    def next(self):
        tmp = self.curr
        self.curr = self.iterator.next() if self.iterator.hasnext() else None
        return tmp

    def hasnext(self):
        return self.curr != None


if __name__ == '__main__':
    p = PeekingIterator([1, 2 , 3])
    p.next()
    print(p.peek())
    p.next()
    p.next()
    p.hasnext()
