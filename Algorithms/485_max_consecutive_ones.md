# [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/submissions/)

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
```
Example 2:
```
Input: nums = [1,0,1,1,0,1]
Output: 2
```
Solution
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        max_cnt = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                max_cnt = max(cnt, max_cnt)
                cnt = 0
        return max(cnt, max_cnt)
```