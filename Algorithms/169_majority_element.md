# [Majority Element](https://leetcode.com/problems/majority-element/)

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
```
Input: nums = [3,2,3]
Output: 3
```
Example 2:
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```
Solution
```python
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i, j in c.items():
            if j >= len(nums) / 2:
                return i
```