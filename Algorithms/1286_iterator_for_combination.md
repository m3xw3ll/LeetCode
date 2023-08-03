# [Iterator for Combination](https://leetcode.com/problems/iterator-for-combination/description/)

Design the CombinationIterator class:

- CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted 
distinct lowercase English letters and a number combinationLength as arguments.
- next() Returns the next combination of length combinationLength in lexicographical order.
- hasNext() Returns true if and only if there exists a next combination.

Example 1:
```
Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False
```
Solution
```python
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def backtrack(start, curr_combination):
            if len(curr_combination) == combinationLength:
                self.combinations_list.append(''.join(curr_combination[:]))
                return

            for i in range(start, len(characters)):
                curr_combination.append(characters[i])
                backtrack(i + 1, curr_combination)
                curr_combination.pop()

        self.combinations_list = []
        self.idx = 0
        backtrack(0, [])
        

    def next(self) -> str:
        nex_comb = self.combinations_list[self.idx]
        self.idx += 1
        return nex_comb
        

    def hasNext(self) -> bool:
        return True if self.idx < len(self.combinations_list) else False
        

if __name__ == '__main__':
    ci = CombinationIterator('abc', 2)
    print(ci.next())
    print(ci.hasNext())
    print(ci.next())
    print(ci.hasNext())
    print(ci.next())
    print(ci.hasNext())
```