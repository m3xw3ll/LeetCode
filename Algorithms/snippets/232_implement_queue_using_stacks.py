class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        self.stack_in.append(x)

    def pop(self):
        self.peek()
        return self.stack_out.pop()

    def peek(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self):
        return not self.stack_in and not self.stack_out


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.peek()
    q.pop()
    q.empty()