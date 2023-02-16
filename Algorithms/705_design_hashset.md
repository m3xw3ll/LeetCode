# [Design HashSet](https://leetcode.com/problems/design-hashset/description/)

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

- void add(key) Inserts the value key into the HashSet.
- bool contains(key) Returns whether the value key exists in the HashSet or not.
- void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:
```
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
```
Solution
```python
class MyHashSet:

    def __init__(self):
        self.d = {}
        

    def add(self, key: int) -> None:
        self.d[key] = 1
        

    def remove(self, key: int) -> None:
        self.d[key] = 0
        

    def contains(self, key: int) -> bool:
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
```