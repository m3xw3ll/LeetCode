# [Make Two Arrays Equal by Reversing Subarrays](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/)

You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of 
arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.

Example 1:
```
Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
```
Example 2:
```
Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.
```
Example 3:
```
Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr does not have value 9 and it can never be converted to target.
```
Solution
```python
from collections import Counter

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(arr) > len(target):
            return False
        t = Counter(target)
        a = Counter(arr)

        for k, v in a.items():
            if k in t and v == t[k]:
                continue
            else:
                return False
        return True
```