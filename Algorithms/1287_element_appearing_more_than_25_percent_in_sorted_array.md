# [Element Appearing More Tahn 25% In Sorted Array](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/)

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more 
than 25% of the time, return that integer.

Example 1:
```
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
```
Example 2:
```
Input: arr = [1,1]
Output: 1
```
Solution
```python
from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        hit = int(0.25 * len(arr))
        for val, cnt in c.items():
            if cnt > hit:
                return val
```