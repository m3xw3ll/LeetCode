# [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
```
Input: a = 1, b = 2
Output: 3
```
Example 2:
```
Input: a = 2, b = 3
Output: 5
```
Solution
```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a,b])
```