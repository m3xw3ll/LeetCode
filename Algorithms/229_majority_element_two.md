# [Majority Element II](https://leetcode.com/problems/majority-element-ii/description/)

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
```
Input: nums = [3,2,3]
Output: [3]
```
Example 2:
```
Input: nums = [1]
Output: [1]
```
Example 3:
```
Input: nums = [1,2]
Output: [1,2]
```
Solution
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = len(nums) / 3
        out = []
        for n in set(nums):
            if nums.count(n) > m:
                out.append(n)
        return list(set(out))
```