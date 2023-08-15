# [Max Pair Sum in an Array](https://leetcode.com/problems/max-pair-sum-in-an-array/description/)

You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of numbers from nums such that 
the maximum digit in both numbers are equal.

Return the maximum sum or -1 if no such pair exists.

Example 1:
```
Input: nums = [51,71,17,24,42]
Output: 88
Explanation: 
For i = 1 and j = 2, nums[i] and nums[j] have equal maximum digits with a pair sum of 71 + 17 = 88. 
For i = 3 and j = 4, nums[i] and nums[j] have equal maximum digits with a pair sum of 24 + 42 = 66.
It can be shown that there are no other pairs with equal maximum digits, so the answer is 88.
```
Example 2:
```
Input: nums = [1,2,3,4]
Output: -1
Explanation: No pair exists in nums with equal maximum digits.
```
Solution
```python
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        out = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                n1 = [int(x) for x in str(nums[i])]
                n2 = [int(x) for x in str(nums[j])]
                if max(n1) == max(n2) and nums[i] + nums[j] > out:
                    out = nums[i] + nums[j]
        return out
```