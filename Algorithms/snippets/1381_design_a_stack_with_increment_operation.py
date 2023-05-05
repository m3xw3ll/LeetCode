class CumstomStack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, x):
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k, val):
        self.stack[:k] = [x + val for x in self.stack[:k]]


if __name__ == '__main__':
    s = CumstomStack(3)
    s.push(1)
    s.push(2)
    s.pop()
    s.push(2)
    s.push(3)
    s.push(4)
    s.increment(5, 100)
    s.increment(2, 100)
    s.pop()
    s.pop()