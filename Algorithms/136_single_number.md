# [Single Number](https://leetcode.com/problems/single-number/)

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
```
Input: nums = [2,2,1]
Output: 1
```
Example 2:
```
Input: nums = [4,1,2,1,2]
Output: 4
```
Example 3:
```
Input: nums = [1]
Output: 1
```
Solution
```python
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i, j in c.items():
            if j == 1:
                return i
```