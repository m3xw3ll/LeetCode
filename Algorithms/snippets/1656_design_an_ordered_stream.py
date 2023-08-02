class OrderedStream:
    def __init__(self, n):
        self.pointer = 0
        self.stream = [None] * n

    def insert(self, id_key, value):
        id_key -= 1
        self.stream[id_key] = value
        if id_key > self.pointer:
            return []

        while self.pointer < len(self.stream) and self.stream[self.pointer]:
            self.pointer += 1
        return self.stream[id_key:self.pointer]


if __name__ == '__main__':
    os = OrderedStream(5)
    os.insert(3, 'ccccc')
    os.insert(1, 'aaaaa')
    os.insert(2, 'bbbbb')
    os.insert(5, 'eeeee')
    os.insert(4, 'ddddd')