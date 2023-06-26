class SnapshotArray:
    def __init__(self, length):
        self.arr = {}
        self.update = True
        self.snapshot = []

    def set(self, index, val):
        self.arr[index] = val
        self.update = True

    def snap(self):
        if self.update:
            self.snapshot.append({**self.arr})
        else:
            self.snapshot.append(self.snapshot[-1])
        self.update = False
        return len(self.snapshot) - 1

    def get(self, index, snap_id):
        return self.snapshot[snap_id].get(index, 0)


if __name__ == '__main__':
    snap_arr = SnapshotArray(3)
    snap_arr.set(0, 5)
    print(snap_arr.snap())
    snap_arr.set(0, 6)
    print(snap_arr.get(0, 0))