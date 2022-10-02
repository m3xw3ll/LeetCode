# [Bitwise AND of Number Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:
```
Input: left = 5, right = 7
Output: 4
```
Example 2:
```
Input: left = 0, right = 0
Output: 0
```
Example 3:
```
Input: left = 1, right = 2147483647
Output: 0
```
Solution
```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        n = right - left
        x = 0
        for b in range(31, -1, -1):
            if (1 << b) < n:
                break
            if (1 << b) & left & right:
                x += 1 << b
        return x  
```