# [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
```
Example 2:
```
Input: nums = [1,1,2]
Output: [1]
```
Example 3:
```
Input: nums = [1]
Output: []
```
Solution
```python
from collections import Counter
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c = Counter(nums)
        return [key for key, val in c.items() if val == 2]
```