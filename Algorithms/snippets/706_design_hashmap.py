class MyHashMap:
    def __init__(self):
        self.m = {}

    def put(self, key, value):
        self.m[key] = value

    def get(self, key):
        if key in self.m.keys():
            return self.m[key]
        else:
            return -1

    def remove(self, key):
        self.m.pop(key, None)


if __name__ == '__main__':
    mymap = MyHashMap()
    mymap.put(1, 1)
    mymap.put(2, 2)
    mymap.get(1)
    mymap.get(3)
    mymap.put(2, 1)
    mymap.get(2)
    mymap.remove(2)
    mymap.get(2)