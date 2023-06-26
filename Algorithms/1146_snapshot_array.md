# [Snapshot Array](https://leetcode.com/problems/snapshot-array/description/?envType=list&envId=eiocrakj)

Implement a SnapshotArray that supports the following interface:

- SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element 
equals 0.
- void set(index, val) sets the element at the given index to be equal to val.
- int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
- int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

Example 1:
```
Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
```
Solution
```python
class SnapshotArray:

    def __init__(self, length: int):
        self.arr = {}
        self.update = True
        self.snapshot = []
        

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val
        self.update = True
        

    def snap(self) -> int:
        if self.update:
            self.snapshot.append({**self.arr})
        else:
            self.snapshot.append(self.snapshot[-1])
        self.update = False
        return len(self.snapshot) - 1
        

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshot[snap_id].get(index, 0)


if __name__ == '__main__':
    snap_arr = SnapshotArray(3)
    snap_arr.set(0, 5)
    print(snap_arr.snap())
    snap_arr.set(0, 6)
    print(snap_arr.get(0, 0))
```