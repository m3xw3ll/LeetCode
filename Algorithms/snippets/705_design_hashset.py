class MyHashSet:
    def __init__(self):
        self.d = {}

    def add(self, key):
        self.d[key] = 1

    def remove(self, key):
        self.d[key] = 0

    def contains(self, key):
        return self.d.get(key, 0) != 0


if __name__ == '__main__':
    m = MyHashSet()
    m.add(1)
    m.add(2)
    m.contains(1)
    m.contains(3)
    m.add(2)
    m.contains(2)
    m.remove(2)
    m.contains(2)